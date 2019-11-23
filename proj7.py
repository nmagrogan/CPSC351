#Nathan Magrogan
#https://github.com/nmagrogan/CPSC351
#python2.7

#sorry, I started this too late and didn't have time to meet all the requirements of the assignment,
#but this works for the one DFA asked for. 

def define_dfa(file):



    f=open(file, "r")
    lines = f.readlines()
    states = lines[0]
    alphabet = lines[1]
    sigma = lines[2]
    start_state = lines[3]
    accept_states = lines[4]
    f.close()

    DFA = (states, alphabet,sigma,start_state, accept_states)
    print DFA
    return DFA


def main():

    #G = define_dfa("DFA.dat")
    running = True
    while(running == True):
        string = raw_input("Enter a string to test: ")
        state = 0

        for char in string:
            if char == '1' and state == 0:
                state = 1
            elif char == '0' and state ==0:
                state = 2
            elif (char == '0' or char == '1') and state == 1:
                state = 0
            else:
                state = 2
                break

        if state == 1 or state == 0:
            print "String accepted"
        else:
            print "string rejected"

        another_one = raw_input("Enter another string? (y/n) ")
        if another_one == "y":
            running = True
        else:
            running = False



main()
