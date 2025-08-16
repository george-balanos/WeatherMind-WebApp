FROM python:3.10.2

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD bash -c "ollama serve & sleep 2 && ollama pull llama3.2:3b-instruct-q8_0 && uvicorn src.api.main:app --host 0.0.0.0 --port 8000"