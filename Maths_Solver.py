
print("Welcome to Maths Solver !!")
print('''
This program is created by SAJAL AGRAWAL''')
print("Address: SALEHA ROAD DEVENDRANAGAR PANNA (M.P.) INDIA -488333")

# This is the code for the factorial of the given number.

def factorial():
    a=(int(input('''
Enter a number to get its factorial : ''')))
    f=1
    for i in range(a,1,-1):
       f=f*i
    print("The factorial of ",a," is ",f)

# The main activity code:

    a=int(input('''
|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
    if a==1:
        factorial()
    elif a==2:
        power()
    elif a==3:
        factorize()
    elif a==4:
        lcm()
    elif a==5:
        hcf()
    elif a==6:
        fibonacci_sequence()
    elif a==7:
        armstrong_number()
    else:
        print('''
Please Enter the correct value !!''')
    

# This is the code for the square or cube or other powers of a number.
# Till now the power supports upto 30 only.

def power():
    a=int(input('''
Enter a number to calculate its power value
(example- if you want to calculate the square of 4 , you only write 4
or if you want to calculate the cube of 4 , you only write 4) : '''))
    b=int(input("Enter the power : "))
    if b==1:
        c=a
    elif b==2:
        c=a*a
    elif b==3:
        c=a*a*a
    elif b==4:
        c=a*a*a*a
    elif b==5:
        c=a*a*a*a*a
    elif b==6:
        c=a*a*a*a*a*a
    elif b==7:
        c=a*a*a*a*a*a*a
    elif b==8:
        c=a*a*a*a*a*a*a*a
    elif b==9:
        c=a*a*a*a*a*a*a*a*a
    elif b==10:
        c=a*a*a*a*a*a*a*a*a*a
    elif b==11:
        c=a*a*a*a*a*a*a*a*a*a*a
    elif b==12:
        c=a*a*a*a*a*a*a*a*a*a*a*a
    elif b==13:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==14:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==15:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==16:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==17:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==18:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==19:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==20:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==21:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==22:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==23:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==24:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==25:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==26:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==27:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    elif b==30:
        c=a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a
    else:
        c="Till now, power supports only upto 30. It will be corrected in the next update !!"
        print(c)
    if b<31:
        print("If ",a," raised to the power ",b," is equal to ",c)

    # The main activity code:

    a=int(input('''

|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
    if a==1:
        factorial()
    elif a==2:
        power()
    elif a==3:
        factorize()
    elif a==4:
        lcm()
    elif a==5:
        hcf()
    elif a==6:
        fibonacci_sequence()
    elif a==7:
        armstrong_number()
    else:
        print('''
Please Enter the correct value !!''')
    

# This is the code to find all prime factors of a given number.

def factorize():
    a=int(input('''
Enter a number to get its Prime Factors : '''))
    while a%2==0:
        print(2)
        a=a/2
    for i in range(3,int(a+1),2):
        while a%i==0:
            print(i),
            a=a/i
    if a>2:
        print(a)

# The main activity code:

    a=int(input('''
|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal


To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
    if a==1:
        factorial()
    elif a==2:
        power()
    elif a==3:
        factorize()
    elif a==4:
        lcm()
    elif a==5:
        hcf()
    elif a==6:
        fibonacci_sequence()
    elif a==7:
        armstrong_number()
    else:
        print('''
Please Enter the correct value !!''')

# This is the code to find the LCM of two numbers.

def lcm():
    a=int(input('''
Enter the First number : '''))
    b=int(input("Enter the second number : "))
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if((greater%a==0)and(greater%b==0)):
            lcm=greater
            break
        greater=greater+1
    print("The LCM of",a,"and",b,"is",lcm)

# The main activity code:

    a=int(input('''
|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   armstrong number or not:           Press 7 and Enter :'''))
    if a==1:
        factorial()
    elif a==2:
        power()
    elif a==3:
        factorize()
    elif a==4:
        lcm()
    elif a==5:
        hcf()
    elif a==6:
        fibonacci_sequence()
    elif a==7:
        armstrong_number()
    else:
        print('''
    Please Enter the correct value !!''')

# This is the code to find the HCF of two numbers.

def hcf():
    a=int(input('''
Enter the First number : '''))
    b=int(input("Enter the second number : "))
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(1,smaller+1):
        if((a%i==0)and(b%i==0)):
            hcf=i
    print("The HCF of",a,"and",b,"is",i)

    # The main activity code

    a=int(input('''
|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
    if a==1:
            factorial()
    elif a==2:
            power()
    elif a==3:
            factorize()
    elif a==4:
            lcm()
    elif a==5:
            hcf()
    elif a==6:
            fibonacci_sequence()
    elif a==7:
            armstrong_number()
    else:
        print('''
    Please Enter the correct value !!''')

# This is the code to print the fibonacci sequence.

def fibonacci_sequence():
    nterms=int(input('''
Enter the number of terms you want : '''))
    n1=0
    n2=1
    count=2
    if nterms <= 0:
        print("Please enter a positive integer to get fibonacci series")
    elif nterms==1:
        print("Fibonacci Sequence - ",n1)
    else:
        print("Fibonacci Sequence - ",n1,",",n2,end=",")
        while count<nterms:
            nth=n1+n2
            print(nth,end=",")
            n1=n2
            n2=nth
            count=count+1

# The main activity code:

    a=int(input('''
|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
    if a==1:
        factorial()
    elif a==2:
        power()
    elif a==3:
        factorize()
    elif a==4:
        lcm()
    elif a==5:
        hcf()
    elif a==6:
        fibonacci_sequence()
    elif a==7:
        armstrong_number()
    else:
        print('''
Please Enter the correct value !!''')

# This is the program to check whether the given number is Armstrong number or not

def armstrong_number():
    num=int(input('''
Enter a number to find whether it is Armstrong number or not : '''))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum += digit**3
        temp//=10
    if num==sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

# The main activity code:

    a=int(input('''

|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
    if a==1:
        factorial()
    elif a==2:
        power()
    elif a==3:
        factorize()
    elif a==4:
        lcm()
    elif a==5:
        hcf()
    elif a==6:
        fibonacci_sequence()
    elif a==7:
        armstrong_number()
    else:
        print('''
Please Enter the correct value !!''')

# The main code of activity begins from here.

a=int(input('''
|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
if a==1:
    factorial()
elif a==2:
    power()
elif a==3:
    factorize()
elif a==4:
    lcm()
elif a==5:
    hcf()
elif a==6:
    fibonacci_sequence()
elif a==7:
    armstrong_number()
else:
    print('''
Please Enter the correct value !!''')

# The main activity code.
    
a=int(input('''
|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal


To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
if a==1:
    factorial()
elif a==2:
     power()
elif a==3:
    factorize()
elif a==4:
    lcm()
elif a==5:
    hcf()
elif a==6:
    fibonacci_sequence()
elif a==7:
    armstrong_number()
else:
        print('''
Please Enter the correct value !!''')

# The main activity code.

a=int(input('''

|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
if a==1:
    factorial()
elif a==2:
    power()
elif a==3:
    factorize()
elif a==4:
    lcm()
elif a==5:
    hcf()
elif a==6:
    fibonacci_sequence()
elif a==7:
    armstrong_number()
else:
    print('''
Please Enter the correct value !!''')

# The main activity code.

a=int(input('''
|\    /|  /\ ~~,~~|    | ___    ___  ___  |  \    / ___  __
|  \/  | /__\  \  |----|(__    (__  /   \ |   \  / |__  |__)
|      ||    | |  |    |___)   ___) \___/ |___ \/  |___ | |

Creator : Sajal Agrawal

To find factorial:                    press 1 and Enter
To find the power value:              press 2 and Enter
To find prime factors of a number:    press 3 and Enter
To find LCM of two numbers:           press 4 and Enter
To find HCF of two numbers:           press 5 and Enter
To get Fibonacci Sequence:            press 6 and Enter
To find whether the number is
   Armstrong number or not:           Press 7 and Enter :'''))
if a==1:
    factorial()
elif a==2:
    power()
elif a==3:
    factorize()
elif a==4:
    lcm()
elif a==5:
    hcf()
elif a==6:
    fibonacci_sequence()
elif a==7:
    armstrong_number()
else:
     print('''
Too many incorrect attempts , closing...........''')

        





