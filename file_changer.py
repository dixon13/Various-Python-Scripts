import sys, getopt
import re

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
    for line in content:
        if "file =" in line:
            print(line)
            leading_spaces = len(line) - len(line.lstrip())
            user_input = input("file = PATHTO_FUNC(var1): ")
            count = 0
            spaces = ""
            while (count < leading_spaces):
                if (count % 2) == 0:
                    spaces += "\t"
                count += 1

            new_input = "{}file = PATHTO_FUNC({});\n".format(spaces,user_input)
            #new_str = re.sub(line, new_input, line)
            new_str = new_input.replace(line, new_input)
            output_f.write(new_str)
            print("")
        else:
            output_f.write(line)

print("Done...")
