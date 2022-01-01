# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

# The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

import os

list_of_commands = []
horizontal_pos_values = []
depth_down_vals = []
depth_up_vals = []


def calculate_horizontal():

    flat_list = [item for sublist in horizontal_pos_values for item in sublist]
    return sum(flat_list)


def calculate_depth():
    flat_downs = [
        item_2 for sublist_2 in depth_down_vals for item_2 in sublist_2]
    flat_ups = [item_3 for sublist_3 in depth_up_vals for item_3 in sublist_3]

    return sum(flat_downs) - sum(flat_ups)


def main():
    for i in open("notes.txt", "r"):
        list_of_commands.append(i.strip())

    for elem in list_of_commands:
        if "forward" in elem:
            number_forwards = [int(s) for s in elem.split() if s.isdigit()]
            horizontal_pos_values.append(number_forwards)

        elif "down" in elem:
            # increases
            number_downs = [int(r) for r in elem.split() if r.isdigit()]
            depth_down_vals.append(number_downs)
        elif "up" in elem:
            # decreases
            number_ups = [int(t) for t in elem.split() if t.isdigit()]
            depth_up_vals.append(number_ups)

    dep = calculate_depth()
    hor = calculate_horizontal()
    print(dep * hor)


if __name__ == "__main__":
    main()
