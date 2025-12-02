import re

def read_file(file):
    with open(file, 'r') as file:
        array = []
        for line in file:
            parts_with_numbers = re.split(r'(\d+)', line)
            array.append((parts_with_numbers[0],int(parts_with_numbers[1])))
    return array

def process_rotation(rotation, number_of_rotations, count, number):
    result = count;
    print(f'Count: {count}, Number: {number}, Number of rotations: {number_of_rotations}')
    if rotation == 'L':
        number = number - number_of_rotations
        if number < 0 : 
            number = number % 100;
            
    else:
        number = number + number_of_rotations
        if number > 99 : 
            number = number % 100;
    
    if number == 0: 
        result += 1

    return number, result

if __name__ == "__main__":
    instructions = read_file('data.txt');
    count = 0;
    number = 50
    for instruction in instructions:
        rotation, number_of_rotations = instruction
        number, count = process_rotation(rotation, number_of_rotations, count, number)
    print(count);
         
        
