from crewai import Crew, Process
from .agents import IdeateAgents
from .tasks import IdeateTasks

class IdeateCrew:
  def __init__(self, user_query, ideate_context):
    self.user_query = user_query
    # self.user_customer = ideate_context.user_customer
    # self.problem_opportunity = ideate_context.problem_opportunity
    # self.innovation_uvp = ideate_context.innovation_uvp
    # self.solution_product = ideate_context.solution_product
    self.ideate_context = ideate_context

  def run(self):
    agents = IdeateAgents()
    tasks = IdeateTasks()

    market_validation = agents.user_and_problem()
    competitive_intelligence = agents.innovation_and_solution()
    product_strategist = agents.general_reviewer()

    market_validation_task = tasks.problem_analysis_task(market_validation, self.user_query, self.ideate_context)
    competitive_intelligence_task = tasks.solution_analysis_task(competitive_intelligence, self.user_query, self.ideate_context)
    product_strategist_task = tasks.strategy_synthesis_task(product_strategist, self.user_query, self.ideate_context)

    crew = Crew(
      agents=[market_validation, competitive_intelligence, product_strategist],
      tasks=[market_validation_task, competitive_intelligence_task, product_strategist_task],
      process=Process.sequential,
      verbose=2,
    )

    result = crew.kickoff()
    return result