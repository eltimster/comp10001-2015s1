###############################################################
#
# Random game player -- generates a shuffled pack of cards and
# deals the cards to the four players, then plays the player
# against itself, optionally in bonus mode
#
# NOTE: relies on an implementation of the following function
# in `program.py':
#
#   get_winner_score(trick, round_id, deck_top):
#
# which takes a single trick `trick' (a tuple), the round_id
# (an int) and `deck_top' (a list of strings, as per `score_game')
# and returns a 2-tuple:
#
#   (ID, trick_score)
#
# where `ID' is the index of the winnder of the trick (relative
# to the order of play in the trick, and *not* the global player IDs)
# and `trick_score' is the score for the current trick (to be
# allocate to the winning player). For example:
#
# >>> get_winner_score(('2S', 'AS', 'QS', '7D'), 2, ['2D', '3S'])
# (3, 0)
# >>> get_winner_score(('2S', 'AS', 'QS', '7D'), 4, ['2D', '3S', 'JS'])
# (1, 13)
#
#
# Author: Tim Baldwin:
#
# Version 1
#
# Date: 22/5/2015
#
#
###############################################################


import itertools, random
from collections import defaultdict 

import program


VALUES = 'AKQJ098765432'
SUITS = 'SHDC'

HANDSIZE = 10

PLAYERS = 4

PHASE_ONE_TRICKS = 3

TOTAL_TRICKS = 13







def generate_random_game(rounds, bonus=False, verbatim=True):
    assert 0 < rounds <= TOTAL_TRICKS
    deck = [val+suit for val,suit in itertools.product(VALUES, SUITS)]
    random.shuffle(deck)
    players = [[], [], [], []]

    for i in range(HANDSIZE):
        for j in range(PLAYERS):
            players[j].append(deck.pop())

    prev_tricks = []
    deck_top = [deck.pop()]

    if bonus:
        pred_scores = []
        player_data = []
        for i in range(PLAYERS):
            score = program.predict_score(players[i])
            pred_scores.append(score)
            player_data.append(score)
        pred_scores = tuple(pred_scores)

    prev_winner = 0
    for round_id in range(rounds):
        curr_trick = []
        for j in range(PLAYERS):
            player_id = (prev_winner + j) % PLAYERS
            if bonus:
                card, player_data[player_id] = program.play(curr_trick, players[player_id], prev_tricks, deck_top, player_data=player_data[player_id])
            else:
                card = program.play(curr_trick, players[player_id], prev_tricks, deck_top, suppress_player_data=True)
            curr_trick.append(card)
            players[player_id].remove(card)
        curr_trick = tuple(curr_trick)
        prev_tricks.append(curr_trick)
        curr_winner, _score = program.get_winner_score(curr_trick, round_id, deck_top)
        prev_winner = (curr_winner + prev_winner) % PLAYERS
        if round_id < PHASE_ONE_TRICKS:
            for j in range(PLAYERS):
                if j == prev_winner:
                    players[j].append(deck_top[round_id])
                else:
                    players[j].append(deck.pop())
            if deck:
                deck_top.append(deck.pop())

    scores = program.score_game(prev_tricks, deck_top)
    if verbatim:
        if bonus:
            print("PREDICTED SCORES: {}".format(pred_scores))
            print("ORIGINAL SCORES: {}".format(scores))
            rev_scores = []
            for i in range(PLAYERS):
                diff = abs(scores[i] - pred_scores[i])
                if diff == 0:
                    rev_scores.append(scores[i] - 10)
                elif 1 <= diff <= 2:
                    rev_scores.append(scores[i] - 2)
                elif 3 <= diff <= 4:
                    rev_scores.append(scores[i])
                elif 5 <= diff <= 6:
                    rev_scores.append(scores[i] + 2)
                elif 7 <= diff <= 8:
                    rev_scores.append(scores[i] + 4)
                else:
                    rev_scores.append(scores[i] + 10)
            scores = tuple(rev_scores)
            print("ADJUSTED SCORES: {}".format(scores))
        else:
            print("SCORES: {}".format(scores))



generate_random_game(13, bonus=True)
