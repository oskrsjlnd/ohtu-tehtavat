from player_reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()
        filtered = []

        for i in players:
            if i.get_nationality() == nationality:
                filtered.append(i)
                
        filtered.sort(key=lambda x: (x.get_points(), x.goals), reverse=True)
        return filtered