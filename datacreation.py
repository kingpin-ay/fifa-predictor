import pandas as pd
import os

file_path = "A:\\fifapredicter\\datasets\\team\\"  #Enter folder location
# df = pd.read_csv(".\\datasets\\allrecords.csv")
# df = pd.read_csv(".\\datasets\\realData.csv")
# df = pd.read_csv(".\\datasets\\Data.csv")
# print(df)

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# data = pd.DataFrame(df)

# colomn_attr = ['date','home_team','away_team','home_team_continent','away_team_continent','tournament','home_team_result']

# data = pd.DataFrame(data, columns=colomn_attr)

# data.to_csv('.\\datasets\\realData.csv', encoding='utf-8' , index=False)

# data = pd.DataFrame(df)
# newdata = data.query("tournament in ('FIFA World Cup','FIFA World Cup qualification')")
# newdata.to_csv('.\\datasets\\Data.csv', encoding='utf-8' , index=False)
# print(newdata)

# data = pd.DataFrame(df)
# newdata = data.query("tournament == 'FIFA World Cup'")

# newdata.to_csv('.\\datasets\\fifaWorldCupData.csv',
#                encoding='utf-8',
#                index=False)

# data = pd.DataFrame(df)
# newdata = data.query("tournament == 'FIFA World Cup qualification'")

# newdata.to_csv('.\\datasets\\fifaWorldCupQualificationData.csv',
#                encoding='utf-8',
#                index=False)


def point_evaluation(name, status):
    if status == "win":
        if "Group" in name:
            return 3
        elif "Semi-finals" in name:
            return 8
        elif "Final" in name:
            return 10
        elif "Quarter-finals" in name:
            return 6
        elif "Round of 16" in name:
            return 4
        else:
            return 0
    elif status == "draw":
        if "Group" in name:
            return 2
        else:
            return 0
    else:
        if "Group" in name:
            return 1
        elif "Semi-finals" in name:
            return 6
        elif "Final" in name:
            return 8
        elif "Quarter-finals" in name:
            return 4
        elif "Round of 16" in name:
            return 2
        else:
            return 0


# script for the individual team concept

fifaWorldCup = pd.read_csv(".\\datasets\\fifaWorldCupData.csv")
fifaWorldCupQualification = pd.read_csv(
    ".\\datasets\\fifaWorldCupQualificationData.csv")
WorldCupMatches = pd.read_csv(".\\datasets\\WorldCupMatches.csv")
WorldCupMatches_colomn = [
    'Stage', 'Home Team Name', 'Away Team Name', 'winner'
]

r16_teams = open('.\\datasets\\r16.txt', 'r')
lines = r16_teams.readlines()

# new_list = []
# idx = 0

# looping through each line in the file
for line in lines:
    # print(line)
    points = 0
    tot_match = 0
    win_match = 0
    win_rate = 0

    # path creation
    line = line.replace("\n", "")
    newpath = file_path + line
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    #data from worldCupMatches.csv
    data = pd.DataFrame(WorldCupMatches, columns=WorldCupMatches_colomn)
    data = data[(data['Home Team Name'] == f'{line}') |
                (data['Away Team Name'] == f'{line}')]
    # data = data.query(
    #     f"'Home Team Name' == '{line}' | 'Away Team Name' == '{line}'")
    data.to_csv(f'.\\datasets\\team\\{line}\\worldCupMatchesData.csv',
                encoding='utf-8')
    for i in data.index:
        tot_match = tot_match + 1
        if data["winner"][i] == line:
            win_match = win_match + 1
            name = data["Stage"][i]
            points = points + point_evaluation(name, "win")
        elif data["winner"][i] == "Draw":
            name = data["Stage"][i]
            points = points + point_evaluation(name, "draw")
        else:
            name = data["Stage"][i]
            points = points + point_evaluation(name, "lose")

    # print(tot_match, " total matches ", line)
    # print(win_match, " win matches ", line)
    #data from fifaWorldCup
    data = pd.DataFrame(fifaWorldCup)
    data = data[(data['home_team'] == f'{line}') |
                (data['away_team'] == f'{line}')]
    data.to_csv(f'.\\datasets\\team\\{line}\\fifaWorldCupData.csv',
                encoding='utf-8')

    #data from fifaWorldCupQualifiers
    data = pd.DataFrame(fifaWorldCupQualification)
    data = data[(data['home_team'] == f'{line}') |
                (data['away_team'] == f'{line}')]
    data.to_csv(f'.\\datasets\\team\\{line}\\fifaWorldCupQualifiersData.csv',
                encoding='utf-8')
    if tot_match != 0:
        win_rate = round((win_match / tot_match) * 100)
    else:
        win_rate = 0

    data = {"win_rate_world_cup": [win_rate], "total_points": [points]}
    data = pd.DataFrame(data)
    data.to_csv(f".\\datasets\\team\\{line}\\data.csv", encoding='utf-8')
    # print(line, " ", win_rate)
r16_teams.close()

# File_object.readline([n])
# newpath = f"A:\\fifapredicter\\datasets\\{}"
# if not os.path.exists(newpath):
#     os.makedirs(newpath)
# df = pd.read_csv(".\\datasets\\Data.csv")

# point Calculation
