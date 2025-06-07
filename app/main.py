# app/main.py

import time
from orchestration.orchestrator import Orchestrator
from config import settings
from debug.debug_logger import log_info

# Initialize Orchestrator
orchestrator = Orchestrator()

# META-SUPERVISOR + FEMTOSECOND LOOP
def meta_supervisor_loop():
    log_info("🚀 AGIengineX Meta-Supervisor starting loop...")
    loop_interval_seconds = settings.get("loop_interval_seconds", 60)
    femtosecond_cycles = settings.get("femtosecond_cycles_per_loop", 1000)

    while True:
        loop_start_time = time.time()
        log_info("🕒 New loop cycle started.")

        # FEMTOSECOND INNER LOOP
        for cycle in range(femtosecond_cycles):
            log_info(f"⚙️ Femtosecond cycle {cycle + 1}/{femtosecond_cycles}")
            orchestrator.run_agents_cycle()

            time.sleep(0.001)  # simulate femtosecond speed (1ms pause for stability)

        # Wait remaining time in the outer loop interval
        elapsed_time = time.time() - loop_start_time
        time_remaining = max(0, loop_interval_seconds - elapsed_time)
        log_info(f"✅ Loop cycle complete. Waiting {time_remaining:.2f} seconds...")
        time.sleep(time_remaining)

if __name__ == "__main__":
    meta_supervisor_loop()
