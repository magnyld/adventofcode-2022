import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''

def parse_input(s):
    return [x for x in s.strip()]

def calc(data):

    look_ahead = 14
    
    for i in range(len(data)):
        if len(set(data[i:look_ahead+i])) == look_ahead:
            return i+look_ahead;
            

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_DATA) #INPUT_TEST_DATA
    print(calc(data))

    return 0

if __name__ == "__main__":
    main()