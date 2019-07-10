'''

Name: Rishabh Singh Kochhar
Student ID: 29869560

'''


# This code will read a list of integers from a user input. The user will have to enter the interger in the console one by one
# and has the option to terminate giving the inputs at any stage. After the list of integers have been entered, the following
# program will identify the all the pairs whose sum is odd and product is even and return them as a formatted output to the user


int_enter = input('Press enter to start')

# The below code block asks for user inputs for integers and whether they wish to continue adding more integers and does validation
# on those inputs.

list_int = []
int_cont = 'y'
while int_cont.lower()=='y':
    int_inp = input('Kindly enter an integer: ')
    try:
        int_mod = int(int_inp)
        list_int.append(int_mod)
    except:
        print('Not a valid integer input')
    int_cont = input('Do you wish to continue?(y/n): ')
    while (int_cont.lower()!='y' and int_cont.lower()!='n'):
        print('Please enter a valid input(y/n)')
        int_cont = input('Do you wish to continue?(y/n): ')



print('This is the list of the integers entered by you: ',list_int)


print('Below are the all possible pairs from the above list whose product is even and sum is odd')

# Logic to identify all the pairs of integers whose sum is odd and product is even.

j=0
for i in list_int:
    for k in range(j+1, len(list_int)):
        if ((list_int[j]*list_int[k])%2==0 and ((list_int[j]+list_int[k])%2==1) and list_int[j]!=0 and list_int[k]!=0):
            print((list_int[j],list_int[k]))
    j = j+1

# sample list [1, 9, 2, 6, -4, -3, -1]
