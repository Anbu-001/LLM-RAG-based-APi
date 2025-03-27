import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# ✅ Load function registry from JSON file
try:
    with open("custom_functions.json", "r") as f:
        functions = json.load(f)["functions"]
except FileNotFoundError:
    functions = {
        "open_calculator": "Open calculator application",
        "get_cpu_usage": "Retrieve CPU usage",
        "open_chrome": "Open Google Chrome"
    }

# ✅ Load Sentence Transformer model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Encode function descriptions into FAISS
function_names = list(functions.keys())
function_embeddings = np.array([embedding_model.encode(desc) for desc in functions.values()])

index = faiss.IndexFlatL2(function_embeddings.shape[1])
index.add(function_embeddings)

# ✅ File to store last executed function
LAST_FUNCTION_FILE = "last_function.json"

def retrieve_function(query):
    """Retrieve the most relevant function."""
    query_embedding = embedding_model.encode(query).reshape(1, -1)
    _, idx = index.search(query_embedding, 1)
    
    function_name = function_names[idx[0][0]]
    
    # ✅ Store last executed function
    with open(LAST_FUNCTION_FILE, "w") as f:
        json.dump({"last_function": function_name}, f)

    return function_name

def get_last_function():
    """Retrieve the last executed function."""
    try:
        with open(LAST_FUNCTION_FILE, "r") as f:
            data = json.load(f)
            return data.get("last_function", None)
    except FileNotFoundError:
        return None

def add_function(name, description):
    """Dynamically add a new function to the registry."""
    functions[name] = description

    # ✅ Update FAISS index dynamically
    new_embedding = embedding_model.encode(description).reshape(1, -1)
    index.add(new_embedding)

    # ✅ Save new function to JSON file
    with open("custom_functions.json", "w") as f:
        json.dump({"functions": functions}, f, indent=4)
