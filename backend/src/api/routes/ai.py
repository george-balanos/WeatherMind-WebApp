import requests

from fastapi import Request, HTTPException, Query, APIRouter
from ..services.agents.domain_verifier import DomainVerifier
from ..services.agents.coordinate_generator import CoordinateGenerator
from .weather import get_weather

router = APIRouter()

model = "llama3.2:3b-instruct-q8_0"
domain_verifier = DomainVerifier(model_name=model)
coordinate_generator = CoordinateGenerator(model_name=model)

@router.post("/ask")
async def query_agent(request: Request):
    data = await request.json()
    
    user_query = data["query"]
    is_relevant = domain_verifier.classify_input_domain(user_query)

    empty_response = {
        "temperature": 0,
        "units": "",
        "coordinates": "Not found"
    }

    if is_relevant:
        coords_info = coordinate_generator.generate_coordinates(user_query)

        if coords_info:

            long = coords_info.longitude
            lat = coords_info.latitude
            name = coords_info.name_of_location

            weather_info = await get_weather(long, lat)

            return {
                "coordinates": f"lat: {lat} long: {long}",
                "units": weather_info["units"],
                "name": name,
                "temperature": weather_info["temperature"]
            }
    
        else:
            return empty_response
    else:
        return empty_response