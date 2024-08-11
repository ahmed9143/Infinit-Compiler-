# Importing required modules and classes
from rply import LexerGenerator, ParserGenerator
from lexer import Lexer
from nltk import Tree
import pandas as pd

# Reading input from a file named 'input.txt'
text_input = ""
with open('input.txt') as file:
    for txt in file:
        text_input += txt

# Lexical Analysis
lexer = Lexer().get_lexer()  # Creating lexer instance
tokens = lexer.lex(text_input)  # Tokenizing input text

# Symbol Table
dic = {}  # Dictionary to store tokens
i = 0
table = {}
idt = ['int', 'str', 'float', 'list']  # Possible data types
lis = []  # List to store identifiers, strings, and numbers
lis2 = []  # List to store identifiers and line numbers
z = 1





try:
    for i, token in enumerate(tokens):
        print(token)
        token_type = token.gettokentype()
        token_str = token.getstr()

        dic[str(i + 1) + " - " + token_type] = token_str  # Storing token in dictionary

        if token_type in ["IDENTIFIER", "STRING", "NUMBER"]:
            lis.append(token_str)

        if token_str.startswith("\n"):
            z += 2 if len(token_str) > 1 else 1

        if token_type in ["IDENTIFIER", "NEWLINE"] and token_str not in ["int", "str", "float"]:
            lis2.extend([token_str, z])

except Exception as e:
    print('There was an error: You have entered an unrecognized token name!')
    print("Error: ", e)
    quit()





m = 0
address = {"int": 2, "str": 4, "lis": 10, "float": 4}
k = 0
lis3 = []
lis4 = []

# Building symbol table
for j in range(len(lis)):
    if m == len(lis):
        break
    if lis[m] == "int" or lis[m] == 'str' or lis[m] == 'float':
        for q in range(len(lis2)):
            if lis[m + 1] == lis2[q]:
                lis3.append(lis2[q + 1])
        lis4.append([lis[m + 1], k, lis[m], 1, lis3[0], lis3[1:]])
        k += address[lis[m]]
        m = m + 3
        lis3 = []
    else:
        m += 1


# Displaying symbol table 
print()
print(   "              ","              ", "         ","   ", "         "    "Symbol Table"     , "          ","                "                                   )
print()
print("VARIABLE NAME", "    ", "OBJECT CODE ADDRESS", "         ", "DATA TYPE", "          ", "NO OF DIMENSIONS",
      "      ", "LINE OF DECLARATION", "         ", "REFERENCE LINE")
print()

for o in lis4:
    for p in o:
        l = 25 - len(str(p))
        print(p, " " * l, end="")

print()

print()
print()


# Parse table
parse_table = {
    'E': {'E': 'E + T', 'T': 'T', 'F': 'T'},
    'T': {'T': 'T * F', 'F': 'F', 'num': 'F'},
    'F': {'id': 'id', '(': '( E )'}
}

# Compute FIRST set
FIRST = {
    'E': {'+', 'id', '('},
    'T': {'*', 'id', '('},
    'F': {'id', '('}
}

# Compute FOLLOW set
FOLLOW = {
    'E': {'$', '+', ')'},
    'T': {'+', '$', ')'},
    'F': {'+', '*', '$', ')'}
}

# Print FIRST and FOLLOW sets
print("FIRST Set:")
for non_terminal, first_set in FIRST.items():
    print(f"{non_terminal}: {first_set}")

print("\nFOLLOW Set:")
for non_terminal, follow_set in FOLLOW.items():
    print(f"{non_terminal}: {follow_set}")




























