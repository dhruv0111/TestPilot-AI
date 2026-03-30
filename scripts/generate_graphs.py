import matplotlib.pyplot as plt

methods = ["LLM", "RAG", "Proposed"]
quality = [0.72, 0.85, 0.93]
latency = [2.1, 3.2, 3.8]

# Quality Graph
plt.figure()
plt.bar(methods, quality)
plt.title("Response Quality Comparison")
plt.xlabel("Method")
plt.ylabel("Quality Score")
plt.savefig("fig_quality.png")

# Latency Graph
plt.figure()
plt.bar(methods, latency)
plt.title("Latency Comparison")
plt.xlabel("Method")
plt.ylabel("Seconds")
plt.savefig("fig_latency.png")