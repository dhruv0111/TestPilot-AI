def decide_and_route(query):
    if "log" in query:
        return "logs"
    elif "bug" in query:
        return "bugs"
    else:
        return "general"