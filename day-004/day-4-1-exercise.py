'''Heads or Tails

Instructions
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails

Example Output
Heads
or

Tails'''

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

random_int = random.randint(0, 10) # returns random integer numbers.
random_rand = random.random()      # returns random floating numbers between 0 and 1.
random_flt = random.uniform(1, 10) # returns random floating numbers over 1.

print(random_int)
print(random_rand)
print(random_flt)

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")
  