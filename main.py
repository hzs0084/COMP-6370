import sys

file = open(sys.argv[1])

data = file.readline()


def evaluate_map(data):
    print("begin-map")

    if data[0] != "<" or data[-1] != ">":
        sys.stderr.write("ERROR -- Invalid format")
        exit(66)

    data = data[1:-1]
    level_data = data.split(",")
    present = set()
    for entities in level_data:
        if entities != '':
            key, val = entities.split(":", 1)
            if key in present:
                sys.stderr.write("ERROR -- Duplicate same level key")
                exit(66)
            else:
                present.add(key)

    for entities in data.split(","):
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
                if '%' in val:
                    index = val.index('%')
                    ascii_code = int(val[index + 1] + val[index + 2], 16)
                    char_val = chr(ascii_code)
                    print(key + " -- string -- " + val[:index] + char_val + val[index + 3:])
                elif val[-1] == "s":
                    print(key + " -- string -- " + val[:-1])

                elif val[:2] == "i-":
                    print(key + " -- integer -- -" + val[2:])
                elif val[0] == "i":
                    print(key + " -- integer -- " + val[1:])
                else:
                    sys.stderr.write("ERROR -- Invalid format")
                    exit(66)

    print("end-map")


evaluate_map(data.strip())

file.close()

