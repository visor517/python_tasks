# python_tasks

### Задача 1 (Почтальон)

В функцию min_way подается список точек, где под индексом 0 стоит точка старта-финиша.

Далее используется класс Way для хранения промежуточных вычислений маршрута. В объекте
класса хранится множество точек которые нужно посетить, текущая точка, уже пройденный
путь и предварительный вариант ответа. У класса есть методы для вычисления расстояния
между двумя точками и перемещения на следующую точку.

Создается очередь объектов пути.

Обрабатывается очередь. Для очередного объекта пути создаются копии по количеству точек
которые еще нужно посетить. В копиях производятся перемещения на соответствующие точки.
После чего копии помещаются в очередь.
_Такая организация была выбрана из-за планов реализовать второй вариант. Помещать объекты
пути в список на обработку основываясь на текущей длине. С таким подходом первый
завершенный маршрут был бы верным. Но замеры времени показали, что с увеличением числа
точек время наоборот увеличивается (_

Когда из очереди берется уже законченный маршрут, его результат сверяется с промежуточным
и заменяет его если он короче.

Выводится итоговый результат.
