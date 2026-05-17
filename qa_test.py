import requests

questions = [
    "What is AI?",
    "What is machine learning?",
    "Explain Python",
    "What is FastAPI?",
    "What is cloud computing?",
    "Explain chatbot",
    "What is NLP?",
    "What is API?",
    "What is data science?",
    "What is deep learning?",
    "What is Docker?",
    "What is GitHub?",
    "Explain Linux",
    "What is cyber security?",
    "What is database?",
    "Explain SQL",
    "What is JavaScript?",
    "What is HTML?",
    "What is CSS?",
    "Explain React",
    "What is backend development?",
    "What is frontend development?",
    "What is AI ethics?",
    "What is neural network?",
    "Explain automation",
    "What is DevOps?",
    "Explain REST API",
    "What is tokenization?",
    "What is prompt engineering?",
    "What is generative AI?"
]

success = 0

for i, q in enumerate(questions, start=1):

    response = requests.post(
        "http://127.0.0.1:8000/query",
        json={"question": q}
    )

    data = response.json()

    print(f"\nTest {i}")
    print("Question:", q)
    print("Answer:", data["answer"][:150])

    if len(data["answer"]) > 20:
        success += 1

print("\n===================")
print("Demo Ready Score:", success, "/ 30")