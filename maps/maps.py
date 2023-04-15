from typing import Union
from functools import reduce
from collections import Counter


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def _country_and_rating_check(dict_obj: dict) -> float:
            countries = dict_obj["country"].split(",")
            rating_kino = dict_obj["rating_kinopoisk"]
            if len(countries) > 1 and rating_kino != "":
                return float(rating_kino)
            return -1

        ratings_list = list(filter(lambda x: x > 0, map(_country_and_rating_check, list_of_movies)))
        avg_rating = reduce(lambda x, y: x + y, ratings_list) / len(ratings_list)
        return avg_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def _rating_filter(dict_obj: dict) -> str:
            rating_value = dict_obj["rating_kinopoisk"]
            movie_name = dict_obj["name"]
            if rating_value != "" and float(rating_value) >= rating:
                return movie_name
            return ""

        def _count_letter(phrase: str) -> int:
            counter = Counter(phrase)
            letter_count = counter["и"]
            return letter_count

        names_list = list(filter(None, map(_rating_filter, list_of_movies)))
        result = reduce(lambda x, y: x + y, map(_count_letter, names_list), 0)
        return result
