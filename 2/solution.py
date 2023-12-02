maxTotals = {'red':12, 'green': 13, 'blue': 14}
maxRed = 12
maxGreen = 13
maxBlue = 14

file = open("input.txt", "r")
lines = file.readlines()
totalGameScore = 0
sumOfPower = 0
for line in lines:
    gameLost = False
    words = line.split()
    if len(words) < 4:
        continue
    i = 2 # first two words are always the game name
    totals = {}
    minTotals = {}
    check = False
    # Get game number and remove ':'
    game = int(words[1][:len(words[1])-1])
    while i < len(words):
        num = int(words[i])
        color = words[i+1]

        # If last character is ',' remove it
        if color[-1] == ',':
            color = color[:len(color)-1]

        # If last character is ';' this is end of instance
        if color[-1] == ';':
            color = color[:len(color)-1]
            check = True

        if color in totals.keys():
            totals[color] += num
        else:
            totals[color] = num
        
        if check or i + 1 == len(words):
            for key in totals:
                if totals[key] > maxTotals[key]:
                    gameLost = True

                if color in minTotals.keys():
                    if totals[key] > minTotals[key]:
                        minTotals[key] = totals[key]
                else: 
                    minTotals[key] = totals[key]
            totals = {}

        i += 2

    if not gameLost:
        totalGameScore += game

    # Start with 1 and multiply
    gamePower = 1
    for value in minTotals.values():
        gamePower *= value
    sumOfPower += gamePower


print(totalGameScore)
print(sumOfPower)
