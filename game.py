import random


user_name = input("Enter your User Name: ").capitalize()
playing_game = True
player_choice = None
player_score  = 0
computer_score = 0
turns = 0

def operate_game():
    print(f"""Welcome {user_name}.          
Can you out guess the Computer?? 
Let's find out...
You have 3 chances to Win
          
          """)
    global player_score
    global computer_score
    global playing_game
    
    valid_choices = ("rock", "paper", "scissors")
    global turns
    global player_choice 
   
    while ((playing_game == True) and (turns != 3)) :
        turns += 1
        player_choice = None
        computer_choice = random.choice(valid_choices)

        while player_choice not in valid_choices:
            print(computer_choice)
            player_choice = input("Enter your choice(rock, paper or scissors): ")

        print(f"{user_name}'s Choice: {player_choice}")
        print(f"Computer's Choice: {computer_choice}")

        if player_choice == computer_choice:
            player_score += 1
            computer_score += 1
            print("It is a tie!")

        elif (player_choice == "rock") and (computer_choice == "scissors"):
            player_score += 1
            print(f"{user_name} Wins!")

        elif (player_choice == "paper") and (computer_choice == "rock"):
            player_score += 1
            print(f"{user_name} Win!")

        elif (player_choice == "scissors") and (computer_choice == "paper"):
            player_score += 1
            print(f"{user_name} Wins!")

        else:
            computer_score += 1
            print(f"{user_name} Loses!")
    if turns == 3:
        playing_game = False
        score()
    return turns


def score():
        if computer_score == 2 and player_score == 2:
            print("It is a Tie")
            print("There is no winner")
        elif (player_score == 3 and computer_score == 0) or (player_score == 2 and computer_score == 1) or (player_score ==3 and computer_score == 2):
            print(f"You are the Overall winner")

        else:
            print("Overall winner is the Computer")
            print("Better Luck Next Time")   

def terminate_game():
        playing_game == False
        print(f"Goodbye {user_name}!!")

def continue_game():
    
    playing_game == True
    operate_game()

def run_game():
    #playing_game = True
    operate_game()
    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == "N" :
        terminate_game()
    else:
        turns = 0
        continue_game()
    
    
     
if __name__ == "__main__":
    run_game()