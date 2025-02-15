from Cube_Scrambler import Scramble
from OverallAlgos import *
from initial_cube_making import Color_Cube
from Movement_Functions import *
from First_Layer import Solve_First_Layer
from Middle_Layer import Solve_Second_Layer
from Last_Layer import Solve_Top_Layer
from time import sleep

def Solving_the_cube (Cube):
    down_section = Cube.State['Down']
    Down = []

    # Printing the Center value
    Down.append(down_section['Center'])

    # Printing all the Edge values
    # print("Edges:")
    for edge, color in down_section['Edges'].items():
        Down.append(color)

    # Printing all the Vertex values
    # print("Vertices:")
    for vertex, color in down_section['Vertices'].items():
        Down.append(color)

    for color in Down:
        if color != Cube.Colours['Yellow']:
            return True
        else:
            pass
    return False


Cube = Color_Cube()

sleep(10)
Scramble(Cube)

sleep(2)
# # Solving centers
Align_Centers(Cube)

Solve_First_Layer(Cube)

while(Solving_the_cube(Cube)):
    Solve_First_Layer(Cube)

Solve_Second_Layer(Cube)
Solve_Top_Layer(Cube)

sleep(60)
