#Nathan Magrogan
#Kaylee Moniz
#https://github.com/nmagrogan/CPSC351
#python2.7
'''
delta functison described in function delta

all other parts of the PDA are in the PDA.dat file
states are line 1
the alphabet is line 2
stack language = line 3
start state is line 4
and the accept states are on line 5
'''


def define_pda(file):

    f=open(file, "r")
    lines = f.readlines()
    states = lines[0].split()
    alphabet = lines[1].split()
    gamma = lines[2].split()
    start_state = lines[3].split()
    accept_states = lines[4].split()
    f.close()


    PDA = (states, alphabet,gamma,start_state, accept_states)
    return PDA

def delta(state, stack,input):

    if len(stack) == 0:
        stack.append("$")
        new_state = "q2"
        new_stack = stack
        return new_state, new_stack
    if state == "q2" and input == "0":
        new_state = "q2"
        stack.append("0")
        new_stack = stack
    elif state == "q2" and input == "1" and stack.pop() == '0':
        new_state = "q3"
        new_stack = stack
    elif state == "q3" and input == "1" and stack.pop() == '0':
        new_state = "q3"
        new_stack = stack
    elif state == "q3" and input =="_" and stack.pop() == '$':
        new_state = "q4"
        new_stack = stack
    else:
        new_state = "reject"
        new_stack = stack

    return new_state, new_stack


def main():

    P = define_pda("PDA.dat")
    running = True
    stack = []

    while(running == True):
        string = raw_input("Enter a string to test: ")
        state = P[3][0]
        alphabet = P[1]
        string = "_"+string+"_"

        for char in string:

            if char not in alphabet:
                print "string rejected, not a valid string."
                state = "reject"
                break
            else:
                state, stack = delta(state,stack,char)

            if state == "q4" or state == "reject":
                break

        if state in P[4]:
            print "String accepted"
        else:
            print "string rejected"

        another_one = raw_input("Enter another string? (y/n) ")
        if another_one == "y":
            running = True
        else:
            running = False



main()
