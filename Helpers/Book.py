from dataclasses import dataclass

from .Item import Item

@dataclass
class Book(Item):
    type: str = "Book"