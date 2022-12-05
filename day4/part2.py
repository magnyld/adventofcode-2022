import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

def parse_input(s: str) -> list[int]:
    return [[[int(b) for b in a.split("-")] for a in x.split(",")] for x in s.strip().split("\n")]


def calc(data):
    total = 0;
    for row in data:
        if((
            (row[0][0] <= row[1][0] and row[0][0] >= row[1][0]) or # start
            (row[0][1] >= row[1][0] and row[0][1] <= row[1][1])) # end
            or
            (row[1][0] <= row[0][0] and row[1][0] >= row[0][0]) or # start
            (row[1][1] >= row[0][0] and row[1][1] <= row[0][1])): # end
            total += 1

    return total

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_DATA)
    print(calc(data))
    #print(calc(data));
 
    return 0

if __name__ == "__main__":
    main()