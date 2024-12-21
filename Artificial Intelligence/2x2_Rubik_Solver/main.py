import numpy as np
import argparse
import time
from state import solved_state, next_state
from location import solved_location, next_location
from algo import solve


if __name__ == '__main__':

    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual', default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument('--testcase', type=str, default=None)
    parser.add_argument('--method', type=str, default='Random')
    parser.add_argument('--max_depth', type=str, nargs='?', help='maximum depth of searching three!')
    args = parser.parse_args()

    if not args.manual:

        # initializing state
        state = solved_state()
        location = solved_location()

        # scramble
        if args.testcase is None:
            scramble_sequence = np.random.randint(1, 12+1, np.random.randint(10, 30))
        else:
            f = open(args.testcase, 'r')
            scramble_sequence = list(map(int, f.readline().split()))
        
        # calculate the state and location
        for a in scramble_sequence:
            state = next_state(state, action=a)
            location = next_location(location, action=a)

        # solve rubik
        print('------------------ START ------------------')
        print('SOLVING...')
        start_time = time.time()
        solve_sequence = solve(state, location, method=args.method, max_depth = args.max_depth)
        print('actions:', solve_sequence)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'SOLVE FINISHED In {elapsed_time:.5f}s.')

        
    if not args.manual:
        print('--------- PRESS ENTER TO VISUALIZE --------')
        input()
    
    # imports
    from ursina import *
    from rubik import Rubik

    # start game
    app = Ursina(size=(1280, 720))
    rubik = Rubik()

    if args.manual:
        rubik.text = Text('Manual', scale=2, origin=rubik.text_position)
        input = lambda key: rubik.action(key, animation_time=0.5)
    else:
        action_dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                    7: 'q', 8: 'w', 9: 'e', 10: 'r', 11: 't', 12: 'y'}

        # perform scramble + solution
        scramble_sequence = [action_dict[i] for i in scramble_sequence]
        solve_sequence = [action_dict[i] for i in solve_sequence]
        invoke(rubik.action_sequence, scramble_sequence, solve_sequence, delay=3.0)
    
    app.run()
