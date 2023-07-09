from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from data import Data

base = Data()

while True:
  text = input()

  tokenizer = Lexer(text)
  tokens = tokenizer.tokenize()

  print("TOKENS")
  print(tokens)

  parser = Parser(tokens)
  tree = parser.parse()

  print("TREE")
  print(tree)

  interpreter = Interpreter(tree, base)
  result = interpreter.interpret()

  if result is not None:
    print(result)
    print("DATA")
    print(base.variables)