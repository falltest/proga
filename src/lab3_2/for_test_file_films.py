import random


with open('input_films.txt', 'w', encoding='utf-8') as file:
    for i in range(1, 1001): #количество фильмов - 1000
        file.write(f'{i},фильм_номер_{i}\n')

with open('input_people.txt', 'w', encoding='utf-8') as file:
    for i in range(1, 101): #количество людей - 100
        for z in range(1, random.randint(1, 100) - 1): #количество просмотренных фильмов от 1 до 100
            file.write(str(random.randint(1, 1000)) + ',')
        file.write(str(random.randint(1, 1000)) + '\n')