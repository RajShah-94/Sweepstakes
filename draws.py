from typing import Dict, Any, List

from config import TeamsLoader, PlayersLoader
from writer import raj_cheats

import random


def random_assigned_draw() -> dict[Any, list[Any]]:
    teams_file = "config/teams.yml"
    players_file = "config/players.yml"

    teams = TeamsLoader(teams_file).list_teams()
    teams_config = TeamsLoader(teams_file).config
    players = PlayersLoader(players_file).list_players()
    players_config = PlayersLoader(players_file).config

    lots = []
    final_draw = {}

    for player in players:
        while players_config[player]['entries'] > 0:
            lots.append(player)
            players_config[player]['entries'] -= 1

    try:
        assert len(lots) <= len(teams)
    except Exception:
       raise Exception(f"More players than teams: {len(lots)} vs {len(teams)}")

    for lot in lots:
        if lot in final_draw:
            teams_removed = []
            for drawn_team in final_draw[lot]:
                group = teams_config[drawn_team]['Group']
                for team in teams_config:
                    if teams_config[team]['Group'] == group:
                        teams_removed.append(team)

            teams_allowed = [team for team in teams if team not in teams_removed]
        else:
            teams_allowed = teams

        try:
            assert len(teams_allowed) > 0
        except Exception:
            raise Exception(f"Unable to complete matchings")

        allocated_team = random.choice(teams_allowed)
        teams.remove(allocated_team)


        if not lot in final_draw:
            final_draw[lot] = [allocated_team]
        else:
            final_draw[lot].append(allocated_team)

    raj_cheats(final_draw)

    return final_draw