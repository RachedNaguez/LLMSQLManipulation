from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import sqlite3


class ExecuteQueryToolInput(BaseModel):
    sql: str = Field(..., description="SQL SELECT query to execute.")


class ExecuteQueryTool(BaseTool):
    name: str = "Execute Query"
    description: str = "Execute an SQL SELECT statement and return the results."
    args_schema: Type[BaseModel] = ExecuteQueryToolInput

    def _run(self, sql: str) -> str:
        print(f' - DB CALL: execute_query({sql})')
        conn = sqlite3.connect('llmbase.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return str(results)
