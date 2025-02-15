from BasicRotations import *
from OverallAlgos import *

def Track_Middle_Edges (Cube):
    Edge_Tracker = []
    for Col in ['Orange','Green','Blue','Red']:
        for side in Cube.Sides:
            for edge in Cube.State[side]['Edges']:
                if Cube.State[side]['Edges'][edge] == Cube.Colours[Col]:
                    Edge_Tracker.append([side,edge,0,[Cube.Colours[Col]]])
        for side in Cube.Sides:
            for edge in Cube.State[side]['Edges']:
                for piece in Edge_Tracker:
                    if edge == piece[1] and side != piece[0]:
                        if Cube.State[side]['Edges'][edge] not in [Cube.Colours['White'],Cube.Colours['Yellow']]:
                            piece[2] = side
                            piece[3].append(Cube.State[side]['Edges'][edge])


    Middle_Edges ={
        'Red Blue' : [],
        'Blue Orange' : [],
        'Green Red' : [],
        'Orange Green' : []
    }
    for piece in Edge_Tracker:
        if Cube.Colours['Red'] in piece[3] and Cube.Colours['Blue'] in piece[3]:
            Middle_Edges['Red Blue'] = piece[:3]
        elif Cube.Colours['Orange'] in piece[3] and Cube.Colours['Blue'] in piece[3]:
            Middle_Edges['Blue Orange'] = piece[:3]
        elif Cube.Colours['Green'] in piece[3] and Cube.Colours['Red'] in piece[3]:
            Middle_Edges['Green Red'] = piece[:3]
        elif Cube.Colours['Green'] in piece[3] and Cube.Colours['Orange'] in piece[3]:
            Middle_Edges['Orange Green'] = piece[:3]

    return Middle_Edges

def Insert_Middle_Edge (Cube,Position,Face):
    if Face == 'Up':
        if Position == 'Front Right Up':
            for move in [y,Middle_Layer_Left,y_]:
                move(Cube)
        elif Position == 'Front Left Up':
            for move in [d_,Middle_Layer_Left,y_]:
                move(Cube)
        elif Position == 'Back Right Up':
            for move in [U,y,Middle_Layer_Left,y_]:
                move(Cube)
        else:
            for move in [U_,d_,Middle_Layer_Left,y_]:
                move(Cube)
    elif Face != 'Up' and Position[-2:] == 'Up':
        if Position == 'Front Right Up':
            for move in [U,Middle_Layer_Right]:
                move(Cube)
        elif Position == 'Front Left Up':
            for move in [Middle_Layer_Right]:
                move(Cube)
        elif Position == 'Back Right Up':
            for move in [U,U,Middle_Layer_Right]:
                move(Cube)
        else:
            for move in [U_,Middle_Layer_Right]:
                move(Cube)
    elif Face == 'Front Right':
        if Position == 'Front':
            for move in [Middle_Layer_Right,U,U,Middle_Layer_Right]:
                move(Cube)
        else:
            for move in [y,Middle_Layer_Right,U_,U_,Middle_Layer_Left,y_]:
                move(Cube)
    elif Face == 'Back Left':
        if Position == 'Left':
            for move in [Middle_Layer_Left,U,U,Middle_Layer_Right]:
                move(Cube)
        else:
            for move in [y_,Middle_Layer_Left,y,y,Middle_Layer_Left,y_]:
                move(Cube)
    elif Face == 'Back Right':
        if Position == 'Right':
            for move in [y,Middle_Layer_Right,y_,U_,Middle_Layer_Right]:
                move(Cube)
        else:
            for move in [y,y,Middle_Layer_Right,y_,U_,Middle_Layer_Left,y_]:
                move(Cube)
    elif Face == 'Front Left':
        if Position == 'Left':
            for move in [Middle_Layer_Left,y,U,Middle_Layer_Left,y_]:
                move(Cube)
        else:
            pass
        
def Solve_Second_Layer (Cube):
    for colors in ['Red Blue','Blue Orange','Orange Green','Green Red']:
        if colors == 'Red Blue':
            Middle_Edges = Track_Middle_Edges(Cube)
            Position , Face = Middle_Edges[colors][1] , Middle_Edges[colors][0]
            Insert_Middle_Edge(Cube,Position,Face)
            Align_Centers(Cube)
        elif colors == 'Blue Orange':
            y(Cube)
            Middle_Edges = Track_Middle_Edges(Cube)
            Position, Face = Middle_Edges[colors][1] , Middle_Edges[colors][0]
            Insert_Middle_Edge(Cube,Position,Face)
            # Align_Centers(Cube)
        elif colors == 'Orange Green':
            y(Cube)
            Middle_Edges = Track_Middle_Edges(Cube)
            Position, Face = Middle_Edges[colors][1] , Middle_Edges[colors][2]
            Insert_Middle_Edge(Cube,Position,Face)
            # Align_Centers(Cube)            
        else:
            y(Cube)
            Middle_Edges = Track_Middle_Edges(Cube)
            Position, Face = Middle_Edges[colors][1] , Middle_Edges[colors][2]
            Insert_Middle_Edge(Cube,Position,Face)
            Align_Centers(Cube)
