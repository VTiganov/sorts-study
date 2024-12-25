#!/bin/bash

# Определите диапазон значений N
for N in $(seq 1000000 1000000 500000000); do
    # Создайте файл с именем data/num${N}.txt
    filename="data/num${N}.txt"

    # Генерируем случайные числа и записываем их в файл
    shuf -i 1-500000 -n $N | awk '{printf "%d\t", $0}' > $filename

    # Добавляем новую строку в конце файла
    echo >> $filename

    echo "Список успешно записан в файл $filename"
done
