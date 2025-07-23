from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles 
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware 

from .crew import IdeateCrew

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
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"], 
  allow_credentials=True,
  allow_methods=["*"], 
  allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    # This serves the index.html file when someone visits the root URL
    return FileResponse('static/index.html')

@app.post("/ideate_assistant")
def get_ideate_assistance(payload: QueryPayload) -> dict:
  """
  Receives the user's query and Ideate context,
  kicks off the Crew AI process, and returns the result.
  """
  # crew = IdeateCrew(payload.user_query, payload.ideate_context.model_dump_json())
  # result = crew.run()
  
  result = f"Crew AI would now process your query: '{payload}'"
  return {"response": result}

@app.get("/")
def root():
  return {"status": "Ideate Assistant API is running"}