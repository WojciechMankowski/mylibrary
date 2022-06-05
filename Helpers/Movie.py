from dataclasses import dataclass, field
from typing import List
from Item import Item


@dataclass
class Movie(Item):
    actors: str = ""
    type: str = "Movie"

    def __str__(self):
        return f"{self.type}: {self.title}"