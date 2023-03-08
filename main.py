# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

letters = 'abcdefghijklmnopqrstuvwxyz'
letter_to_value = {}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.

def create_dict():
    index = 1
    for letter in letters:
        letter_to_value[letter] = {letter, index}

def print_chart():
    index = 1
    for i in range(9):
        print(index, ' ', sep='', end='')
        index += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    create_dict()
    print_chart()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
