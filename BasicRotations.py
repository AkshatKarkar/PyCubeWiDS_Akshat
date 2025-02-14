from vpython import *
from time import sleep
from initial_cube_making import cube_piece,Color_Cube


def R (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        horz_axis = vector(1, 0, 0)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Front'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Right'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, horz_axis,i)    

        Edge_F = Cube.Edges['Front Right Down']
        Edge_R = Cube.Edges['Front Right Up']
        Edge_FRU = Cube.Edges['Front']
        Edge_FRD = Cube.Edges['Right']
        Vert_FU = Cube.Vertices['Front Down']
        Vert_FD = Cube.Vertices['Right Down']
        Vert_RD = Cube.Vertices['Right Up']
        Vert_RU = Cube.Vertices['Front Up']

        Cube.Edges['Front'] = Edge_F
        Cube.Edges['Right'] = Edge_R
        Cube.Edges['Front Right Up'] = Edge_FRU
        Cube.Edges['Front Right Down'] = Edge_FRD
        Cube.Vertices['Front Up'] = Vert_FU
        Cube.Vertices['Front Down'] = Vert_FD
        Cube.Vertices['Right Down'] = Vert_RD
        Cube.Vertices['Right Up'] = Vert_RU
        Cube.Update_State()


def R_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        horz_axis = vector(1, 0, 0)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Front'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Right'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, horz_axis,i)    

        Edge_R = Cube.Edges['Front Right Down']
        Edge_F = Cube.Edges['Front Right Up']
        Edge_FRD = Cube.Edges['Front']
        Edge_FRU = Cube.Edges['Right']
        Vert_RD = Cube.Vertices['Front Down']
        Vert_RU = Cube.Vertices['Right Down']
        Vert_FU = Cube.Vertices['Right Up']
        Vert_FD = Cube.Vertices['Front Up']

        Cube.Edges['Front'] = Edge_F
        Cube.Edges['Right'] = Edge_R
        Cube.Edges['Front Right Up'] = Edge_FRU
        Cube.Edges['Front Right Down'] = Edge_FRD
        Cube.Vertices['Front Up'] = Vert_FU
        Cube.Vertices['Front Down'] = Vert_FD
        Cube.Vertices['Right Down'] = Vert_RD
        Cube.Vertices['Right Up'] = Vert_RU
        Cube.Update_State()


def U (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        vert_axis = vector(0, 1, 0)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps
        
        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, vert_axis,i)

        Edge_FLU = Cube.Edges['Front Right Up']
        Edge_BLU = Cube.Edges['Front Left Up']
        Edge_FRU = Cube.Edges['Back Right Up']
        Edge_BRU = Cube.Edges['Back Left Up']
        Vert_LU = Cube.Vertices['Front Up']
        Vert_FU = Cube.Vertices['Right Up']
        Vert_BU = Cube.Vertices['Left Up']
        Vert_RU = Cube.Vertices['Back Up']

        Cube.Edges['Front Left Up'] = Edge_FLU
        Cube.Edges['Back Left Up'] = Edge_BLU
        Cube.Edges['Front Right Up'] = Edge_FRU
        Cube.Edges['Back Right Up'] = Edge_BRU
        Cube.Vertices['Left Up'] = Vert_LU
        Cube.Vertices['Front Up'] = Vert_FU
        Cube.Vertices['Back Up'] = Vert_BU
        Cube.Vertices['Right Up'] = Vert_RU
        Cube.Update_State()

    

