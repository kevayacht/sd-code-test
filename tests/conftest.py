import pytest

@pytest.fixture
def league_missing_argument_exception():
    return "League.__init__() takes 1 positional argument but 2 were given"

@pytest.fixture
def match_bad_input_score_exception():
    return "Input error, looks like a team's score is missing."

@pytest.fixture
def match_bad_input_name_exception():
    return "Input error, looks like a team's name is missing."

@pytest.fixture
def match_positional_argument_exception():
    return "MatchResult.__init__() missing 1 required positional argument: 'item'"

@pytest.fixture
def input_array_item_fixture():
    return 'Lions 3, Snakes 3'

@pytest.fixture
def input_array_fixture():
    return [
        'Lions 3, Snakes 3', 
        'Tarantulas 1, FC Awesome 0', 
        'Lions 1, FC Awesome 1', 
        'Tarantulas 3, Snakes 1', 
        'Lions 4, Grouches 0'
        ]

@pytest.fixture
def match_result_fixture():
    return [
            {'Lions': 3, 'Snakes': 3},
            {'Tarantulas': 1, 'FC Awesome': 0},
            {'Lions': 1, 'FC Awesome': 1},
            {'Tarantulas': 3, 'Snakes': 1},
            {'Lions': 4, 'Grouches': 0}
        ]

@pytest.fixture
def league_result_fixture():
    return [
            {'Lions': 1, 'Snakes': 1},
            {'Lions': 1, 'Snakes': 1, 'Tarantulas': 3, 'FC Awesome': 0},
            {'Lions': 2, 'Snakes': 1, 'Tarantulas': 3, 'FC Awesome': 1},
            {'Lions': 2, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1},
            {'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0},
        ]

@pytest.fixture
def league_ranking_result_fixture():
    return [
        '1. Tarantulas, 6 pts',
        '2. Lions, 5 pts',
        '3. FC Awesome, 1 pt',
        '3. Snakes, 1 pt',
        '5. Grouches, 0 pts'
        ]

@pytest.fixture
def league_ranking_result_input_2_fixture():
    return [
        '1. Boring Team, 6 pts',
        '2. Made up Team, 5 pts',
        '3. Not Awesome Team, 1 pt',
        '3. Snitches ZZZ, 1 pt',
        '5. My Couche, 0 pts'
        ]

@pytest.fixture
def league_ranking_result_input_3_fixture():
    return [
        '1. Tarantulas, 8 pts',
        '2. Lions, 5 pts',
        '3. Grouches, 4 pts',
        '4. Snakes, 2 pts',
        '5. FC Awesome, 1 pt'
        ]

@pytest.fixture
def league_ranking_result_input_4_fixture():
    return [
        '1. Witches, 15 pts',
        '2. Wizzards, 11 pts',
        '3. Knights, 10 pts',
        '4. Twisters, 9 pts',
        '5. Trolls, 8 pts',
        '6. Coldplay, 4 pts',
        '7. Zombies, 3 pts',
        '8. Invisible Monkeys, 1 pt',
        '9. Potatoes, 0 pts'
        ]