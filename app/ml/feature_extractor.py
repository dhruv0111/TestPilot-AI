import json

# Load bug data
with open("data/bugs.json", "r") as f:
    bugs = json.load(f)

# Load logs
with open("data/logs.txt", "r") as f:
    logs = f.readlines()


def detect_module(query):
    query = query.lower()

    if "login" in query or "auth" in query:
        return "Authentication"
    elif "payment" in query:
        return "Payments"
    elif "user" in query:
        return "UserService"
    else:
        return "General"


def extract_features(query):
    module = detect_module(query)

    # Filter bugs
    module_bugs = [b for b in bugs if module.lower() in b["module"].lower()]

    failures = len(module_bugs)

    # Severity mapping
    severity_map = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}

    severity_scores = [severity_map.get(b["severity"], 1) for b in module_bugs]

    high_severity_bugs = sum(1 for s in severity_scores if s >= 3)

    # 🔥 Improved log matching (IMPORTANT)
    keywords = module.lower().split()

    relevant_logs = [
        l for l in logs
        if any(k in l.lower() for k in keywords)
    ]

    error_rate = len(relevant_logs) / max(len(logs), 1)

    # 🔥 Better response time logic
    avg_response_time = 100 + (high_severity_bugs * 50) + (failures * 20)

    return [
        failures * 10,                # scale up
        avg_response_time,
        error_rate * 10,             # scale up
        high_severity_bugs * 5       # scale up
    ]