import csv
import os

output_filename = "images.csv"
# базовые шаблоны URL (без номера и без ?raw=true)
centr_base = "https://github.com/Ainsw0rt/Nikonov/blob/main/centr/{}.jpg?raw=true"
degaz_base = "https://github.com/Ainsw0rt/Nikonov/blob/main/degaz/{}.jpg?raw=true"

# диапазон номеров (0..53 включительно)
start = 0
end = 53

# создаём/перезаписываем CSV
with open(output_filename, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    # заголовок
    writer.writerow(["label", "url"])
    
    # сначала centr → метка "центрифуга"
    for i in range(start, end + 1):
        url = centr_base.format(i)
        writer.writerow(["центрифуга", url])
    
    # затем degaz → метка "дегазатор"
    for i in range(start, end + 1):
        url = degaz_base.format(i)
        writer.writerow(["дегазатор", url])

print(f"CSV создан: {os.path.abspath(output_filename)}")
