# agents/factory_agent.py

from debug.debug_logger import log_info
from memory.memory import Memory

class Agent:
    def __init__(self, memory: Memory):
        self.memory = memory
        self.agent_name = "Factory-Agent"

    def run(self):
        log_info(f"🏭 [{self.agent_name}] Running Factory cycle...")

        # Example behavior → check if new agents should be spawned
        # For simplicity → just a static decision (can evolve to be dynamic)
        spawn_decision = self.memory.get_agent_spawn_decision()

        if spawn_decision.get("spawn", False):
            new_agent_type = spawn_decision.get("agent_type", "opportunity_agent")
            log_info(f"🆕 [{self.agent_name}] Spawning new agent: {new_agent_type}")

            # Save this action to MEMORY for orchestrator to pick up
            self.memory.save_spawn_request(new_agent_type)

        else:
            log_info(f"⏳ [{self.agent_name}] No new agents to spawn this cycle.")

        log_info(f"✅ [{self.agent_name}] Factory cycle complete.")
