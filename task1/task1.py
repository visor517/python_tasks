'''
Программа для вычисления кратчайшего пути для почтальона.

Почтальон выходит из почтового отделения, объезжает всех адресатов один раз для вручения посылки
и возвращается в почтовое отделение. Необходимо найти кратчайший маршрут для почтальона.
'''

from copy import deepcopy
# import time

# основная функция
def min_way(points: list):

    start_point = points[0]
    points = points[1:]

    # класс маршрута
    class Way:
        def __init__(self):
            self.targets = set(points)
            self.current_point = start_point
            self.length = 0
            self.result = f'{start_point}'

        # шаг к следующей точке
        def reach_point(self, point):
            self.targets.remove(point)
            self.length += self.distance(self.current_point, point)
            self.result += f' -> {point}[{self.length}]'
            self.current_point = point

            # возврат на старт
            if len(self.targets) == 0:
                self.length += self.distance(self.current_point, start_point)
                self.result += f' {start_point}[{self.length}] = {self.length}'
                self.current_point = start_point

        # определяет расстояние между двумя точками
        def distance(self, start_point, end_point):
            return (abs(start_point[0] - end_point[0]) ** 2 + abs(start_point[1] - end_point[1]) ** 2) ** 0.5

    result = [None, None]
    queue = [Way()]

    while queue:
        cur_way = queue[0]
        queue = queue[1:]

        # выводим, если маршрут закончен
        if len(cur_way.targets) == 0:
            if result[0] == None or result[0] > cur_way.length:
                result = [cur_way.length, cur_way.result]

        # разделяем текущий маршрут
        for point in cur_way.targets:
            branch = deepcopy(cur_way)
            branch.reach_point(point)
            queue.append(branch)

    return result[1]


points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]

# start_time = time.time()

print(min_way(points))

# end_time = time.time()
# print(end_time - start_time)  # ~0.0045
