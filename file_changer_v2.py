import sys

print(str(sys.argv))

fname = "{}\CfgFunctions.hpp".format(sys.argv[1])
print("Opening {}".format(fname))
with open(fname) as f:
    content = f.readlines()

print("File read...")
print("")
print("======================================================================================================================")
print("")

with open('{}\output.txt'.format(sys.argv[1]), 'w') as output_f:
    count = 0
    for line in content:
        if (("CfgFunctions" in line) or ("cfgFunctions" in line) or ("PREFIX" in line) or ("COMPONENT" in line)):
            if ("cfgFunctions" in line) or ("CfgFunctions" in line):
                cfgfunc_space = len(line) - len(line.lstrip())
                cnt = 0
                spaces = ""
                while (cnt < cfgfunc_space):
                    cnt += 1
                    if (cnt % 2) == 0:
                        spaces += "\t"
                cfgFuncSpaces = spaces

            elif "PREFIX" in line:
                prefix_space = len(line) - len(line.lstrip())
                cnt = 0
                spaces = ""
                while (cnt < prefix_space):
                    cnt += 1
                    if (cnt % 2) == 0:
                        spaces += "\t"
                prefix_spaces = spaces

            elif "COMPONENT" in line:
                component_space = len(line) - len(line.lstrip())
                cnt = 0
                spaces = ""
                while (cnt < component_space):
                    cnt += 1
                    if (cnt % 2) == 0:
                        spaces += "\t"
                component_spaces = spaces

            print(line)
            output_f.write(line)

        elif ("class" in line) or ("description" in line) or ("file" in line) or ("recompile" in line) or count <= 5:
            count += 1
            if ("class" and "{") in line:
                split_class = line.split()
                func = split_class[1]

                leading_spaces = len(line) - len(line.lstrip())

            if "description" in line:
                split_str = line.split()
                #print(split_str)
                del split_str[0]

                split_str.remove('=')
                #print(split_str)

                last_index = split_str[-1]
                #print(last_index)
                str_list = list(last_index)
                str_list.remove(';')
                new_last_index = "".join(str_list)
                split_str[-1] = new_last_index
                #print(split_str)
                desc = " ".join(split_str)
                #print(desc)

                cnt = 0
                spaces = ""
                while (cnt < leading_spaces):
                    cnt += 1
                    if (cnt % 2) == 0:
                        spaces += "\t"

            if count == 5:
                print("FUNC_FILEPATH({},{});".format(func,desc))
                output_f.write("{}FUNC_FILEPATH({},{});\n".format(spaces,func,desc))
                count = 0

        else:
            output_f.write(line)
            print(line)

    #print(component_spaces,"};")
    #spacing = component_spaces + "};"
    component_spaces += "};\n"
    output_f.write(component_spaces)
    #print(prefix_spaces,"};")
    prefix_spaces += "};\n"
    output_f.write(prefix_spaces)
    #print(cfgFuncSpaces,"};")
    cfgFuncSpaces += "};\n"
    output_f.write(cfgFuncSpaces)

#change_strings = [change_str(line), for line in content]
print("Done...")
