import matplotlib.pyplot as plt

f = open('lion.txt', 'r', encoding='UTF-8')  # открываем
t = f.read()  # читаем
f.close()  # закрываем
print('файл прочитан')  # отчёт

w = t.split()  # слова
n = len(w)  # число
print('слова готовы')  # отчёт

d = {}  # словарь
for x in w:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def k(i):  # функция для сортировки
    return i[1]

sw = sorted(d.items(), key=k, reverse=True)  # сортируем слова
print('слова отсортированы')  # отчёт

o = open('word_stats.csv', 'w', encoding='UTF-8')  # файл
o.write('Слово,Частота встречи, раз,Частота встречи в %\n')  # шапка
for x in sw:
    pr = round(x[1] / n * 100, 2)  # процент
    o.write(x[0] + ',' + str(x[1]) + ',' + str(pr) + '\n')  # строка
o.close()  # закрываем
print('таблица сохранена')  # отчёт

b = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # алфавит
ld = {}  # буквы
for x in t:
    if x.lower() in b:  # проверка
        xl = x.lower()
        if xl in ld:
            ld[xl] = ld[xl] + 1
        else:
            ld[xl] = 1
print('буквы посчитаны')  # отчёт

sl = sorted(ld.items(), key=k, reverse=True)  # сортируем буквы

lt = []  # буквы
ct = []  # числа
for x in sl:
    lt.append(x[0])
    ct.append(x[1])

plt.bar(lt, ct, color='skyblue')  # график
plt.title('буквы')  # заголовок
plt.xlabel('буква')  # ось x
plt.ylabel('число')  # ось y
plt.savefig('histogram.png')  # сохраняем
print('готово')  # конец