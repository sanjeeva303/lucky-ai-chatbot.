import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="documents"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def add_documents():

    docs = [
        "Artificial Intelligence is the simulation of human intelligence.",
        "Machine Learning is a subset of AI.",
        "Python is widely used in AI development."
    ]

    for i, doc in enumerate(docs):

        embedding = model.encode(doc).tolist()

        collection.add(
            documents=[doc],
            embeddings=[embedding],
            ids=[str(i)]
        )

def search_documents(query):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results["documents"][0]