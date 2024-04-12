# cube_heart.py
# A central framework and representation of a standard 3x3 Rubik's Cube
# Joey Goetz

from random import choice

class Cube:

    def __init__(self, config=None):
        """Initializes a 3x3 Rubik's Cube, setting the top face as white
        and the front face as red

        """
        self.face = {
            "Top": [
                ["W", "W", "W"],
                ["W", "W", "W"],
                ["W", "W", "W"]
                ],
            "Bottom": [
                ["Y", "Y", "Y"],
                ["Y", "Y", "Y"],
                ["Y", "Y", "Y"]
                ],
            "Left": [
                ["G", "G", "G"],
                ["G", "G", "G"],
                ["G", "G", "G"]
                ],
            "Right": [
                ["B", "B", "B"],
                ["B", "B", "B"],
                ["B", "B", "B"]
                ],
            "Front": [
                ["R", "R", "R"],
                ["R", "R", "R"],
                ["R", "R", "R"]
                ],
            "Back": [
                ["O", "O", "O"],
                ["O", "O", "O"],
                ["O", "O", "O"]
                ]
            }
        self.face_list = [face for face in self.face]
        self.move_list = [self.rotate_top_clockwise, self.rotate_top_counter_clockwise,
                          self.rotate_bottom_clockwise, self.rotate_bottom_counter_clockwise,
                          self.rotate_left_clockwise, self.rotate_left_counter_clockwise,
                          self.rotate_right_clockwise, self.rotate_right_counter_clockwise,
                          self.rotate_front_clockwise, self.rotate_front_counter_clockwise,
                          self.rotate_back_clockwise, self.rotate_back_counter_clockwise]
        self.notation_list = ['U', 'U\'', 'D', 'D\'', 'L', 'L\'', 'R', 'R\'', 'F', 'F\'', 'B', 'B\'']
        self.sequence_list = []
        if config:
            self.config_cube(config)

    def config_cube(self, config):
        """If an initial cube state is given, initializes the cube faces
        with that given state

        """
        front_list = []
        for item in config[0]:
            color = item[0].capitalize()
            front_list.append(color)
        front_list = [front_list[i:i+3] for i in range (0, len(front_list), 3)]
        self.face["Front"] = front_list

        right_list = []
        for item in config[1]:
            color = item[0].capitalize()
            right_list.append(color)
        right_list = [right_list[i:i+3] for i in range (0, len(right_list), 3)]
        self.face["Right"] = right_list

        back_list = []
        for item in config[2]:
            color = item[0].capitalize()
            back_list.append(color)
        back_list = [back_list[i:i+3] for i in range (0, len(back_list), 3)]
        self.face["Back"] = back_list

        left_list = []
        for item in config[3]:
            color = item[0].capitalize()
            left_list.append(color)
        left_list = [left_list[i:i+3] for i in range (0, len(left_list), 3)]
        self.face["Left"] = left_list

        bottom_list = []
        for item in config[4]:
            color = item[0].capitalize()
            bottom_list.append(color)
        bottom_list = [bottom_list[i:i+3] for i in range (0, len(bottom_list), 3)]
        self.face["Bottom"] = bottom_list

        top_list = []
        for item in config[5]:
            color = item[0].capitalize()
            top_list.append(color)
        top_list = [top_list[i:i+3] for i in range (0, len(top_list), 3)]
        top_list[1][1] = "W"
        self.face["Top"] = top_list

    def rotate_face_clockwise(self, face_name):
        """Takes a face as input and rotates the face colors clockwise

        """
        face = self.face[face_name]

        temp = face[0][0]
        face[0][0] = face[2][0]
        face[2][0] = face[2][2]
        face[2][2] = face[0][2]
        face[0][2] = temp

        temp = face[0][1]
        face[0][1] = face[1][0]
        face[1][0] = face[2][1]
        face[2][1] = face[1][2]
        face[1][2] = temp

    def rotate_face_counter_clockwise(self, face_name):
        """Takes a face as input and rotates the face colors counterclockwise

        """
        face = self.face[face_name]

        temp = face[0][0]
        face[0][0] = face[0][2]
        face[0][2] = face[2][2]
        face[2][2] = face[2][0]
        face[2][0] = temp

        temp = face[0][1]
        face[0][1] = face[1][2]
        face[1][2] = face[2][1]
        face[2][1] = face[1][0]
        face[1][0] = temp

    def rotate_top_clockwise(self):
        """Rotates the top face clockwise, accounting for adjacent squares
        Cubic notation: U

        """
        self.rotate_face_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Right"][0]
        self.face["Right"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Left"][0]
        self.face["Left"][0] = temp
        return 'U'

    def rotate_top_counter_clockwise(self):
        """Rotates the top face counterclockwise, accounting for adjacent squares
        Cubic notation: U'

        """
        self.rotate_face_counter_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Left"][0]
        self.face["Left"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Right"][0]
        self.face["Right"][0] = temp
        return 'U\''

    def rotate_bottom_clockwise(self):
        """Rotates the bottom face clockwise, accounting for adjacent squares
        Cubic notation: D

        """
        self.rotate_face_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp
        return 'D'

    def rotate_bottom_counter_clockwise(self):
        """Rotates the bottom face counterclockwise, accounting for adjacent squares
        Cubic notation: D'

        """
        self.rotate_face_counter_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Right"][2]
        self.face["Right"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Left"][2]
        self.face["Left"][2] = temp
        return 'D\''

    def rotate_left_clockwise(self):
        """Rotates the left face clockwise, accounting for adjacent squares
        Cubic notation: L

        """
        self.rotate_face_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]
        return 'L'

    def rotate_left_counter_clockwise(self):
        """Rotates the left face counterclockwise, accounting for adjacent squares
        Cubic notation: L'

        """
        self.rotate_face_counter_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = temp_col[i]
        return 'L\''

    def rotate_right_clockwise(self):
        """Rotates the right face clockwise, accounting for adjacent squares
        Cubic notation: R

        """
        self.rotate_face_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]
        return 'R'

    def rotate_right_counter_clockwise(self):
        """Rotates the right face counterclockwise, accounting for adjacent squares
        Cubic notation: R'

        """
        self.rotate_face_counter_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range (3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = temp_col[i]
        return 'R\''

    def rotate_front_clockwise(self):
        """Rotates the front face clockwise, accounting for adjacent squares
        Cubic notation: F

        """
        self.rotate_face_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Left"][2 - i][2]
            self.face["Left"][2 - i][2] = self.face["Bottom"][0][2 - i]
            self.face["Bottom"][0][2 - i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = temp[i]
        return 'F'

    def rotate_front_counter_clockwise(self):
        """Rotates the front face counterclockwise, accounting for adjacent squares
        Cubic notation: F'

        """
        self.rotate_face_counter_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = self.face["Bottom"][0][2 - i]
            self.face["Bottom"][0][2 - i] = self.face["Left"][2 - i][2]
            self.face["Left"][2 - i][2] = temp[i]
        return 'F\''

    def rotate_back_clockwise(self):
        """Rotates the back face clockwise, accounting for adjacent squares
        Cubic notation: B

        """
        self.rotate_face_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = self.face["Bottom"][2][2 - i]
            self.face["Bottom"][2][2 - i] = self.face["Left"][2 - i][0]
            self.face["Left"][2 - i][0] = temp[i]
        return 'B'

    def rotate_back_counter_clockwise(self):
        """Rotates the back face counterclockwise, accounting for adjacent squares
        Cubic notation: B'

        """
        self.rotate_face_counter_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Left"][2 - i][0]
            self.face["Left"][2 - i][0] = self.face["Bottom"][2][2 - i]
            self.face["Bottom"][2][2 - i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = temp[i]
        return 'B\''

    def move(self, move):
        """Makes a move on the cube based on input move in cubic notation
        
        """
        if move == 'U':
            self.rotate_top_clockwise()
            self.sequence_list.append(move)
        elif move == 'U\'':
            self.rotate_top_counter_clockwise()
            self.sequence_list.append(move)
        elif move == 'D':
            self.rotate_bottom_clockwise()
            self.sequence_list.append(move)
        elif move == 'D\'':
            self.rotate_bottom_counter_clockwise()
            self.sequence_list.append(move)
        elif move == 'L':
            self.rotate_left_clockwise()
            self.sequence_list.append(move)
        elif move == 'L\'':
            self.rotate_left_counter_clockwise()
            self.sequence_list.append(move)
        elif move == 'R':
            self.rotate_right_clockwise()
            self.sequence_list.append(move)
        elif move == 'R\'':
            self.rotate_right_counter_clockwise()
            self.sequence_list.append(move)
        elif move == 'F':
            self.rotate_front_clockwise()
            self.sequence_list.append(move)
        elif move == 'F\'':
            self.rotate_front_counter_clockwise()
            self.sequence_list.append(move)
        elif move == 'B':
            self.rotate_back_clockwise()
            self.sequence_list.append(move)
        elif move == 'B\'':
            self.rotate_back_counter_clockwise()
            self.sequence_list.append(move)
        else:
            print("Invalid move")

    def undo_move(self, move):
        """Undos the recent input move and removes it from the sequence list
        
        """
        if move == 'U':
            self.rotate_top_counter_clockwise()
            self.sequence_list.pop()
        elif move == 'U\'':
            self.rotate_top_clockwise()
            self.sequence_list.pop()
        elif move == 'D':
            self.rotate_bottom_counter_clockwise()
            self.sequence_list.pop()
        elif move == 'D\'':
            self.rotate_bottom_clockwise()
            self.sequence_list.pop()
        elif move == 'L':
            self.rotate_left_counter_clockwise()
            self.sequence_list.pop()
        elif move == 'L\'':
            self.rotate_left_clockwise()
            self.sequence_list.pop()
        elif move == 'R':
            self.rotate_right_counter_clockwise()
            self.sequence_list.pop()
        elif move == 'R\'':
            self.rotate_right_clockwise()
            self.sequence_list.pop()
        elif move == 'F':
            self.rotate_front_counter_clockwise()
            self.sequence_list.pop()
        elif move == 'F\'':
            self.rotate_front_clockwise()
            self.sequence_list.pop()
        elif move == 'B':
            self.rotate_back_counter_clockwise()
            self.sequence_list.pop()
        elif move == 'B\'':
            self.rotate_back_clockwise()
            self.sequence_list.pop()
        else:
            print("Invalid move")


    def scramble(self):
        """Loops through 20 random moves in order to properly scramble 
        the cube's state

        """
        self.face = {
            "Top": [
                ["W", "W", "W"],
                ["W", "W", "W"],
                ["W", "W", "W"]
                ],
            "Bottom": [
                ["Y", "Y", "Y"],
                ["Y", "Y", "Y"],
                ["Y", "Y", "Y"]
                ],
            "Left": [
                ["G", "G", "G"],
                ["G", "G", "G"],
                ["G", "G", "G"]
                ],
            "Right": [
                ["B", "B", "B"],
                ["B", "B", "B"],
                ["B", "B", "B"]
                ],
            "Front": [
                ["R", "R", "R"],
                ["R", "R", "R"],
                ["R", "R", "R"]
                ],
            "Back": [
                ["O", "O", "O"],
                ["O", "O", "O"],
                ["O", "O", "O"]
                ]
            }
        for i in range(25):
            choice(self.move_list)()

    def is_solved(self):
        """Returns a boolean value based on whether or not the cube is 
        in a solved state

        """
        for face in self.face_list:
            colors = self.face[face]
            testcolor = colors[0][0]
            for i in range(3):
                for j in range(3):
                    if testcolor == colors[i][j]:
                        pass
                    else:
                        return False
        return True
            
    def get_face(self, face):
        """Returns the configuration of input face

        """
        content = f"---| {face} |---\n"
        for row in self.face[face]:
            content += f"\n| {row[0]} | {row[1]} | {row[2]} |\n"
        return content
    
    def get_cube(self):
        """Returns the configuration of the entire cube

        """
        return self.face
    
    def print_cube(self):
        """Prints the configuration of each face of the cube

        """
        for face in self.face_list:
            print(self.get_face(face))

    def get_cubestate(self):
        """Returns the configuration of the cube in a list of lists format

        """
        cubestate = []
        front = []
        for row in self.face["Front"]:
            for color in row:
                front.append(color)
        cubestate.append(front)
        right = []
        for row in self.face["Right"]:
            for color in row:
                right.append(color)
        cubestate.append(right)
        back = []
        for row in self.face["Back"]:
            for color in row:
                back.append(color)
        cubestate.append(back)
        left = []
        for row in self.face["Left"]:
            for color in row:
                left.append(color)
        cubestate.append(left)
        bottom = []
        for row in self.face["Bottom"]:
            for color in row:
                bottom.append(color)
        cubestate.append(bottom)
        top = []
        for row in self.face["Top"]:
            for color in row:
                top.append(color)
        cubestate.append(top)
        return cubestate