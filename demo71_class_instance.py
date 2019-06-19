class Team:
    name = 'Normal Team'


team1 = Team()
print team1.name
team1.name = 'R&D Team'
team2 = Team()
print team1.name, team2.name, Team.name
del team1.name
print team1.name, team2.name, Team.name
team1.member = 9
print team1.name, team1.member