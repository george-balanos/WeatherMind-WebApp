# Weather-Mind Web App

* A full-stack web application combining React frontend, FastAPI backend, and Ollama LLM for local AI queries.
* This app allows users to ask the LLM for the current temperature in a specific location (approximately 5 minutes prior). Fully Dockerized for easy setup and sharing.
* The application uses Open-Meteo(https://open-meteo.com/), a free weather forecast API (usage may be limited by IP-based throttling)⚠️

### ⚠️ Caution: For better performance, users can switch to a more advanced LLM by changing the corresponding model name in the docker-compose.yml.

### LLM currently used: ```llama3.2:3b-instruct-q8_0```

---

<img width="1918" height="905" alt="Στιγμιότυπο οθόνης 2025-08-16 203845" src="https://github.com/user-attachments/assets/dfcd2bbe-ec37-4275-958c-4e4d0e309cc4" />

---

## Project Structure

```
weather-mind/
│
├── backend/             # FastAPI backend
│   ├── src/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/            # React frontend
│   ├── weather-mind/
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml   # Orchestrates frontend, backend, Ollama
└── README.md
```

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Docker Compose

Optional (if running locally without Docker):

- Ollama installed on your machine

---

## Running the App

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-mind.git
cd weather-mind
```

### 2. Build and run with Docker

```bash
docker-compose up --build
```

This will start three containers:

- **frontend** → React app ([http://localhost:3000](http://localhost:3000))
- **backend** → FastAPI API ([http://localhost:8000](http://localhost:8000))
- **ollama** → Ollama AI server (internal API for backend)

### 3. Access the App

- Frontend UI: [http://localhost:3000](http://localhost:3000)
- Backend API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Development Notes

- Frontend can still be run locally:

  ```bash
  cd frontend/weather-mind
  npm install
  npm start
  ```

- Backend can still be run locally:

  ```bash
  cd backend
  uvicorn src.api.main:app --reload
  ```
---

License

MIT License

## License

MIT License

