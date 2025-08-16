import json

from typing import Literal
from pydantic import BaseModel, ValidationError
from ollama import chat

class DomainResponse(BaseModel):
    domain: Literal["weather", "other"]

class DomainVerifier:
    def __init__(self, model_name):
        self.model = model_name
    
    def classify_input_domain(self, input_query):
        system_prompt = {
            "role": "system",
            "content": """You are an AI Agent. Classify the user query as either 'weather' or 'other'.

## Output Rules
- Output **only** a single JSON object.
- The object must have exactly one key: "domain".
- "domain" must be either "weather" or "other" (lowercase).
- No extra keys, no explanations, no second JSON object, no schema.

Example of correct output:
{
  "domain": "weather"
}"""
        }

        response = chat(
            model=self.model,
            messages=[
                system_prompt,
                {
                    "role": "user",
                    "content": input_query
                }
            ],
            options={"temperature": 0}
        )

        raw_output = response["message"]["content"].strip()

        print(raw_output)

        try: 
            domain = DomainResponse.model_validate_json(raw_output)
            return domain
        except ValidationError as e:
            print("\nValidation Error: \n", e)
            return None
        
if __name__ == "__main__":

    dv = DomainVerifier(model_name="llama3.1:8b-instruct-q2_K")

    query = "How is the weather today?"
    print(dv.classify_input_domain(query))


