data = 'data = \'X\'\ntheprogram = ""\nescaped = False\ndef escape(string):\n    output = ""\n    for c in string:\n        if c == "\\n":\n            output = output + "\\\\n"\n        elif c == "\\\'":\n            output = output + "\\\\\'"\n        elif c == "\\\\":\n            output = output + "\\\\\\\\"\n        else:\n            output = output + c\n    return output\nfor c in data:\n    if escaped:\n        theprogram = theprogram + c\n        escaped = False\n    elif c == "EE":\n        escaped = True\n    elif c == "EX":\n        theprogram = theprogram + escape(data)\n    else:\n        theprogram = theprogram + c\nprint(theprogram)'
theprogram = ""
escaped = False
def escape(string):
    output = ""
    for c in string:
        if c == "\n":
            output = output + "\\n"
        elif c == "\'":
            output = output + "\\'"
        elif c == "\\":
            output = output + "\\\\"
        else:
            output = output + c
    return output
for c in data:
    if escaped:
        theprogram = theprogram + c
        escaped = False
    elif c == "E":
        escaped = True
    elif c == "X":
        theprogram = theprogram + escape(data)
    else:
        theprogram = theprogram + c
print(theprogram)