'''
# FIRST and FOLLOW sets
FIRST = {
    'program': {'identifier', 'print', 'if', 'while'},
    'statement_list': {'identifier', 'print', 'if', 'while'},
    'statement': {'identifier', 'print', 'if', 'while'},
    'assignment': {'identifier'},
    'print': {'print'},
    'if_statement': {'if'},
    'while_loop': {'while'},
    'expression': {'number', 'identifier', 'string', '('},
    'term': {'number', 'identifier', 'string', '('},
    'number': {'digit'},
    'identifier': {'[a-zA-Z_]'},
    'op': {'+', '-', '*', '/'},
    'string': {'[a-zA-Z_]'},
    'digit': {'[0-9]'}
}

FOLLOW = {
    'program': {'$'},
    'statement_list': {'$', 'identifier'},
    'statement': {';', '', '}', 'identifier'},
    'assignment': {';', '}', 'identifier'},
    'print': {';', '', '}', 'identifier'},
    'if_statement': {'$', 'identifier', '}', 'while', 'print', 'if'},
    'while_loop': {'$', 'identifier', '}', 'while', 'print', 'if'},
    'expression': {')', 'op', '}', 'identifier', 'print', 'if', 'while'},
    'term': {'op', ')', '}', 'identifier', 'print', 'if', 'while'},
    'number': {'op', ')', '}', 'identifier', 'print', 'if', 'while'},
    'identifier': {'op', '=', ')', '}', 'identifier', 'print', 'if', 'while'},
    'op': {'number', 'identifier', 'string', '('},
    'string': {'op', ')', '}', 'identifier', 'print', 'if', 'while'},
    'digit': {'op', ')', '}', 'identifier', 'print', 'if', 'while'},
}

# Printing FIRST sets
print("\nFIRST sets:")
for non_terminal in FIRST:
    print(f"FIRST({non_terminal}): {FIRST[non_terminal]}")

# Printing FOLLOW sets
print("\nFOLLOW sets:")
for non_terminal in FOLLOW:
    print(f"FOLLOW({non_terminal}): {FOLLOW[non_terminal]}")

'''

















'''
# Parse Table
parse_table = {
    'statement_list': {
        'identifier': 'statement ; statement_list',
        'print': 'statement ; statement_list',
        'if': 'statement ; statement_list',
        'while': 'statement ; statement_list',
        ';': 'statement_list',
        '{': 'statement_list { statement_list } statement_list'
    },
    'statement': {
        'identifier': 'assignment',
        'print': 'print expression ;',
        'if': 'if expression { statement_list }',
        'while': 'while expression { statement_list }'
    },
    'assignment': {
        'identifier': 'identifier = expression ;'
    },
    'print': {
        'print': 'print expression ;'
    },
    'if_statement': {
        'if': 'if expression { statement_list }'
    },
    'while_loop': {
        'while': 'while expression { statement_list }'
    },
    'expression': {
        'identifier': 'term',
        '(': 'term',
        'number': 'term',
    },
    'term': {
        'identifier': 'identifier',
        'string': 'string',
        '(': '( expression )',
        'number': 'number'
    },
    'number': {
        'digit': 'digit'
    },
    'identifier': {
        'identifier': 'identifier ( expression ) op term',
        '(': '( expression ) op term'
    },
    'op': {
        '+': '+ term',
        '-': '- term',
        '*': '* term',
        '/': '/ term'
    },
    'string': {
        'identifier': 'identifier',
        'string': 'string'
    },
    'digit': {'digit': 'digit'}
}




'''























# PARSE TABLE


'''
# Creating DataFrame from Parse Table
df = pd.DataFrame.from_dict(parse_table, orient='index')
df.index.name = 'Non-terminal'
df.columns.name = 'Terminal'
df.fillna('', inplace=True)
df = df.rename(columns=lambda x: 'digit' if x.isdigit() else x)

# Displaying Parse Table
print()
print("PARSE TABLE:")
print()
print(df)

# Parse Tree created using rules.
# Sample input sequences for different statements
assign_st = ["IDENTIFIER", "IDENTIFIER", "EQUALS", ["NUMBER", "STRING", ["NUMBER", ["PLUS", "MINUS", "TIMES", "DIVIDE"], "NUMBER"]], "SEMI_COLON"]
print_st = ["IDENTIFIER", "LPAREN", ["IDENTIFIER", "NUMBER", "STRING"], "RPAREN", "SEMI_COLON"]
if_st = ["IDENTIFIER", "LPAREN", "IDENTIFIER", ["GREATER_THAN", "LESS_THAN", "EQUALS", ">=", "<="], "NUMBER", " RPAREN", "{", "IDENTIFIER", "LPAREN", "IDENTIFIER", "RPAREN", "SEMI_COLON", "}"]
else_st = ["IDENTIFIER", "{", "IDENTIFIER", "LPAREN", "IDENTIFIER", "RPAREN", "SEMI_COLON", "}"]
while_st = ["IDENTIFIER", "LPAREN", "IDENTIFIER", ["GREATER_THAN", "LESS_THAN", "EQUALS", ">=", "<="], "NUMBER", " RPAREN", "{", "IDENTIFIER", "LPAREN", "IDENTIFIER", "RPAREN", "SEMI_COLON", "}"]

program1 = []
program2 = []

tokens = lexer.lex(text_input)

# Counting the number of semicolons in the input for loop iterations
w = 0
for token in tokens:
    if token.gettokentype() == "SEMI_COLON":
        w += 1

stmt = 1
tokens = lexer.lex(text_input)

inp1 = []
inp2 = []

'''















