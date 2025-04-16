from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import sqlite3


class DescribeTableToolInput(BaseModel):
    table_name: str = Field(..., description="Name of the table to describe.")


class DescribeTableTool(BaseTool):
    name: str = "Describe Table"
    description: str = "Look up the schema of a table in the llmbase.db database."
    args_schema: Type[BaseModel] = DescribeTableToolInput

    def _run(self, table_name: str) -> str:
        print(f' - DB CALL: describe_table({table_name})')
        conn = sqlite3.connect('llmbase.db')
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        schema = cursor.fetchall()
        conn.close()
        # Format as "column_name (type)"
        return ", ".join([f"{col[1]} ({col[2]})" for col in schema])
