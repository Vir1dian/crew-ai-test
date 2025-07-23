# Ideate AI Assistant (crew-ai-test)
This project is a demo of an AI assistant built with Crew AI to help users with the "Ideate" activity for PilotCity R&D.

## Requirements:
1. Python 3.12
2. Poetry

## Setup:
1. Copy example `.env` and add your own OpenAI and Serper API keys
2. Run the following from root directory (Installs all dependencies listed in `pyproject.toml`)

    ```
    poetry install
    ```

## Run Application:
1. Run the following from root directory (Serve application with FastAPI)

    ```
    poetry run uvicorn ideate_assistant.main:app --reload
    ```

2. Open your web browser and navigate to http://127.0.0.1:8000 