def U_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        vert_axis = vector(0, 1, 0)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps
        
        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, vert_axis,i)

        Edge_BRU = Cube.Edges['Front Right Up']
        Edge_FRU = Cube.Edges['Front Left Up']
        Edge_BLU = Cube.Edges['Back Right Up']
        Edge_FLU = Cube.Edges['Back Left Up']
        Vert_RU = Cube.Vertices['Front Up']
        Vert_BU = Cube.Vertices['Right Up']
        Vert_FU = Cube.Vertices['Left Up']
        Vert_LU = Cube.Vertices['Back Up']

        Cube.Edges['Front Left Up'] = Edge_FLU
        Cube.Edges['Back Left Up'] = Edge_BLU
        Cube.Edges['Front Right Up'] = Edge_FRU
        Cube.Edges['Back Right Up'] = Edge_BRU
        Cube.Vertices['Left Up'] = Vert_LU
        Cube.Vertices['Front Up'] = Vert_FU
        Cube.Vertices['Back Up'] = Vert_BU
        Cube.Vertices['Right Up'] = Vert_RU
        Cube.Update_State()


def D (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        vert_axis = vector(0, 1, 0)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps
        
        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, vert_axis,i)

        Edge_BRD = Cube.Edges['Front Right Down']
        Edge_FRD = Cube.Edges['Front Left Down']
        Edge_BLD = Cube.Edges['Back Right Down']
        Edge_FLD = Cube.Edges['Back Left Down']
        Vert_RD = Cube.Vertices['Front Down']
        Vert_BD = Cube.Vertices['Right Down']
        Vert_FD = Cube.Vertices['Left Down']
        Vert_LD = Cube.Vertices['Back Down']

        Cube.Edges['Front Left Down'] = Edge_FLD
        Cube.Edges['Back Left Down'] = Edge_BLD
        Cube.Edges['Front Right Down'] = Edge_FRD
        Cube.Edges['Back Right Down'] = Edge_BRD
        Cube.Vertices['Left Down'] = Vert_LD
        Cube.Vertices['Front Down'] = Vert_FD
        Cube.Vertices['Back Down'] = Vert_BD
        Cube.Vertices['Right Down'] = Vert_RD
        Cube.Update_State()


def D_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        vert_axis = vector(0, 1, 0)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps
        
        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, vert_axis,i)

        Edge_FLD = Cube.Edges['Front Right Down']
        Edge_BLD = Cube.Edges['Front Left Down']
        Edge_FRD = Cube.Edges['Back Right Down']
        Edge_BRD = Cube.Edges['Back Left Down']
        Vert_LD = Cube.Vertices['Front Down']
        Vert_FD = Cube.Vertices['Right Down']
        Vert_BD = Cube.Vertices['Left Down']
        Vert_RD = Cube.Vertices['Back Down']

        Cube.Edges['Front Left Down'] = Edge_FLD
        Cube.Edges['Back Left Down'] = Edge_BLD
        Cube.Edges['Front Right Down'] = Edge_FRD
        Cube.Edges['Back Right Down'] = Edge_BRD
        Cube.Vertices['Left Down'] = Vert_LD
        Cube.Vertices['Front Down'] = Vert_FD
        Cube.Vertices['Back Down'] = Vert_BD
        Cube.Vertices['Right Down'] = Vert_RD
        Cube.Update_State()

def L (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        horz_axis = vector(1, 0, 0)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Back'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Left'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, horz_axis,i)    

        Edge_B = Cube.Edges['Back Left Down']
        Edge_L = Cube.Edges['Back Left Up']
        Edge_BLU = Cube.Edges['Back']
        Edge_BLD = Cube.Edges['Left']
        Vert_BU = Cube.Vertices['Back Down']
        Vert_BD = Cube.Vertices['Left Down']
        Vert_LD = Cube.Vertices['Left Up']
        Vert_LU = Cube.Vertices['Back Up']

        Cube.Edges['Back'] = Edge_B
        Cube.Edges['Left'] = Edge_L
        Cube.Edges['Back Left Up'] = Edge_BLU
        Cube.Edges['Back Left Down'] = Edge_BLD
        Cube.Vertices['Back Up'] = Vert_BU
        Cube.Vertices['Back Down'] = Vert_BD
        Cube.Vertices['Left Down'] = Vert_LD
        Cube.Vertices['Left Up'] = Vert_LU
        Cube.Update_State()


