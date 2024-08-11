from rply import LexerGenerator
import re

class Lexer:
    def __init__(self):
        self.lexer = self._build_lexer()

    def _build_lexer(self):
        lexer_gen = LexerGenerator()

        # Define tokens and their corresponding regular expressions
        lexer_gen.add('TYPE_STRING', r'str(?!\w)')
        lexer_gen.add('ASSIGN_STRING', r'=')
        lexer_gen.add('FLOAT', r'-?\d+\.\d+')  # Matches floating-point numbers
        lexer_gen.add('INTEGER', r'-?\d+')  # Matches integers
        lexer_gen.add('NEWLINE', r'\n+ *\n*')
        lexer_gen.add('SEMI_COLON', r';')
        lexer_gen.add('BOOLEAN', r'true(?!\w)|false(?!\w)')  # Matches boolean values

        # Keywords, operators, and identifier token
        lexer_gen.add('KEYWORD', r'\b(?:if|else|end|and|or|not|let|for|while|break|continue|match|enum|new|return|type|array|dict|integer|float|char|long|double|record|function|lambda|private|module|trait|implement|import|send|receive)\b')
        lexer_gen.add('OPERATOR', r'\+|-|\*|/|%|==|!=|>=|<=|>|<|=|\[|\]|\{|\}|\||,|\.|:|\(|\)')
        lexer_gen.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')

        # Ignore whitespace
        lexer_gen.ignore(r'[ \t\r\f\v]+')

        return lexer_gen.build()

    def get_lexer(self):
        return self.lexer

    # Function to tokenize the input source code
    def lex(self, source):
        return self.lexer.lex(source)  # Tokenize the modified source code
