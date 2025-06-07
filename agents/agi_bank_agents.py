# agents/agi_bank_agents.py

from debug.debug_logger import log_info
from memory.memory import Memory
import random

class Agent:
    def __init__(self, memory: Memory):
        self.memory = memory
        self.agent_name = "AGI-Bank-Agent"

    def run(self):
        log_info(f"🏦 [{self.agent_name}] Running finance cycle...")

        # Example → simulate checking bank balances
        bank_accounts = {
            "Stripe": random.uniform(1000, 10000),
            "PayPal": random.uniform(500, 5000),
            "Wise": random.uniform(2000, 15000)
        }

        log_info(f"🏦 [{self.agent_name}] Current balances: {bank_accounts}")

        # Log balance check action
        self.memory.log_action(
            agent_name=self.agent_name,
            action_type="Checked Balances",
            payload=bank_accounts
        )

        # Example → simulate making a payout if balance high
        for account, balance in bank_accounts.items():
            if balance > 7000:
                payout_amount = balance * 0.3  # Pay out 30%
                log_info(f"💸 [{self.agent_name}] Triggering payout of ${payout_amount:.2f} from {account}.")

                # Log payout action
                self.memory.log_action(
                    agent_name=self.agent_name,
                    action_type="Triggered Payout",
                    payload={
                        "account": account,
                        "payout_amount": payout_amount
                    }
                )

        log_info(f"✅ [{self.agent_name}] Finance cycle complete.")
