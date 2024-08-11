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






# Iterating through tokens
try:
    for token in tokens:
        print(token)
        i += 1
        dic[str(i) + " - " + token.gettokentype()] = token.getstr()  # Storing token in dictionary

        token_type = token.gettokentype()
        token_str = token.getstr()

        if token_type in ["IDENTIFIER", "STRING", "NUMBER"]:
            lis.append(token_str)

        if token_str.startswith("\n"):
            z += 2 if len(token_str) > 1 else 1

        if token_type in ["IDENTIFIER", "NEWLINE"] and token_str not in ["int", "str", "float"]:
            lis2.append(token_str)
            lis2.append(z)

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