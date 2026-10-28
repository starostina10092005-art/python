list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
total = len(list_players)
team = total // 2

team_1 = list_players[0:team]
team_2 = list_players[team:total]

print(team_1)
print(team_2)