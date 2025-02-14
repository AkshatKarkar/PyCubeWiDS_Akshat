
from OverallAlgos import *
import random

def Scramble(Cube):

    commands = [r,r_,l,l_,f,f_,b,b_,u,u_,d,d_,M,M_,E,E_,S,S_,U,U_,D,D_,R,R_,L,L_,F,F_,B,B_]

    for i in range(50):
        move = random.choice(commands)
        move(Cube)

    return Cube