# agents/competitor_scan_agent.py

from debug.debug_logger import log_info
from memory.memory import Memory
import random

class Agent:
    def __init__(self, memory: Memory):
        self.memory = memory
        self.agent_name = "Competitor-Scan-Agent"

    def run(self):
        log_info(f"🔍 [{self.agent_name}] Running competitor scan cycle...")

        # Example → simulate finding competitor insights
        competitor_insights = [
            {"competitor": "AI Health Co", "activity": "Launched new patient portal"},
            {"competitor": "Global Med Travel", "activity": "Opened new clinic in Dubai"},
            {"competitor": "SmartCare SaaS", "activity": "Partnership with insurance provider"}
        ]

        selected_insight = random.choice(competitor_insights)
        log_info(f"📊 [{self.agent_name}] Found competitor activity: {selected_insight}")

        # Log competitor insight as an action
        self.memory.log_action(
            agent_name=self.agent_name,
            action_type="Competitor Insight",
            payload=selected_insight
        )

        log_info(f"✅ [{self.agent_name}] Competitor scan cycle complete.")
