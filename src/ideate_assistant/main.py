from fastapi import FastAPI
from pydantic import BaseModel

class IdeateContext(BaseModel):
  user_customer: str
  problem_opportunity: str
  innovation_uvp: str  # innovation or unique value proposition
  solution_product: str

class QueryPayload(BaseModel):
  user_query: str
  ideate_context: IdeateContext

app = FastAPI(
  title="PilotCity Ideate Assistant API",
  description="An API for getting help with the Ideate activity."
)

@app.post("/ideate_assistant")
def get_ideate_assistance(payload: QueryPayload) -> dict:
  """
  Receives the user's query and Ideate context,
  kicks off the Crew AI process, and returns the result.
  """
  # Extract the data from the payload
  inputs = {
    'user_query': payload.user_query,
    'ideate_context': payload.ideate_context.model_dump_json() # Pass context as a JSON string
  }

  # Kick off the crew
  # ideate_crew = IdeateCrew()
  # result = ideate_crew.kickoff(inputs=inputs)
  
  result = f"Crew AI would now process your query: '{payload.user_query}'"
  return {"response": result}

@app.get("/")
def root():
  return {"status": "Ideate Assistant API is running"}