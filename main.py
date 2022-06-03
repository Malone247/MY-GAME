import random


while True:
 ai_score, player_score = 0, 0
 game = ['R','P','S']
 rounds = int(input('Welcome to the Rock Paper Scissor game. Before starting, how many rounds would you like to choose : 3, 5 or 7?'))

 for round in range(rounds):
    player_choice = input('Please choose your move : R for rock, P for paper, S for scissors :')
    ai_choice = random.choice(game)
    if player_choice in game:
        if player_choice == ai_choice:
            print("it's a draw")
        elif player_choice == 'R':
            if ai_choice == 'S':
                player_score += 1
                print("Rock('R') smashes scissors('S')! You win!")
            elif ai_choice == 'P':
                ai_score += 1
                print("Paper covers rock! You lose.")
        elif player_choice == 'P':
            if ai_choice == 'R':
                player_score += 1
                print("Paper('P') covers rock! You win!")
            elif ai_choice == 'S':
                ai_score += 1
                print("Scissors cuts paper! You lose.")
        elif player_choice == 'S':
            if ai_choice == 'P':
                player_score += 1
                print("Scissors('S') cuts paper! You win!")
            elif ai_choice == 'R':
                ai_score += 1
                print("Rock smashes scissors! You lose.")
        print("This is round %d" % round)
        score = [ai_score, player_score]
        print("The score is %s" % score)
        print(score)
    else:
        print('Please enter one of the 3 choices')
       