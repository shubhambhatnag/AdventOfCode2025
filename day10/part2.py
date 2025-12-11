from z3 import Int, Optimize, Sum, sat

file = open("input.txt", "r")

total = 0

for line in file.readlines():
    line = line.strip().split()

    needed_joltage = tuple([int(val) for val in line[-1][1:-1].split(",")])
    buttons = []
    for button in line[1:-1]:
        button = [int(num) for num in button[1:-1].split(",")]
        buttons.append(button)

    joltage_start_state = tuple([0] * len(needed_joltage))

    opt = Optimize()

    press_counts = [Int(f"button_{i}") for i in range(len(buttons))]

    for button in press_counts:
        opt.add(button >= 0)

    for pos in range(len(joltage_start_state)):
        total_increment = Sum(
            [press_counts[i] for i in range(len(buttons)) if pos in buttons[i]]
        )
        opt.add(joltage_start_state[pos] + total_increment == needed_joltage[pos])

    opt.minimize(Sum(press_counts))

    if opt.check() == sat:
        total += opt.model().evaluate(Sum(press_counts)).as_long()


print(total)
