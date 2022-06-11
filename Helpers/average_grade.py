
def CalculateTheAverage(new_rating: float, rating_witch_db: float,  number_of_ratings: int) -> float:
    suma = new_rating + rating_witch_db
    number_of_ratings +=1
    average = round(suma/number_of_ratings, 2)
    return average

