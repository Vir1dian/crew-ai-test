from crewai import Agent
from langchain_openai import ChatOpenAI
from .tools.search_tools import search_tool, scrape_tool

from textwrap import dedent

class IdeateAgents():
  def __init__(self):
    self.llm = ChatOpenAI(model="gpt-3.5-turbo")

  def user_and_problem(self):
    return Agent(
      role='Market Validation Expert',
      goal=dedent(f""" 
        Validate whether the identified problem is real and significant for the defined user group. 
        Deliver a clear verdict on the problem-user fit based on logic and available data.
      """),
      backstory=dedent(f""" 
        As a former lead researcher for a top-tier venture capital firm, I've spent my career dissecting thousands of startup pitches. 
        My expertise lies in cutting through the noise to identify genuine, high-value user problems and verifying target customer bases.        
      """),
      tools=[
        search_tool,
        scrape_tool,
      ],
      verbose=True, 
      llm=self.llm,
    )
  
  def innovation_and_solution(self):
    return Agent(
      role='Competitive Intelligence Analyst',
      goal=dedent(f""" 
        Analyze the proposed solution and its unique value against the current market. 
        Identify key competitors and deliver a concise summary of the competitive landscape and the idea's level of true innovation.
      """),
      backstory=dedent(f""" 
        With a background as a senior tech journalist for The Verge and later a product manager at a major SaaS company, 
        I excel at reverse-engineering products and mapping market dynamics.
        I have a knack for quickly identifying established players and uncovering the subtle nuances that define a truly unique and defensible product.
      """),
      tools=[
        search_tool,
        scrape_tool,
      ],
      verbose=True,
      llm=self.llm,
    )

  def general_reviewer(self):
    return Agent(
      role='Lead Product Strategist',
      goal=dedent(f""" 
        Synthesize the analyses of the problem-user fit and the competitive landscape to provide a final, actionable recommendation. 
        Answer the user's specific query with a holistic strategic assessment of their idea.
      """),
      backstory=dedent(f""" 
        I am a seasoned product leader who has successfully guided multiple products from a simple sketch to market leadership. 
        Having navigated the entire product lifecycle, I specialize in connecting the dots between user needs, market realities, 
        and product features to form a coherent and winning strategy.
      """),
      # tools=[
      #   
      # ],
      verbose=True,
      llm=self.llm,
    )