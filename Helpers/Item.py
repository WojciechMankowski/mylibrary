from dataclasses import dataclass


@dataclass
class Item:
    title: str
    image: str
    description: str
    writers: str
    number_of_ratings: int = 0
    average_grade: float = 0