teamPoints = [0, 0, 0, 0, 0]
allGames = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
favouriteTeam = int(input())
gamesPlayed = int(input())
def possibilities(gamesLeft, teams, points, results):
    if results == 1:
        teams[points[0]] += 3
    elif results == 0:
        teams[points[0]] += 1
        teams[points[1]] += 1
    elif results == -1:
        teams[points[1]] += 1
    if not gamesLeft:
        for i in range(1,5):
            if i != favouriteTeam:
                if teams[i] >= teams[favouriteTeam]:
                    return 0
        return 1
    nextGame = gamesLeft.pop()
    return sum([possibilities(list(gamesLeft), list(teams), nextGame, i) for i in range(-1, 2)])
for _ in range(gamesPlayed):
    a, b, c, d = map(int, input().split())
    if (a, b) in allGames:
        allGames.remove((a, b))
    if c > d:
        teamPoints[a] += 3
    if c < d:
        teamPoints[b] += 3
    if c == d:
        teamPoints[a] += 1
        teamPoints[b] += 1
print(possibilities(allGames, teamPoints, [], 2))