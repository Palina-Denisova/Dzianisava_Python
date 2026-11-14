# input > 7
def check_number():

    int_input = int(input("Enter a number greater than 7: "))
    if int_input > 7:
        print("Hello")

# input == or != "John"
def check_name():

    str_input = input("Enter your name: ")
    if str_input == "John":
        print("Hello, John")
    else:
        print("There is no such name")

# array
def find_multiples_of_three():
    array_input = [int(s) for s in input("Enter numbers separated by space: ").split()]
    array_output = []
    for s in array_input:
        if s % 3 == 0:
            array_output.append(s)
    print(array_output)

check_number()
check_name()
find_multiples_of_three()