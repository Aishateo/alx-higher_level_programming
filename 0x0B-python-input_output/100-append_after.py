#!/usr/bin/python3
'''
Contains the "append after" function
'''


def append_after(filename="", search_string="", new_string=""):
    '''appends "new_string" after a line containing
    "search_string" in "filename"
    '''

    with open(filename, 'r', encoding='utf-8') as y:
        _line_list = []
        while True:
            _line = y.readline()
            if _line == "":
                break
            _line_list.append(_line)
            if search_string in _line:
                _line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as y:
        y.writelines(_line_list)
