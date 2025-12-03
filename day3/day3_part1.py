def read_file(file):
    lines = []
    with open(file, 'r') as file:
        for line in file:
            lines.append(line[:-1])
    return lines 

def process_rotation(line):
    max = 0
    for digit_idx in range(len(line) - 1):
        number = int(line[digit_idx])
        other_numbers = line[digit_idx + 1:]
        for other_number in other_numbers:
            combined_number = (number * 10) + int(other_number)
            if combined_number > max:
                max = combined_number
    return max
    

if __name__ == "__main__":
    lines = read_file('data.txt');
    sum = 0
    print(lines)
    for line in lines:
        sum += process_rotation(line)
    print(sum)
