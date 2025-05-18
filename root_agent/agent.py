from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import Session
from google.adk.memory import InMemoryMemoryService
from dotenv import load_dotenv

from root_agent.sub_agents.greeting_agent.agent import greeting_agent
from root_agent.sub_agents.off_topic_guard_agent.agent import off_topic_guard_agent
from root_agent.sub_agents.tester_agent.agent import tester_agent

load_dotenv('./.env')

root_agent_model="gemini-2.0-flash-exp"
greeting_agent_model="gemini-2.0-flash"


session_service= InMemoryMemoryService()

APP_NAME="Google_ADK"
USER_ID= "user_1"
SESSION_ID="session_1"

session= Session(
    app_name= APP_NAME,
    user_id= USER_ID,
    id= SESSION_ID,
)

session= session_service.add_session_to_memory(session= session)

root_agent= Agent(
    name= "root_agent",
    model=root_agent_model,
    description="The main coordinating agent that analyzes user queries and routes them to appropriate specialized sub-agents.",
    instruction="""
    **Subagents**:
- greeting_agent: Handles greeting and farewell queries
- off_topic_guard_agent: Handles off-topic queries other than related to Quality Assurance or Software Testing
- tester_agent: Handles visual testing and quality assurance tasks

**Decision Process**:
1. Analyze incoming user query
2. Classify query type (greeting, farewell, off-topic, testing, etc.)
3. Route to appropriate sub-agent
4. Return sub-agent's response

**Response Guidelines**:
- Maintain professional and clear communication
- Ensure responses are contextually appropriate
- Handle errors gracefully with informative messages

**Subagent Selection Logic**:
- If query contains greetings like "hi", "hello", "hey", "good morning", etc. → greeting_agent
- If query contains farewells like "bye", "goodbye", "see you", etc. → greeting_agent
- If query is about testing, QA, or visual testing → tester_agent
- If query is about general topics not related to QA/Testing (like git, programming, etc.) → off_topic_guard_agent
- For all other queries, handle them directly as the root agent

IMPORTANT: Always route greeting and farewell queries to the greeting_agent, regardless of other content in the query.
""",
    sub_agents=[greeting_agent, off_topic_guard_agent, tester_agent]
    )

runner_root= Runner(
    app_name=APP_NAME,
    session_service= session,
    agent= root_agent,
)