
# initialise list to hold game history
game_history = []

# get data (base component does this already, code below fore testing purposes)

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("User points? "))
    comp_points = int(input("Computer points?"))
    winner = input("who won?")
    user_score = int(input("user score: "))
    comp_score = int(input("computer score: "))

    game_results = (f"Round {rounds_played}: User Points: {user_points} | "
                    f"Computer points {comp_points}, {winner} wins"
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("game history")

for item in game_history:
    print(item)
