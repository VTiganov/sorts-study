def cocktailSort(INPUTLIST):
    n = len(INPUTLIST)
    sortedList = INPUTLIST.copy()

    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if sortedList[i] > sortedList[i + 1]:
                sortedList[i], sortedList[i + 1] = sortedList[i + 1], sortedList[i]
                swapped = True

        if not swapped:
            break

        swapped = True

        end -= 1

        for i in range(end - 1, start - 1, -1):
            if sortedList[i] > sortedList[i + 1]:
                sortedList[i], sortedList[i + 1] = sortedList[i + 1], sortedList[i]
                swapped = True

        start += 1

    return sortedList
