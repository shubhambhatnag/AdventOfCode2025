file = open("input.txt", "r")
lines = [line.rstrip("\n") + "x" for line in file.readlines()]
curr = []
total = []
op = None

max_len = max(len(s) for s in lines)

for line in range(len(lines)):
    lines[line] += " " * (max_len - len(lines[line]))
for i in range(len(lines[0])):
    if lines[-1][i] == "+" or lines[-1][i] == "*" or lines[-1][i] == "x":
        if op:
            if op == "+":
                total.append(sum(curr))
            else:
                product = 1
                for num in curr:
                    product *= num
                total.append(product)
        curr = []
        if lines[-1][i] == "x":
            break
        op = lines[-1][i]

    num = ""
    for row in lines[:-1]:
        if row[i].isdigit():
            num += row[i]

    if num:
        curr.append(int(num))

print(sum(total))