def L_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        horz_axis = vector(1, 0, 0)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Back'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Edges['Left'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
            Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, horz_axis,i)    

        Edge_L = Cube.Edges['Back Left Down']
        Edge_B = Cube.Edges['Back Left Up']
        Edge_BLD = Cube.Edges['Back']
        Edge_BLU = Cube.Edges['Left']
        Vert_LD = Cube.Vertices['Back Down']
        Vert_LU = Cube.Vertices['Left Down']
        Vert_BU = Cube.Vertices['Left Up']
        Vert_BD = Cube.Vertices['Back Up']

        Cube.Edges['Back'] = Edge_B
        Cube.Edges['Left'] = Edge_L
        Cube.Edges['Back Left Up'] = Edge_BLU
        Cube.Edges['Back Left Down'] = Edge_BLD
        Cube.Vertices['Back Up'] = Vert_BU
        Cube.Vertices['Back Down'] = Vert_BD
        Cube.Vertices['Left Down'] = Vert_LD
        Cube.Vertices['Left Up'] = Vert_LU
        Cube.Update_State()


def F (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        z_axis = vector(0, 0, 1)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Front'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Left'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, z_axis,i)    

        Edge_L = Cube.Edges['Front Left Down']
        Edge_F = Cube.Edges['Front Left Up']
        Edge_FLD = Cube.Edges['Front']
        Edge_FLU = Cube.Edges['Left']
        Vert_LD = Cube.Vertices['Front Down']
        Vert_LU = Cube.Vertices['Left Down']
        Vert_FU = Cube.Vertices['Left Up']
        Vert_FD = Cube.Vertices['Front Up']

        Cube.Edges['Front'] = Edge_F
        Cube.Edges['Left'] = Edge_L
        Cube.Edges['Front Left Up'] = Edge_FLU
        Cube.Edges['Front Left Down'] = Edge_FLD
        Cube.Vertices['Front Up'] = Vert_FU
        Cube.Vertices['Front Down'] = Vert_FD
        Cube.Vertices['Left Down'] = Vert_LD
        Cube.Vertices['Left Up'] = Vert_LU    
        Cube.Update_State()


def F_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        z_axis = vector(0, 0, 1)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Front'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Left'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, z_axis,i)    

        Edge_F = Cube.Edges['Front Left Down']
        Edge_L = Cube.Edges['Front Left Up']
        Edge_FLU = Cube.Edges['Front']
        Edge_FLD = Cube.Edges['Left']
        Vert_FU = Cube.Vertices['Front Down']
        Vert_FD = Cube.Vertices['Left Down']
        Vert_LD = Cube.Vertices['Left Up']
        Vert_LU = Cube.Vertices['Front Up']

        Cube.Edges['Front'] = Edge_F
        Cube.Edges['Left'] = Edge_L
        Cube.Edges['Front Left Up'] = Edge_FLU
        Cube.Edges['Front Left Down'] = Edge_FLD
        Cube.Vertices['Front Up'] = Vert_FU
        Cube.Vertices['Front Down'] = Vert_FD
        Cube.Vertices['Left Down'] = Vert_LD
        Cube.Vertices['Left Up'] = Vert_LU
        Cube.Update_State()


def B (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        z_axis = vector(0, 0, 1)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Back'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Right'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, z_axis,i)    

        Edge_R = Cube.Edges['Back Right Down']
        Edge_B = Cube.Edges['Back Right Up']
        Edge_BRD = Cube.Edges['Back']
        Edge_BRU = Cube.Edges['Right']
        Vert_RD = Cube.Vertices['Back Down']
        Vert_RU = Cube.Vertices['Right Down']
        Vert_BU = Cube.Vertices['Right Up']
        Vert_BD = Cube.Vertices['Back Up']

        Cube.Edges['Back'] = Edge_B
        Cube.Edges['Right'] = Edge_R
        Cube.Edges['Back Right Up'] = Edge_BRU
        Cube.Edges['Back Right Down'] = Edge_BRD
        Cube.Vertices['Back Up'] = Vert_BU
        Cube.Vertices['Back Down'] = Vert_BD
        Cube.Vertices['Right Down'] = Vert_RD
        Cube.Vertices['Right Up'] = Vert_RU   
        Cube.Update_State()


