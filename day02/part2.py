total = 0

file = open("input.txt", "r")

ranges = file.readlines()[0].split(",")


for interval in ranges:
    interval = interval.strip().split("-")

    for i in range(int(interval[0]), int(interval[1]) + 1):
        num = str(i)

        for j in range(1, len(num)):
            substr = num[:j]

            if num.count(substr) == len(num) / len(substr):
                total += i
                break


print(total)
