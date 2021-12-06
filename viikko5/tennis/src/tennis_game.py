class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1
    
    def players_tied(self, score):
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        elif self.player1_score == 3:                
            score = "Forty-All"
        else:
            score = "Deuce"
        return score
    
    def overtime(self, score):
        score_dif = self.get_score_difference()
        
        if score_dif == 1:
            score = "Advantage player1"
        elif score_dif == -1:
            score = "Advantage player2"
        elif score_dif >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def non_overtime(self, score):
        for i in range(1,3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score += "-"
                temp_score = self.player2_score
            
            if temp_score == 0:
                score += "Love"
            elif temp_score == 1:
                score += "Fifteen"
            elif temp_score == 2:
                score += "Thirty"
            else:
                score += "Forty"
        return score

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.players_tied(score)
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.overtime(score)
        else:
            score = self.non_overtime(score)
        return score
    
    def get_score_difference(self):
        return self.player1_score - self.player2_score
    