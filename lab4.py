from itertools import combinations, groupby

print("Taks 1: ")
string_word = input("Enter your word: ") # вводим любое слово (String)
convert_tuple = tuple(string_word) # переводим string на tuple через команду tuple
print("Converted word:", convert_tuple)

print("--------------------------------")
print("Task 2: ")
tuple_word = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n') 
convert_string = ''.join(tuple_word) # здесь мы используем комманду join так как эта команда обеденяет все элементы а также добавляем '' чтобы не было никаких символов и тд между элементами
print("Output: ", convert_string) # тут прсото идет вывод 



print("--------------------------------")
print("Task 3: ") # в этом задании нужно объяденить два tuple, но только по половине, то есть первая половина и вторая половина tuple комбинируем
a = (1, 2, 3, 4, 5, 6, 7) 
b = (5, 6, 7, 9, 7, 1, 10, 10)
sum = a[:4] + b[4:] # тут в первом tuple мы пишем [:4] потому что он берет первые 4 элемента первого tuple, аналогично [4:] только тут он берет элементы начиная с 5 элемента и до конца
print(sum) # то есть цифра в этом случае определяет с какого элемента начинать или до какого элемента заканчивать, знак который это определяет :

print("--------------------------------")
print("Task 4: ") # в этом задании нужно сделать счетчик элменетов которые повторяются в tuple 
my_tuple = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
element_count = {} # мы создаем пустое хранилище и будем туда пихать элементы которые мы будем находить
for element in my_tuple: # используем цикл for чтобы он проверял элементы столько раз сколько количество элементов в выделенном tuple (my_tuple)
    element_count[element] = element_count.get(element, 0) + 1 # тут самое интересное, он используется для получения текущего значения  element из  element_count, то есть если элемент уже существует в словаре, его значение возвращается, в противном случае возвращается 0, а также +1 просто увеличивает значение element на 1
result_tuple = tuple((k, v) for k, v in element_count.items()) # начну с k и v,  k это уникальный ключ (уникальные элементы) в element_count, а v количество вхождений для каждого ключа, и потом делает подсчеты 
print("Элементы и их вхождения:", result_tuple) # тут просто вывод

print("--------------------------------")
print("Task 5:  ")
# в эта задача про создание кортежа и нужно организовать элементы по данному условию
data = (55, 6, 777, 70.0, '7', 'A')
integers = tuple(x for x in data if isinstance(x, int)) # тут мы используем цикл и условный оператов, цикл для того чтобы он прошелся по всем элементам, а if чтобы он проверил являются ли эти элементы int. 
floats = tuple(x for x in data if isinstance(x, float)) # аналогично с float и str, то есть просто проверят вид данных и выводит
strings = tuple(x for x in data if isinstance(x, str))
print(integers)
print(floats)
print(strings)

print("--------------------------------")
print("Task 6: ")
user_input = input("Enter your word: ")
my_set = {char for char in user_input} #сам не понял что тут сделал, шучу, это генератор множества, который проходит по каждому символу char в строке user_input и добавляет его в множество my_set
# так как в Python множество содержит только уникальные элементы то по логике все элементы которые повторяются будут исключены и в mychar останутся только уникальные
print("Созданное множество:", my_set)

print("--------------------------------")
print("Task 7: ")
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
difference_set = set_A.difference(set_B) # тут мы используем метод difference, то есть по названия можно понять что он отвечает за разницу элементов
# короче говоря difference_set содержит элементы, присутствующие в set_A, но отсутствующие в set_B
print(difference_set)

print("--------------------------------")
print("Task 8: ")
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
set_A.difference_update(set_B) #тут поховая схема но есть различие, в этом случае мы добавляем update, то есть метод difference_update обноваляет (удаляет) разницу элементов
print(set_A)

print("--------------------------------")
print("Task 9: ")
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}

for element in set_C: # создаем цикл чтобы прошелся по всем элементам 
    if element in set_A: # в if если в элементы есть в setA то мы их удаляем и добавляем в setB
        set_A.remove(element)  
        set_B.add(element)     

print("Updated set A:", set_A)
print("Updated set B:", set_B)

print("----------------------------------------------------------------")
print("Task 10: ") # для это задачи мы импортируем библиотеку itertools (я не знаю как это называется но в Java это библиотеки) для использование метод combination
A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5
result = [set(combo) for combo in combinations(A, n)][:m] # здесь для каждой созданной комбинации преобразуется в множество (set), это делается для каждой комбинации
# также [:m] штука которая была уже ранее, то есть m это просто до какого элемента отсавлять, в этом случае m=5 то есть оставляет только первые 5 комбинации
print(result)

print("----------------------------------------------------------------")
print("Task 11: ") # тут также понадобится itertools 
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

sorted_cars = sorted(cars_list, key=lambda x: x[0]) # в этой задаче мы делаем сортировку по manufacter и group моделей машин
for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]): # key=lambda x: x[0] - это анонимная (лямбда) функция, которая принимает элемент x и возвращает значение x[0], то есть первый элемент кортежа, в данном случае, марку автомобиля
    group_list = list(group)
    count = len(group_list)
    models = [car[1] for car in group_list]
    print(f"{manufacturer} {count} - {', '.join(models)}")