def B_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        z_axis = vector(0, 0, 1)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Back'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Edges['Right'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, z_axis,i)    
            Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, z_axis,i)    

        Edge_B = Cube.Edges['Back Right Down']
        Edge_R = Cube.Edges['Back Right Up']
        Edge_BRU = Cube.Edges['Back']
        Edge_BRD = Cube.Edges['Right']
        Vert_BU = Cube.Vertices['Back Down']
        Vert_BD = Cube.Vertices['Right Down']
        Vert_RD = Cube.Vertices['Right Up']
        Vert_RU = Cube.Vertices['Back Up']

        Cube.Edges['Back'] = Edge_B
        Cube.Edges['Right'] = Edge_R
        Cube.Edges['Back Right Up'] = Edge_BRU
        Cube.Edges['Back Right Down'] = Edge_BRD
        Cube.Vertices['Back Up'] = Vert_BU
        Cube.Vertices['Back Down'] = Vert_BD
        Cube.Vertices['Right Down'] = Vert_RD
        Cube.Vertices['Right Up'] = Vert_RU  
        Cube.Update_State()


def M (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        horz_axis = vector(1, 0, 0)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Up'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Centers['Down'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)   

        Center_FL = Cube.Centers['Up']
        Center_D = Cube.Centers['Front Left']
        Center_U = Cube.Centers['Back Right']
        Center_BR = Cube.Centers['Down']
        Edge_FLD = Cube.Edges['Front Left Up']
        Edge_BRD = Cube.Edges['Front Left Down']
        Edge_BRU = Cube.Edges['Back Right Down']
        Edge_FLU = Cube.Edges['Back Right Up'] 

        Cube.Centers['Up'] = Center_U
        Cube.Centers['Front Left'] = Center_FL
        Cube.Centers['Back Right'] = Center_BR
        Cube.Centers['Down'] = Center_D
        Cube.Edges['Front Left Up'] = Edge_FLU
        Cube.Edges['Front Left Down'] = Edge_FLD
        Cube.Edges['Back Right Down'] = Edge_BRD
        Cube.Edges['Back Right Up'] = Edge_BRU
        Cube.Update_State()



def M_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        horz_axis = vector(1, 0, 0)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Up'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Centers['Down'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)
            Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)   

        Center_BR = Cube.Centers['Up']
        Center_U = Cube.Centers['Front Left']
        Center_D = Cube.Centers['Back Right']
        Center_FL = Cube.Centers['Down']
        Edge_BRU = Cube.Edges['Front Left Up']
        Edge_FLU = Cube.Edges['Front Left Down']
        Edge_FLD = Cube.Edges['Back Right Down']
        Edge_BRD = Cube.Edges['Back Right Up'] 

        Cube.Centers['Up'] = Center_U
        Cube.Centers['Front Left'] = Center_FL
        Cube.Centers['Back Right'] = Center_BR
        Cube.Centers['Down'] = Center_D
        Cube.Edges['Front Left Up'] = Edge_FLU
        Cube.Edges['Front Left Down'] = Edge_FLD
        Cube.Edges['Back Right Down'] = Edge_BRD
        Cube.Edges['Back Right Up'] = Edge_BRU
        Cube.Update_State()



