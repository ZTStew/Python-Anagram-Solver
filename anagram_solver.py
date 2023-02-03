
# User string
anagram = "abc"

# sets first letter in solution
i = len(anagram) - 1
# counts backwards through given anagram
while i >= 0:
  # will be each solution value, set first with letter
  option = anagram[i]
  print(option)

  i -= 1

