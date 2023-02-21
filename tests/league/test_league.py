import pytest
import tests.conftest

from app.league.league import League
from app.match.match import MatchResult

def test_league_class_create_failing(league_missing_argument_exception):
    with pytest.raises(Exception) as exception:
        league = League("grabage")
    assert exception.value.args[0] == league_missing_argument_exception

def test_league_class_init():
    league = League()
    assert(isinstance(league, League))
    assert(isinstance(league.table, dict))
    assert(isinstance(league.rankings, list))

def test_league_add_result_from_match_results_class_single():
    league = League()
    league.add_results(MatchResult('Lions 3, Snakes 3'))
    assert(isinstance(league, League))
    assert(isinstance(league.table, dict))
    assert(league.table == {'Lions': 1, 'Snakes': 1})

def test_league_ranking_from_match_results_class_single():
    league = League()
    league.add_results(MatchResult('Lions 3, Snakes 3'))
    league._determine_rankings()
    assert(isinstance(league, League))
    assert(isinstance(league.table, dict))
    assert(league.rankings == ['1. Lions, 1 pt', '1. Snakes, 1 pt'])

def test_league_add_result_from_match_results_class_multiple(input_array_fixture, league_result_fixture):
    league = League()
    for index, item in enumerate(input_array_fixture, start=0):
        league.add_results(MatchResult(item))
        assert(isinstance(league, League))
        assert(isinstance(league.table, dict))
        assert(isinstance(league.rankings, list))
        assert(league.table == league_result_fixture[index])

def test_league_ranking_from_match_results_class_multiple(input_array_fixture, league_ranking_result_fixture):
    league = League()
    for item in input_array_fixture:
        league.add_results(MatchResult(item))
        assert(isinstance(league, League))
        assert(isinstance(league.table, dict))
    league._determine_rankings()
    assert(isinstance(league.rankings, list))
    assert(league.rankings == league_ranking_result_fixture)


def test_league_get_winner():
    league = League()
    assert(league._get_winner({'Lions': 4, 'Snakes': 3}) == 'Lions')

def test_league_is_draw():
    league = League()
    assert(league._is_draw((3, 3)) == True)

@pytest.mark.parametrize(
    'team_one, team_two, winner, output',
    [
        ('Team one', 'Team two', 'Team one', {'Team one': 3, 'Team two': 0}),
        ('Team one', 'Team two', 'Team two', {'Team one': 0, 'Team two': 3})
    ]
)
def test_league_win_points_add(team_one, team_two, winner, output):
    league = League()
    league.table[team_one] = 0
    league.table[team_two] = 0
    league._win(winner)
    assert(league.table == output)

@pytest.mark.parametrize(
    'team_one, team_two, output',
    [
        ('Team one', 'Team two', {'Team one': 1, 'Team two': 1}),
        ('Team one one', 'Team two two', {'Team one one': 1, 'Team two two': 1})
    ]
)
def test_league_draw_points_add(team_one, team_two, output):
    league = League()
    league.table[team_one] = 0
    league.table[team_two] = 0
    league._draw(team_one)
    league._draw(team_two)
    assert(league.table == output)

@pytest.mark.parametrize(
    'rank, team, sorted_table, result', 
    [
        (1, 'Team one', {'Team one': 10 }, '1. Team one, 10 pts'),
        (2, 'Team two', {'Team two': 5 }, '2. Team two, 5 pts'),
        (3, 'Team three', {'Team three': 3 }, '3. Team three, 3 pts'),
        (3, 'Team four', {'Team four': 3 }, '3. Team four, 3 pts'),
        (5, 'Team five', {'Team five': 1 }, '5. Team five, 1 pt'),
        (6, 'Team six', {'Team six': 0 }, '6. Team six, 0 pts')
    ]
)
def test_build_ranking_string(rank, team, sorted_table, result):
    league = League()
    assert(league._build_ranking_string(rank, team, sorted_table) == result)

def test_point_decisioning(match_result_fixture, league_result_fixture):
    league = League()
    for index, item in enumerate(match_result_fixture, start=0):
        for entry in item:
            if not (entry in league.table):
                league.table[entry] = 0
        league._point_decisioning(item)
        assert(league.table == league_result_fixture[index])


def test_league_full_flow_export_result_and_print(capfd, input_array_fixture):
    league = League()
    league.table['Lions'] = 0
    for item in input_array_fixture:
        league.add_results(MatchResult(item))
    league.export_result()

    out, err = capfd.readouterr()
    assert out == '1. Tarantulas, 6 pts\n2. Lions, 5 pts\n3. FC Awesome, 1 pt\n3. Snakes, 1 pt\n5. Grouches, 0 pts\n'
    