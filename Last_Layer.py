from BasicRotations import *
from OverallAlgos import *

def White_Cross (Cube):
    if Cube.State['Up']['Edges']['Front Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Front Right Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Right Up'] == Cube.Colours['White']:
        pass
    elif Cube.State['Up']['Edges']['Back Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Right Up'] == Cube.Colours['White']:
        L_to_Cross(Cube)
    elif Cube.State['Up']['Edges']['Back Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Front Left Up'] == Cube.Colours['White']:
        for move in [U,L_to_Cross]:
            move(Cube)
    elif Cube.State['Up']['Edges']['Front Right Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Right Up'] == Cube.Colours['White']:
        for move in [U_,L_to_Cross]:
            move(Cube)
    elif Cube.State['Up']['Edges']['Front Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Front Right Up'] == Cube.Colours['White']:
        for move in [U,U,L_to_Cross]:
            move(Cube)

    elif Cube.State['Up']['Edges']['Front Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Right Up'] == Cube.Colours['White']:
        I_to_Cross(Cube)
    elif Cube.State['Up']['Edges']['Back Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Front Right Up'] == Cube.Colours['White']:
        for move in [U,I_to_Cross]:
            move(Cube)

    else:
        L_to_Cross(Cube)
        White_Cross(Cube)

def Track_Top_Edges (Cube):
    cnt = 0
    while cnt < 2:
        U(Cube)
        Correct_Edges, cnt = [] , 0
        for face in ['Front Left','Front Right','Back Left','Back Right']:
            if Cube.State[face]['Edges'][face+' Up'] == Cube.State[face]['Center']:
                Correct_Edges.append(face)
                cnt += 1
    
    # print(Correct_Edges)
    
    if len(Correct_Edges) == 2:
        if any(set(Correct_Edges) == set(pair) for pair in [['Front Left','Front Right'],['Front Left','Back Left'],['Front Right','Back Right'],['Back Left','Back Right']]):
            Correct_Edges.append('L')
        else:
            Correct_Edges.append('I')
    
    # print(Correct_Edges)
    return Correct_Edges

def Top_Edges (Cube):
    Top_Edges_ = Track_Top_Edges(Cube)
    if len(Top_Edges_) == 4:
        pass
    elif len(Top_Edges_) == 3:
        if Top_Edges_[-1] == 'L':
            if 'Front Right' in Top_Edges_ and 'Back Right' in Top_Edges_:
                Align_Top_Edges(Cube)
            elif 'Front Left' in Top_Edges_ and 'Front Right' in Top_Edges_:
                for move in [y_,Align_Top_Edges,y]:
                    move(Cube)
            elif 'Back Left' in Top_Edges_ and 'Back Right' in Top_Edges_:
                for move in [y,Align_Top_Edges,y_]:
                    move(Cube)
            else:
                for move in [y,y,Align_Top_Edges,y_,y_]:
                    move(Cube)
        elif Top_Edges_[-1] == 'I':
            if 'Front Left' in Top_Edges_:
                for move in [Align_Top_Edges,Top_Edges]:
                    move(Cube)
            else:
                for move in [y,Align_Top_Edges,y_,Top_Edges]:
                    move(Cube)

    Align_Centers(Cube)

def Check_Position (Cube,Position):
    if Position == 'Front Up':
        Expected_Colors = [Cube.Colours['White'],Cube.Colours['Red'],Cube.Colours['Blue']]
        Actual_Colors = []
        for side in ['Front Right','Front Left','Up']:
            Actual_Colors.append(Cube.State[side]['Vertices'][Position])
        for color in Actual_Colors:        
            if color not in Expected_Colors:
                return False
        return True
    elif Position == 'Right Up':
        Expected_Colors = [Cube.Colours['White'],Cube.Colours['Orange'],Cube.Colours['Blue']]
        Actual_Colors = []
        for side in ['Front Right','Back Right','Up']:
            Actual_Colors.append(Cube.State[side]['Vertices'][Position])
        for color in Actual_Colors:        
            if color not in Expected_Colors:
                return False
        return True 
    elif Position == 'Left Up':
        Expected_Colors = [Cube.Colours['White'],Cube.Colours['Red'],Cube.Colours['Green']]
        Actual_Colors = []
        for side in ['Back Left','Front Left','Up']:
            Actual_Colors.append(Cube.State[side]['Vertices'][Position])
        for color in Actual_Colors:        
            if color not in Expected_Colors:
                return False
        return True  
    else:
        Expected_Colors = [Cube.Colours['White'],Cube.Colours['Orange'],Cube.Colours['Green']]
        Actual_Colors = []
        for side in ['Back Right','Back Left','Up']:
            Actual_Colors.append(Cube.State[side]['Vertices'][Position])
        for color in Actual_Colors:        
            if color not in Expected_Colors:
                return False
        return True     
        

def Track_Top_Corners (Cube):
    Corner_Tracker = {}
    for corner in Cube.State['Up']['Vertices']:
        Corner_Tracker[corner] = Check_Position(Cube,corner)
    return Corner_Tracker

def Top_Corners (Cube):
    Corners = Track_Top_Corners(Cube)
    Correct_Corners = []
    for corner, correct_position in Corners.items():
        if correct_position == True:
            Correct_Corners.append(corner)
    
    if len(Correct_Corners) == 4:
        return False
    elif len(Correct_Corners) == 1:
        if Correct_Corners[0] == 'Front Up':
            Align_Top_Corners(Cube)
        elif Correct_Corners[0] == 'Right Up':
            for move in [y,Align_Top_Corners,y_]:
                move(Cube)
        elif Correct_Corners[0] == 'Left Up':
            for move in [y_,Align_Top_Corners,y]:
                move(Cube)
        else:
            for move in [y,y,Align_Top_Corners,y_,y_]:
                move(Cube)
    else:
        Align_Top_Corners(Cube)
        Top_Corners(Cube)

    return True

def Orient_Corners_Correctly (Cube):
    for i in range(4):
        while Cube.State['Up']['Vertices']['Front Up'] != Cube.Colours['White']:
            Orient_Correctly(Cube)
        U(Cube)


def Solve_Top_Layer (Cube):
    White_Cross(Cube)
    Top_Edges(Cube)
    cnt = 0
    while(Top_Corners(Cube) and cnt < 10):
        Top_Corners(Cube)
        cnt += 1
    if cnt == 10:
        Top_Edges(Cube)
        while(Top_Corners(Cube) and cnt < 10):
            Top_Corners(Cube)
    Orient_Corners_Correctly(Cube)
