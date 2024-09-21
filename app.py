import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI  # Updated OpenAI class
from langchain.schema.runnable import RunnableSequence  # For using RunnableSequence

# Step 1: Load environment variables from the .env file
load_dotenv()

# Step 2: Get the OpenAI API key from the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Step 3: Ensure the API key is properly loaded
if openai_api_key is None:
    raise ValueError("OpenAI API key is not set in the environment variables")

# Step 4: Set the OpenAI API key as an environment variable for the script to use
os.environ["OPENAI_API_KEY"] = openai_api_key

# Step 5: Define the SQL query prompt template
template = """
You are a SQL expert. Given a request, create a SQL query to satisfy the user's need.
Request: {request}

SQL Query:
"""
prompt = PromptTemplate(
    input_variables=["request"],  # The input variable is the user request
    template=template,            # The template that the model will follow to generate SQL queries
)

# Step 6: Initialize the OpenAI LLM (with low temperature for deterministic outputs)
llm = OpenAI(temperature=0)  # Temperature=0 means more focused and consistent outputs

# Step 7: Create a RunnableSequence for the pipeline-style execution
sequence = prompt | llm

# Step 8: Define a function to generate an SQL query from a user request
def generate_sql_query(user_request):
    # The sequence's `invoke` method takes the user's request and generates the SQL query
    result = sequence.invoke({"request": user_request})
    return result

# Step 9: Example usage of the SQL query generator
if __name__ == "__main__":
    user_request = "Find departments where the average salary is more than 5000"
    sql_query = generate_sql_query(user_request)
    print("Generated SQL Query:\n", sql_query)
