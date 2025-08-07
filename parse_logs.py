import re
from collections import Counter

alerts = []
with open("/var/log/snort/alert", 'r') as file:
    for line in file:
        if "[**]" in line:
            match = re.search(r'\[\*\*\] \[.*?\] (.*?) \[\*\*\]', line)
            if match:
                alerts.append(match.group(1))


summary = Counter(alerts)
for alert, count in summary.items():
    print(f"{alert}: {count} times")

with open("snort_summary.csv", "w") as f:
    f.write("Alert Type,Count\n")
    for alert, count in summary.items():
        f.write(f"{alert},{count}\n")
