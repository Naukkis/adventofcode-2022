from input_reader import read_input

action_type = {'A': 'rock',
               'B': 'paper',
               'C': 'scissors',
               'X': 'rock',
               'Y': 'paper',
               'Z': 'scissors'}


def part1(input_data):
    total_score = 0
    for game in input_data:
        moves = game.split(" ")
        opponent_action = action_type[moves[0]]
        player_action = action_type[moves[1]]
        winner = determine_winner(opponent_action, player_action)
        score = calculate_score(player_action, winner)
        total_score = total_score + score
    print(total_score)


def part2(input_data):
    total_score = 0

    for game in input_data:
        moves = game.split(" ")
        opponent_action = action_type[moves[0]]
        player_action = determine_move(moves[1], opponent_action)
        winner = determine_winner(opponent_action, player_action)
        score = calculate_score(player_action, winner)
        total_score = total_score + score

    print(total_score)


def determine_move(desired_result, opponent_action):
    if desired_result == 'X':
        if opponent_action == 'rock':
            return 'scissors'
        elif opponent_action == 'scissors':
            return 'paper'
        else:
            return 'rock'
    elif desired_result == 'Y':
        return opponent_action
    else:
        if opponent_action == 'rock':
            return 'paper'
        elif opponent_action == 'scissors':
            return 'rock'
        else:
            return 'scissors'


def determine_winner(opponent_action, player_action):
    if opponent_action == player_action:
        return 0
    elif opponent_action == 'rock':
        if player_action == 'scissors':
            return 1
        else:
            return 2
    elif opponent_action == 'paper':
        if player_action == 'rock':
            return 1
        else:
            return 2
    elif opponent_action == 'scissors':
        if player_action == 'paper':
            return 1
        else:
            return 2


def calculate_score(player_move, winner):
    score_rules = {'rock': 1, 'paper': 2, 'scissors': 3}

    if winner == 1:
        score = score_rules[player_move]
    elif winner == 2:
        score = 6 + score_rules[player_move]
    else:
        score = 3 + score_rules[player_move]
    return score


if __name__ == '__main__':
    input_data = read_input(2, str, False)
    part1(input_data)
    part2(input_data)
