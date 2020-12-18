try:
    file = open("scores.txt", "r")
    first_line = file.readline()
    scoresArray = []
    while True:
        content = file.readline()
        if not content:
            break
        splitStr = content.split(',')
        scoresArray.append(int(splitStr[1].rstrip()))
    s = 0
    high = scoresArray[0]
    low = scoresArray[0]
    for val in scoresArray:
        if val > high:
            high = val
        if val < low:
            low = val
        s = s + val
    avg = s/len(scoresArray)
    print("\nHighest Score: ", high)
    print("Lowest Score: ", low)
    print("Average Score: "+"{:.2f}".format(avg))
except IOError:
    print("File not accessible")
finally:
    file.close()
