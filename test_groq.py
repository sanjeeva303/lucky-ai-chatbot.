import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from services.groq_client import ask_groq

response = ask_groq(
    "What is Artificial Intelligence?"
)

print(response)