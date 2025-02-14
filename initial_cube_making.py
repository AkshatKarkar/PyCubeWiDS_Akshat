from vpython import *
from time import *
from time import sleep

class cube_piece:
    def __init__(self, center, size, color):
        thickness = 0.001
        self.center = center
        self.front = box(pos=center+vector(0,0,size.z/2),size=vector(size.x,size.y,thickness),color=color[0])
        self.back = box(pos=center-vector(0,0,size.z/2),size=vector(size.x,size.y,thickness),color=color[1])
        self.right = box(pos=center+vector(size.x/2,0,0),size=vector(thickness,size.y,size.z),color=color[2])
        self.left = box(pos=center-vector(size.x/2,0,0),size=vector(thickness,size.y,size.z),color=color[3])
        self.up = box(pos=center+vector(0,size.y/2,0),size=vector(size.x,thickness,size.z),color=color[4])
        self.down = box(pos=center-vector(0,size.y/2,0),size=vector(size.x,thickness,size.z),color=color[5])
        self.sides = {
            'Front': self.front,
            'Back': self.back,
            'Right': self.right,
            'Left': self.left,
            'Up': self.up,
            'Down': self.down
        }


    def rotate_piece(self,angle_of_rot,axis_of_rot,counter):
        self.center = self.center.rotate(angle=angle_of_rot,axis=axis_of_rot)
        
        self.front.pos = self.front.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.back.pos = self.back.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.right.pos = self.right.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.left.pos = self.left.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.up.pos = self.up.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.down.pos = self.down.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)

        self.front.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.back.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.right.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.left.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.up.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.down.rotate(angle=angle_of_rot,axis=axis_of_rot)


        if counter == 0:
            if axis_of_rot == vector(1,0,0):
                tempx = self.up
                if angle_of_rot > 0 :
                    self.up,self.front,self.down,self.back= self.back,tempx,self.front,self.down
                elif angle_of_rot < 0 :
                    self.up,self.front,self.down,self.back= self.front,self.down,self.back,tempx
            elif axis_of_rot == vector(0,1,0):
                tempy = self.right
                if angle_of_rot < 0 :
                    self.right,self.front,self.left,self.back = self.back,tempy,self.front,self.left
                elif angle_of_rot > 0 :
                    self.right,self.front,self.left,self.back = self.front,self.left,self.back,tempy
            elif axis_of_rot == vector(0,0,1):
                tempz = self.right
                if angle_of_rot > 0 :
                    self.right,self.up,self.left,self.down = self.down,tempz,self.up,self.left
                elif angle_of_rot < 0 :
                    self.right,self.up,self.left,self.down = self.up,self.left,self.down,tempz

            self.sides = {
            'Front': self.front,
            'Back': self.back,
            'Right': self.right,
            'Left': self.left,
            'Up': self.up,
            'Down': self.down
        }

print("section 1 done")