def E (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        vert_axis = vector(0, 1, 0)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Left'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Right'].rotate_piece(rot_angle_anim, vert_axis,i)   

        Center_BR = Cube.Centers['Front Right']
        Center_FR = Cube.Centers['Front Left']
        Center_BL = Cube.Centers['Back Right']
        Center_FL = Cube.Centers['Back Left']
        Edge_R = Cube.Edges['Front']
        Edge_F = Cube.Edges['Left']
        Edge_L = Cube.Edges['Back']
        Edge_B = Cube.Edges['Right'] 

        Cube.Centers['Front Right'] = Center_FR
        Cube.Centers['Front Left'] = Center_FL
        Cube.Centers['Back Right'] = Center_BR
        Cube.Centers['Back Left'] = Center_BL
        Cube.Edges['Front'] = Edge_F
        Cube.Edges['Left'] = Edge_L
        Cube.Edges['Back'] = Edge_B
        Cube.Edges['Right'] = Edge_R
        Cube.Update_State()



def E_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        vert_axis = vector(0, 1, 0)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Front'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Left'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Back'].rotate_piece(rot_angle_anim, vert_axis,i)
            Cube.Edges['Right'].rotate_piece(rot_angle_anim, vert_axis,i)   

        Center_FL = Cube.Centers['Front Right']
        Center_BL = Cube.Centers['Front Left']
        Center_FR = Cube.Centers['Back Right']
        Center_BR = Cube.Centers['Back Left']
        Edge_L = Cube.Edges['Front']
        Edge_B = Cube.Edges['Left']
        Edge_R = Cube.Edges['Back']
        Edge_F = Cube.Edges['Right'] 

        Cube.Centers['Front Right'] = Center_FR
        Cube.Centers['Front Left'] = Center_FL
        Cube.Centers['Back Right'] = Center_BR
        Cube.Centers['Back Left'] = Center_BL
        Cube.Edges['Front'] = Edge_F
        Cube.Edges['Left'] = Edge_L
        Cube.Edges['Back'] = Edge_B
        Cube.Edges['Right'] = Edge_R
        Cube.Update_State()



