import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

def parse_input(s):
    data = s.split("\n\n");
    stacks = data[0];
    rules = data[1].strip();

    rules_output = ([[int(x.split(" ")[1]), int(x.split(" ")[3]), int(x.split(" ")[5])] for x in rules.split("\n")])
    
    stacks_data = ([[char for char in x] for x in stacks.split("\n")])

    height = len(stacks_data);
    width = len(stacks_data[0]);

    cols = int((width+1) / 4) # imagine an extra space in the end to align the data
    stack_output = [[] for y in range( cols )]


    for row in range(height-1, 0, -1): # skip first row with the numbers
        
        for col in range(cols):
            stack_data = stacks_data[row-1][(col*4)+1].strip()

            if(len(stack_data)):
                stack_output[col].append(stack_data)
   
    return {
        "stack": stack_output, 
        "rules": rules_output
    }


def calc(data):
    total = "";

    stack = data["stack"];
    rules = data["rules"];
    
    #move 1 from 2 to 1

    for rule in rules:
        amount = rule[0]
        f = rule[1] - 1
        t = rule[2] - 1

        #print("from", stack[f][-amount:][::-1], "to", stack[t], "amount", amount)

        stack[t] += stack[f][-amount:]; # remove the reverse array
        del stack[f][-amount:]
      

    for s in stack:
        total += s[-1]

    return total

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_DATA)
    print(calc(data))
    

    return 0

if __name__ == "__main__":
    main()