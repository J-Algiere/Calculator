# Build a calculator program
import sys

def main():
    while True:
        equation = userinput()
        try:
            print(eval(equation))
            sys.exit()
        except ZeroDivisionError:
            print("Can not divide by zero")
        except NameError:
            print("Invalid input")
        except SyntaxError:
            print("Invalid input")

# get user input for numbers to calculate
def userinput():
        x = input("Enter a math problem: ")
        return x
if __name__ == '__main__':
    main()