test_cases = {
    "is_broken_hearts":
        [
        # QS doesn't break hearts
         ("""submission.is_broken_hearts([('AD', 'JD', '3D', '6D'), ('0S', '2S', 'JS', '5S'), ('5H', '9H', '2H', 'QH'), ('3C', 'QC', '0C', 'KC'), ('4D', '9D', '8D', '7D'), ('2D', '8C', 'KD', '0D'), ('3S', '8S', '4S', '7S'), ('9S', '6S', 'AS', 'QS')])""", False),  
        ],
    "is_valid_play":
        [
        ],

    "score_game":
        [
        # example of shooting the moon before the last trick
        ("""submission.score_game([('KD', '9D', '0D', '5D'), ('QD', '3S', 'AD', 'JD'), ('4H', '6H', '7H', 'QS'), ('7C', '6C', '0C', 'JC'), ('4C', '4D', '3C', 'QC'), ('6D', '8D', '2C', '2H'), ('9C', '0H', 'KH', '7D'), ('3D', '7S', '9H', 'AH'), ('QH', '5H', 'JH', '3H'), ('2D', 'JS', '2S', '8H')], ['QH', '0S', 'JH'])""",(0, 0, 0, -10)),
        ],

    "play":
        [
         ("""submission.play(['8C'], ['KH', '7C', '2S', '6S', 'JS', '0D', '8H', '3S'], [('AC', '3C', '0C', '6C'), ('KD', '8D', '5D', '4D'), ('JH', '0H', '5H', '2H'), ('AS', 'KS', 'QS', '9S'), ('3D', '9D', 'JD', '7D')], ['JH', 'AS', '7S'], suppress_player_data=True)""", '7C'),
         ],

        }
