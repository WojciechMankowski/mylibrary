from dataclasses import dataclass, field
from .Item import Item

@dataclass
class Movie(Item):
    actors: str = ""
    type: str = "Movie"

    def __str__(self):
        return f"{self.type}: {self.title}"

    def data_to_json(self):
        return {
            "title": self.title, "autor": self.writers, "greade": self.average_grade,
            "how_grade": self.number_of_ratings, "desciption": self.description, "type": self.type,
            "image": self.image, "actors": self.actors
        }