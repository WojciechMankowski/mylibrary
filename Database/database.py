import sqlite3
from  dataclasses import dataclass
from typing import List
from Helpers.Movie import Movie

@dataclass
class SQLLite:

    name_file: str
    def connect_db(self):
        self.connect = sqlite3.connect(self.name_file)
        self.cursor = self.connect.cursor()

    def CreateTable(self, name_table: str, collection_columns, type_columns):
        query = f"CREATE TABLE {name_table}   ("
        for index in range(0, len(collection_columns)):

            if index != len(collection_columns) - 1:
                query += f"{collection_columns[index]} {type_columns[index]} ,"
            else:
                query += f"{collection_columns[index]} {type_columns[index]} "

        query += ")"
        self.cursor.execute(query)

    def AddItem(self, nametable: str, *kwags):
        query = f"INSERT INTO {nametable} VALUES  {kwags}"
        self.cursor.execute(query)
        self.connect.commit()


    def FindAllItem(self, nametable: str) -> List[Movie]:
        query = f"Select * from {nametable}"
        collection_items: List[Movie] = []
        result = self.cursor.execute(query)
        for item in result:
            items = Movie(item[0], item[6], item[4], item[1], item[3], item[2], item[7])
            collection_items.append(items)
        return collection_items

    def FindHow_Grade(self, nametable: str, title: str) -> int:
        query = f"SELECT how_grade, Greade FROM {nametable} WHERE title = '{title}'"
        result = self.cursor.execute(query)
        item = result.fetchone()
        return item
    def UpdateItem(self, nametable: str, rate: float, title: str, how_grade):

        query = f"UPDATE {nametable} SET Greade = {rate}, how_grade={how_grade+1} WHERE title = '{title}'"
        self.cursor.execute(query)
        self.connect.commit()
    def __del__(self):
        self.connect.close()
if __name__ == '__main__':
    db = SQLLite("../kultura.db")
    db.connect_db()
    db.FindAllItem("Movie")
    