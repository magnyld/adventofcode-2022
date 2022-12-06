import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
bvwbjplbgvbhsrlpgdmjqwftvncz
'''

def parse_input(s):
    return [x for x in s.strip()]


def calc(data):
    count = 0
    for i in range(len(data)):

        if (count == 4):
            return i

        if(data[i] == data[i+1] or data[i] == data[i+2] or data[i] == data[i+3]):
            count = 0
        else:
            count += 1

    return count

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_DATA)
    print(calc(data))
    

    return 0

if __name__ == "__main__":
    main()