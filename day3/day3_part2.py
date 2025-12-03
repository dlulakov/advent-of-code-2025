def read_file(file):
    lines = []
    with open(file, 'r') as file:
        for line in file:
            lines.append(line[:-1])
    return lines 

def find_idx_of_max(other_numbers, ignore_idx):
    max = 0
    max_idx = 0
    for i in range(len(other_numbers)):
        if int(other_numbers[i]) > max and i not in ignore_idx:
            max = int(other_numbers[i])
            max_idx = i
    return  max_idx


def process_rotation(line):
    max_pattern = []
    ignore_idx = []
    while len(max_pattern) != 12:
        x = find_idx_of_max(list(line), ignore_idx)
        if len(max_pattern) != 12 and (len(line) - x) >= (12 - len(max_pattern)):
            max_pattern.append(line[x])
            line = line[x + 1:]
            ignore_idx = []
        else:
            ignore_idx.append(x)

    return int(''.join(max_pattern))
    

if __name__ == "__main__":
    lines = read_file('data.txt');
    sum = 0
    print(lines)
    for line in lines:
        sum += process_rotation(line)
    print(sum)
