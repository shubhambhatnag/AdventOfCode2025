total = 0

file = open("input.txt", "r")

ranges = file.readlines()[0].split(",")

for interval in ranges:
    interval = interval.strip().split("-")
    for i in range(int(interval[0]), int(interval[1]) + 1):
        num = str(i)
        if len(num) % 2 == 0:
            if num[: (len(num) // 2)] == num[(len(num) // 2) :]:
                total += i


print(total)
