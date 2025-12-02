def read_file(file):
    ids = []
    with open(file, 'r') as file:
        for line in file:
            sections = line.split(',')
            for section in sections: 
                ids.append(section.split('-'))
    return ids 

def process_rotation(left_id, right_id):
    sum_inner = 0
    for number in range(int(left_id), int(right_id)+1):
        print(f'Number: {number}')
        digits = len(str(number))
        print(f'Digits: {digits}')
        if digits % 2 == 0 :
            last_part = number % (10 ** (digits // 2))
            first_part = number // (10 ** (digits // 2))
            print(f'Last part: {last_part}, First Part: {first_part}')
            if last_part == first_part:
                sum_inner += number

    return sum_inner
    

if __name__ == "__main__":
    ids = read_file('data.txt');
    sum = 0
    for first_id, last_id in ids:
        sum += process_rotation(first_id, last_id)
    print(sum)
