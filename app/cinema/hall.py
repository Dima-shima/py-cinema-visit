from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

class CinemaHall:
    def __init__(self, hall_number) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for i in customers:
            Customer.watch_movie(i, movie_name)
        print(f'"{movie_name}" ended.')
        Cleaner.clean_hall(cleaning_staff, self.hall_number)
