import numpy as np
import utils
from student_utils import *

def solve_input(file, params):
    input_data = utils.read_file(file)
    num_locs, num_houses, list_locations, list_houses, starting_loc, adj_matrix = data_parser(input_data)

    go_to = list_locations[0]
    while go_to == starting_loc:
        go_to = list_locations[np.random.choice(num_locs)]

    with open("outputs/{}.out".format(num_locs), "w+") as f:
        f.write(" ".join([starting_loc, go_to, starting_loc]) + "\n") # First line is path 
        f.write("1\n") # Second line is number of drop offs
        # One line per drop off: drop-off, then sequence of homes of TAs dropped off 
        print(len([go_to] + list_houses))
        f.write(" ".join([go_to] + list_houses) + "\n")
        f.close()

def solve_all_inputs(input_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_input(input_file, params=params)

if __name__ == "__main__":
    solve_all_inputs("inputs")