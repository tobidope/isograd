
def visitor(data):
    time = data[1]
    count = 0
    for line in data[2:]:
        come, gone = line.split()
        if come <= time <= gone:
            count += 1
    return count