class Color_Cube:

    def __init__(self):

        cube_size = vector(1,1,1)

        # # Create the canvas
        bg = canvas(width=1500, height=800, background=color.black)
        print("Canvas Created")
        all_directions = [
            vector(1,0,0),vector(0,1,0),vector(0,0,1),vector(-1,0,0),vector(0,-1,0),vector(0,0,-1)
        ]
        for vect in all_directions:
            distant_light(direction=vect,color=color.white*0.3)

        Centers , Edges , Vertices = {} , {} , {}

        all_colors = [
            color.red,
            color.magenta,
            color.blue,
            color.green,
            color.white,
            color.yellow
        ]
        center_coords = [
            # vp.vector(0, 0, 0),
            vector(0, 1.05, 0),
            vector(0, -1.05, 0),
            vector(1.05, 0, 0),
            vector(-1.05, 0, 0),
            vector(0, 0, 1.05),
            vector(0, 0, -1.05)
        ]
        edge_coords = [
            vector(1.05,1.05,0),
            vector(1.05,-1.05,0),
            vector(-1.05,1.05,0),
            vector(-1.05,-1.05,0),
            vector(1.05,0,1.05),
            vector(1.05,0,-1.05),
            vector(-1.05,0,1.05),
            vector(-1.05,0,-1.05),
            vector(0,1.05,1.05),
            vector(0,1.05,-1.05),
            vector(0,-1.05,1.05),
            vector(0,-1.05,-1.05)
        ]
        vertex_coords = [
            vector(1.05,1.05,1.05),
            vector(1.05,1.05,-1.05),
            vector(1.05,-1.05,1.05),
            vector(1.05,-1.05,-1.05),
            vector(-1.05,1.05,1.05),
            vector(-1.05,1.05,-1.05),
            vector(-1.05,-1.05,1.05),
            vector(-1.05,-1.05,-1.05)
        ]
        

        def assign_color(all_colors, active_colors):
            return [color if color in active_colors else vector(0,0,0) for color in all_colors]
        
        CenterMost = cube_piece(center=vector(0,0,0),size=cube_size,color=[color.black]*6)
        
        center_map = {
            0: ('Up', [color.white]),
            1: ('Down', [color.yellow]),
            2: ('Front Right', [color.blue]),
            3: ('Back Left', [color.green]),
            4: ('Front Left', [color.red]),
            5: ('Back Right', [color.magenta]),
        }

        for i, coord in enumerate(center_coords):
            name, active_colors = center_map[i]
            c = assign_color(all_colors, active_colors)
            Centers[name] = cube_piece(center=coord, size=cube_size, color=c)

        edge_map = {
            0: ('Front Right Up', [color.blue, color.white]),
            1: ('Front Right Down', [color.blue, color.yellow]),
            2: ('Back Left Up', [color.green, color.white]),
            3: ('Back Left Down', [color.green, color.yellow]),
            4: ('Front', [color.red, color.blue]),
            5: ('Right', [color.blue, color.magenta]),
            6: ('Left', [color.red, color.green]),
            7: ('Back', [color.green, color.magenta]),
            8: ('Front Left Up', [color.red, color.white]),
            9: ('Back Right Up', [color.magenta, color.white]),
            10: ('Front Left Down', [color.red, color.yellow]),
            11: ('Back Right Down', [color.magenta, color.yellow])
        }
        for i,coord in enumerate(edge_coords):
            name, active_colors = edge_map[i]
            c = assign_color(all_colors, active_colors)
            Edges[name] = cube_piece(center=coord,size=cube_size,color=c)

        vertex_map = {
            0: ('Front Up', [color.red, color.blue, color.white]),
            1: ('Right Up', [color.magenta, color.blue, color.white]),
            2: ('Front Down', [color.red, color.blue, color.yellow]),
            3: ('Right Down', [color.magenta, color.blue, color.yellow]),
            4: ('Left Up', [color.red, color.green, color.white]),
            5: ('Back Up', [color.magenta, color.white, color.green]),
            6: ('Left Down', [color.red, color.green, color.yellow]),
            7: ('Back Down', [color.magenta, color.green, color.yellow])
        }
        for i,coord in enumerate(vertex_coords):
            name, active_colors = vertex_map[i]
            c = assign_color(all_colors, active_colors)
            Vertices[name] = cube_piece(center=coord,size=cube_size,color=c)

        Cube_colors = {
            'Red' : color.red,
            'Orange' : color.magenta,
            'Blue' : color.blue,
            'Green' : color.green,
            'White' : color.white,
            'Yellow' : color.yellow
        }
        Cube_Sides = ['Up','Down','Front Right','Front Left','Back Right','Back Left']

        
        bg.camera.pos = vector(4, 4, 4)  
        bg.camera.axis = vector(-4, -4, -4)  
        bg.camera.up = vector(0, 1, 0)  
        
        self.Centers = Centers
        self.Edges = Edges
        self.Vertices = Vertices
        self.Colours = Cube_colors
        self.Sides = Cube_Sides
        self.Update_State()
        print("Section2")
    def Update_State(self):
        Unwrapped = {
                'Up': {
                    'Center': self.Centers['Up'].sides['Up'].color,
                    'Edges': {
                        'Front Right Up': self.Edges['Front Right Up'].sides['Up'].color,
                        'Front Left Up': self.Edges['Front Left Up'].sides['Up'].color,
                        'Back Right Up': self.Edges['Back Right Up'].sides['Up'].color,
                        'Back Left Up': self.Edges['Back Left Up'].sides['Up'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Up'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Up'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Up'].color,
                        'Back Up': self.Vertices['Back Up'].sides['Up'].color
                    }
                },
                'Down': {
                    'Center': self.Centers['Down'].sides['Down'].color,
                    'Edges': {
                        'Front Right Down': self.Edges['Front Right Down'].sides['Down'].color,
                        'Front Left Down': self.Edges['Front Left Down'].sides['Down'].color,
                        'Back Right Down': self.Edges['Back Right Down'].sides['Down'].color,
                        'Back Left Down': self.Edges['Back Left Down'].sides['Down'].color
                    },
                    'Vertices': {
                        'Front Down': self.Vertices['Front Down'].sides['Down'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Down'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Down'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Down'].color
                    }
                },
                'Front Right': {
                    'Center': self.Centers['Front Right'].sides['Right'].color,
                    'Edges': {
                        'Front Right Up': self.Edges['Front Right Up'].sides['Right'].color,
                        'Front Right Down': self.Edges['Front Right Down'].sides['Right'].color,
                        'Front': self.Edges['Front'].sides['Right'].color,
                        'Right': self.Edges['Right'].sides['Right'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Right'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Right'].color,
                        'Front Down': self.Vertices['Front Down'].sides['Right'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Right'].color
                    }
                },
                'Back Left': {
                    'Center': self.Centers['Back Left'].sides['Left'].color,
                    'Edges': {
                        'Back Left Up': self.Edges['Back Left Up'].sides['Left'].color,
                        'Back Left Down': self.Edges['Back Left Down'].sides['Left'].color,
                        'Back': self.Edges['Back'].sides['Left'].color,
                        'Left': self.Edges['Left'].sides['Left'].color
                    },
                    'Vertices': {
                        'Back Up': self.Vertices['Back Up'].sides['Left'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Left'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Left'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Left'].color
                    }
                },
                'Front Left': {
                    'Center': self.Centers['Front Left'].sides['Front'].color,
                    'Edges': {
                        'Front Left Up': self.Edges['Front Left Up'].sides['Front'].color,
                        'Front Left Down': self.Edges['Front Left Down'].sides['Front'].color,
                        'Front': self.Edges['Front'].sides['Front'].color,
                        'Left': self.Edges['Left'].sides['Front'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Front'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Front'].color,
                        'Front Down': self.Vertices['Front Down'].sides['Front'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Front'].color
                    }
                },
                'Back Right': {
                    'Center': self.Centers['Back Right'].sides['Back'].color,
                    'Edges': {
                        'Back Right Up': self.Edges['Back Right Up'].sides['Back'].color,
                        'Back Right Down': self.Edges['Back Right Down'].sides['Back'].color,
                        'Back': self.Edges['Back'].sides['Back'].color,
                        'Right': self.Edges['Right'].sides['Back'].color
                    },
                    'Vertices': {
                        'Back Up': self.Vertices['Back Up'].sides['Back'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Back'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Back'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Back'].color
                    }
                }
            }   
        self.State = Unwrapped
if __name__ == "__main__": 
    cube = Color_Cube()
    sleep(20)
    