from dataclasses import dataclass, field
from .Item import Item

@dataclass
class Movie(Item):
    time: str = "0"
    actors: str = ""
    type: str = "Movie"

    def __str__(self):
        return f"{self.type}: {self.title}"