import pandas as pd

r16_teams = open('.\\datasets\\r16.txt', 'r')
lines = r16_teams.readlines()

quater = []
semi = []
final = []


def team_finder(status):

    end_line = 0

    if status == "r16":
        end_line = 16

    elif status == "quater":
        end_line = 8

    elif status == "semi":
        end_line = 4

    else:
        end_line = 1

    for i in range(0, end_line, 2):
        if status == "r16":
            team_a = lines[i].replace("\n", "")
            team_b = lines[i + 1].replace("\n", "")
        elif status == "quater":
            team_a = quater[i].replace("\n", "")
            team_b = quater[i + 1].replace("\n", "")

        elif status == "semi":
            team_a = semi[i].replace("\n", "")
            team_b = semi[i + 1].replace("\n", "")

        else:
            team_a = final[i].replace("\n", "")
            team_b = final[i + 1].replace("\n", "")
        team_a_data = pd.read_csv(f".\\datasets\\team\\{team_a}\\data.csv")
        team_b_data = pd.read_csv(f".\\datasets\\team\\{team_b}\\data.csv")
        team_a_win_chance = 0
        team_b_win_chance = 0
        team_a_win_rate = team_a_data._get_value(0, 'win_rate_world_cup')
        team_a_points = team_a_data._get_value(0, 'total_points')
        team_b_win_rate = team_b_data._get_value(0, 'win_rate_world_cup')
        team_b_points = team_b_data._get_value(0, 'total_points')

        if team_a_win_rate > team_b_win_rate:
            team_a_win_chance = team_a_win_chance + 3
        else:
            team_b_win_chance = team_b_win_chance + 3
        if team_a_points > team_b_points:
            team_a_win_chance = team_a_win_chance + 5
        else:
            team_b_win_chance = team_b_win_chance + 5

        if team_a_win_chance > team_b_win_chance:
            if status == "r16":
                print(team_a, " wins in ", team_a, " vs ", team_b)
                quater.append(team_a + "\n")
            elif status == "quater":
                print(team_a, " wins in ", team_a, " vs ", team_b)
                semi.append(team_a + "\n")
            elif status == "semi":
                print(team_a, " wins in ", team_a, " vs ", team_b)
                final.append(team_a + "\n")
            elif status == "final":
                print(team_a, " wins in ", team_a, " vs ", team_b,
                      " and wins the final ")

        else:
            if status == "r16":
                print(team_b, " wins in ", team_b, " vs ", team_a)
                quater.append(team_b + "\n")
            elif status == "quater":
                print(team_b, " wins in ", team_b, " vs ", team_a)
                semi.append(team_b + "\n")
            elif status == "semi":
                print(team_b, " wins in ", team_b, " vs ", team_a)
                final.append(team_b + "\n")
            elif status == "final":
                print(team_b, " wins in ", team_b, " vs ", team_a,
                      " and wins the final ")


print("round of 16")
team_finder("r16")
print("\n\n")
print("quater finals")
team_finder("quater")
print("\n\n")
print("semi Finals")
team_finder("semi")
print("\n\n")
print("Finals")
team_finder("final")

# for i in range(0, 16, 2):
#     team_a = lines[i].replace("\n", "")
#     team_b = lines[i + 1].replace("\n", "")
#     team_a_data = pd.read_csv(f".\\datasets\\{team_a}\\data.csv")
#     team_b_data = pd.read_csv(f".\\datasets\\{team_b}\\data.csv")
#     team_a_win_chance = 0
#     team_b_win_chance = 0
#     team_a_win_rate = team_a_data._get_value(0, 'win_rate_world_cup')
#     team_a_points = team_a_data._get_value(0, 'total_points')
#     team_b_win_rate = team_b_data._get_value(0, 'win_rate_world_cup')
#     team_b_points = team_b_data._get_value(0, 'total_points')

#     if team_a_win_rate > team_b_win_rate:
#         team_a_win_chance = team_a_win_chance + 3
#     else:
#         team_b_win_chance = team_b_win_chance + 3
#     if team_a_points > team_b_points:
#         team_a_win_chance = team_a_win_chance + 5
#     else:
#         team_b_win_chance = team_b_win_chance + 5

#     if team_a_win_chance > team_b_win_chance:
#         print(team_a, " wins in ", team_a, " vs ", team_b)
