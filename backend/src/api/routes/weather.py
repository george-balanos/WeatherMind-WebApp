import requests

from fastapi import Request, HTTPException, Query, APIRouter

router = APIRouter()

@router.get("/weather")
async def get_weather(
    longitude: float = Query(..., description="Longitude"),
    latitude: float = Query(..., description="Latitude")
):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m&timezone=auto"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch weather data!"}
    
    current_temperature = response.json()["current"]["temperature_2m"]
    units = response.json()["current_units"]["temperature_2m"]

    return {"temperature": current_temperature, "units": units}