#!/usr/bin/env python3

import sys



file = open(sys.argv[1])

data = file.readline()

def evaluate_map(data):
    print("begin-map")
    if data[0] != "<" or data[-1] != ">":
        sys.stderr.write("ERROR -- Invalid map brackets")
        exit(66)

    data = data[1:-1]

    split_indexes = []
    stack = []
    for i, char in enumerate(data):
        if char == "<":
            stack.append("<")
        elif char == ">":
            stack.pop()
        elif char == ",":
            if stack == []:
                split_indexes.append(i)

    start = 0
    level_data = []
    for ind in split_indexes:
        level_data.append(data[start:ind])
        start = ind+1
    level_data.append(data[start:])

    # level_data = data.split(",")
    present = set()
    for entities in level_data:
        if entities != '':
            key, val = entities.split(":", 1)
            if key in present:
                sys.stderr.write("ERROR -- Duplicate same level key")
                exit(66)
            else:
                present.add(key)

    for entities in level_data:

        if entities != '':
            
            key, val = entities.split(":", 1)

            if len(key.strip()) != len(key):
                sys.stderr.write("ERROR -- Invalid space formatting")
                exit(66)

            if len(val.strip()) != len(val):
                sys.stderr.write("ERROR -- Invalid space formatting")
                exit(66)

            if val[0] == "<":
                print(key + " -- map -- ")
                evaluate_map(val)

            else:
                for char in val:
                    if char.isdigit() or char.isalpha() or char == "%" or char ==" " or char=="-":
                        pass
                    else:
                        sys.stderr.write("ERROR -- Invalid character")
                        exit(66)
                    
                if '%' in val:
                    index = val.index('%')
                    ascii_code = int(val[index+1] + val[index+2], 16)
                    char_val = chr(ascii_code)
                    print(key + " -- string -- " + val[:index] + char_val + val[index+3:])
                elif val[-1] == "s":
                    print(key + " -- string -- " + val[:-1])

                elif val[:2] == "i-":
                    try:
                        int(val[2:])
                    except ValueError:
                        sys.stderr.write("ERROR -- Invalid negative integer")
                        exit(66)

                    print(key + " -- integer -- -" + val[2:])
                elif val[0] == "i":
                    print(key + " -- integer -- " + val[1:])
                    try:
                        int(val[1:])
                    except ValueError:
                        sys.stderr.write("ERROR -- Invalid integer")
                        exit(66)

                else:
                    sys.stderr.write("ERROR -- Invalid value")
                    exit(66)

    print("end-map")


evaluate_map(data.strip())

file.close()

