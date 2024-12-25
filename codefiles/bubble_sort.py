def bubbleSort(INPUTLIST):
    n = len(INPUTLIST)
    sortedList = INPUTLIST.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if sortedList[j] > sortedList[j+1]:
                sortedList[j], sortedList[j+1] = sortedList[j+1], sortedList[j]
    return sortedList





