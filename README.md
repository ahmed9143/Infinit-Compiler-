# Infinite Compiler

Welcome to the Infinite Compiler repository! This repository contains all the necessary documents, design specifications, implementation details and related tools for Infinite Compiler. Infinite Compiler is an easy-to-learn programming language that has a simple syntax which makes it perfect for beginners.

Infinite Compiler is an open source programming language that makes it easy to build simple.

## Infinite Compiler - Language Features:

* Visualize Compiler `Lexer`.
* Visualize Compiler `Symbol Table`.
* Visualize Compiler `Parser`.
* Visualize Compiler `Parse Tree`.
* Visualize Compiler `Parse Table`.

## Infinite Compiler - Language Definition: 

* `Language Delimiter` will be defined as “;” as end of line.
* `Boolean:` True and False.
* `Blocks` will be contained in ‘{’ and ‘}’.
* `Keywords (Reserved Words):` ‘#’, ‘;’, ‘for’, ‘while’, ‘if’, ‘elif’, ‘else’, ‘and’, ‘or’, ‘def’ and ‘print’. Identifiers (Variables Name): starts with a letter (A to Z or a to z), lowercase and uppercase letters are distinct, and does not allow punctuation characters such as @, $, and %.
* `Operators:` + , - , * , / , **, == , != , < , > , <= , >=.
* `Literals:` Integers, Floating Points and Strings.
* `Data Structure:` List defined by double brackets ‘[]’.
* `Types` may `not change after assignment`, but `values may change`.

## Infinite Compiler - Language Grammar:

```python
program
   : statement+
   ;

statement
   : 'if' paren_expr statement
   | 'if' paren_expr statement 'else' statement
   | 'while' paren_expr statement
   | '{' statement* '}'
   | expr ';'
   | ';'
   ;

expr
   : test
   | id '=' expr
   ;

test
   : sum
   | sum '<' sum
   ;

sum
   : term
   | sum '+' term
   | sum '-' term
   ;

term
   : id
   | integer
   | paren_expr
   ;

id
   : STRING
   ;

integer
   : INT
   ;


STRING
   : [A-Za-z][A-Za-z0-9_]*
   ;


INT
   : [0-99999]+
   ;
