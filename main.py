import random
import pprint

names = ["Raj", "Jay", "Jash", "Mausmi", "Akash", "Jinali", "Dipal", "Ron", "Nakul", "Disha", "Viral", "Neeti", "Khush", "Dhaval", "Mudra", "Juhi"]
seed_high_a = ["France", "Argentina", "England", "Mexico", "Netherlands", "Denmark", "United States", "Wales"]
seed_high_b = ["Brazil", "Belgium", "Spain", "Portugal", "Germany", "Uruguay", "Switzerland", "Croatia"]
seed_low_a = ["Senegal", "Iran", "Poland", "Tunisia", "Australia", "Ecuador", "Saudi Arabia", "Qatar"]
seed_low_b = ["Japan", "Morocco", "Serbia", "South Korea", "Costa Rica", "Cameroon", "Canada", "Ghana"]

sweepstakes = {}

for i in range(1):
    seed_high = seed_high_a + seed_high_b

    random.shuffle(names)
    random.shuffle(seed_high)
    random.shuffle(seed_low_a)
    random.shuffle(seed_low_b)

    a = 0
    b = 0

    for index, (name, team_high) in enumerate(zip(names, seed_high)):
        sweepstakes[name] = team_high

    for name, team_high in sweepstakes.items():
        if team_high in seed_high_a:
            team_low = seed_low_b[b]
            sweepstakes[name] = (team_high, team_low)
            b += 1
        else:
            team_low = seed_low_a[a]
            sweepstakes[name] = (team_high, team_low)
            a += 1

    pprint.pprint(sweepstakes)
    sweepstakes = {}
