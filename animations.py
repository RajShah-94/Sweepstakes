import time
import os


class Animations:
    def __init__(self, results):
        self.results = results


    def draw(self):
        for player, teams in self.results.items():
            self._animate_drums()
            self._banner(player, teams)
            time.sleep(3)

    @staticmethod
    def _animate_drums(repeat=5, delay=0.2):
        # Frames of the drum animation
        drum_frames = [
            """
                    
                                o=========
                =========o     
                    _________________
                   |_________________|
                    |______/\______/|
                    |\____/__\____/_|
                    |_\__/____\__/__|
                    |__\/______\/___|
                   |_________________|
                       
            """,
            """
                    
                =========o     
                                o=========
                    _________________
                   |_________________|
                    |______/\______/|
                    |\____/__\____/_|
                    |_\__/____\__/__|
                    |__\/______\/___|
                   |_________________|
                       
            """
        ]

        for _ in range(repeat):
            for frame in drum_frames:
                os.system('clear')
                print(frame)
                time.sleep(delay)


    @staticmethod
    def _banner(player, teams):
        player = player + (' ' * (20 - len(player)))

        x = 0

        for team in teams:
            teams[x] = team + (' ' * (20 - len(team)))
            x += 1

        while x < 3:
            teams.append(' ' * 20)
            x += 1

        banner_image = f"""
        
                __________________________
               |  ______________________  |
               | |                      | |
               | | {player} | |
               | | -------------------- | |
               | | {teams[0]} | |
               | | {teams[1]} | |
               | | {teams[2]} | |
               | |______________________| |
               |__________________________|
            """
        os.system('clear')
        print(banner_image)
