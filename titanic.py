import pyarrow.parquet as pq  # parquet
import pandas as pd  # для csv
import matplotlib.pyplot as plt  # график
t = pq.read_table('titanic.parquet')  # читаем
d = t.to_pandas()  # в pandas
d.to_csv('titanic.csv', index=False)  # в csv
print('csv сохранен')  # отчёт
c1 = c2 = c3 = 0  # выжил
n1 = n2 = n3 = 0  # не выжил
# считаем без индексов, сразу по именам столбцов
for i in range(len(d)):
    p = d['Pclass'][i]  # класс
    s = d['Survived'][i]  # выжил
    if p == 1 and s == 1:
        c1 = c1 + 1
    elif p == 2 and s == 1:
        c2 = c2 + 1
    elif p == 3 and s == 1:
        c3 = c3 + 1
    elif p == 1 and s == 0:
        n1 = n1 + 1
    elif p == 2 and s == 0:
        n2 = n2 + 1
    elif p == 3 and s == 0:
        n3 = n3 + 1
x = [1, 2, 3]  # классы
y1 = [c1, c2, c3]  # выжил
y2 = [n1, n2, n3]  # не выжил
plt.bar(x, y1, color='green', label='выжил')  # выжил
plt.bar(x, y2, color='red', bottom=y1, label='не выжил')  # не выжил
plt.xlabel('класс')  # ось x
plt.ylabel('число')  # ось y
plt.title('выживаемость')  # заголовок
plt.legend()  # легенда
plt.savefig('titanic_hist.png')  # сохраняем
print('график сохранен')  # конец