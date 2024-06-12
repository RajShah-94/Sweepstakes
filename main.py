from draws import random_assigned_draw, raj_cheats
from writer import write_results_to_yml
from animations import animate_drums, banner
import time

if __name__ == '__main__':
    results = random_assigned_draw()

    write_results_to_yml(results)

    for player, teams in results.items():
        animate_drums()
        banner(player, teams)
        time.sleep(3)
