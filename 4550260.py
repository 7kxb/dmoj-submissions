ant = int(input())
eye = int(input())

if ant >= 3 and eye <= 4:
    print('TroyMartian')
elif ant <= 6 and eye >= 2:
    print('VladSaturnian')
elif ant <= 2 and eye <= 3:
    print('GraemeMercurian')