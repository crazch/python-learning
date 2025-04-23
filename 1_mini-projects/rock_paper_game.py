"""
Rock-Paper-Scissors (CLI)
- Inputs: 'r', 'p', 's'.
- AI: Random choice.
- Output: Win/loss/tie.
- Usage: Run `rockpaper.py`
"""

import random

def play():
	user = input("Choose 'r', 'p', 's': ") 
	computer = random.choice(['r', 'p', 's']) 
	if user == computer:
		return "It's a Tie!" 
	
	if is_win(user, computer):
		return ("You Win") 
		
	return "You lost'"
def is_win(player, opponent):
	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
		return True
	
print(play())