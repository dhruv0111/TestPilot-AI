from app.rag.retriever import get_retriever
from app.rag.generator import generate_answer
from app.rag.vector_store import load_vector_store
from app.rag.embeddings import get_embeddings
from app.ml.predict import predict_risk
from app.ml.feature_extractor import extract_features
import time
from app.evaluation.metrics import (
    measure_latency,
    evaluate_retrieval,
    evaluate_response_quality
)
import logging


embeddings = get_embeddings()
db = load_vector_store(embeddings)
retriever = get_retriever(db)

def process_query(query):
    start_time = time.time()

    try:
        docs = retriever.invoke(query)
        answer = generate_answer(query, docs)

        # ML features
        features = extract_features(query)
        prediction = predict_risk(features)

        # 🔥 METRICS
        latency = measure_latency(start_time)
        retrieval_score = evaluate_retrieval(docs, query)
        response_score = evaluate_response_quality(answer)

        return {
            "answer": answer,
            "risk_score": prediction["risk_score"],
            "predicted_risk": prediction["risk"],
            "metrics": {
                "latency_sec": latency,
                "retrieval_score": retrieval_score,
                "response_quality": response_score
            }
        }

    except Exception as e:
        logging.error(f"Error processing query: {e}")
        return {"error": "Internal server error"}