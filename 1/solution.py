numbers = ["one","two","three","four","five","six","seven","eight","nine"]

total = 0
file = open("input.txt", "r")
lines = file.readlines()
for line in lines:
    i = 0
    j = len(line) - 1
    left = 0
    right = 0

    # Read line left to right
    while i < len(line):
        if line[i].isnumeric():
            left = line[i]
            break
        i += 1 

    # Read line right to left
    while j > -1:
        if line[j].isnumeric():
            right = line[j]
            break
        j -= 1 

    # Look for left most instances of written numbers
    for number in numbers:
        res = line.find(number)
        if res > -1 and res < i:
            i = res
            left = numbers.index(number) + 1

    # Look for right most instances of written numbers
    for number in numbers:
        res = line[::-1].find(number[::-1])
        if res > -1 and len(line) - res - 1 > j:
            j = len(line) - res -1
            right = numbers.index(number) + 1
    num = str(left) + str(right)
    total += int(num)
print(total)
