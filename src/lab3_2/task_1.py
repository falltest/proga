from collections import defaultdict

class Movie:
    def __init__(self, id, title):
        self.id = id
        self.title = title

class People:
    def __init__(self, films):
        self.films = films

id_films = []
with open('input_films.txt', 'r', encoding='utf-8') as file:
    for line in file:
        ls = line.strip().split(',')
        id_films.append(Movie(int(ls[0]), ls[1]))


peoples_films = []
d = defaultdict(int)
with open('input_people.txt', 'r', encoding='utf-8') as file:
    for line in file:
        ls = list(map(int, line.split(',')))
        for el in ls:
            d[el] += 1
        peoples_films.append(People(set(ls)))

file_out = open('output.txt', 'w', encoding='utf-8')
with open('input.txt', 'r', encoding='utf-8') as file_in:
    s = file_in.readline()
    initial_films = set(list(map(int, s.split(','))))
    rec_films = set()
    for films in peoples_films:
        if len(films.films & initial_films) >= (len(initial_films) / 2):
            rec_films |= films.films
    rec_films -= initial_films
    films_sorted = sorted(d, key=d.get, reverse=True)
    for el in films_sorted:
        if el in rec_films:
            for Film in id_films:
                if Film.id == el:
                    file_out.write(Film.title)
                    file_out.close()
                    exit(0)


