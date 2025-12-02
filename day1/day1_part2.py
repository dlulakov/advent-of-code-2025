def process(pairs, part2=False):
    cur = 50
    total_zero = 0
    last_was_zero = False
    for direction, num in pairs:
        if num >= 100:
            cycles = int(num / 100)
            if part2:
                total_zero += cycles
            num = num % 100
        if direction == 'L':
            cur -= num
        else:
            cur += num
        new_cur = cur % 100
        if new_cur == 0:
            total_zero += 1
        elif part2 and new_cur != cur and not last_was_zero:
            total_zero += 1
        last_was_zero = (new_cur == 0)
        cur = new_cur
    return total_zero

def parse_pairs(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            num = int(line[1:])
            parsed_data.append((direction, num))

    return parsed_data


input_data = parse_pairs("data.txt")
#Part 1
print(process(input_data))

#Part 2
print(process(input_data, True))
