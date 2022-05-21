class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def players(self):
        return self.__players

    @name.setter
    def name(self, name):
        self.__name = name

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @players.setter
    def players(self, players):
        self.__players = players

    def add_player(self, player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.name}"
        else:
            return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        try:
            filtered_player = [p for p in self.__players if p.name == player_name][0]
            self.players.remove(filtered_player)
            return filtered_player
        except IndexError:
            return f"Player {player_name} not found"
