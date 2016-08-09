import sys
import os

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

        elif "FUNC_FILEPATH" in line:
            # if ("class" and "{") in line:
            #     split_class = line.split()
            #     func = split_class[1]
            #
            #     leading_spaces = len(line) - len(line.lstrip())
            #
            # if "description" in line:
            #     split_str = line.split()
            #     #print(split_str)
            #     del split_str[0]
            #
            #     split_str.remove('=')
            #     #print(split_str)
            #
            #     last_index = split_str[-1]
            #     #print(last_index)
            #     str_list = list(last_index)
            #     str_list.remove(';')
            #     new_last_index = "".join(str_list)
            #     split_str[-1] = new_last_index
            #     #print(split_str)
            #     desc = " ".join(split_str)
            #     #print(desc)

            leading_spaces = len(line) - len(line.lstrip())
            split_line = line.split()
            list_line = list(line)
            #print(split_line[0])
            index_loc = split_line[0].find('(')
            length = len(split_line[0])

            sub_line = split_line[0][index_loc + 1:length]
            index_loc = sub_line.find(',')
            sub_line = sub_line[0:index_loc]
            func = ''.join(sub_line)
            new_line = '\t\t\tF_FILEPATH({});\n'.format(func)
            print(new_line)
            output_f.write(new_line)
        elif 'recompile' in line:
            recompile_line = "\t\t\t\tRECOMPILE;\n"
            print(recompile_line)
            output_f.write(recompile_line)
        else:
            output_f.write(line)
            print(line)

print("Done...")
