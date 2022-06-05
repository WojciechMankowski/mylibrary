# TODO założyć bazę danych
from  dataclasses import dataclass



@dataclass
class DataBase:
    host: str
    port: int

    def __int__(self, ):
        self.connect = self.connect_db()
        self.db = ""

    def connect_db(self):
        ...
    def add_item(self, **kwargs): ...

    def find_item(self): ...

    def find_item_title(self, title: str): ...




# if __name__ == '__main__':
#     db = MongoDB(host="localhost", port=27017)
#     db.connect_db()
#     # db.add_item(title = "Men", autor = "AA", greade = 3, how_grade = 2, desciption = "",
#     #             type = "Movie", year="2021",
#     #             time="2 h 30 mint", image = "", writers="")
#     # title = "Men", autor = "AA", greade = 3, how_grade = 2, desciption = "", type = "Movie"
#     x = db.find_item_title("Men")
#     print(x)
#     # db.delet_item(title = "Men")
#     # db.find_item()