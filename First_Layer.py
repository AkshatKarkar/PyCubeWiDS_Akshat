from BasicRotations import *
from OverallAlgos import *

def Track_Yellow_Edges (Cube):
    Edge_Tracker = []
    for side in Cube.Sides:
        for edge in Cube.State[side]['Edges']:
            if Cube.State[side]['Edges'][edge] == Cube.Colours['Yellow']:
                Edge_Tracker.append([side,edge,0,0])
    for side in Cube.Sides:
        for edge in Cube.State[side]['Edges']:
            for piece in Edge_Tracker:
                if edge == piece[1] and side != piece[0]:
                    piece[2] = side
                    piece[3] = Cube.State[side]['Edges'][edge]

    Yellow_Edges ={
        'Red' : [],
        'Blue' : [],
        'Green' : [],
        'Orange' : []
    }
    for piece in Edge_Tracker:
        if piece[3] == Cube.Colours['Red']:
            Yellow_Edges['Red'] = piece[:3]
        elif piece[3] == Cube.Colours['Blue']:
            Yellow_Edges['Blue'] = piece[:3]
        elif piece[3] == Cube.Colours['Green']:
            Yellow_Edges['Green'] = piece[:3]
        else:
            Yellow_Edges['Orange'] = piece[:3]

    return Yellow_Edges


def Wrong_Orientation(Cube,Position,Other_Face):
    if Other_Face == 'Up':
        if Position == 'Front Right Up':
            for move in [R_,F,R]:
                move(Cube)
        elif Position == 'Front Left Up':
            for move in [U_,R_,F,R]:
                move(Cube)
        elif Position == 'Back Right Up':
            for move in [U,R_,F,R]:
                move(Cube)
        elif Position == 'Back Left Up':
            for move in [U,U,R_,F,R]:
                move(Cube)
    elif Other_Face == 'Down':
        if Position == 'Front Right Down':
            for move in [R,F,R]: #Change this [R,R,R_,F,R]
                move(Cube)
        elif Position == 'Front Left Down':
            for move in [F,F,U_,R_,F,R]:
                move(Cube)
        elif Position == 'Back Right Down':
            for move in [B,B,U,R_,F,R]:
                move(Cube)
        elif Position == 'Back Left Down':
            for move in [L,L,U,U,R_,F,R]:
                move(Cube)
def Align_Upper_Edges(Cube,Position):
    if Position == 'Front Right Up':
        U(Cube)
        F(Cube,2)
    elif Position == 'Front Left Up':
        F(Cube,2)
    elif Position == 'Back Right Up':
        U(Cube,2)
        F(Cube,2)
    elif Position == 'Back Left Up':
        U_(Cube)
        F(Cube,2)
def Align_Lower_Edges(Cube,Position):
    if Position == 'Front Right Down':
        for move in [R,R,U,F,F]:
            move(Cube)
    elif Position == 'Front Left Down':
        pass
    elif Position == 'Back Right Down':
        for move in [B,B,U,U,F,F]:
            move(Cube)
    elif Position == 'Back Left Down':
        for move in [L,L,U_,F,F]:
            move(Cube)
def Align_Middle_Edges(Cube,Position,Face):
    if Position == 'Front':
        if Face == 'Front Right':
            F(Cube)
        else:
            for move in [R,U,R_,F,F]:
                move(Cube)
    elif Position == 'Back':
        if Face == 'Back Right':
            for move in [L,U_,L_,F,F]:
                move(Cube)
        else:
            for move in [B_,U,U,B,F,F]:
                move(Cube)
    elif Position == 'Right':
        if Face == 'Front Right':
            for move in [B,U_,U_,B_,F,F]:
                move(Cube)
        else:
            for move in [R_,U,R,F,F]:
                move(Cube)
    elif Position == 'Left':
        if Face == 'Front Left':
            for move in [L_,U_,L,F,F]:
                move(Cube)
        else:
            F_(Cube)

