#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import Llmbase

from dotenv import load_dotenv

from database import init_db, insert_data
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# create database with sqllite and  create tables and insert data into it


def run():
    """
    Run the crew.
    """
    inputs = {
        "question": "What is the most expensive product?"
    }

    try:
        result = Llmbase().crew().kickoff(inputs=inputs)
        # Fallback: extract the final answer from result.raw using a simple search
        import re
        match = re.search(r'Final Answer:\s*(.+)', str(result.raw))
        if match:
            print(match.group(1).strip())
        else:
            print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == '__main__':
    init_db()
    insert_data()
    run()


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         Llmbase().crew().train(n_iterations=int(
#             sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")


# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         Llmbase().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")


# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
#     try:
#         Llmbase().crew().test(n_iterations=int(
#             sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
