import pytest
import tests.conftest

from app.match.match import MatchResult

def test_match_class_fails_missing_input(match_positional_argument_exception):
    with pytest.raises(Exception) as exception:
        match = MatchResult()
    assert exception.value.args[0] == match_positional_argument_exception

def test_match_bad_input_score(match_bad_input_score_exception):
    with pytest.raises(Exception) as exception:
        match = MatchResult('Lions 3, Snakes ')
    assert exception.value.args[0] == match_bad_input_score_exception

def test_match_bad_input_name(match_bad_input_name_exception):
    with pytest.raises(Exception) as exception:
        match = MatchResult(' 3, Snakes 3')
    assert exception.value.args[0] == match_bad_input_name_exception

def test_match_result_class_init(input_array_item_fixture):
    match = MatchResult(input_array_item_fixture)
    assert(isinstance(match, MatchResult))
    assert(isinstance(match.result, dict))

@pytest.mark.parametrize(
    "entry, output", 
    [
        ('Snakes 1', 'Snakes'), 
        ('Lions 2', 'Lions'), 
        ('Tarantulas 3', 'Tarantulas'), 
        ('Grouches 4', 'Grouches'), 
        ('FC Awesome 5', 'FC Awesome')
    ]
)
def test_match_determine_name(input_array_item_fixture, entry, output):
    match = MatchResult(input_array_item_fixture)
    assert match.determine_name(entry) == output

@pytest.mark.parametrize(
    "entry, output", 
    [
        ('Snakes 1', 1), 
        ('Lions 2', 2), 
        ('Tarantulas 3', 3), 
        ('Grouches 4', 4), 
        ('FC Awesome 5', 5)
    ]
)
def test_match_determine_score(input_array_item_fixture, entry, output):
    match = MatchResult(input_array_item_fixture)
    assert match.determine_score(entry) == output

def test_match_results(input_array_fixture, match_result_fixture):
    for index, item in enumerate(input_array_fixture, start=0):
        match = MatchResult(item)
        assert(isinstance(match, MatchResult))
        assert(isinstance(match.result, dict))
        assert(match.result == match_result_fixture[index])