# orchestration/orchestrator.py

import importlib
import threading
from debug.debug_logger import log_info
from memory.memory import Memory
import time

# Initialize MEMORY (shared across agents)
memory = Memory()

class Orchestrator:
    def __init__(self):
        log_info("🧠 Initializing Orchestrator...")
        self.agent_registry = {}
        self.active_threads = []

        # List of AGENTS TO RUN → can expand dynamically
        self.agent_classes = [
            "meta_agent",
            "self_monetization_agent",
            "agi_bank_agents",
            "agi_healthcare_agents",
            "opportunity_agent",
            "next_move_agent",
            "competitor_scan_agent",
            "code_agent"
        ]

        # Dynamically import agent modules
        self.agent_modules = {}
        for agent_name in self.agent_classes:
            module = importlib.import_module(f"agents.{agent_name}")
            self.agent_modules[agent_name] = module
            log_info(f"✅ Loaded agent: {agent_name}")

    def run_agents_cycle(self):
        log_info("🎯 Orchestrator running agents cycle...")

        # LOOP over agents → check if ready → run individually
        for agent_name, agent_module in self.agent_modules.items():
            agent_id = f"{agent_name}_1"  # for simplicity (can expand with Factory)

            # Check agent state
            agent_state = self.agent_registry.get(agent_id, {"status": "ready"})

            if agent_state["status"] == "ready":
                log_info(f"🚀 Launching agent: {agent_id}")

                # Run agent in its own THREAD → NON-BLOCKING
                agent_thread = threading.Thread(
                    target=self._run_agent_safe,
                    args=(agent_id, agent_module)
                )
                agent_thread.start()

                # Track thread + status
                self.active_threads.append(agent_thread)
                self.agent_registry[agent_id] = {"status": "running"}

            else:
                log_info(f"⏳ Agent {agent_id} is {agent_state['status']} — skipping.")

    def _run_agent_safe(self, agent_id, agent_module):
        try:
            # Instantiate agent (assuming agent class is Agent)
            agent_class = getattr(agent_module, "Agent")
            agent_instance = agent_class(memory=memory)

            # Run agent logic
            agent_instance.run()

            # Mark as done
            self.agent_registry[agent_id]["status"] = "done"
            log_info(f"✅ Agent {agent_id} finished and marked DONE.")

        except Exception as e:
            self.agent_registry[agent_id]["status"] = "error"
            log_info(f"❌ ERROR in agent {agent_id}: {str(e)}")