def Yellow_Cross(Cube):
    for color in ['Red','Blue','Orange','Green']:
        if color == 'Red':
            Yellow_Edges = Track_Yellow_Edges(Cube)
            Position, Face , Other_Face = Yellow_Edges[color][1] , Yellow_Edges[color][0] , Yellow_Edges[color][2]
            if Other_Face == 'Up' or 'Down':
                Wrong_Orientation(Cube,Position,Other_Face)
            if Face == 'Down':
                Align_Lower_Edges(Cube,Position)
            elif Face == 'Up' :
                Align_Upper_Edges(Cube,Position)
            else:
                Align_Middle_Edges(Cube,Position,Face)
            # Align_Centers(Cube)
        elif color == 'Blue':
            y(Cube)
            Yellow_Edges = Track_Yellow_Edges(Cube)
            Position, Face , Other_Face = Yellow_Edges[color][1] , Yellow_Edges[color][0] , Yellow_Edges[color][2]
            if Other_Face == 'Up' or 'Down':
                Wrong_Orientation(Cube,Position,Other_Face)
            if Face == 'Down':
                Align_Lower_Edges(Cube,Position)
            elif Face == 'Up' :
                Align_Upper_Edges(Cube,Position)
            else:
                Align_Middle_Edges(Cube,Position,Face)
            # Align_Centers(Cube)
        elif color == 'Orange':
            y(Cube)
            Yellow_Edges = Track_Yellow_Edges(Cube)
            Position, Face , Other_Face = Yellow_Edges[color][1] , Yellow_Edges[color][0] , Yellow_Edges[color][2]
            if Other_Face == 'Up' or 'Down':
                Wrong_Orientation(Cube,Position,Other_Face)
            if Face == 'Down':
                Align_Lower_Edges(Cube,Position)
            elif Face == 'Up' :
                Align_Upper_Edges(Cube,Position)
            else:
                Align_Middle_Edges(Cube,Position,Face)
            # Align_Centers(Cube)
        else:
            y(Cube)
            Yellow_Edges = Track_Yellow_Edges(Cube)
            Position, Face , Other_Face = Yellow_Edges[color][1] , Yellow_Edges[color][0] , Yellow_Edges[color][2]
            if Other_Face == 'Up' or 'Down':
                Wrong_Orientation(Cube,Position,Other_Face)
            if Face == 'Down':
                Align_Lower_Edges(Cube,Position)
            elif Face == 'Up' :
                Align_Upper_Edges(Cube,Position)
            else:
                Align_Middle_Edges(Cube,Position,Face)
            Align_Centers(Cube)

def Track_Yellow_Corners (Cube):
    Corner_Tracker = []
    for side in Cube.Sides:
        for corner in Cube.State[side]['Vertices']:
            if Cube.State[side]['Vertices'][corner] == Cube.Colours['Yellow']:
                Corner_Tracker.append([side,corner,[],[]])
    for side in Cube.Sides:
        for corner in Cube.State[side]['Vertices']:
            for piece in Corner_Tracker:
                if corner == piece[1] and side != piece[0]:
                    piece[2].append(side)
                    piece[3].append(Cube.State[side]['Vertices'][corner])

    Yellow_Corners ={
        'Red Blue' : [],
        'Blue Orange' : [],
        'Green Red' : [],
        'Orange Green' : []
    }
    for piece in Corner_Tracker:
        if Cube.Colours['Red'] in piece[3] and Cube.Colours['Blue'] in piece[3]:
            Yellow_Corners['Red Blue'] = piece[:3]
        elif Cube.Colours['Orange'] in piece[3] and Cube.Colours['Blue'] in piece[3]:
            Yellow_Corners['Blue Orange'] = piece[:3]
        elif Cube.Colours['Green'] in piece[3] and Cube.Colours['Red'] in piece[3]:
            Yellow_Corners['Green Red'] = piece[:3]
        else:
            Yellow_Corners['Orange Green'] = piece[:3]

    return Yellow_Corners

def Change_Corner_Orientation(Cube):
    R(Cube)
    U(Cube)
    R_(Cube)
    U_(Cube)

