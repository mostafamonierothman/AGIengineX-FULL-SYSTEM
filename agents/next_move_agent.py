# agents/next_move_agent.py

from debug.debug_logger import log_info
from memory.memory import Memory
import random

class Agent:
    def __init__(self, memory: Memory):
        self.memory = memory
        self.agent_name = "Next-Move-Agent"

    def run(self):
        log_info(f"📈 [{self.agent_name}] Running next move cycle...")

        # Example → propose next moves
        possible_moves = [
            "Target 5 new healthcare clients",
            "Initiate outbound campaign for AI SaaS",
            "Research 3 emerging markets",
            "Partner with 2 medical tourism clinics",
            "Optimize LinkedIn outreach"
        ]

        selected_move = random.choice(possible_moves)
        log_info(f"🎯 [{self.agent_name}] Proposed next move: {selected_move}")

        # Log next move as an action
        self.memory.log_action(
            agent_name=self.agent_name,
            action_type="Proposed Next Move",
            payload={"next_move": selected_move}
        )

        log_info(f"✅ [{self.agent_name}] Next move cycle complete.")
