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


def define_TM(file):

    f=open(file, "r")
    lines = f.readlines()
    states = lines[0].split()
    alphabet = lines[1].split()
    gamma = lines[2].split()
    start_state = lines[3].split()
    accept_state = lines[4].split()
    reject_state = lines[5].split()
    f.close()


    TM = (states, alphabet,gamma,start_state, accept_state,reject_state)
    return TM

def delta(state,string, head_pos):
    input = string[head_pos]

    if state == 'q1':
        if input == '_' or input == 'x':
            new_head = head_pos + 1
            new_state = 'reject'
            new_string = string
        elif input == '0':
            new_head = head_pos + 1
            string[head_pos] = '_'
            new_string = string
            new_state = 'q2'
    elif state == 'q2':
        if input == 'x':
            new_head = head_pos+1
            new_state = 'q2'
            new_string = string
        elif input == '_':
            new_head = head_pos+1
            new_state = 'accept'
            new_string = string
        elif input == '0':
            string[head_pos] = 'x'
            new_string = string
            new_head = head_pos+1
            new_state = 'q3'
    elif state == 'q3':
        if input == 'x':
            new_string = string
            new_state = 'q3'
            new_head = head_pos +1
        elif input == '_':
            new_string = string
            new_state = 'q5'
            new_head = head_pos-1
        elif input =='0':
            new_string = string
            new_state = 'q4'
            new_head = head_pos+1
    elif state == 'q4':
        if input == 'x':
            new_string = string
            new_state = 'q4'
            new_head = head_pos +1
        elif input == '_':
            new_string = string
            new_state = 'reject'
            new_head = head_pos+1
        elif input =='0':
            string[head_pos] = 'x'
            new_string = string
            new_state = 'q3'
            new_head = head_pos+1
    elif state == 'q5':
        if input == 'x' or input == '0':
            new_string = string
            new_state = 'q5'
            new_head = head_pos -1
        elif input == '_':
            new_string = string
            new_state = 'q2'
            new_head = head_pos+1


    return new_state, new_string, new_head


def main():

    M = define_TM("TM.dat")
    running = True


    while(running == True):
        string = raw_input("Enter a string to test: ")
        state = M[3][0]
        alphabet = M[1]
        head_pos = 1
        string = "_"+string+"__"
        string = list(string)

        while state != 'accept' and state != 'reject':

            #checks to make sure there is a valid input
            if string[head_pos] not in alphabet and string[head_pos] not in M[2]:
                print "string rejected, not a valid string."
                state = 'reject'
            else:
                state, string, head_pos= delta(state,string,head_pos)



        if state in M[4]:
            print "accept"
        else:
            print "reject"

        another_one = raw_input("Enter another string? (y/n) ")
        if another_one == "y":
            running = True
        else:
            running = False



main()
