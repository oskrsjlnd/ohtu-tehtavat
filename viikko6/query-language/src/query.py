from matchers import *

class QueryBuilder:
    def __init__(self, query=All()):
        self.queries = query
    
    def hasAtLeast(self, value, stats):
        return QueryBuilder(And(self._query, HasAtLeast(value, stats)))
    
    def hasFewerThan(self, value, stats):
        return QueryBuilder(And(self._query, HasFewerThan(value, stats)))
    
    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))
    
    def notIn(self, *matchers):
        return QueryBuilder(Not(*matchers))
    
    def build(self):
        return self.queries
    
    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))
