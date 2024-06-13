import sys

from config import DrawLoader
from draws import random_assigned_draw
from writer import write_results_to_yml
from animations import Animations

def argParse() -> str:
    if len(sys.argv) > 1:
        run_type = sys.argv[1]
    else:
        raise Exception("""Invalid arguments!
Allowed arguments:
-l or --lots to draw lots
-r or --results to replay animation for sweepstakes draw
                        """)

    if run_type not in ['-l', '--lots', '-r', '--results']:
        raise Exception("""Invalid arguments!
Allowed arguments:
-l or --lots to draw lots
-r or --results to replay animation for sweepstakes draw
                        """)

    return run_type


def run(run_type: str) -> dict:
    if run_type in ['-l', '--lots']:
        results = random_assigned_draw()
        write_results_to_yml(results)
    elif run_type in ['-r', '--results']:
        results = DrawLoader("results.yml").config
    else:
        raise Exception("""Invalid arguments!
Allowed arguments:
-l or --lots to draw lots
-r or --results to replay animation for sweepstakes draw
                        """)
    return results

if __name__ == '__main__':

    arg = argParse()

    draw = run(arg)

    Animations(draw).draw()