# memory/memory.py

from supabase import create_client, Client
from debug.debug_logger import log_info
import os

class Memory:
    def __init__(self):
        log_info("🧠 Initializing Memory Layer (Supabase)...")

        # Load Supabase URL & KEY → from ENV or CONFIG (safe!)
        supabase_url = os.getenv("SUPABASE_URL", "https://your-supabase-url.supabase.co")
        supabase_key = os.getenv("SUPABASE_KEY", "your-supabase-service-role-key")

        self.supabase: Client = create_client(supabase_url, supabase_key)

    def get_recent_actions(self, limit=5):
        try:
            response = self.supabase.table("actions_log").select("*").order("timestamp", desc=True).limit(limit).execute()
            return response.data
        except Exception as e:
            log_info(f"❌ MEMORY ERROR: get_recent_actions: {str(e)}")
            return []

    def save_agent_state(self, agent_name, state_dict):
        try:
            data = {
                "agent_name": agent_name,
                "state": state_dict,
                "timestamp": "now()"
            }
            self.supabase.table("agents_memory").insert(data).execute()
            log_info(f"💾 MEMORY: Saved state for {agent_name}.")
        except Exception as e:
            log_info(f"❌ MEMORY ERROR: save_agent_state: {str(e)}")

    def log_action(self, agent_name, action_type, payload, result="success"):
        try:
            data = {
                "agent_name": agent_name,
                "action_type": action_type,
                "payload": payload,
                "result": result,
                "timestamp": "now()"
            }
            self.supabase.table("actions_log").insert(data).execute()
            log_info(f"📜 MEMORY: Logged action for {agent_name}.")
        except Exception as e:
            log_info(f"❌ MEMORY ERROR: log_action: {str(e)}")

    def save_opportunity(self, opportunity_data):
        try:
            self.supabase.table("opportunities_memory").insert(opportunity_data).execute()
            log_info("🌟 MEMORY: Saved new opportunity.")
        except Exception as e:
            log_info(f"❌ MEMORY ERROR: save_opportunity: {str(e)}")

    def get_agent_spawn_decision(self):
        try:
            # For now, mock static decision (can evolve to dynamic policy!)
            return {"spawn": True, "agent_type": "opportunity_agent"}
        except Exception as e:
            log_info(f"❌ MEMORY ERROR: get_agent_spawn_decision: {str(e)}")
            return {"spawn": False}
    
    def save_spawn_request(self, agent_type):
        try:
            data = {
                "agent_type": agent_type,
                "status": "pending",
                "timestamp": "now()"
            }
            self.supabase.table("spawn_requests").insert(data).execute()
            log_info(f"🆕 MEMORY: Spawn request logged for agent type {agent_type}.")
        except Exception as e:
            log_info(f"❌ MEMORY ERROR: save_spawn_request: {str(e)}")
