from league.league import League
from match.match import MatchResult
from utils.get_input import get_input

def main():
    input_array = get_input()
    leaque = League()
    for item in input_array:
        leaque.add_results(MatchResult(item))
    leaque.export_result()

if __name__ == '__main__':
    main()