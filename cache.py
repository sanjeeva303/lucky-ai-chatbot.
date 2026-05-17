cache_store = {}

def make_key(question: str):
    return question.lower().strip()

def get_cache(key):
    return cache_store.get(key)

def set_cache(key, value):
    cache_store[key] = value

def get_stats():
    return {
        "cache_items": len(cache_store)
    }