file = 'workfile.txt'


def count_lines(file_name):
    '''функция, которая читает входной файл
       и подсчитывает количество строк в нем'''
    with open(file_name, 'r') as my_file:
        my_lines = my_file.readlines()
        return f'Lines: {len(my_lines)}'


def count_chars(file_name):
    '''функция, которая читает входной файл
    и подсчитывает количество символов в нем'''
    with open(file_name, 'r') as my_file:
        my_symbols = my_file.read()
        return f'Symbols: {len(my_symbols)}'



def test(file_name):
    ans = input('Lines[L],Symbols[S],All[A]')
    if ans.capitalize() == 'L':
        print(count_lines(file_name))
    elif ans.capitalize() == 'S':
        print(count_chars(file_name))
    elif ans.capitalize() == 'A':
        print(count_lines(file_name),count_chars(file_name))

