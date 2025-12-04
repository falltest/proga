class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = []
with open("people.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.split(",")
        people.append(People(line[0], int(line[1])))
people.sort(key=lambda x: x.age)

with open('vozrast.txt', 'r', encoding="utf-8") as file:
    vozrast = sorted(list(map(int, file.readline().split())))

vozrast.insert(0, -1)
d = {}
for i in range(len(vozrast) - 1):
    down_ch = vozrast[i]
    up_ch = vozrast[i + 1]
    d[f'{down_ch+1}-{up_ch}'] = []
d[f'{vozrast[-1]+1}+'] = []
ind = 0
it = iter(d)
cur_ch = next(it)
people = sorted(people, key=lambda x: (x.age, x.name))
for human in people:
    while ind < len(vozrast) - 1 and human.age > vozrast[ind + 1]:
        ind += 1
        cur_ch = next(it)
    d[cur_ch].append(human)
ans = []
for el in d:
    if len(d[el]) > 0:
        d[el] = sorted(d[el], key=lambda x: (-x.age, x.name))
        ans.append('')
        ans[-1] += el + ': '
        for i in range(len(d[el]) - 1):
            human = d[el][i]
            ans[-1] += f'{human.name} ({human.age}), '
        ans[-1] += f'{d[el][-1].name} ({d[el][-1].age})'
ans.reverse()
with open('output.txt', 'w', encoding="utf-8") as file:
    for line in ans:
        file.write(line + '\n')
