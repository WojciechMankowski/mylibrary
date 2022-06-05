from dataclasses import dataclass


@dataclass
class Item:
    id: str
    title: str
    image: str
    year : str
    time: str
    description: str
    writers: str
    number_of_ratings: int = 0
    average_grade: float = 0