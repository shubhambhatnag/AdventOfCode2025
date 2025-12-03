total = 0

file = open("input.txt", "r")

for bank in file.readlines():
    bank = bank.strip()

    bank = [int(battery) for battery in bank]

    batteries = []

    last = 0
    while len(batteries) < 12:
        subset = bank[last : (len(bank) - (12 - len(batteries) - 1))]

        largest_idx = None

        for i in range(len(subset)):
            if largest_idx is None:
                largest_idx = i
            else:
                if subset[i] > subset[largest_idx]:
                    largest_idx = i

        batteries.append(subset[largest_idx])

        last += largest_idx + 1

    total += int("".join(map(str, batteries)))

print(total)
