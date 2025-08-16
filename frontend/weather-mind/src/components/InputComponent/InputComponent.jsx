import { useState } from "react";

function InputComponent() {
    const [temperature, setTemperature] = useState("-")
    const [units, setUnits] = useState("-")
    const [coordinates, setCoordinates] = useState("-")

    const handleSubmit = (event) => {
        event.preventDefault();

        const user_query = event.target.elements.llm_input.value;
        event.target.elements.llm_input.value = "";

        console.log(user_query)
        
        fetch("http://localhost:8000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                query: user_query 
            })
        })
        .then(response => response.json())
        .then(data => {
            setTemperature(data["temperature"]);
            setUnits(data["units"]);
            setCoordinates(data["coordinates"]);
        })
        .catch(err => {
            console.error("Something went wrong: ", err);
        })
    };

    return (
        <>
            <div className="input-panel">
                <h1>WeatherMind</h1>
                <div className="weather-info">
                    <div className="weather-display">
                        <span className="weather-diplay-span">Temperature: <span class="text-display">{temperature} {units}</span></span>
                        <br/>
                        <span className="weather-diplay-span">Location cordinates:<br /> <span class="text-display">{coordinates}</span></span>
                    </div>
                    <form action="submit" id="input-form" onSubmit={handleSubmit}>
                        <label htmlFor="lln-input" id="llm-input-label">Ask our <span id="ai">AI</span> for any location’s temperature</label>
                        <div className="input-container">
                            <textarea name="llm_input" id="llm-input" placeholder="Type here..."/>
                        </div>
                        <button type="submit">
                            Confirm
                        </button>
                    </form>
                </div>
            </div>
        </>
    )
}

export default InputComponent;