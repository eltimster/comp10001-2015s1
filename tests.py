# dictionary of tests, one for each function in the project spec; in each case, list a number of function calls (as a str), and the correct output for each

# Version: 1.2
# Updated 19/5/15
#
# Changelog:
#
# v1.1: tweaks to test cases to remove impossible game states
# v1.2: tweaks to `play' tests, to make the first argument a tuple rather than a list


test_cases = {
    "is_broken_hearts":
        [
         ("""submission.is_broken_hearts([('AD', 'JD', '3D', '6D'), ('0S', '2S', 'JS', '5S'), ('5H', '9H', '2H', 'QH'), ('3C', 'QC', '0C', 'KC'), ('4D', '9D', '8D', '7D'), ('2D', '8C', 'KD', '0D'), ('3S', '8S', '4S', '7S'), ('9S', '6S', 'AS', 'KS')])""", False), 
         ("""submission.is_broken_hearts([('AD', 'JD', '3D', '6D'), ('0S', '2S', 'JS', '5S'), ('5H', '9H', '2H', 'QH'), ('3C', 'QC', '0C', 'KC'), ('4D', '9D', '8D', '7D'), ('2D', '8C', 'KD', '0D'), ('3S', '8S', '4S', '7S'), ('9S', '6S', 'AS', 'KS')], ('4H',))""", True), 
         ("""submission.is_broken_hearts([('6S', '9S', '2S', '5S'), ('KH', '6H', '0H', '9H'), ('KD', '6D', '0D', 'AD'), ('JD', '2D', '3D', 'QD'), ('7D', 'AH', '8D', '3S'), ('4S', 'JS', 'QS', '0S'), ('KC', 'AC', '4C', '7C'), ('7S', 'JC', 'KS', '8S')], ())""", True), 
         ("""submission.is_broken_hearts([('JD', '6D', '0D', '9D')])""", False), 
         ("""submission.is_broken_hearts([])""", False), 
        ],
    "is_valid_play":
        [
         # can lead '0D' whether hearts are broken or not
         ("""submission.is_valid_play('0D', (), ['0D', '9S', '3S', '3D', '3H', '5D', 'AD', '6C', '7D', '6H'], [])""", True), 
         ("""submission.is_valid_play('0D', (), ['0D', '9S', '3S', '3D', '3H', '5D', 'AD', '6C', '7D', '6H', 'JH'], [])""", True),

         # must follow suit if card of that suit held
         ("""submission.is_valid_play('4H', ('KH',), ['7C', '4H'], [('QH', 'AH', '3H', '0H'), ('2H', '8H', '9H', '7H'), ('6C', '0C', '9C', 'QC'), ('9D', '8D', '5D', 'JD'), ('7D', '6D', 'AD', '4D'), ('2C', 'AC', 'JC', 'KC'), ('3S', '8S', '2S', '7S'), ('4S', '0S', 'QS', 'AS'), ('6S', '3D', '9S', 'KS'), ('5S', '2D', 'JS', '3C'), ('4C', '8C', '0D', '5C')])""", True),

         # must play card actually held in hand
         ("""submission.is_valid_play('KS', (), ['0D', '9S', '3S', '3D', '3H', '5D', 'AD', '6C', '7D', 'JH'], [])""", False), # updated to hand size of 10 (v1.1)

         # can lead with heart in phase one
         ("""submission.is_valid_play('JH', (), ['0D', '9S', '3S', '3D', '3H', '5D', 'AD', '6C', '7D', 'JH'], [])""", True),

         # can't lead with heart in phase two if hearts not broken and hold non-hearts
         ("""submission.is_valid_play('JH', (), ['JH', '3S', '2H', '9H', 'JS', '5C', '8H', 'KD', 'AD', '7H'], [('QC', 'QS', '0S', '4H'), ('4C', '4S', 'QD', '6H'), ('2C', 'AH', '6S', 'AC')])""", False),

         # can lead with queen of spaces in phase two even if hearts not broken
         ("""submission.is_valid_play('QS', (), ['JS', '6H', '3D', 'QS', '6C', '4H', '9H', 'AS', 'QC', '0D'], [('JD', '9S', '2H', '6D'), ('5C', '0S', 'AC', '2D'), ('KC', '9D', '5S', '4S')])""", True),

         # can discard any card if no card of the suit lead is held
         ("""submission.is_valid_play('QS', ('JH',), ['6S', '5C', '7C', '5D', 'JD', '7D', '4D', '2C', 'QS', '9C'], [('2H', '4H', '5S', '6D'), ('JC', '5H', 'QC', 'KH'), ('AS', 'QD', 'QH', '3H')])""", True),

         # can discard any card if no card of the suit lead is held
         ("""submission.is_valid_play('5C', ('JH',), ['6S', '5C', '7C', '5D', 'JD', '7D', '4D', '2C', 'QS', '9C'], [('2H', '4H', '5S', '6D'), ('JC', '5H', 'QC', 'KH'), ('AS', 'QD', 'QH', '3H')])""", True),

         # can lead with penalty card if hearts are broken
         ("""submission.is_valid_play('5H', (), ['8D', '6S', '8S', '5H', '0C', '7D', '3D', 'KC', '4C'], [('JH', 'JC', '6H', '7C'), ('0D', '4S', '9C', 'AH'), ('JD', '4D', 'QD', '5D'), ('AD', '5C', 'QH', '7H')])""", True),

         # can lead with a penalty card even if hearts isn't broken, if no non-penalty cards held in hand
         ("""submission.is_valid_play('2H', (), ['JH', '3H', '2H', '9H', '5H', '7H', '8H', '0H', 'QH', 'KH'], [('QC', 'QS', '0S', '4H'), ('4C', '4S', 'QD', '6H'), ('2C', 'AH', '6S', 'AC')])""", True),
        ],

    "score_game":
        [
        ("""submission.score_game([('AH', '2H', '9H', 'JH'), ('KS', '2S', 'AS', 'QS')], ['9S', '0H', '7D'])""",(0, 0, 0, 0)),
        ("""submission.score_game([('3S', '0S', '8S', 'JS'), ('9H', 'QH', '0D', '5H'), ('AD', '8D', '2D', '3D'), ('4S', 'QS', '9S', '2S')], ['5D', '2S', '7S'])""",(0, 0, 13, 0)),
        ("""submission.score_game([('2H', '7H', 'KH', '3H'), ('2C', '0C', '9C', 'KC'), ('6S', 'JS', '0S', '9S'), ('5D', '4D', '6D', 'QD'), ('4C', '7C', '3C', '8C'), ('7S', '4S', '8S', '5S'), ('9D', '2D', '8D', '5C')], ['8C', 'QS', 'QH'])""",(0, 0, 0, 0)),
        ("""submission.score_game([('8D', '4D', 'QD', '6D'), ('JS', '2S', '0S', 'QS'), ('9H', '6C', '3H', 'KH'), ('3S', 'KS', '6S', '4S'), ('AD', '5D', '0D', '7D'), ('2C', 'JC', '4C', 'QH'), ('5H', 'JH', '4H', '9S')], ['AH', '8S', 'QH'])""",(0, 0, 1, 3)),
        ("""submission.score_game([('6D', 'KD', 'AD', 'JD'), ('0H', '2H', 'KH', '4H'), ('2C', 'QC', 'KC', '8C'), ('4D', '0D', '5D', '3D'), ('JS', '9S', '6S', 'QS'), ('9C', '3C', '5C', '7C'), ('8S', '7S', 'AS', '5S'), ('9D', '8D', '7D', '7H'), ('2D', '9H', '2S', 'QD'), ('QH', 'AH', '8H', 'JH'), ('6C', '4C', '0C', '0S'), ('AC', '3H', '4S', 'JC'), ('3S', 'KS', '5H', '6H')], ['AC', '4D', 'JH'])""",(5, 0, 14, 3)),
        ("""submission.score_game([('KD', '9D', '0D', '5D'), ('QD', '3S', 'AD', 'JD'), ('4H', '6H', '7H', 'QS'), ('0S', 'KS', '5S', '8S'), ('AS', '4S', '6S', '9S'), ('KC', '8C', '5C', 'AC'), ('7C', '6C', '0C', 'JC'), ('4C', '4D', '3C', 'QC'), ('6D', '8D', '2C', '2H'), ('9C', '0H', 'KH', '7D'), ('3D', '7S', '9H', 'AH'), ('QH', '5H', 'JH', '3H'), ('2D', 'JS', '2S', '8H')], ['QH', '0S', 'JH'])""",(0, 0, 0, -10)),
        ],

    # v1.2: all tests updated to make the first argument a tuple rather than a list
    "play":
        [
         ("""submission.play(('8C',), ['KH', '7C', '2S', '6S', 'JS', '0D', '8H', '3S'], [('AC', '3C', '0C', '6C'), ('KD', '8D', '5D', '4D'), ('JH', '0H', '5H', '2H'), ('AS', 'KS', 'QS', '9S'), ('3D', '9D', 'JD', '7D')], ['JH', 'AS', '7S'], suppress_player_data=True)""", '7C'),
         ("""submission.play(('JH', '6H'), ['7S', '5C', '9S', '7C', '4C', '7D', '6S', '3H', '9D', '0S'], [('QS', 'KS', '8S', 'AS')], ['JD', 'AH'], suppress_player_data=True)""", '3H'),
         ("""submission.play((), ['KH', '3H', '6H', '2H', 'AH', '2S'], [('7H', 'QH', '4H', '0H'), ('6C', '5C', 'QC', 'JC'), ('7C', '3C', 'KC', '4S'), ('9D', 'AD', 'JD', '6D'), ('8S', '6S', 'QS', '9S'), ('9C', '0C', '2C', '4C'), ('0S', 'KS', 'AS', '5S')], ['8H', '2S', 'KS'], suppress_player_data=True)""", '2S'),
         ("""submission.play(('KC', '0C'), ['QD', 'JS', '7H', 'AS', 'AH', '4C', '8H', '3D', 'KD', 'QS'], [('9C', '5C', '7C', 'JC')], ['2S', 'JH'], suppress_player_data=True)""", '4C'),
         ],

        }
