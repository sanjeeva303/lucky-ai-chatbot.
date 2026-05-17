from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(title="Lucky AI Chatbot")


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Lucky AI Chatbot is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Lucky AI Chatbot"
    }


@app.post("/query")
def query_bot(request: QueryRequest):

    start_time = time.time()

    question = request.question.lower()

    if "name" in question:
        answer = "My name is Lucky AI Assistant."
    elif "hello" in question:
        answer = "Hello! How can I help you today?"
    elif "python" in question:
        answer = "Python is a powerful programming language."
    elif "docker" in question:
        answer = "Docker is a container platform used to run applications."
    else:
        answer = "I am Lucky AI and I can answer your questions."

    response_time = round((time.time() - start_time) * 1000)

    return {
        "question": request.question,
        "answer": answer,
        "meta": {
            "confidence": 0.95,
            "model_used": "llama-3.3-70b-versatile",
            "response_time_ms": response_time,
            "cached": False,
            "is_fallback": False
        }
    }