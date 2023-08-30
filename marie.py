# Marrie Interpreter

# Define the functions
def p(arg):
    print(arg)

def s(args):
    return ''.join([chr(x) for x in args])

def i(arg):
    return int(arg)

def fd(arg):
    return float(arg)

def b(arg):
    return bool(arg)

# Define the variables
variables = {}

# Read code from the Marrie file
filename = "file.marie"  # Replace with your desired file name
with open(filename, "r") as file:
    code = file.read()

# Split the code into lines
lines = code.split("\n")

# Interpret each line of code
for line in lines:
    if line.startswith("p("):
        arg = line[2:-1]
        p(eval(arg))
    elif "=" in line:
        var_name, var_value = line.split("=")
        variables[var_name.strip()] = eval(var_value.strip())
    elif line.startswith("?"):
        condition = eval(line[1:])
        if condition:
            inside_if = True
        else:
            inside_if = False
    elif line.startswith("!?"):
        inside_if = not inside_if
    elif line.startswith("p(") and inside_if:
        arg = line[2:-1]
        p(eval(arg.replace("s[", "s(")))  # Fix the usage of s() function
