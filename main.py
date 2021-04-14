
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
get_choose = random.randint(0,2)
print(" Professional Rock Paper Scissors GAME")
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
my_choose = [rock,paper, scissors]
'''               computer
      computer    ["Rock","Paper", "Scissors"]
      vs 
      you
  y    "Rock"      ['Even', 'Loose', 'Win']
  o    "Paper"    [ 'Win','Even', 'Loose']
  u    "Scissors"  [ 'Loose','Win', 'Even']
'''
choose_rock = ['Even', 'Loose', 'Win']
choose_paper = [ 'Win','Even', 'Loose']
choose_scissors =  [ 'Loose','Win', 'Even']
win_loose_even = [choose_rock, choose_paper, choose_scissors]
if choose <= 2:
  print(f"Your play its:\n")
  print(my_choose[choose])
  print(f"My play its: \n")
  print(my_choose[get_choose])

  if win_loose_even[choose][get_choose] == 'Even':
    print("We are Even")
  else:
    print(f"You {win_loose_even[choose][get_choose]}")
else:
  print("Bad choosed option")

