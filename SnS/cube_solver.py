# cube_solver.py
# A program that solves a cube generated from cube_heart.py
# Joey Goetz

from cube_heart import Cube

class CubeSolver:

    def __init__(self, cube):
        """Initializes a cube solver with input cube's state

        
        """
        self.original_cube = cube
        self.cube = Cube(cube.get_cubestate())
        self.movelist = []
        self.movecount = len(self.movelist)

    def solve_cross_adjacent(self):
        """Helper function to ensure each piece of the white cross matches
        its corresponding adjacent face
        
        """
        self.cube.move('F')
        self.cube.move('F')
        self.cube.move('L')
        self.cube.move('L')
        self.cube.move('R')
        self.cube.move('R')
        self.cube.move('B')
        self.cube.move('B')
        while self.cube.face["Front"][2][1] != 'R' or self.cube.face["Bottom"][0][1] != 'W':
            self.cube.move('D')
        self.cube.move('F')
        self.cube.move('F')
        while self.cube.face["Left"][2][1] != 'G' or self.cube.face["Bottom"][1][0] != 'W':
            self.cube.move('D')
        self.cube.move('L')
        self.cube.move('L')
        while self.cube.face["Right"][2][1] != 'B' or self.cube.face["Bottom"][1][2] != 'W':
            self.cube.move('D')
        self.cube.move('R')
        self.cube.move('R')
        while self.cube.face["Back"][2][1] != 'O' or self.cube.face["Bottom"][2][1] != 'W':
            self.cube.move('D')
        self.cube.move('B')
        self.cube.move('B')
        
        
    def solve_cross(self):
        """Performs the first step of CFOP by solving the white cross
        systematically
        
        """
        if self.cube.face["Top"][0][1] == 'W' and self.cube.face["Top"][1][0] == 'W' and self.cube.face["Top"][1][2] == 'W' and self.cube.face["Top"][2][1] == 'W':
            if self.cube.face["Front"][0][1] == 'R' and self.cube.face["Right"][0][1] == 'B' and self.cube.face["Back"][0][1] == 'O' and self.cube.face["Left"][0][1] == 'G':
                return
            else:
                self.solve_cross_adjacent()
        else:
            while True:
                if self.cube.face["Front"][0][1] == 'W':
                    self.cube.move('F')
                    self.cube.move('F')
                    self.cube.move('D')
                    while self.cube.face["Top"][2][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('R')
                    self.cube.move('F\'')
                if self.cube.face["Front"][1][0] == 'W':
                    while self.cube.face["Top"][2][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    while self.cube.face["Top"][2][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('R')
                    self.cube.move('F\'')
                if self.cube.face["Front"][1][2] == 'W':
                    while self.cube.face["Top"][2][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('F')
                    self.cube.move('D')
                    while self.cube.face["Top"][2][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('R')
                    self.cube.move('F\'')
                if self.cube.face["Front"][2][1] == 'W':
                    while self.cube.face["Top"][2][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('D')
                    while self.cube.face["Top"][2][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('R')
                    self.cube.move('F\'')

                if self.cube.face["Right"][0][1] == 'W':
                    self.cube.move('R')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    while self.cube.face["Top"][1][2] == 'W':
                        self.cube.move('U')
                    self.cube.move('U')
                    self.cube.move('F\'')
                    self.cube.move('U\'')
                    self.cube.move('R')
                if self.cube.face["Right"][1][0] == 'W':
                    while self.cube.face["Top"][1][2] == 'W':
                        self.cube.move('U')
                    self.cube.move('R\'')
                    self.cube.move('D\'')
                    while self.cube.face["Top"][1][2] == 'W':
                        self.cube.move('U')
                    self.cube.move('U')
                    self.cube.move('F\'')
                    self.cube.move('U\'')
                    self.cube.move('R')
                if self.cube.face["Right"][1][2] == 'W':
                    while self.cube.face["Top"][1][2] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    while self.cube.face["Top"][1][2] == 'W':
                        self.cube.move('U')
                    self.cube.move('U')
                    self.cube.move('F\'')
                    self.cube.move('U\'')
                    self.cube.move('R')
                if self.cube.face["Right"][2][1] == 'W':
                    self.cube.move('D\'')
                    while self.cube.face["Top"][1][2] == 'W':
                        self.cube.move('U')
                    self.cube.move('U')
                    self.cube.move('F\'')
                    self.cube.move('U\'')
                    self.cube.move('R')

                if self.cube.face["Back"][0][1] == 'W':
                    self.cube.move('B')
                    self.cube.move('B')
                    self.cube.move('D')
                    while self.cube.face["Top"][0][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('L')
                    self.cube.move('B\'')
                    self.cube.move('L\'')
                if self.cube.face["Back"][1][0] == 'W':
                    while self.cube.face["Top"][0][1] == 'W':
                        self.cube.move('U')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    while self.cube.face["Top"][0][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('L')
                    self.cube.move('B\'')
                    self.cube.move('L\'')
                if self.cube.face["Back"][1][2] == 'W':
                    while self.cube.face["Top"][0][1] == 'W':
                        self.cube.move('U')
                    self.cube.move('B')
                    self.cube.move('D')
                    while self.cube.face["Top"][0][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('L')
                    self.cube.move('B\'')
                    self.cube.move('L\'')
                if self.cube.face["Back"][2][1] == 'W':
                    self.cube.move('D')
                    while self.cube.face["Top"][0][1] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('L')
                    self.cube.move('B\'')
                    self.cube.move('L\'')

                if self.cube.face["Left"][0][1] == 'W':
                    self.cube.move('L')
                    self.cube.move('L')
                    self.cube.move('D')
                    while self.cube.face["Top"][1][0] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('F')
                    self.cube.move('U')
                    self.cube.move('L\'')
                if self.cube.face["Left"][1][0] == 'W':
                    while self.cube.face["Top"][1][0] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    while self.cube.face["Top"][1][0] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('F')
                    self.cube.move('U')
                    self.cube.move('L\'')
                if self.cube.face["Left"][1][2] == 'W':
                    while self.cube.face["Top"][1][0] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('L')
                    self.cube.move('D')
                    while self.cube.face["Top"][1][0] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('F')
                    self.cube.move('U')
                    self.cube.move('L\'')
                if self.cube.face["Left"][2][1] == 'W':
                    self.cube.move('D')
                    while self.cube.face["Top"][1][0] == 'W':
                        self.cube.move('U\'')
                    self.cube.move('U\'')
                    self.cube.move('F')
                    self.cube.move('U')
                    self.cube.move('L\'')

                if self.cube.face["Bottom"][0][1] == 'W':
                    while self.cube.face["Top"][2][1] == 'W':
                        self.cube.move('U')
                    self.cube.move('F')
                    self.cube.move('F')
                if self.cube.face["Bottom"][1][0] == 'W':
                    while self.cube.face["Top"][1][0] == 'W':
                        self.cube.move('U')
                    self.cube.move('L')
                    self.cube.move('L')
                if self.cube.face["Bottom"][1][2] == 'W':
                    while self.cube.face["Top"][1][2] == 'W':
                        self.cube.move('U')
                    self.cube.move('R')
                    self.cube.move('R')
                if self.cube.face["Bottom"][2][1] == 'W':
                    while self.cube.face["Top"][0][1] == 'W':
                        self.cube.move('U')
                    self.cube.move('B')
                    self.cube.move('B')
                if self.cube.face["Top"][0][1] == 'W' and self.cube.face["Top"][1][0] == 'W' and self.cube.face["Top"][1][2] == 'W' and self.cube.face["Top"][2][1] == 'W':
                    break
            self.solve_cross_adjacent()

    def solve_white_corners(self):
        """Performs the first step of F2L by solving for the white corners

        Hard codes 96 algorithms to account for every possible position
        of each white corner, implementing the correct set of moves
        to put them each in place

        """
        while True:
            if self.cube.face["Front"][0][0] == 'W':
                if self.cube.face["Top"][2][0] == 'G':
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                elif self.cube.face["Top"][2][0] == 'O':
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                elif self.cube.face["Top"][2][0] == 'B':
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Top"][2][0] == 'R':
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('F')
                    self.cube.move('D\'')
                    self.cube.move('F\'')
                    
            if self.cube.face["Front"][0][2] == 'W':
                if self.cube.face["Top"][2][2] == 'G':
                    self.cube.move('F')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F\'')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')
                elif self.cube.face["Top"][2][2] == 'R':
                    self.cube.move('F')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F\'')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
                elif self.cube.face["Top"][2][2] == 'O':
                    self.cube.move('F')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')
                elif self.cube.face["Top"][2][2] == 'B':
                    self.cube.move('F')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')

            if self.cube.face["Front"][2][0] == 'W':
                if self.cube.face["Bottom"][0][0] == 'O':
                    self.cube.move('D\'')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Bottom"][0][0] == 'G':
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                elif self.cube.face["Bottom"][0][0] == 'R':
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                elif self.cube.face["Bottom"][0][0] == 'B':
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('D\'')
                    self.cube.move('F\'')


            if self.cube.face["Front"][2][2] == 'W':
                if self.cube.face["Bottom"][0][2] == 'G':
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
                elif self.cube.face["Bottom"][0][2] == 'B':
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')
                elif self.cube.face["Bottom"][0][2] == 'R':
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
                elif self.cube.face["Bottom"][0][2] == 'O':
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')

            if self.cube.face["Right"][0][0] == 'W':
                if self.cube.face["Top"][2][2] == 'B':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Top"][2][2] == 'G':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('D\'')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                elif self.cube.face["Top"][2][2] == 'O':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                elif self.cube.face["Top"][2][2] == 'R':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('F')
                    self.cube.move('D\'')
                    self.cube.move("F\'")

            if self.cube.face["Right"][0][2] == 'W':
                if self.cube.face["Top"][0][2] == 'O':
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')
                elif self.cube.face["Top"][0][2] == 'G':
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')
                elif self.cube.face["Top"][0][2] == 'R':
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D\'')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
                elif self.cube.face["Top"][0][2] == 'B':
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')

            if self.cube.face["Right"][2][0] == 'W':
                if self.cube.face["Bottom"][0][2] == 'O':
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Bottom"][0][2] == 'G':
                    self.cube.move('D\'')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                elif self.cube.face["Bottom"][0][2] == 'R':
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                elif self.cube.face["Bottom"][0][2] == 'B':
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('D\'')
                    self.cube.move('F\'')

            if self.cube.face["Right"][2][2] == 'W':
                if self.cube.face["Bottom"][2][2] == 'B':
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')
                elif self.cube.face["Bottom"][2][2] == 'O':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')
                elif self.cube.face["Bottom"][2][2] == 'R':
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
                elif self.cube.face["Bottom"][2][2] == 'G':
                    self.cube.move('D')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')

            if self.cube.face["Back"][0][0] == 'W':
                if self.cube.face["Top"][0][2] == 'B':
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Top"][0][2] == 'R':
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('D\'')
                    self.cube.move('F\'')
                elif self.cube.face["Top"][0][2] == 'O':
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                elif self.cube.face["Top"][0][2] == 'G':
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')

            if self.cube.face["Back"][0][2] == 'W':
                if self.cube.face["Top"][0][0] == 'O':
                    self.cube.move('B')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B\'')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')
                elif self.cube.face["Top"][0][0] == 'G':
                    self.cube.move('B')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')
                elif self.cube.face["Top"][0][0] == 'R':
                    self.cube.move('B')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
                elif self.cube.face["Top"][0][0] == 'B':
                    self.cube.move('B')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B\'')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
            if self.cube.face["Back"][2][0] == 'W':
                if self.cube.face["Bottom"][2][2] == 'G':
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                elif self.cube.face["Bottom"][2][2] == 'O':
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Bottom"][2][2] == 'B':
                    self.cube.move('F')
                    self.cube.move('D')
                    self.cube.move('F\'')
                elif self.cube.face["Bottom"][2][2] == 'R':
                    self.cube.move('D\'')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
            if self.cube.face["Back"][2][2] == 'W':
                if self.cube.face["Bottom"][2][0] == 'O':
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')
                elif self.cube.face["Bottom"][2][0] == 'G':
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
                elif self.cube.face["Bottom"][2][0] == 'R':
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
                elif self.cube.face["Bottom"][2][0] == 'B':
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')

            if self.cube.face["Left"][0][0] == 'W':
                if self.cube.face["Top"][0][0] == 'R':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('D\'')
                    self.cube.move('F\'')
                elif self.cube.face["Top"][0][0] == 'G':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                elif self.cube.face["Top"][0][0] == 'B':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Top"][0][0] == 'O':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
            if self.cube.face["Left"][0][2] == 'W':
                if self.cube.face["Top"][2][0] == 'G':
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')
                elif self.cube.face["Top"][2][0] == 'R':
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
                elif self.cube.face["Top"][2][0] == 'B':
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
                elif self.cube.face["Top"][2][0] == 'O':
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')

            if self.cube.face["Left"][2][0] == 'W':
                if self.cube.face["Bottom"][2][0] == 'R':
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                elif self.cube.face["Bottom"][2][0] == 'B':
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('D')
                    self.cube.move('F\'')
                elif self.cube.face["Bottom"][2][0] == 'O':
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Bottom"][2][0] == 'G':
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'') 
            if self.cube.face["Left"][2][2] == 'W':
                if self.cube.face["Bottom"][0][0] == 'R':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
                elif self.cube.face["Bottom"][0][0] == 'G':
                    self.cube.move('D\'')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
                elif self.cube.face["Bottom"][0][0] == 'B':
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
                elif self.cube.face["Bottom"][0][0] == 'O':
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')

            if self.cube.face["Bottom"][0][0] == 'W':
                if self.cube.face["Front"][2][0] == 'R':
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
                elif self.cube.face["Front"][2][0] == 'B':
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')
                elif self.cube.face["Front"][2][0] == 'O':
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')
                elif self.cube.face["Front"][2][0] == 'G':
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
                    self.cube.move('D\'')
                    self.cube.move('D\'')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
            if self.cube.face["Bottom"][0][2] == 'W':
                if self.cube.face["Front"][2][2] == 'B':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('F')
                    self.cube.move('D\'')
                    self.cube.move('F\'')
                elif self.cube.face["Front"][2][2] == 'R':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                elif self.cube.face["Front"][2][2] == 'G':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                elif self.cube.face["Front"][2][2] == 'O':
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')


            if self.cube.face["Bottom"][2][0] == 'W':
                if self.cube.face["Back"][2][2] == 'G':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B')
                    self.cube.move('D\'')
                    self.cube.move('B\'')
                elif self.cube.face["Back"][2][2] == 'R':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                elif self.cube.face["Back"][2][2] == 'O':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('R')
                    self.cube.move('D\'')
                    self.cube.move('R\'')
                elif self.cube.face["Back"][2][2] == 'B':
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
                    self.cube.move('F')
                    self.cube.move('D\'')
                    self.cube.move('F\'')
            if self.cube.face["Bottom"][2][2] == 'W':
                if self.cube.face["Back"][2][0] == 'G':
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('F\'')
                    self.cube.move('D')
                    self.cube.move('F')
                elif self.cube.face["Back"][2][0] == 'B':
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('B\'')
                    self.cube.move('D')
                    self.cube.move('B')
                elif self.cube.face["Back"][2][0] == 'R':
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('R')
                elif self.cube.face["Back"][2][0] == 'O':
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
                    self.cube.move('D\'')
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('L')



            if self.cube.face["Top"][0][0] == 'W':
                if self.cube.face['Left'][0][0] == 'G':
                    pass
                else:
                    self.cube.move('L\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L')
            if self.cube.face["Top"][0][2] == 'W':
                if self.cube.face["Right"][0][2] == 'B':
                    pass
                else:
                    self.cube.move('R')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R\'')
            if self.cube.face["Top"][2][0] == 'W':
                if self.cube.face["Left"][0][2] == 'G':
                    pass
                else:
                    self.cube.move('L')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('L\'')
            if self.cube.face["Top"][2][2] == 'W':
                if self.cube.face["Right"][0][0] == 'B':
                    pass
                else:
                    self.cube.move('R\'')
                    self.cube.move('D')
                    self.cube.move('D')
                    self.cube.move('R')


            if self.cube.face["Top"][0][0] == 'W' and self.cube.face["Left"][0][0] == 'G' and self.cube.face["Back"][0][2] == 'O':
                if self.cube.face["Top"][0][2] == 'W' and self.cube.face["Right"][0][2] == 'B' and self.cube.face["Back"][0][0] == 'O':
                    if self.cube.face["Top"][2][0] == 'W' and self.cube.face["Left"][0][2] == 'G' and self.cube.face["Front"][0][0] == 'R':
                        if self.cube.face["Top"][2][2] == 'W' and self.cube.face["Right"][0][0] == 'B' and self.cube.face["Front"][0][2] == 'R':
                            break
    
    def redleft(self):
        """F2L helper function to move a red edge to the left side
        
        """
        self.cube.move('D\'')
        self.cube.move('R\'')
        self.cube.move('D')
        self.cube.move('R')
        self.cube.move('D')
        self.cube.move('F')
        self.cube.move('D\'')
        self.cube.move('F\'')
    
    def redright(self):
        """F2L helper function to move a red edge to the right side
        
        """
        self.cube.move('D')
        self.cube.move('L')
        self.cube.move('D\'')
        self.cube.move('L\'')
        self.cube.move('D\'')
        self.cube.move('F\'')
        self.cube.move('D')
        self.cube.move('F')

    def greenleft(self):
        """F2L helper function to move a green edge to the left side
        
        """
        self.cube.move('D\'')
        self.cube.move('F\'')
        self.cube.move('D')
        self.cube.move('F')
        self.cube.move('D')
        self.cube.move('L')
        self.cube.move('D\'')
        self.cube.move('L\'')

    def greenright(self):
        """F2L helper function to move a green edge to the right side
        
        """
        self.cube.move('D')
        self.cube.move('B')
        self.cube.move('D\'')
        self.cube.move('B\'')
        self.cube.move('D\'')
        self.cube.move('L\'')
        self.cube.move('D')
        self.cube.move('L')

    def orangeleft(self):
        """F2L helper function to move an orange edge to the left side
        
        """
        self.cube.move('D\'')
        self.cube.move('L\'')
        self.cube.move('D')
        self.cube.move('L')
        self.cube.move('D')
        self.cube.move('B')
        self.cube.move('D\'')
        self.cube.move('B\'')

    def orangeright(self):
        """F2L helper function to move an orange edge to the right side
        
        """
        self.cube.move('D')
        self.cube.move('R')
        self.cube.move('D\'')
        self.cube.move('R\'')
        self.cube.move('D\'')
        self.cube.move('B\'')
        self.cube.move('D')
        self.cube.move('B')

    def blueleft(self):
        """F2L helper function to move a blue edge to the left side
        
        """
        self.cube.move('D\'')
        self.cube.move('B\'')
        self.cube.move('D')
        self.cube.move('B')
        self.cube.move('D')
        self.cube.move('R')
        self.cube.move('D\'')
        self.cube.move('R\'')

    def blueright(self):
        """F2L helper function to move a blue edge to the right side
        
        """
        self.cube.move('D')
        self.cube.move('F')
        self.cube.move('D\'')
        self.cube.move('F\'')
        self.cube.move('D\'')
        self.cube.move('R\'')
        self.cube.move('D')
        self.cube.move('R')

    def solve_f2l_edges(self):
        """Performs the second step in F2L by solving each edge on the
        second layer using the above helper functions
        
        """
        while True:
            for i in range(4):
                if self.cube.face["Front"][2][1] == 'R':
                    if self.cube.face["Bottom"][0][1] == 'G':
                        self.redright()
                    elif self.cube.face["Bottom"][0][1] == 'B':
                        self.redleft()
                if self.cube.face["Left"][2][1] == 'G':
                    if self.cube.face["Bottom"][1][0] == 'O':
                        self.greenright()
                    elif self.cube.face["Bottom"][1][0] == 'R':
                        self.greenleft()
                if self.cube.face["Back"][2][1] == 'O':
                    if self.cube.face["Bottom"][2][1] == 'B':
                        self.orangeright()
                    elif self.cube.face["Bottom"][2][1] == 'G':
                        self.orangeleft()
                if self.cube.face["Right"][2][1] == 'B':
                    if self.cube.face["Bottom"][1][2] == 'R':
                        self.blueright()
                    elif self.cube.face["Bottom"][1][2] == 'O':
                        self.blueleft()
                self.cube.move('D')

            if self.cube.face["Left"][1][2] == 'B' or self.cube.face["Left"][1][2] == 'O' or self.cube.face["Left"][1][2] == 'R':
                self.greenleft()
            elif self.cube.face["Left"][1][0] == 'B' or self.cube.face["Left"][1][0] == 'O' or self.cube.face["Left"][1][0] == 'R':
                self.greenright()
            elif self.cube.face["Right"][1][2] == 'G' or self.cube.face["Right"][1][2] == 'O' or self.cube.face["Right"][1][2] == 'R':
                self.blueleft()
            elif self.cube.face["Right"][1][0] == 'G' or self.cube.face["Right"][1][0] == 'O' or self.cube.face["Right"][1][0] == 'R':
                self.blueright()
            elif self.cube.face["Front"][1][2] == 'B' or self.cube.face["Front"][1][2] == 'O' or self.cube.face["Front"][1][2] == 'G':
                self.redleft()
            elif self.cube.face["Front"][1][0] == 'B' or self.cube.face["Front"][1][0] == 'O' or self.cube.face["Front"][1][0] == 'G':
                self.redright()
            elif self.cube.face["Back"][1][2] == 'B' or self.cube.face["Back"][1][2] == 'G' or self.cube.face["Back"][1][2] == 'R':
                self.orangeleft()
            elif self.cube.face["Back"][1][0] == 'B' or self.cube.face["Back"][1][0] == 'G' or self.cube.face["Back"][1][0] == 'R':
                self.orangeright()

            if self.cube.face["Front"][1][0] == 'R' and self.cube.face["Front"][1][2] == 'R':
                if self.cube.face["Right"][1][0] == 'B' and self.cube.face["Right"][1][2] == 'B':
                    if self.cube.face["Back"][1][0] == 'O' and self.cube.face["Back"][1][2] == 'O':
                        if self.cube.face["Left"][1][0] == 'G' and self.cube.face["Left"][1][2] == 'G':
                            break

    def solve_f2l(self):
        """Peforms both steps of the F2L process, ending with the first
        two layers being completely solved
        
        """
        self.solve_white_corners()
        self.solve_f2l_edges()

    def solve_yellow_edges(self):
        """Performs the first step in the OLL process, solving for each
        yellow edge
        
        """
        while True:
            if self.cube.face["Bottom"][0][1] == 'Y' and self.cube.face["Bottom"][1][0] == 'Y' and self.cube.face["Bottom"][1][2] == 'Y' and self.cube.face["Bottom"][2][1] == 'Y':
                break

            if self.cube.face["Bottom"][0][1] == 'Y' and self.cube.face["Bottom"][1][0] != 'Y' and self.cube.face["Bottom"][1][2] != 'Y' and self.cube.face["Bottom"][2][1] == 'Y':
                self.cube.move('D')
            elif self.cube.face["Bottom"][0][1] != 'Y' and self.cube.face["Bottom"][1][0] == 'Y' and self.cube.face["Bottom"][1][2] == 'Y' and self.cube.face["Bottom"][2][1] != 'Y':
                self.cube.move('F')
                self.cube.move('L')
                self.cube.move('D')
                self.cube.move('L\'')
                self.cube.move('D\'')
                self.cube.move('F\'')
            elif self.cube.face["Bottom"][0][1] == 'Y' and self.cube.face["Bottom"][1][0] != 'Y' and self.cube.face["Bottom"][1][2] == 'Y' and self.cube.face["Bottom"][2][1] != 'Y':
                self.cube.move('D')
            elif self.cube.face["Bottom"][0][1] != 'Y' and self.cube.face["Bottom"][1][0] == 'Y' and self.cube.face["Bottom"][1][2] != 'Y' and self.cube.face["Bottom"][2][1] == 'Y':
                self.cube.move('D\'')
            elif self.cube.face["Bottom"][0][1] != 'Y' and self.cube.face["Bottom"][1][0] != 'Y' and self.cube.face["Bottom"][1][2] == 'Y' and self.cube.face["Bottom"][2][1] == 'Y':
                self.cube.move('D')
                self.cube.move('D')
            elif self.cube.face["Bottom"][0][1] == 'Y' and self.cube.face["Bottom"][1][0] == 'Y' and self.cube.face["Bottom"][1][2] != 'Y' and self.cube.face["Bottom"][2][1] != 'Y':
                self.cube.move('F')
                self.cube.move('L')
                self.cube.move('D')
                self.cube.move('L\'')
                self.cube.move('D\'')
                self.cube.move('F\'')
            else:
                self.cube.move('F')
                self.cube.move('L')
                self.cube.move('D')
                self.cube.move('L\'')
                self.cube.move('D\'')
                self.cube.move('F\'')

    def solve_yellow_corners(self):
        """Performs the second step in the OLL process, solving for each
        yellow corner
        
        """
        while True:
            if self.cube.face["Bottom"][0][0] == 'Y' and self.cube.face["Bottom"][0][2] == 'Y' and self.cube.face["Bottom"][2][0] == 'Y' and self.cube.face["Bottom"][2][2] == 'Y':
                break

            elif self.cube.face["Bottom"][0][0] != 'Y' and self.cube.face["Bottom"][0][2] == 'Y' and self.cube.face["Bottom"][2][0] != 'Y' and self.cube.face["Bottom"][2][2] != 'Y':
                self.cube.move('D\'')
            elif self.cube.face["Bottom"][0][0] != 'Y' and self.cube.face["Bottom"][0][2] != 'Y' and self.cube.face["Bottom"][2][0] == 'Y' and self.cube.face["Bottom"][2][2] != 'Y':
                self.cube.move('D')
            elif self.cube.face["Bottom"][0][0] != 'Y' and self.cube.face["Bottom"][0][2] != 'Y' and self.cube.face["Bottom"][2][0] != 'Y' and self.cube.face["Bottom"][2][2] == 'Y':
                self.cube.move('D')
                self.cube.move('D')
            elif self.cube.face["Bottom"][0][0] == 'Y' and self.cube.face["Bottom"][0][2] != 'Y' and self.cube.face["Bottom"][2][0] != 'Y' and self.cube.face["Bottom"][2][2] != 'Y':
                self.cube.move('L\'')
                self.cube.move('D')
                self.cube.move('D')
                self.cube.move('L')
                self.cube.move('D')
                self.cube.move('L\'')
                self.cube.move('D')
                self.cube.move('L')
            else:
                while self.cube.face["Front"][2][0] != 'Y':
                    self.cube.move('D')
                self.cube.move('L\'')
                self.cube.move('D')
                self.cube.move('D')
                self.cube.move('L')
                self.cube.move('D')
                self.cube.move('L\'')
                self.cube.move('D')
                self.cube.move('L')

    def solve_oll(self):
        """Peforms both steps of the OLL process, ending up with the
        yellow face being solved
        
        """
        self.solve_yellow_edges()
        self.solve_yellow_corners()

    def headlights_alg(self):
        """Helper function for the PLL process, adds "headlights" to the
        last layer of the cube (matching corners)
        
        """
        self.cube.move('L\'')
        self.cube.move('F')
        self.cube.move('L\'')
        self.cube.move('B')
        self.cube.move('B')
        self.cube.move('L')
        self.cube.move('F\'')
        self.cube.move('L\'')
        self.cube.move('B')
        self.cube.move('B')
        self.cube.move('L')
        self.cube.move('L')

    def solve_headlights(self):
        """Performs first step of the PLL process, ending with all but
        the final edges in the last layer being solved
        
        """
        while True:
            if self.cube.face["Front"][2][0] == self.cube.face["Front"][2][2]:
                if self.cube.face["Right"][2][0] == self.cube.face["Right"][2][2]:
                    if self.cube.face["Back"][2][0] == self.cube.face["Back"][2][2]:
                        if self.cube.face["Left"][2][0] == self.cube.face["Left"][2][2]:
                            break

            if self.cube.face["Front"][2][0] == self.cube.face["Front"]:
                    self.cube.move('D')
                    self.cube.move('D')
                    self.headlights_alg()
            elif self.cube.face["Right"][2][0] == self.cube.face["Right"][2][2]:
                self.cube.move('D')
                self.headlights_alg()
            elif self.cube.face["Left"][2][0] == self.cube.face["Left"][2][2]:
                self.cube.move('D\'')
                self.headlights_alg()
            elif self.cube.face["Back"][2][0] == self.cube.face["Back"][2][2]:
                self.headlights_alg()
            else:
                self.headlights_alg()

    def cycle_alg(self):
        """Helper function for the final permutation algorithm
        
        """
        self.cube.move('L')
        self.cube.move('D\'')
        self.cube.move('L')
        self.cube.move('D')
        self.cube.move('L')
        self.cube.move('D')
        self.cube.move('L')
        self.cube.move('D\'')
        self.cube.move('L\'')
        self.cube.move('D\'')
        self.cube.move('L')
        self.cube.move('L')

    def solve_final_permutation(self):
        """Cycles the edges in the last layer, ends with a solved cube
        
        """
        while True:
            if self.cube.face["Front"][2][0] == self.cube.face["Front"][2][1] == self.cube.face["Front"][2][2]:
                if self.cube.face["Right"][2][0] == self.cube.face["Right"][2][1] == self.cube.face["Right"][2][2]:
                    if self.cube.face["Back"][2][0] == self.cube.face["Back"][2][1] == self.cube.face["Back"][2][2]:
                        if self.cube.face["Left"][2][0] == self.cube.face["Left"][2][1] == self.cube.face["Left"][2][2]:
                            break
            if self.cube.face["Front"][2][0] == self.cube.face["Front"][2][1] == self.cube.face["Front"][2][2]:
                self.cube.move('D')
                self.cube.move('D')
                self.cycle_alg()
            elif self.cube.face["Right"][2][0] == self.cube.face["Right"][2][1] == self.cube.face["Right"][2][2]:
                self.cube.move('D')
                self.cycle_alg()
            elif self.cube.face["Back"][2][0] == self.cube.face["Back"][2][1] == self.cube.face["Back"][2][2]:
                self.cycle_alg()
            elif self.cube.face["Left"][2][0] == self.cube.face["Left"][2][1] == self.cube.face["Left"][2][2]:
                self.cube.move('D\'')
                self.cycle_alg()
            else:
                self.cycle_alg()
        while not self.cube.is_solved():
            self.cube.move('D')

            

    def solve_pll(self):
        """Performs both of the steps in the PLL process, ending with
        a solved cube
        
        """
        self.solve_headlights()
        self.solve_final_permutation()


    def solve_cube(self):
        """Performs each step of the CFOP method, returning the sequence
        list to solve input cube
        
        """
        self.cube.sequence_list.append("Cross:\n")
        self.solve_cross()
        self.cube.sequence_list.append("\n\nF2L:\n")
        self.solve_f2l()
        self.cube.sequence_list.append("\n\nOLL:\n")
        self.solve_oll()
        self.cube.sequence_list.append("\n\nPLL:\n")
        self.solve_pll()
        return self.cube.sequence_list