# Importing required modules and classes
from rply import LexerGenerator, ParserGenerator
from lexer import Lexer  # Assuming there's a separate file named 'lexer.py' containing the Lexer class
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

        # Storing identifiers, strings, and numbers
        if token.gettokentype() == "IDENTIFIER" or token.gettokentype() == "STRING" or token.gettokentype() == "NUMBER":
            lis.append(token.getstr())  

        # Incrementing line number counter for various newline patterns
        if token.getstr() == "\n\n" or token.getstr() == "\n     \n" or token.getstr() == "\n    \n": 
            z += 2

        # Incrementing line number counter for newline characters
        if token.getstr() == "\n    " or token.getstr() == "\n" or token.getstr() == "\n     ":
            z += 1
            
        # Storing identifiers and their line numbers
        if token.gettokentype() == "IDENTIFIER" or token.gettokentype() == "NEWLINE":
            if token.getstr() == "int" or token.getstr() == 'str' or token.getstr() == 'float':
                continue

            lis2.append(token.getstr())
            lis2.append(z)

except Exception as e:
    # Handling unrecognized token name error
    print('There was an error: You have entered unrecognized token name!')
    print("Error: ", e)
    quit()

# Code for building symbol table is present here but not commented. It seems to be populating a symbol table based on the lexed tokens.

# Displaying symbol table
# Print the symbol table data

# Creating symbol table as a list of dictionaries
# Each dictionary contains information about a variable
# Name, Address, Type, Dimensions, Line Declared, Reference Line

# Parse Table
# A dictionary representing the parse table for a grammar

# FIRST and FOLLOW sets
# Dictionaries representing the FIRST and FOLLOW sets for various non-terminals in the grammar

# Creating DataFrame from Parse Table
# Converting parse table dictionary into a DataFrame for better visualization

# Displaying Parse Table

# Parse Tree creation section starts here
# Sample input sequences for different statements

# Initialization
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

# Placeholder variables for the parse tree generation
prog = ""
item_1 = ["IDENTIFIER", "NUMBER", "STRING", "PLUS", "MINUS", "TIMES", "DIVIDE", "SEMI_COLON"]
eq = 0
pr = 0

# Parse Tree creation loop
add = ""
for u in range(w):
    if program2[u][0] in item_1 or program2[u][1] in item_1:  # Parse Tree for Assignment Statement
        # Add nodes to parse tree for assignment statement
    if program2[u][0] == "print":  # Parse Tree for Print Statement
        # Add nodes to parse tree for print statement
    if program2[u][0] == "if":  # Parse Tree for If Statement
        # Add nodes to parse tree for if statement
    if program2[u][0] == "while":  # Parse Tree for While Statement
        # Add nodes to parse tree for while statement
    if program2[u][0] == "else":  # Parse Tree for Else Statement
        # Add nodes to parse tree for else statement


























