# Weather-Mind Web App

A full-stack web application combining **React frontend**, **FastAPI backend**, and **Ollama LLM** for local AI queries. Fully Dockerized for easy setup and sharing.

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

## Environment Variables

### Backend

- `OLLAMA_URL` → URL to the Ollama service
  - In Docker: `http://ollama:11434`
  - Local fallback: uses Ollama Python library directly

### Frontend

- `REACT_APP_API_URL` → URL to backend API
  - Local dev: `http://localhost:8000`
  - In Docker: `http://backend:8000`

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

## Docker Networking Notes

- Each container has its own network namespace.
- Services communicate by **Docker service name** (e.g., `backend`, `ollama`) instead of `localhost`.
- Inside Docker:
  - Frontend → Backend: `http://backend:8000`
  - Backend → Ollama: `http://ollama:11434`

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

- Use `.env` files for switching between **local dev** and **Dockerized environment**.

---

## Troubleshooting

- **Ollama not responding in Docker**
  - Make sure the `ollama` container is running
  - Backend should use `OLLAMA_URL=http://ollama:11434`
- **Ports conflicts**
  - Ensure `3000` (frontend) and `8000` (backend) are free on your host machine
- **Frontend can’t reach backend**
  - In Docker, frontend must call `http://backend:8000`, not `localhost:8000`

---

## License

MIT License

