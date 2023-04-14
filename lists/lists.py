class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        max_idx = 0
        for i in range(len(input_list)):
            if input_list[i] > input_list[max_idx]:
                max_idx = i
        for i in range(len(input_list)):
            if input_list[i] > 0:
                input_list[i] = input_list[max_idx]
        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if len(input_list) == 0:
            return -1
        else:
            left_idx = 0
            right_idx = len(input_list) - 1
            return ListExercise.recursion_search(left_idx, right_idx, input_list, query)

    @staticmethod
    def recursion_search(left: int, right: int, lst: list[int], num: int) -> int:
        mid = (right + left + 1) // 2

        if left == right and lst[mid] != num:
            return -1

        if lst[mid] > num:
            right = mid - 1
            return ListExercise.recursion_search(left, right, lst, num)
        elif lst[mid] < num:
            left = mid
            return ListExercise.recursion_search(left, right, lst, num)
        else:
            return mid
