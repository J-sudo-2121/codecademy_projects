import random

money = 100

#Coin Flip
def coin_flip(call, amount):
  if random.randint(1,2) == 2:
    flip = 'Heads'
  else:
    flip = 'Tails'
  if call == flip:
    result = 'won'
    total_amount = money + amount
  else:
    result = 'lost'
    total_amount = money - amount
  
  print('You flipped %s and you called %s! You %s and now have $%.2f' %(flip, call, result, total_amount))
  return total_amount


print()

#Cho-Han
def cho_han(guess, amount):
  num1 = random.randint(1, 6)
  num2 = random.randint(1, 6)
  total = num1 + num2
  result = ''
  if total % 2 == 0:
    outcome = 'Even'
  else:
    outcome = 'Odd'
  
  if guess == outcome:
    result = 'won'
    total_amount = money + amount
  else:
    result = 'lost'
    total_amount = money - amount
  print('You guessed %s and rolled an %s number! You %s and now have $%.2f!' %(guess, outcome, result, total_amount))
  return total_amount

print()

#Pick a Card
def pick_a_card(amount):
  house = random.randint(1,13)
  player = random.randint(1,13)
  if house > player:
    outcome = house
  elif house < player:
    outcome = player
  else:
    outcome = 'Tie'
    
  if outcome == house:
    winner = 'House'
    total_amount = money - amount
  elif outcome == player:
    winner = 'Player'
    total_amount = money + amount
  else:
    winner = 'Nobody'
    total_amount = money
  
  print('You drew %s. %s has been drawn by the house. %s wins and you now have $%.2f!' %(player, house, winner, total_amount))
  return total_amount

print()

#Roulette

def roulette(guess, amount):
  spin = random.randint(0, 37)
 # 37 == 00
  if guess == 'Odd' and spin % 2 == 1 and guess != 37:
    outcome = 'won'
    total_amount = (amount *2) + money
  elif guess == 'Even' and spin % 2 == 0 and guess != 37:
    outcome = 'won'
    total_amount = (amount *2) + money
  elif guess == spin and guess != 0 and guess != 37:
    outcome = 'won'
    total_amount = (amount *35) + money
  elif guess == 0 and spin == 0 and guess != 37:
    outcome = 'won'
    total_amount = (amount * 17) + money
  elif guess == 37 and spin == 37 and guess != 0:
    outcome = 'won'
    total_amount = (amount * 17) + money
  else:
    outcome = 'lose'
    total_amount = money - amount
    
  print('You bet on %s and the ball landed on %s. You %s. You bet $%s and now have $%.2f.' %(guess, spin, outcome, amount, total_amount))
  return total_amount

print()
