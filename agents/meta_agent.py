# agents/meta_agent.py

from debug.debug_logger import log_info
from memory.memory import Memory

class Agent:
    def __init__(self, memory: Memory):
        self.memory = memory
        self.agent_name = "Meta-Agent"

    def run(self):
        log_info(f"🧠 [{self.agent_name}] Thinking...")

        # Example Meta-Agent behavior:
        # 1️⃣ Reflect on past actions
        past_actions = self.memory.get_recent_actions(limit=5)
        log_info(f"🧠 [{self.agent_name}] Reflecting on past actions: {past_actions}")

        # 2️⃣ Adjust strategy (placeholder logic)
        new_strategy = "Focus on high-value opportunities"
        log_info(f"🧠 [{self.agent_name}] Decided new strategy: {new_strategy}")

        # 3️⃣ Save new strategy to memory
        self.memory.save_agent_state(self.agent_name, {"strategy": new_strategy})

        # 4️⃣ Done
        log_info(f"✅ [{self.agent_name}] Cycle complete.")
