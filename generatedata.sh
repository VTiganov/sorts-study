#!/bin/bash

for N in $(seq 1000000 1000000 500000000); do
    filename="data/num${N}.txt"

    shuf -i 1-500000 -n $N | awk '{printf "%d\t", $0}' > $filename

    echo >> $filename

    echo "Список успешно записан в файл $filename"
done