def Align_Downer (Cube,Position,Face):
    if Position == 'Front Down' :
        if Face == 'Down':
            pass
        elif Face == 'Front Right':
            Change_Corner_Orientation(Cube)
            Change_Corner_Orientation(Cube)
        else:
            Change_Corner_Orientation(Cube)
            Change_Corner_Orientation(Cube)
            Change_Corner_Orientation(Cube)
            Change_Corner_Orientation(Cube)
    elif Position == 'Right Down':
        if Face == 'Down':
           for move in [B,U,U,B_,R,U_,R_]:
               move(Cube)
        elif Face == 'Front Right':
           for move in [R_,U,U,R,R,U_,R_]:
                move(Cube)             
        else:
            for move in [B,U,B_,U_,F_,U,F]:
                move(Cube)
    elif Position == 'Left Down':
        if Face == 'Down':
            for move in [L_,U,U,L,F_,U,F]:
                move(Cube)
        elif Face == 'Front Left':
            for move in [F,U,U,F_,F_,U,F]:
                move(Cube)         
        else:
            for move in [L_,R,U_,R_,L]:
                move(Cube)
    else:
        if Face == 'Down':
            for move in [L,R,U,U,R_,L_]:
                move(Cube)
        elif Face == 'Back Right':
            for move in [B_,U_,B,R,U_,R_]:
                move(Cube)
        else:
           for move in [L,U,L_,F_,U,F]:
               move(Cube)

def Align_Upper_Corners(Cube,Position,Face):
    if Position == 'Front Up' :
        if Face == 'Up':
            for move in [R,U,U,R_,U_]:
                move(Cube)
            Change_Corner_Orientation(Cube)
        elif Position == 'Front Right':
            Change_Corner_Orientation(Cube)
        else:
            for move in [U,R,U_,R_]:
                move(Cube)
    elif Position == 'Right Up':
        if Face == 'Up':
            for move in [U,R,U,U,R_,U_]:
                move(Cube)
            Change_Corner_Orientation(Cube)
        elif Face == 'Front Right':
           for move in [U,U,R,U_,R_]:
                move(Cube)             
        else:
            for move in [F_,U,F]:
                move(Cube)
    elif Position == 'Left Up':
        if Face == 'Up':
            for move in [U_,R,U,U,R_,U_,Change_Corner_Orientation]:  #### Maybe wrong
                move(Cube)
        elif Face == 'Front Left':
            for move in [U,U,F_,U,F]:
                move(Cube)         
        else:
            for move in [R,U_,R_]:
                move(Cube)
    else:
        if Face == 'Up':
            for move in [U_,U_,R,U,U,R_,U_]:
                move(Cube)
            Change_Corner_Orientation(Cube)
        elif Face == 'Back Right':
            for move in [R,U,U,R_]:
                move(Cube)
        else:
           for move in [F_,U,U,F]:
               move(Cube)
    

def Yellow_Corners (Cube):
    for colors in ['Red Blue','Blue Orange','Orange Green','Green Red']:
        if colors == 'Red Blue':
            Yellow_Corners = Track_Yellow_Corners(Cube)
            Position , Face = Yellow_Corners[colors][1] , Yellow_Corners[colors][0]
            if Position[-4:] == 'Down':
                Align_Downer(Cube,Position,Face)
            elif Position[-2:] == 'Up':
                Align_Upper_Corners(Cube,Position,Face)
        elif colors == 'Blue Orange':
            y(Cube)
            Yellow_Corners = Track_Yellow_Corners(Cube)
            Position , Face = Yellow_Corners[colors][1] , Yellow_Corners[colors][0]
            if Position[-4:] == 'Down':
                Align_Downer(Cube,Position,Face)
            elif Position[-2:] == 'Up':
                Align_Upper_Corners(Cube,Position,Face)
            # Align_Centers(Cube)
        elif colors == 'Orange Green':
            y(Cube)
            Yellow_Corners = Track_Yellow_Corners(Cube)
            Position , Face = Yellow_Corners[colors][1] , Yellow_Corners[colors][0]
            if Position[-4:] == 'Down':
                Align_Downer(Cube,Position,Face)
            elif Position[-2:] == 'Up':
                Align_Upper_Corners(Cube,Position,Face)
            # Align_Centers(Cube)            
        else:
            y(Cube)
            Yellow_Corners = Track_Yellow_Corners(Cube)
            Position , Face = Yellow_Corners[colors][1] , Yellow_Corners[colors][0]
            if Position[-4:] == 'Down':
                Align_Downer(Cube,Position,Face)
            elif Position[-2:] == 'Up':
                Align_Upper_Corners(Cube,Position,Face)
            Align_Centers(Cube)


def Solve_First_Layer (Cube):
    Yellow_Cross(Cube)
    Yellow_Corners(Cube)
