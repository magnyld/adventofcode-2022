import os.path

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

def parse_input(s: str) -> list[int]:
    return [([char for char in x]) for x in s.strip().split("\n")]


def calc(data):
    total = 0;
    for row in data:
        p1 = row[:len(row)//2]
        p2 = row[len(row)//2:]
        diff = (list(set(p1) - (set(p1) - set(p2))))

        total += char_to_priority(diff[0]);
        
    return total

def char_to_priority(char):
    ascii_char = ord(char)

    if (ascii_char > 96):
        return ascii_char - 96
    
    return ascii_char - 38

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_DATA)
    print(calc(data));
 
    return 0

if __name__ == "__main__":
    main()