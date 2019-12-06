#Nathan Magrogan
#Kaylee Moniz
#https://github.com/nmagrogan/CPSC351
#python2.7
'''
DFA description found in sigma.dat and DFA.dat
sigma.dat format
state+input state_to_go_to

all other parts of the DFA are in the DFA.dat file
states are line 1
the alphabet is line 2
start state is line 3
and the accept states are on line 3
'''


def define_dfa(file):



    f=open(file, "r")
    lines = f.readlines()
    states = lines[0].split()
    alphabet = lines[1].split()
    start_state = lines[2].split()
    accept_states = lines[3].split()
    f.close()

    sigma = {}
    with open("sigma.dat") as f:
        for line in f:
            (key, val) = line.split()
            sigma[key] = val


    DFA = (states, alphabet,sigma,start_state, accept_states)
    return DFA


def main():

    G = define_dfa("DFA.dat")
    running = True

    while(running == True):
        string = raw_input("Enter a string to test: ")
        state = G[3][0]

        for char in string:
            if char not in G[1]:
                state = "reject"
                print "not a valid string"
                break
            state_char = str(state)+str(char)
            state = G[2][state_char]

        if state in G[4]:
            print "String accepted"
        else:
            print "string rejected"

        another_one = raw_input("Enter another string? (y/n) ")
        if another_one == "y":
            running = True
        else:
            running = False



main()
