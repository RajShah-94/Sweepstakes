import yaml


class ConfigLoader:
    def __init__(self, file):
        self.file = file
        self.yml = self._load_yml()

    def _load_yml(self):
        with open(f'config/{self.file}', 'r') as yml_file:
            return yaml.safe_load(yml_file)


class TeamsLoader(ConfigLoader):
    def __init__(self, file):
        super().__init__(file)
        self.config = self._config()

    def _config(self):
        teams_config = {}
        for config in self.yml:
            teams_config[config['Team']] = config
        return teams_config

    def list_teams(self):
        return [team['Team'] for team in self.yml]

    def list_ranks(self):
        return [rank['Rank'] for rank in self.yml]


class PlayersLoader(ConfigLoader):
    def __init__(self, file):
        super().__init__(file)
        self.config = self.yml

    def list_players(self):
        return [player for player in self.yml]
