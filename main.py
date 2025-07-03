# Build a calculator program

def main():
    equation = userinput()
    print(eval(equation))



# get user input for numbers to calculate
def userinput():
    x = input("Enter a math problem: ")
    return x



main()