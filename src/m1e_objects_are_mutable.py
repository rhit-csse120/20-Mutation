"""
This module demonstrates   MUTATION   of an OBJECT in two ways:
  -- From an assignment in main.
  -- From within a function call.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, and their colleagues.
"""
# -----------------------------------------------------------------------------
# Students: You might like to run this program in the debugger as you read it,
# stepping from line to line to watch assignment and mutation in action.
#
# This is a contrived example whose purpose is only to show
# the concepts behind assignment and mutation, using simple code.
# It is the same as the previous example but mutating OBJECTS instead of LISTS.
# -----------------------------------------------------------------------------

import rosegraphics as rg


def main():
    # -------------------------------------------------------------------------
    # 1. Constructs an rg.Point, assigning its instance variables values.
    # 2. Assigns an instance variable in the object a new value,
    #      thus MUTATING the OBJECT (because one of
    #      its INSTANCE VARIABLES was ASSIGNED a new value).
    # -------------------------------------------------------------------------
    point = rg.Point(45, 100)
    point.y = 33
    print(point)  # To see that the INSIDES of   point   has changed

    # -------------------------------------------------------------------------
    # 3. Mutates the object again, this time from within a function call
    # -------------------------------------------------------------------------

    mutate_point(point)
    print(point)  # To see that the INSIDES of   point   has changed

    # -------------------------------------------------------------------------
    # 4. Assigns another variable to refer to the same rg.Point
    #       to which the    point   variable refers.
    # 5. Re-assigns the   point   variable to refer to another rg.Point.
    # This is ASSIGNMENT and NOT mutation.
    # -------------------------------------------------------------------------
    point2 = point
    point = rg.Point(10, 6)

    print(point, point2)  # Prints the two DIFFERENT rg.Points

    # -------------------------------------------------------------------------
    # Shows the difference between the   is   operator
    #    (two things refer to the same place in memory)
    # and the   ==   operator (two things contain the same data).
    # -------------------------------------------------------------------------
    point3 = rg.Point(100, 20)
    point4 = rg.Point(100, 20)
    point5 = point3

    print(point3 is point4)  # False
    print(point3 == point4)  # True

    point3.fill_color = 'blue'
    print(point3 == point4)  # False

    print(point3 is point5)  # True
    print(point3 == point5)  # True


def mutate_point(point):
    point.y = 77


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
