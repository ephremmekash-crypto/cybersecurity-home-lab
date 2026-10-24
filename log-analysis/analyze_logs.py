from collections import defaultdict
from datetime import datetime
import re

LOG_FILE = "sample_logs.txt"

failed_attempts = defaultdict(list)
successful_logins = defaultdict(list)

pattern = re.compile(
    r"(?P<timestamp>\S+)\s+"
    r"(?P<ip>\S+)\s+"
    r"(?P<status>FAILED|SUCCESS)"
)

with open(LOG_FILE, "r", encoding="utf-8") as file:
    for line in file:
        match = pattern.search(line)

        if not match:
            continue

        timestamp = match.group("timestamp")
        ip = match.group("ip")
        status = match.group("status")

        if status == "FAILED":
            failed_attempts[ip].append(timestamp)
        else:
            successful_logins[ip].append(timestamp)


print("=" * 50)
print("CYBERSECURITY LOG ANALYSIS")
print("=" * 50)

for ip, attempts in failed_attempts.items():
    failures = len(attempts)
    successes = len(successful_logins.get(ip, []))

    print(f"\nIP Address: {ip}")
    print(f"Failed attempts: {failures}")
    print(f"Successful logins: {successes}")

    if failures >= 5:
        print("Status: ⚠️ SUSPICIOUS")
        print("Possible repeated authentication attempts.")
    else:
        print("Status: NORMAL")
