import os.path

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

def parse_input(s: str) -> list[int]:
    return sorted([(sum([int(a) for a in x.split("\n")])) for x in s.strip().split("\n\n")], reverse=True)

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    #data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)

    print(data[0])
    print(sum(data[:3]))


    #print([6000, 4000, 11000, 24000, 10000].sort());

    #print([float(x) for x in INPUT_S_TEST.split()])
    #print(sum([True,False]))
    #print(sum([2,4]))

    return 0

if __name__ == "__main__":
    main()