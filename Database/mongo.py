from typing import List
from pymongo import MongoClient
from Database.database import DataBase
from Helpers.Movie import Movie


class MongoDB(DataBase):

    def __int__(self):
        self.connect = self.connect_db()

    # łączy się z bazą danych
    def connect_db(self):
        client = MongoClient(host="localhost", port=27017)
        self.db = client["rptutorials"]

    # dodaje nowy element
    def add_item(self, **kwargs):
        print(kwargs["data"])
        movie = self.db.movie
        movie.insert_one(kwargs["data"])
        # print(resultat.title)

    # szuka wszystkie elementy w bazie danych i zwraca lsitę tych obiektów
    def find_item(self) -> List[Movie]:
        movie = self.db.movie
        resultat = movie.find()
        collections_items: List[Movie] = []
        for item in resultat:
            movie_item = Movie(
                title=item["title"], actors=item['autor'], image=item["image"],
                description=item['desciption'], writers=item["autor"],
                average_grade=item['greade'], number_of_ratings=item['how_grade'],

                type="Movie"
            )
            collections_items.append(movie_item)
        return collections_items

    # usuwa element pasujący do przekazanych danych
    def delet_item(self, **kwargs) -> bool:
        movie = self.db.movie
        r = movie.delete_one(kwargs)
        print()
        if r.deleted_count != 0:
            return True
        else:
            return False

    # szuka elementu w bazie danych po tytule
    def find_item_title(self, title: str) -> List[Movie]:
        movie = self.db.movie
        resultat = movie.find({"title": title})
        collections_items: List[Movie] = []
        for item in resultat:
            movie_item = Movie(
                title=item["title"], actors=item['autor'], image=item["image"],
                description=item['desciption'], writers=item["writers"],
                average_grade=item['greade'], number_of_ratings=item['how_grade'],

                type="Movie"
            )
            collections_items.append(movie_item)
        return collections_items

if __name__ == '__main__':
    db = MongoDB(host="localhost", port=27017)
    db.connect_db()
    text = """
        Harry jest jedyną osobą, której udaje się przeżyć spotkanie ze złym czarnoksiężnikiem - Lordem Voldemortem. W zdarzeniu jednak giną jego rodzice. Osierocony trafia pod opiekę ciotki Petunii i wuja Vernona.
    """
    print(len(text))
    # x = db.delet_item(title="HARRY POTTER I KAMIEŃ FILOZOFICZNY")
    # # print(x)
    # l = db.find_item()
    # for item in l:
    #     print(item.title)
    #     # print(item.description)
    #     # print(len(item.description))