def S (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        z_axis = vector(0, 0, 1)
        rot_angle = (-1)*pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Centers['Up'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Centers['Down'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, z_axis,i)   

        Center_D = Cube.Centers['Front Right'] 
        Center_FR = Cube.Centers['Up']
        Center_BL = Cube.Centers['Down']
        Center_U = Cube.Centers['Back Left']
        Edge_FRD = Cube.Edges['Front Right Up']
        Edge_FRU = Cube.Edges['Back Left Up']
        Edge_BLU = Cube.Edges['Back Left Down']
        Edge_BLD = Cube.Edges['Front Right Down'] 

        Cube.Centers['Front Right'] = Center_FR
        Cube.Centers['Up'] = Center_U
        Cube.Centers['Down'] = Center_D
        Cube.Centers['Back Left'] = Center_BL
        Cube.Edges['Front Right Up'] = Edge_FRU
        Cube.Edges['Back Left Up'] = Edge_BLU
        Cube.Edges['Back Left Down'] = Edge_BLD
        Cube.Edges['Front Right Down'] = Edge_FRD    
        Cube.Update_State()



def S_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        fps , speed = 100 , 4
        z_axis = vector(0, 0, 1)
        rot_angle = pi / 2
        rot_angle_anim = rot_angle/fps

        for i in range(fps):
            rate(speed*fps)
            Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Centers['Up'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Centers['Down'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, z_axis,i)
            Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, z_axis,i)   

        Center_U = Cube.Centers['Front Right'] 
        Center_BL = Cube.Centers['Up']
        Center_FR = Cube.Centers['Down']
        Center_D = Cube.Centers['Back Left']
        Edge_BLU = Cube.Edges['Front Right Up']
        Edge_BLD = Cube.Edges['Back Left Up']
        Edge_FRD = Cube.Edges['Back Left Down']
        Edge_FRU = Cube.Edges['Front Right Down'] 

        Cube.Centers['Front Right'] = Center_FR
        Cube.Centers['Up'] = Center_U
        Cube.Centers['Down'] = Center_D
        Cube.Centers['Back Left'] = Center_BL
        Cube.Edges['Front Right Up'] = Edge_FRU
        Cube.Edges['Back Left Up'] = Edge_BLU
        Cube.Edges['Back Left Down'] = Edge_BLD
        Cube.Edges['Front Right Down'] = Edge_FRD  
        Cube.Update_State()



def x (Cube,num_rotations=1):
    for counter in range(num_rotations):
        L_(Cube,num_rotations=1)
        M_(Cube,num_rotations=1)
        R(Cube,num_rotations=1)
        Cube.Update_State()


def x_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        L(Cube,num_rotations=1)
        M(Cube,num_rotations=1)
        R_(Cube,num_rotations=1)
        Cube.Update_State()


def y (Cube,num_rotations=1):
    for counter in range(num_rotations):
        U(Cube,num_rotations=1)
        E_(Cube,num_rotations=1)
        D_(Cube,num_rotations=1)
        Cube.Update_State()


def y_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        U_(Cube,num_rotations=1)
        E(Cube,num_rotations=1)
        D(Cube,num_rotations=1)
        Cube.Update_State()


def z (Cube,num_rotations=1):
    for counter in range(num_rotations):
        F(Cube,num_rotations=1)
        S(Cube,num_rotations=1)
        B_(Cube,num_rotations=1)
        Cube.Update_State()


def z_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        F_(Cube,num_rotations=1)
        S_(Cube,num_rotations=1)
        B(Cube,num_rotations=1)
        Cube.Update_State()


def u (Cube,num_rotations=1):
    for counter in range(num_rotations):
        U(Cube,num_rotations=1)
        E_(Cube,num_rotations=1)
        Cube.Update_State()


def u_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        U_(Cube,num_rotations=1)
        E(Cube,num_rotations=1)
        Cube.Update_State()


def d (Cube,num_rotations=1):
    for counter in range(num_rotations):
        D(Cube,num_rotations=1)
        E(Cube,num_rotations=1)
        Cube.Update_State()


def d_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        D_(Cube,num_rotations=1)
        E_(Cube,num_rotations=1)
        Cube.Update_State()


def r (Cube,num_rotations=1):
    for counter in range(num_rotations):
        R(Cube,num_rotations=1)
        M_(Cube,num_rotations=1)
        Cube.Update_State()


def r_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        R_(Cube,num_rotations=1)
        M(Cube,num_rotations=1)
        Cube.Update_State()


def l (Cube,num_rotations=1):
    for counter in range(num_rotations):
        L(Cube,num_rotations=1)
        M(Cube,num_rotations=1)
        Cube.Update_State()


def l_(Cube,num_rotations=1):
    for counter in range(num_rotations):
        L_(Cube,num_rotations=1)
        M_(Cube,num_rotations=1)
        Cube.Update_State()


def f (Cube,num_rotations=1):
    for counter in range(num_rotations):
        F(Cube,num_rotations=1)
        S(Cube,num_rotations=1)
        Cube.Update_State()


def f_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        F_(Cube,num_rotations=1)
        S_(Cube,num_rotations=1)
        Cube.Update_State()


def b (Cube,num_rotations=1):
    for counter in range(num_rotations):
        B(Cube,num_rotations=1)
        S_(Cube,num_rotations=1)
        Cube.Update_State()


def b_ (Cube,num_rotations=1):
    for counter in range(num_rotations):
        B_(Cube,num_rotations=1)
        S(Cube,num_rotations=1)
        Cube.Update_State()


cube = Color_Cube()
sleep(3)
U(cube,num_rotations=1)
sleep(1)
R(cube,num_rotations=1)
sleep(1)
F(cube,num_rotations=1)
F_(cube,num_rotations=1)
R_(cube,num_rotations=1)
U(cube,num_rotations=1)
sleep(10)