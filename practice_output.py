"""
A little assignment to practice printing text 
output to the Python command line.
Do not run this file... run main.py instead.
"""

def print_with_line_break():
  """
  Prints out the text, 'Hello world!' with a line break at the end
  """
  # write your code here
print('Hello World!', end='\n')

def print_without_line_break():
  """
  Prints out the text, 'Hello world!' without a line break at the end
  """
  # write your code here
print('Hello world!', end='')

def print_with_separator_dash_and_with_line_break():
  """
  Prints out the following words, with dashes "-" between them
  and a line break at the end:
  "Twas", "brillig", "and", "the", "slithy", "toves"
  """
  # write your code here
  # you must supply each word as a separate argument to the print() function
print("Twas", end='-')
print("brillig", end='-')
print("and", end='-')
print("the", end='-')
print("slithy", end='-')
print("toves", end='\n')

def print_with_separator_dash_and_without_line_break():
  """
  Prints out the following words, with dashes "-" between them
  and without a line break at the end:
  "Twas", "brillig", "and", "the", "slithy", "toves"
  """
  # write your code here
  # you must supply each word as a separate argument to the print() function
print("Twas", end='-')
print("brillig", end='-')
print("and", end='-')
print("the", end='-')
print("slithy", end='-')
print("toves", end='')
