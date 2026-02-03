class footballteam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, jersey_number, age, nationality):
        player = {
            "name": name,
            "position": position,
            "jersey_number": jersey_number,
            "age": age,
            "nationality": nationality
        }
        self.players.append(player)

    def delete_player(self, jersey_number):
        self.players = [p for p in self.players if p["jersey_number"] != jersey_number]

    def update_player_info(self, jersey_number, key, value):
        for player in self.players:
            if player["jersey_number"] == jersey_number:
                player[key] = value
                break

    def show_club_info(self):
        print("team_name", self.team_name)
        print("coach", self.coach)
        print("players", self.players)

    def show_player_info(self, jersey_number):
        for player in self.players:
            if player["jersey_number"] == jersey_number:
                print(player)
                break

team = footballteam("lions", "smith")
team.add_player("john doe", "forward", 9, 24, "england")
team.add_player("mike brown", "midfielder", 10, 22, "spain")

team.show_club_info()
team.show_player_info(9)

team.update_player_info(9, "goal", 1)
team.show_player_info(9)

team.delete_player(10)
team.show_club_info()
