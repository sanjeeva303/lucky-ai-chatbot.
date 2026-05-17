from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_groq(question):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        return {
            "answer": answer,
            "is_fallback": False
        }

    except Exception as e:

        fallback_answer = (
            "Sorry, AI service is temporarily unavailable. "
            "Please try again later."
        )

        return {
            "answer": fallback_answer,
            "is_fallback": True
        }