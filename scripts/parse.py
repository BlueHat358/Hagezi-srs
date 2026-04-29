import json, sys, os

tag = os.environ.get('TAG', 'unknown')

with open('raw.txt', 'r') as f:
    raw_lines = f.readlines()

domains = []
for line in raw_lines:
    line = line.strip()
    if not line or line.startswith('#') or line.startswith('!'):
        continue
    if line.startswith('*.'):
        line = line[2:]
    elif line.startswith('.'):
        line = line[1:]
    if '.' in line:
        domains.append(line)

domains = sorted(set(domains))
print(f"  Unique domains: {len(domains)}")

if not domains:
    print("  WARNING: No domains found!")
    sys.exit(1)

with open('rule.json', 'w') as f:
    json.dump({"version": 1, "rules": [{"domain_suffix": domains}]}, f)

print(f"  rule.json OK")
