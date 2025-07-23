from crewai import Task
from textwrap import dedent

class IdeateTasks:
  def problem_analysis_task(self, agent, user_query, ideate_context):
    return Task(
      description=dedent(f'''
        **Task**: Analyze the Problem-User Fit.
        **Description**: 
        As a Market Validation Expert, your job is to critically analyze the "User or Customer" and "Problem or Opportunity" sections of the user's submission. 
        You must determine if the problem is significant and if the chosen user group is the right one to target. 
        Perform logical reasoning and, if necessary, use your search tools to find data that supports or refutes the problem's scale and impact.

        **Parameters**:
        - User's Query: {user_query}
        - Ideate Submission: {ideate_context}

        **Note**: 
        The user is in the early stages of ideation. Your feedback should be constructive and critical, aimed at strengthening their core concept. 
        Your analysis will be the foundation for the entire idea evaluation.
      '''),
      expected_output=dedent(f'''
        A concise, two-paragraph analysis. The first paragraph should detail your findings on the problem's significance and the user fit. 
        The second paragraph must conclude with a clear and bolded verdict: **Strong Problem-User Fit**, **Medium Problem-User Fit**, or **Weak Problem-User Fit**.
      '''),
      agent=agent
    )

  def solution_analysis_task(self, agent, user_query, ideate_context):
    return Task(
      description=dedent(f'''
        **Task**: Analyze the Solution & Competitive Landscape.
        **Description**: As a Competitive Intelligence Analyst, your job is to analyze the "Solution or Product" and "Innovation" sections of the submission. 
        You must use the prior "Problem-User Fit" analysis as a starting point. Your goal is to determine if the solution is a viable competitor in the current market.

        **Parameters**:
        - User's Query: {user_query}
        - Ideate Submission: {ideate_context}

        **Note**: Use your search tools to find existing products and competitors. The quality of your competitive analysis is critical for determining 
        if this idea has a real chance to succeed.
      '''),
      expected_output=dedent(f'''
        A concise, two-paragraph analysis. The first paragraph should summarize the competitive landscape and how the proposed solution fits in. 
        The second paragraph must conclude with a clear and bolded verdict: **High Innovation Potential**, **Medium Innovation Potential**, or **Low Innovation Potential**.
      '''),
      agent=agent
    )

  def strategy_synthesis_task(self, agent, user_query, ideate_context):
    return Task(
      description=dedent(f'''
        **Task**: Synthesize Analyses and Formulate Final Response.
        **Description**: As the Lead Product Strategist, your final task is to synthesize the 'Problem-User Fit Analysis' and the 'Competitive Landscape Analysis' into 
        a single, coherent, and actionable recommendation for the user. Your response must directly address the user's original query.

        **Parameters**:
        - User's Query: {user_query}
        - Ideate Submission: {ideate_context}

        **Note**: This is the final output the user will see. It must be clear, encouraging, and directly helpful. 
        Combine the insights from the previous experts into a unified strategy.
      '''),
      expected_output=dedent(f'''
        A final, user-facing response of 3-4 paragraphs. It must directly answer the user's original query, seamlessly 
        integrating the key findings about the problem, user, solution, and competitive market.
      '''),
      agent=agent
    )