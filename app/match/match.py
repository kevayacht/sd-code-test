import re

class MatchResult():
    def __init__(self, item):
        self.result = {}
        self.handle_result(item)
    
    def handle_result(self, item):
        for entry in item.split(','):
            self.result[self.determine_name(entry)] = self.determine_score(entry)
        
    def determine_name(self, entry):
        detected = str(re.search("\D+", entry).group().strip())
        if len(detected) == 0:
            raise Exception("Input error, looks like a team's name is missing.")
        return detected

    def determine_score(self, entry):
        detected = re.search("\d", entry)
        if detected is None:
            raise Exception("Input error, looks like a team's score is missing.")
        return int(detected.group())
