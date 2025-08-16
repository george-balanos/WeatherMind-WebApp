import json

from pydantic import BaseModel, ValidationError
from ollama import chat

class Coordinates(BaseModel):
    longitude: float
    latitude: float
    temperature_units: str
    name_of_location: str

class CoordinateGenerator:
    def __init__(self, model_name):
        self.model = model_name

    def generate_coordinates(self, user_query):
        system_prompt = {
            "role": "system",
            "content": f"""You are an AI Agent.

        ## Instructions
        1. Provide the exact coordinates of the location referenced in the user query.
        2. Provide the name of the location.
        3. The JSON must have exactly these keys: longitude, latitude, temperature_units, name_of_location.

        Output MUST be a valid JSON object matching this schema:

        {json.dumps(Coordinates.model_json_schema(), indent=2)}

        Do not include any nested objects or properties field.
        Do not include any extra text, explanations, or comments — only the JSON."""
        }

        response = chat(
            model=self.model,
            messages=[
                system_prompt,
                {
                    "role": "user",
                    "content": user_query
                }
            ],
            options={"temperature": 0}
        )

        raw_output = response["message"]["content"].strip()

        try:
            coords = Coordinates.model_validate_json(raw_output)
            return coords
        except ValidationError as e:
            print("\nValidation Error: \n", e)

if __name__ == "__main__":

    cg = CoordinateGenerator(model_name="llama3.1:8b-instruct-q2_K")

    query = "How is the weather today in Ioannina?"
    print(cg.generate_coordinates(query))