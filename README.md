
# Llmbase Crew

Welcome to the Llmbase Crew project, powered by [crewAI](https://crewai.com). This project demonstrates a multi-agent AI system that can interact with an SQL database for a computer store. Agents collaborate to answer user questions by translating them into SQL queries, exploring the database schema, and returning clear, data-driven answers.

## Features

- Multi-agent architecture using CrewAI
- Agents equipped with SQL tools: list tables, describe table, and execute queries
- Example SQLite database for a computer store (products, staff, orders)
- Easily customizable agents and tasks via YAML configuration
- Simple entry point for running and testing your crew

## Installation

Ensure you have Python >=3.10 and <3.13 installed.  
This project uses [UV](https://docs.astral.sh/uv/) for dependency management.

Install UV if you haven't already:

```bash
pip install uv
```

Navigate to your project directory and install dependencies:

```bash
uv pip install -r requirements.txt
```

Or, if using the CrewAI CLI:

```bash
crewai install
```

## Setup

1. **Add your `OPENAI_API_KEY` to the `.env` file** in the project root.
2. The SQLite database (`llmbase.db`) will be created automatically when you run the project.

## Customization

- Edit `src/llmbase/config/agents.yaml` to define your agents and their roles.
- Edit `src/llmbase/config/tasks.yaml` to define your tasks and expected outputs.
- Edit `src/llmbase/crew.py` to add or modify agent logic and tools.
- Edit `src/llmbase/main.py` to change the questions or inputs for your agents.

## Running the Project

To initialize the database, insert sample data, and run your crew, execute:

```bash
python src/llmbase/main.py
```

You can modify the question in `main.py` to ask anything about the computer store database, such as:

- "What is the cheapest product?"
- "List all staff members."
- "How many orders did John Doe make?"

## Example Output

When you run the project, you will see a detailed execution trace of the agents' reasoning and tool usage, followed by the final answer, for example:

```
The most expensive product is the Laptop, with a price of 799.99.
```

## Understanding Your Crew

- **Agents**: Defined in `config/agents.yaml`, each with unique roles and access to SQL tools.
- **Tasks**: Defined in `config/tasks.yaml`, specifying what the agents should accomplish.
- **Tools**: SQL utilities (list tables, describe table, execute query) implemented as CrewAI tools in `database.py`.

## Support

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with CrewAI Docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of CrewAI!
