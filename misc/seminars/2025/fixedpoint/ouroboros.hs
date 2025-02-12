data1 = "data1 = \'X\'\ndata2 = \'Y\'\ntheprogram = \"\"\nescaped = False\ndef escape(string):\n    output = \"\"\n    for c in string:\n        if c == \"\\n\":\n            output = output + \"\\\\n\"\n        elif c == \"\\\'\":\n            output = output + \"\\\\\'\"\n        elif c == \"\\\\\":\n            output = output + \"\\\\\\\\\"\n        elif c == \"\\\"\":\n            output = output + \"\\\\\\\"\"\n        else:\n            output = output + c\n    return output\nfor c in data2:\n    if escaped:\n        theprogram = theprogram + c\n        escaped = False\n    elif c == \"EE\":\n        escaped = True\n    elif c == \"EX\":\n        theprogram = theprogram + escape(data1)\n    elif c == \"EY\":\n        theprogram = theprogram + escape(data2)\n    else:\n        theprogram = theprogram + c\nprint(theprogram)"
data2 = "data1 = \"X\"\ndata2 = \"Y\"\nescape [] = []\nescape (\'\\\\\':cs) = \'\\\\\':\'\\\\\':escape cs\nescape (\'\\n\':cs) = \'\\\\\':\'n\':escape cs\nescape (\'\\\"\':cs) = \'\\\\\':\'\\\"\':escape cs\nescape (\'\\\'\':cs) = \'\\\\\':\'\\\'\':escape cs\nescape (c:cs) = c:escape cs\n\nquinefy [] = []\nquinefy (\'EE\':c:cs) = c:quinefy cs\nquinefy (\'EX\':cs) = (escape data1) ++ quinefy cs\nquinefy (\'EY\':cs) = (escape data2) ++ quinefy cs\nquinefy (c:cs) = c:quinefy cs\n\nmain = do\n        putStrLn  $ quinefy data1"
escape [] = []
escape ('\\':cs) = '\\':'\\':escape cs
escape ('\n':cs) = '\\':'n':escape cs
escape ('\"':cs) = '\\':'\"':escape cs
escape ('\'':cs) = '\\':'\'':escape cs
escape (c:cs) = c:escape cs

quinefy [] = []
quinefy ('E':c:cs) = c:quinefy cs
quinefy ('X':cs) = (escape data1) ++ quinefy cs
quinefy ('Y':cs) = (escape data2) ++ quinefy cs
quinefy (c:cs) = c:quinefy cs

main = do
        putStrLn  $ quinefy data1