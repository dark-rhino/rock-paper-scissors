import random
options = ['rock' , 'paper' , 'scissors']
comp_choice = random.choice(options)
comp_choice1 = print(comp_choice)
print(''' _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)''')
user_choice =(input("enter youre choice\n r-rock\n p-paper\n s-scissors\n"))
if user_choice not in ["r","p","s"]:
  print("invalid choice")
comp_choice1 = print(comp_choice)
if user_choice == "r" and comp_choice == "rock":
 print("you chose rock and comp chose rock\n its a draw!")
elif user_choice == "r" and comp_choice == "paper":
  print("you chose rock and comp chose paper\n you lose!")
elif user_choice == "r" and comp_choice == "scissors":
  print("you chose rock and comp chose scissors\n you win!")
elif user_choice == "p" and comp_choice == "rock":
  print("you chose paper and comp chose rock\n you win!")
elif user_choice == "p" and comp_choice == "paper":
  print("you chose paper and comp chose paper\n its a draw!")
elif user_choice == "p" and comp_choice == "scissors":
  print("you chose paper and comp chose scissors\nyou lose!")
elif user_choice == "s" and comp_choice == "rock":
  print("you chose scissors and comp chose rock\nyou lose!")
elif user_choice == "s" and comp_choice == "paper":
  print("you chose scissors and comp chose paper\n you win!")
elif user_choice == "s" and comp_choice == "scissors":
  print("you chose scisssors and comp chose scissors\n its a draw")