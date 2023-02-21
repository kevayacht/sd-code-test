import pytest
import tests.conftest

from app.league.league import League
from app.match.match import MatchResult
from app.utils.get_input import read_file

@pytest.mark.parametrize(
    'filepath, output_fixture', 
    [
        ('tests/testfiles/input_1.txt', 'league_ranking_result_fixture'),
        ('tests/testfiles/input_2.txt', 'league_ranking_result_input_2_fixture'),
        ('tests/testfiles/input_3.txt', 'league_ranking_result_input_3_fixture'),
        ('tests/testfiles/input_4.txt', 'league_ranking_result_input_4_fixture'),
    ]
)
def test_end_to_end(filepath, output_fixture, request):
    expected_result = request.getfixturevalue(output_fixture)
    input_array = read_file(filepath)
    leaque = League()
    for item in input_array:
        leaque.add_results(MatchResult(item))
    leaque.export_result()
    assert (leaque.rankings == expected_result)