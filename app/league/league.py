class League: 
    def __init__(self):
        self.table = {}
        self.rankings = []

    def _win(self, team):
        self.table[team] += 3
    
    def _draw(self, team):
        self.table[team] += 1

    def _is_draw(self, values):
        if values[0] == values[1]: 
            return True        

    def _get_winner(self, results):
        return max(results, key=lambda x:results[x])

    def _point_decisioning(self, results):
        keys, values = zip(*results.items())

        if self._is_draw(values):
            [self._draw(item) for item in keys]
        else:
            self._win(self._get_winner(results))

    def add_results(self, match):
        for entry in match.result:
            if not (entry in self.table):
                self.table[entry] = 0

        self._point_decisioning(match.result)

    def _build_ranking_string(self, rank, item, sorted_table):
        if sorted_table[item] == 1:
            return f'{rank}. {item}, {sorted_table[item]} pt'
        else:
            return f'{rank}. {item}, {sorted_table[item]} pts'

    def _determine_rankings(self):
        sorted_table = dict(sorted(self.table.items(), key=lambda x: (-x[1], x[0])))
        rank = 0
        previous_value = 0
        for item in sorted_table:
            if sorted_table[item] == previous_value:
                self.rankings.append(self._build_ranking_string(rank, item, sorted_table))
                previous_value = sorted_table[item]
            else:
                if len(self.rankings) != rank:
                    rank = len(self.rankings) + 1
                else: 
                    rank += 1
                self.rankings.append(self._build_ranking_string(rank, item, sorted_table))
            previous_value = sorted_table[item]

    def export_result(self):
        self._determine_rankings()
        for entry in self.rankings:
            print(f'{entry}')
            