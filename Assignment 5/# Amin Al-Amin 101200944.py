 # Amin Al-Amin 101200944
from comp1405_f23_special_library_loomwork_simplified import *

# Define how many threads are in the main pattern
pattern_repeats = 14

# Define the number of threads and beads within the main pattern
num_threads = 12
num_beads = 20

# Define the columns within the main pattern corresponding to a type of thread
blue_thread = [6, 8]
red_thread = [7, 9]
brown_thread = [1, 2, 3, 4, 5]
wine_thread = [10, 11, 12]

open_window(168, 20)

# Loop through the total number of times the pattern should repeat
for pattern in range(pattern_repeats):
    # Loop through each thread that occurs within the main pattern
    for thread in range(1, num_threads+1):
        # Loop through each bead within the thread
        for bead in range(1, num_beads+1):
            # If the thread corresponds to a "brown" thread
            if thread in brown_thread:
                if bead in [2, 10]:
                    add_bead("coral")
                else:
                    add_bead("leather")
            # If the thread corresponds to a "wine" thread
            elif thread in wine_thread:
                if bead == (thread-9)*3:
                    add_bead("sky")
                else:
                    add_bead("wine")
            # If the thread corresponds to a "blue" thread
            if thread in blue_thread:
                add_bead("denim")
            # If the thread corresponds to a "red" thread
            elif thread in red_thread:
                add_bead("ember")
        next_thread()

keep_window()