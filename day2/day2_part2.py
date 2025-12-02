from ast import pattern


def read_file(file):
    ids = []
    with open(file, 'r') as file:
        for line in file:
            sections = line.split(',')
            for section in sections: 
                ids.append(section.split('-'))
    return ids 


def check_for_pattern(number: int):
    number_as_str = str(number)
    stack = []
    digit_len = len(number_as_str)
    for digit_idx in range(len(number_as_str) // 2):
        stack.append(number_as_str[digit_idx])
        numbers = ''.join(stack)
        pattern = numbers;
        while(len(pattern) < digit_len):
            pattern += numbers
        if pattern == number_as_str :
            return True
    return False



def process_rotation(left_id, right_id):
    sum_inner = 0
    for number in range(int(left_id), int(right_id)+1):
        if check_for_pattern(number):
            sum_inner += number
    return sum_inner
    

if __name__ == "__main__":
    ids = read_file('data.txt');
    sum = 0
    for first_id, last_id in ids:
        sum += process_rotation(first_id, last_id)
    print(sum)