'''
# Parsing the input into statements
for token in tokens:
    # Skipping whitespace and newline characters
    if token.getstr() == "\n" or token.gettokentype() == "NEWLINE" or token.getstr() == " " or token.gettokentype() == "NEWLINE" or token.getstr() == "}":
        continue

    # Adding token information to lists
    inp2.append(token.getstr())
    inp1.append(token.gettokentype())

    # Checking for semicolon to split statements
    if token.gettokentype() == "SEMI_COLON":
        program1.append(inp1)
        program2.append(inp2)

        # Resetting lists for the next statement
        inp1 = []
        inp2 = []

        # Checking if all statements have been processed
        if stmt == w:
            break
        stmt += 1


        prog = ""  # Placeholder for prog variable
        item_1 = ["IDENTIFIER", "NUMBER", "STRING", "PLUS", "MINUS", "TIMES", "DIVIDE", "SEMI_COLON"]
        eq = 0  # Placeholder value for 'eq' variable
        pr = 0  # Placeholder value for 'pr' variable


add = ""
for u in range(w):
    if program2[u][0] in item_1 or program2[u][1] in item_1:  # Parse Tree for Assignment Statement
        add += "(stm"
        add += "(assign_stm "
        bro = 0
        eq += 1
        for k in range(len(program1[u])):
            if k == 3:
                if program1[u][3] in assign_st[3][2]:
                    if len(program1[u]) > 6:
                        qqq = k
                        for c in range(2):
                            add += " " + "(" + program1[u][qqq] + " ( " + program2[u][qqq] + " ) " +")"
                            bro += 1
                            if qqq == 3 and program1[u][qqq + 1] in assign_st[3][2][1]:
                                add += " " + "(" + program1[u][qqq + 1] + " ( " + program2[u][qqq + 1] + " ) " +")"
                                bro += 1
                            qqq += 2

                        add += " " + "(" + "SEMI_COLON" +  "(" +   ";" + " ) " +")"
                        bro += 1
                        
                    else:
                        add += " " + "(" + program1[u][3] + " ( " + program2[u][3] + " ) " +")"
                        bro += 1
                        continue
                    break

            if assign_st[k] == program1[u][k]:
                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1

                '''













# PARSE TREE



'''    
    if program2[u][0] == "print":  # Parse Tree for Print Statement
        add += "(print_stm "
        bro = 0
        pr += 1

        for k in range(len(program1[u])):
            if k == 2:
                if program1[u][2] in print_st[2]:
                    add += " " + "(" + program1[u][2] + " ( " + program2[u][2] + " ) " +")"
                    bro += 1
            if print_st[k] == program1[u][k]:
                if program2[u][k] == ")" or program2[u][k] == "(" or program2[u][k] == ";":
                    add += " " + program1[u][k]
                    continue                    

                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1


    if program2[u][0] == "if":  # Parse Tree for If Statement
        add += "(if_stm "
        bro = 0
        pr += 1
        for k in range(len(program1[u])):
            if k == 3:
                if program1[u][3] in if_st[3]:
                    add += " " + "(" + "Operator" + " ( " + program2[u][3] + " ) " +")"
                    bro += 1
            if if_st[k] == program1[u][k]:
                if program2[u][k] == ")" or program2[u][k] == "(" or program2[u][k] == ";":
                    add += " " + program1[u][k]
                    continue                    

                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1


    if program2[u][0] == "while":  # Parse Tree for While Statement
        add += "(while_stm "
        bro = 0
        pr += 1
        for k in range(len(program1[u])):
            if k == 3:
                if program1[u][3] in while_st[3]:
                    add += " " + "(" + "Operator" + " ( " + program2[u][3] + " ) " +")"
                    bro += 1
            if while_st[k] == program1[u][k]:
                if program2[u][k] == ")" or program2[u][k] == "(" or program2[u][k] == ";":
                    add += " " + program1[u][k]
                    continue                    

                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1

    if program2[u][0] == "else":  # Parse Tree for Else Statement
        add += "(else_stm "
        bro = 0
        pr += 1
        for k in range(len(program1[u])):
            if else_st[k] == program1[u][k]:
                if program2[u][k] == ")" or program2[u][k] == "(" or program2[u][k] == ";":
                    add += " " + program1[u][k]
                    continue                    

                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1
'''