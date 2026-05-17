import requests
import time
import statistics

URL = "http://127.0.0.1:8000/query"

times = []

for i in range(50):

    start = time.time()

    response = requests.post(
        URL,
        json={"question": "What is AI?"}
    )

    end = time.time()

    response_time = (end - start) * 1000
    times.append(response_time)

    print(f"Request {i+1}: {int(response_time)} ms")

times.sort()

p50 = statistics.median(times)
p95 = times[int(0.95 * len(times)) - 1]
p99 = times[int(0.99 * len(times)) - 1]

print("\nBenchmark Results")
print(f"p50: {int(p50)} ms")
print(f"p95: {int(p95)} ms")
print(f"p99: {int(p99)} ms")