total = 0

file = open("input.txt", "r")

for bank in file.readlines():
    bank = bank.strip()
    max_joltage = 0

    first = 0

    for second in range(1, len(bank)):
        joltage = int(bank[first] + bank[second])

        max_joltage = max(max_joltage, joltage)

        if bank[second] > bank[first]:
            first = second

    total += max_joltage

print(total)
