""" Leaderboard module """
from modules.google_sheets import get_highscores_worksheet


def show_leaderboard():
    """ leaderboard functionality """
    highscores = get_highscores_worksheet()
    rows = highscores.get_all_values()[1:]  # Skip the header row

    # Sort by score
    sorted_rows = sorted(rows, key=lambda row: int(row[2]), reverse=True)

    print("Leaderboard:")
    print(f"{'Rank':<5} {'Name':<20} {'City':<20} {'Score':<10}")
    print("-" * 55)

    for i, row in enumerate(sorted_rows[:15]):
        name, city, score = row
        print(f"{i + 1:<5} {name:<20} {city:<20} {score:<10}")
