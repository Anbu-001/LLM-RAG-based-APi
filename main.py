import logging
from fastapi import FastAPI
from pydantic import BaseModel
from retrieval import retrieve_function, get_last_function, add_function
from code_generator import generate_code
from automation_functions import open_calculator, get_cpu_usage, open_chrome, run_shell_command

# ✅ Setup Logging
logging.basicConfig(filename="execution.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/execute")
def execute_function(request: PromptRequest):
    """Retrieve and execute a function, with logging & monitoring."""
    
    logging.info(f"Received API request: {request.prompt}")  # Log request

    if "last function" in request.prompt.lower():
        last_function = get_last_function()
        if last_function:
            logging.info(f"Returning last function: {last_function}")
            return {"status": "Last function retrieved.", "last_function": last_function}
        else:
            logging.warning("No previous function found.")
            return {"error": "No previous function found."}

    function_name = retrieve_function(request.prompt)
    logging.info(f"Retrieved function: {function_name}")

    code = generate_code(function_name)

    # ✅ Execute Function & Log it
    if function_name == "open_calculator":
        open_calculator()
        logging.info("Executed: open_calculator")
        return {"function": function_name, "code": code, "status": "Calculator opened successfully."}

    elif function_name == "get_cpu_usage":
        result = get_cpu_usage()
        logging.info(f"Executed: get_cpu_usage, Result: {result}")
        return {"function": function_name, "code": code, "status": "Executed successfully.", "output": result}

    elif function_name == "open_chrome":
        open_chrome()
        logging.info("Executed: open_chrome")
        return {"function": function_name, "code": code, "status": "Chrome opened successfully."}

    logging.warning(f"Function not found for prompt: {request.prompt}")
    return {"error": "Function not found."}

@app.post("/add_function")
def add_custom_function(name: str, description: str):
    """Allows users to add custom functions dynamically."""
    add_function(name, description)
    logging.info(f"New function added: {name} - {description}")
    return {"status": f"Function '{name}' added successfully."}
