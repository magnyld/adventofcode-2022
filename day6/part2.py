import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''

def parse_input(s):
    return [x for x in s.strip()]

def calc(data):
    count = 0
    look_ahead = 14
    for i in range(len(data)):

        if (count == look_ahead):
            return i

        count += 1
        for x in range(1, look_ahead-(count-1)):
            if(data[i] == data[i+x]):
                count = 0

    return count

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_DATA) #INPUT_TEST_DATA
    print(calc(data))

    return 0

if __name__ == "__main__":
    main()