def generate_code(function_name):
    """Generates a Python script for executing the function."""
    return f"""
from automation_functions import {function_name}

def main():
    try:
        result = {function_name}()  # Execute function
        print(result if result else "{function_name} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
