from datetime import datetime

with open(f"{datetime.now().strftime('%H_%m')}.txt", "w") as log_file:
    log_file.write(f"Right now time in GERMERY {datetime.now()}")
