from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import sqlite3


class ListTablesToolInput(BaseModel):
    pass


class ListTablesTool(BaseTool):
    name: str = "List Tables"
    description: str = "Retrieve the names of all tables in the llmbase.db database."
    args_schema: Type[BaseModel] = ListTablesToolInput

    def _run(self) -> str:
        print(' - DB CALL: list_tables()')
        conn = sqlite3.connect('llmbase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()
        return ", ".join([t[0] for t in tables])
