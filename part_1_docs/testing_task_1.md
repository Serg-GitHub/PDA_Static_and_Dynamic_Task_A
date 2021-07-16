### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python


class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  # on line 22, the if statement  is missing a = it should be double equals ==
      return True
    else # on line 24 the else statement is missing a colon : right after it to close it
      return False
   
   
  dif highest_card(self, card1 card2): # on line 28 dif should be def, a comma is also missing after card1 inside the parentheses,
  if card1.value > card2.value: #on line 29 the if statement has an indentation error
    return card #on line 30 return card should be return card1
  else:
    return card2
  

def cards_total(self, cards): # on line 35 def has an indentation error it should be further in

  total # on line 37 total is an undefined variable, as we don't know what the value is we use 0
  for card in cards:
    total += card.value
    return "You have a total of" + total # on line 40 the return statement is not indented to match the for loop and should be in line with the for statement on line 38, also on line 40 + total is an integer, it has to be concatenated into a string.
  
```
