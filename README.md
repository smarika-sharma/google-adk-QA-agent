# Google ADK QA Agent

A multi-agent system built with Google ADK for handling Quality Assurance and testing tasks, with specialized sub-agents for different functionalities.

## Project Structure

```
root_agent/
├── agent.py                 # Main root agent configuration
└── sub_agents/
    ├── greeting_agent/      # Handles greetings and farewells
    ├── off_topic_guard_agent/ # Manages off-topic queries
    └── tester_agent/        # Performs visual testing using Playwright
```

## Prerequisites

- Python 3.10 or higher
- Google ADK
- Playwright (for visual testing)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/smarika-sharma/google-adk-QA-agent.git
cd google-adk-QA-agent
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install
```

## Agent System

### Root Agent
The main coordinating agent that analyzes user queries and routes them to appropriate specialized sub-agents.

### Sub-Agents

1. **Greeting Agent**
   - Handles greetings and farewells
   - Manages basic social interactions
   - Provides friendly responses

2. **Off-Topic Guard Agent**
   - Identifies and handles off-topic queries
   - Redirects conversations back to relevant topics
   - Maintains conversation focus

3. **Tester Agent**
   - Performs visual testing using Playwright
   - Captures screenshots
   - Performs basic visual checks
   - Reports testing results

## Usage

1. Start the ADK server:
```bash
adk serve
```

2. Access the development UI at `http://localhost:8000/dev-ui`

3. Example queries:
   - Greetings: "hi", "hello", "good morning"
   - Testing: "run a visual test", "check the page appearance"
   - Off-topic: "what is git?", "tell me about programming"

## Features

- Multi-agent architecture
- Intelligent query routing
- Visual testing capabilities
- Off-topic detection and handling
- Friendly social interactions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 