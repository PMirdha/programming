import string
ALPHABET = string.uppsercase

def get_pattern(pattern):
    if pattern[0] == 'R' and pattern[1].isdigit():
        return 1
    return 0

def to_row_col_type(pattern):
    pass

def to_xl_type(pattern):
    r = pattern.find('R') + 1
    row_num = int(pattern[r:])
    c = pattern.find('C') + 1
    col_num = int(pattern[c:])
    
    

def convert_to(pattern, type):
    if type:
        converted_pattern = to_xl_type(pattern)
    else:
        converted_pattern = to_row_col_type(pattern)
    return converted_pattern

def solve(pattern):
    type = get_pattern(pattern)
    print(convert_to(pattern, type))
    # print(converted_pattern)

def take_input():
    instr = raw_input()
    a = list(map(int, instr.strip().split(" ")))

def get_input():
    n = int(take_input()[0])
    for i in range(n):
        solve(take_input()[0])

if __name__ == "__main__":
    get_input()