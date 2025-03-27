# LLM + RAG-Based Function Execution API

## 📌 Overview
This project implements a **Function Execution API** that dynamically retrieves, generates, and executes Python functions based on user queries using **LLM (Large Language Model) and RAG (Retrieval-Augmented Generation)** techniques.

## 🚀 Features
- **Function Registry**: Supports predefined automation functions (e.g., `open_calculator`, `get_cpu_usage`).
- **LLM + RAG for Function Retrieval**: Uses **FAISS** and **sentence embeddings** to retrieve the best-matching function.
- **Dynamic Code Generation**: Generates executable Python scripts dynamically.
- **FastAPI Service**: Provides an API endpoint (`/execute`) for function execution.
- **Extendability**: Supports adding custom user-defined functions.

---


## 🔧 Installation
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Anbu-001/LLM-RAG-based-APi.git
cd LLM-RAG-based-APi
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv LLM
LLM\Scripts\activate    
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the API Server
```bash
uvicorn main:app --reload
```

Once the server starts, access the API at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 API Endpoints
### 🔹 `POST /execute`
#### **Request Body**
```json
{
  "prompt": "Open calculator"
}
```
#### **Response**
```json
{
  "function": "open_calculator",
  "code": "from automation_functions import open_calculator\n\ndef main():\n    open_calculator()\nif __name__ == \"__main__\":\n    main()",
  "status": "Calculator opened successfully."
}
```

---

## 📌 Testing via cURL
```bash
curl -X POST "http://127.0.0.1:8000/execute" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Open calculator"}'
```

---

## 📊 Logging & Monitoring
### 🔹 Logging Execution Details
Function execution events are logged in `logs/execution.log`. The logging mechanism in `main.py` ensures all function calls are recorded:
```python
import logging
logging.basicConfig(level=logging.INFO, filename='logs/execution.log', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
```
Each function execution is logged as follows:
```
[2025-03-27 14:05:32] INFO - Executed: open_calculator | Status: Success
[2025-03-27 14:07:15] INFO - Executed: get_cpu_usage | Status: Success | Output: 32%
```

---
