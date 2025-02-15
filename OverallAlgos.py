from BasicRotations import *

def Align_Centers (Cube):
    if Cube.State['Down']['Center'] != Cube.Colours['Yellow']:
        for side in Cube.Sides:
            if Cube.State[side]['Center'] == Cube.Colours['Yellow']:
                current_side = side
        # print("Current side is",current_side)
        if current_side == 'Up':
            x(Cube,2)
        elif current_side == 'Front Left':
            x_(Cube)
        elif current_side == 'Back Right':
            x(Cube)
        elif current_side == 'Front Right':
            z(Cube)
        else:
            z_(Cube)
    if Cube.State['Front Right']['Center'] != Cube.Colours['Blue']:
        for side in Cube.Sides[2:]:
            # print(side)
            if Cube.State[side]['Center'] == Cube.Colours['Blue']:
                current_side = side
        # print("Current side is",current_side)
        if current_side == 'Front Left':
            y_(Cube)
        elif current_side == 'Back Right':
            y(Cube)
        elif current_side == 'Back Left':
            y(Cube,2)

def Middle_Layer_Right (Cube):
    for move in [U,R,U_,R_,U_,F_,U,F]:
        move(Cube)

def Middle_Layer_Left (Cube):
    for move in [U_,L_,U,L,U,F,U_,F_]:
        move(Cube)

def L_to_Cross (Cube):
    for move in [F,U,R,U_,R_,F_]:
        move(Cube)

def I_to_Cross (Cube):
    for move in [R,B,U,B_,U_,R_]:
        move(Cube)

def Align_Top_Edges (Cube):
    for move in [R,U,R_,U,R,U,U,R_,U]:
        move(Cube)

def Align_Top_Corners (Cube):
    for move in [U,R,U_,L_,U,R_,U_,L]:
        move(Cube)

def Orient_Correctly (Cube):
    for move in [R_,D_,R,D,R_,D_,R,D]:
        move(Cube) 
