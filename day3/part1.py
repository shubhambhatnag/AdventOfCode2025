total = 0

file = open("input.txt", "r")

for bank in file.readlines():
    bank = bank.strip()
    max_joltage = 0

    l = 0

    for r in range(1, len(bank)):
        joltage = int(bank[l] + bank[r])

        max_joltage = max(max_joltage, joltage)

        if bank[r] > bank[l]:
            l = r

    total += max_joltage

print(total)
