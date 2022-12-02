import os.path

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
A Y
B X
C Z
'''

def parse_input(s: str) -> list[int]:
    return [x.split(" ") for x in s.strip().split("\n")]

'''
A for Rock, B for Paper, and C for Scissors

X means you need to lose, 
Y means you need to end the round in a draw,
Z means you need to win


1 for Rock, 
2 for Paper, 
3 for Scissors

'''

def calc_game(hand):
    if (hand[0] == 'A'):
        if(hand[1] == 'X'): #lose
            return 3 + 0
        elif(hand[1] == 'Y'): #draw
            return 1 + 3
        elif(hand[1] == 'Z'): #win
            return 2 + 6
    elif (hand[0] == 'B'):
        if(hand[1] == 'X'): #lose
            return 1 + 0
        elif(hand[1] == 'Y'): #draw
            return 2 + 3
        elif(hand[1] == 'Z'): #win
            return 3 + 6
    elif (hand[0] == 'C'):
        if(hand[1] == 'X'): #lose
            return 2 + 0
        elif(hand[1] == 'Y'): #draw
            return 3 + 3
        elif(hand[1] == 'Z'): #win
            return 1 + 6


def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    #data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)

    results = []
    for game in data:
        results.append(calc_game(game))
        
    print(sum(results));

    return 0

if __name__ == "__main__":
    main()