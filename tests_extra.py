# dictionary of extra tests, one for each function in the project spec; in each case, list a number of function calls (as a str), and the correct output for each

# Version: 1.2
# Updated 25/5/15
#
# Changelog:
#
# v1.1: tweaks to test cases to test optional arguments
# v1.2: fix to first test case for `play' to make first argument a tuple

test_cases = {
    "is_broken_hearts":
        [
        # QS doesn't break hearts
         ("""submission.is_broken_hearts([('AD', 'JD', '3D', '6D'), ('0S', '2S', 'JS', '5S'), ('5H', '9H', '2H', 'QH'), ('3C', 'QC', '0C', 'KC'), ('4D', '9D', '8D', '7D'), ('2D', '8C', 'KD', '0D'), ('3S', '8S', '4S', '7S'), ('9S', '6S', 'AS', 'QS')])""", False),  
         # test to make sure optional second argument supported
         ("""submission.is_broken_hearts([], ('AH',))""", False), 
        ],

    "is_valid_play":
        [
         ("""submission.is_valid_play('2H', ('4S', '0D'), ['2H', 'KH', 'QH', '5D', '8H', '8D', 'JD'], [('9H', '5H', '7H', 'JH'), ('QD', '2D', 'AD', 'KD'), ('3S', '2S', '8S', 'AS'), ('JC', '4C', '0C', '5C'), ('JS', '0S', '9S', 'QS'), ('6D', '4D', '9D','3D')])""", True),
        ],

    "score_game":
        [
        # example of shooting the moon before the last trick
        ("""submission.score_game([('KD', '9D', '0D', '5D'), ('QD', '3S', 'AD', 'JD'), ('4H', '6H', '7H', 'QS'), ('7C', '6C', '0C', 'JC'), ('4C', '4D', '3C', 'QC'), ('6D', '8D', '2C', '2H'), ('9C', '0H', 'KH', '7D'), ('3D', '7S', '9H', 'AH'), ('QH', '5H', 'JH', '3H'), ('2D', 'JS', '2S', '8H')], ['QH', '0S', 'JH'])""",(0, 0, 0, -10)),
        ],

    "play":
        [
         ("""submission.play(('8C',), ['KH', '7C', '2S', '6S', 'JS', '0D', '8H', '3S'], [('AC', '3C', '0C', '6C'), ('KD', '8D', '5D', '4D'), ('JH', '0H', '5H', '2H'), ('AS', 'KS', 'QS', '9S'), ('3D', '9D', 'JD', '7D')], ['JH', 'AS', '7S'], suppress_player_data=True)""", '7C'),
         # test case of suppress_player_data=False (in which case function should return a 2-tuple)
         ("""submission.play(('KC', '0C'), ['QD', 'JS', '7H', 'AS', 'AH', '4C', '8H', '3D', 'KD', 'QS'], [('9C', '5C', '7C', 'JC')], ['2S', 'JH'], suppress_player_data=False)""", ('4C', None)),
         # test to make sure code handles optional arguments
         ("""submission.play(('KC', '0C'), ['QD', 'JS', '7H', 'AS', 'AH', '4C', '8H', '3D', 'KD', 'QS'], [('9C', '5C', '7C', 'JC')], ['2S', 'JH'], suppress_player_data=False, score=submission.score_game, player_data=None)""", ('4C', None)),
         ],

        }
