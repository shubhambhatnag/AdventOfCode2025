file = open("input.txt", "r")
lines = file.readlines()
operations = [i for i in lines[-1].strip().split(" ") if i != ""]
total = [0 if i == "+" else 1 for i in operations]
for line in lines[:-1]:
    line = line.strip().split()
    for num in range(len(line)):
        if operations[num] == "+":
            total[num] += int(line[num])
        else:
            total[num] *= int(line[num])


print(sum(total))
