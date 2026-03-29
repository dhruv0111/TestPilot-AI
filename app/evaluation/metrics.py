import time

def measure_latency(start_time):
    latency = time.time() - start_time
    return round(latency, 2)


def evaluate_retrieval(docs, query):
    query_words = set(query.lower().split())

    score = 0

    for doc in docs:
        doc_words = set(doc.page_content.lower().split())

        overlap = query_words.intersection(doc_words)

        if len(overlap) > 0:
            score += 1

    return round(score / max(len(docs), 1), 2)


def evaluate_response_quality(answer):
    # simple heuristic
    keywords = ["root cause", "risk", "test"]

    score = sum(1 for k in keywords if k in answer.lower())

    return score / len(keywords)


def evaluate_ml_prediction(predicted, expected):
    return 1 if predicted == expected else 0