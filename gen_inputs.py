# Generates 50.in, 100.in, 200.in 
import numpy as np 
import string


# Random name can have up to 20 characters, only characters A-Z, a-z, 0-9 
# Source: https://pythontips.com/2013/07/28/generating-a-random-string/ 
def generate_random_name():
    arr_of_chars = list(string.ascii_letters + string.digits)
    random_name = "".join(np.random.choice(arr_of_chars, size=20, replace=True))
    return random_name

# Generate a list of random points that contains no duplicates 
def gen_locs(x_range, y_range, num):
    loc_set = set()
    while len(loc_set) < num:
        x = np.random.uniform(x_range)
        y = np.random.uniform(y_range)
        loc_set.add((x, y))
    return list(loc_set)

# Returns a list of lists. adj_matrix[0][1] is (string) positive weight from vertex 0 to vertex 1, x if no path exists. p_edge is probability edge exists
def gen_random_adj_matrix(points, p_edge):
    adj_matrix = np.zeros((len(points), len(points)), dtype=object)
    for i in range(len(points)):
        for j in range(i, len(points)):
            if i == j:
                # same point
                adj_matrix[i][j] = 'x'
            elif np.random.choice([0, 1], p=[1-p_edge, p_edge]) == 1:
                # edge should exist
                dist = np.linalg.norm(np.subtract(points[i], points[j])) + .0001 # np.subtract returns an array 
                matrix_val = str(round(dist, 5)) # Round to 5 decimal places 
                adj_matrix[i][j] = matrix_val 
                adj_matrix[j][i] = matrix_val
            else:
                adj_matrix[i][j] = 'x'
                adj_matrix[j][i] = 'x'
    return adj_matrix

# Make sure there's a path to every vertex !

def generate_input(num_TAs, num_locs):
    # Generate random names of locations 
    location_names = []
    for i in range(num_locs):
        location_names.append(generate_random_name())

    # Choose names of homes   
    home_names = np.random.choice(location_names, size=num_TAs, replace=False)

    # Choose starting location that isn't a home 
    # Source: https://stackoverflow.com/questions/25220975/find-the-non-intersecting-values-of-two-arrays
    no_homes = list(set(location_names).symmetric_difference(home_names))
    starting_loc = np.random.choice(no_homes)

    # Generate graph 
    V = gen_locs(1000, 1000, num_locs)

    # Convert graph to adjacency matrix 
    adj_matrix = gen_random_adj_matrix(V, 1)

    # Write to file 
    file_name = "{}.in".format(num_locs)
    print("File name is: ", file_name)

    with open("inputs/{}".format(file_name), "w+") as f:
        f.write(str(num_locs) + "\n") # First line is |L|
        f.write(str(num_TAs) + "\n") # Second line is |H|
        f.write(" ".join(location_names) + "\n") # Third line is location names separated by spaces 
        f.write(" ".join(home_names) + "\n") # Fourth line is home names separated by spaces (I don't think order matters here)
        f.write(str(starting_loc) + "\n") # Fifth line is starting location
        for i in range(num_locs):
            f.write(" ".join(adj_matrix[i]) + "\n") # Last |L| lines is adjacency matrix
        f.close()




if __name__ == "__main__":
    generate_input(25, 50)
    generate_input(50, 100)
    generate_input(100, 200) 