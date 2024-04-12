# sns.py
# A master program for scanning, initializing, and solving a Rubik's Cube
# Joey Goetz

from cube_heart import Cube
from cube_solver import CubeSolver
import tkinter as tk
import rcv

class SNS:

    def __init__(self):
        """Initializes a Tkinter interface with buttons to scan, show, solve
        and reset
        
        """
        self.cube = Cube()
        self.cubestate = self.cube.get_cubestate()

        self.color_map = {
            "R": "red",
            "B": "blue",
            "O": "orange",
            "G": "green",
            "Y": "yellow",
            "W": "white"
        }
        
        self.root = tk.Tk()
        self.root.title("Sim and Solve")
        self.root.geometry("720x480")

        self.bg_color = "light gray"
        self.root.configure(bg=self.bg_color)

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.grid(row=0, column=0, sticky="nsew")

        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)
        button_frame.grid_columnconfigure(3, weight=1)
        
        button_width = 20
        button_height = 3
        self.button_color = "light blue"

        scan_button = tk.Button(button_frame, text="Scan", command=self.scan_action, width=button_width, height=button_height, bg=self.button_color)
        scan_button.grid(row=0, column=0, pady=15, padx=10)
        scan_button.bind("<Enter>", self.button_enter)
        scan_button.bind("<Leave>", self.button_leave)

        show_button = tk.Button(button_frame, text="Show", command=self.show_action, width=button_width, height=button_height, bg=self.button_color)
        show_button.grid(row=0, column=1, pady=15, padx=10)
        show_button.bind("<Enter>", self.button_enter)
        show_button.bind("<Leave>", self.button_leave)

        solve_button = tk.Button(button_frame, text="Solve", command=self.solve_action, width=button_width, height=button_height, bg=self.button_color)
        solve_button.grid(row=0, column=2, pady=15, padx=10)
        solve_button.bind("<Enter>", self.button_enter)
        solve_button.bind("<Leave>", self.button_leave)

        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_action, width=button_width, height=button_height, bg=self.button_color)
        reset_button.grid(row=0, column=3, pady=15, padx=10)
        reset_button.bind("<Enter>", self.button_enter)
        reset_button.bind("<Leave>", self.button_leave)

        self.face_frame_container = tk.Frame(self.root, bg=self.bg_color)
        self.face_frame_container.grid(row=1, column=0, pady=20)

        self.move_buttons_frame = None
        self.move_buttons_displayed = False

        self.root.mainloop()

    def button_enter(self, event):
        """Config to sink a button when it's hovered over
        
        """
        event.widget.config(relief=tk.SUNKEN)

    def button_leave(self, event):
        """Config to raise a button when it's not hovered over
        
        """
        event.widget.config(relief=tk.RAISED)

    def scan_action(self):
        """Config for the scan button, implementing RCV to get the cube
        faces
        
        """
        print("Scan button clicked")
        self.cubestate = rcv.main()
        self.cube = Cube(self.cubestate)
        self.update_faces()

    def show_action(self):
        """Config for the show button
        Shows cube faces if clicked once, vanishes them if clicked again
        
        """
        print("Show button clicked")
        if hasattr(self, "face_frames"):
            for face_frame in self.face_frames:
                face_frame.destroy()
            del self.face_frames
            
            if self.move_buttons_displayed:
                self.move_buttons_frame.destroy()
                self.move_buttons_displayed = False
            return
        self.update_faces()

    def update_faces(self):
        """Updates and displays the cube faces according to the current 
        cube state
        
        """
        self.root.grid_rowconfigure(2, weight=1)
        if hasattr(self, "face_frames"):
            for face_frame in self.face_frames:
                face_frame.destroy()

        self.face_frames = []
        for i, (face, label_text) in enumerate(zip(self.cubestate, ["Front", "Right", "Back", "Left", "Bottom", "Top"])):
            face_frame = tk.Frame(self.face_frame_container, bg=self.bg_color)
            if i == 0: 
                face_frame.grid(row=1, column=1, padx=20)
            elif i == 1: 
                face_frame.grid(row=1, column=2, padx=20)
            elif i == 2: 
                face_frame.grid(row=1, column=3, padx=20)
            elif i == 3: 
                face_frame.grid(row=1, column=0, padx=20)
            elif i == 4: 
                face_frame.grid(row=2, column=1, padx=20)
            elif i == 5: 
                face_frame.grid(row=0, column=1, padx=20)

            label = tk.Label(face_frame, text=label_text, bg=self.bg_color)
            label.grid(row=0, column=0, pady=2)

            for j, color_abbr in enumerate(face):
                row = (j // 3) + 1
                col = j % 3
                if color_abbr in ["R","B","O","G","Y","W"]:
                    color = self.color_map.get(color_abbr, "white")
                else:
                    color = color_abbr
                label = tk.Label(face_frame, bg=color, width=3, height=1, relief="raised")
                label.grid(row=row, column=col, padx=2, pady=2)
                label.bind("<Button-1>", lambda event, row=row, col=col, face_index=i, cuboid_pos=j: self.handle_cuboid_click(face_index, cuboid_pos, row, col))
                label.bind("<Enter>", self.button_enter)
                label.bind("<Leave>", self.button_leave)    
            self.face_frames.append(face_frame)


        if not self.move_buttons_displayed:
            self.create_move_buttons_frame()
            self.move_buttons_displayed = True

    def handle_cuboid_click(self, face_index, cuboid_pos, row, col):
        """Config for swapping cuboids
        Allows for user to click on two cuboids to swap their colors
        
        """
        if not hasattr(self, 'selected_cuboid'):
            self.selected_cuboid = (face_index, cuboid_pos, row, col)
        else:
            prev_face_index, prev_cuboid_pos, prev_row, prev_col = self.selected_cuboid
            
            color1 = self.cubestate[prev_face_index][(prev_row - 1) * 3 + prev_col]
            color2 = self.cubestate[face_index][(row - 1) * 3 + col]
            
            prev_label = self.face_frames[prev_face_index].grid_slaves(row=prev_row, column=prev_col)[0]
            curr_label = self.face_frames[face_index].grid_slaves(row=row, column=col)[0]
            prev_label.config(bg=self.color_map.get(color2, "white"))
            curr_label.config(bg=self.color_map.get(color1, "white"))

            self.cubestate[face_index][cuboid_pos], self.cubestate[prev_face_index][prev_cuboid_pos] = self.cubestate[prev_face_index][prev_cuboid_pos], self.cubestate[face_index][cuboid_pos]
            self.cube = Cube(self.cubestate)

            del self.selected_cuboid
            self.update_faces()

    def create_move_buttons_frame(self):
        """Creates a new frame to pack move buttons into when 'show' is
        pressed
        
        """
        self.move_buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        self.move_buttons_frame.grid(row=2, column=0, pady=10)

        basic_moves = ['U', 'U\'', 'D', 'D\'', 'L', 'L\'', 'R', 'R\'', 'F', 'F\'', 'B', 'B\'', 'scramble']
        for move in basic_moves:
            button = tk.Button(self.move_buttons_frame, text=move, command=lambda m=move: self.make_move(m), bg=self.button_color)
            button.pack(side="left", padx=5, pady=5)
            button.bind("<Enter>", self.button_enter)
            button.bind("<Leave>", self.button_leave)

    def make_move(self, move):
        """Implements functionality for each move button
        Updates cube faces to show moves 'live'

        """
        if move == 'F':
            print(move)
            self.cube.rotate_front_clockwise()
        elif move == 'B':
            print(move)
            self.cube.rotate_back_clockwise()
        elif move == 'L':
            print(move)
            self.cube.rotate_left_clockwise()
        elif move == 'R':
            print(move)
            self.cube.rotate_right_clockwise()
        elif move == 'U':
            print(move)
            self.cube.rotate_top_clockwise()
        elif move == 'D':
            print(move)
            self.cube.rotate_bottom_clockwise()
        elif move == 'F\'':
            print(move)
            self.cube.rotate_front_counter_clockwise()
        elif move == 'B\'':
            print(move)
            self.cube.rotate_back_counter_clockwise()
        elif move == 'L\'':
            print(move)
            self.cube.rotate_left_counter_clockwise()
        elif move == 'R\'':
            print(move)
            self.cube.rotate_right_counter_clockwise()
        elif move == 'U\'':
            print(move)
            self.cube.rotate_top_counter_clockwise()
        elif move == 'D\'':
            print(move)
            self.cube.rotate_bottom_counter_clockwise()
        elif move == 'scramble':
            print(move)
            self.cube.scramble()
        
        self.cubestate = self.cube.get_cubestate()    
        self.update_faces()

    def solve_action(self):
        """Config for solve button
        Returns a move list on any valid cube
        
        """
        print("Solve button clicked")
        if self.cube.is_solved():
            solvealg = "Cube already solved!"
        else:
            cubesolver = CubeSolver(self.cube)
            solvealg = cubesolver.solve_cube()

        if solvealg:
            if type(solvealg) == list:
                print(len(solvealg))
                move_text = "\n".join(" ".join(solvealg[i:i+25]) for i in range(0, len(solvealg), 25))
            else:
                move_text = solvealg

            move_window = tk.Toplevel(self.root)
            move_window.title("Move List")

            move_label = tk.Label(move_window, text=move_text, justify="center")
            move_label.pack(padx=20, pady=10)

            if type(solvealg) == list:
                current_move_index = 0

                def play_moves():
                    nonlocal current_move_index
                    if current_move_index < len(solvealg):
                        if solvealg[current_move_index] not in ['U', 'U\'', 'D', 'D\'', 'L', 'L\'', 'R', 'R\'', 'F', 'F\'', 'B', 'B\'']:
                            current_move_index += 1
                        move = solvealg[current_move_index]
                        self.make_move(move)
                        current_move_index += 1
                        move_window.after(250, play_moves)
                    else:
                        move_label.config(text=move_label.cget("text") + "\n\n\nCube Solved!")
                        next_move_button.pack_forget()
                        play_button.pack_forget()

                buttons_frame = tk.Frame(move_window)
                buttons_frame.pack(side="bottom", pady=10)

                next_move_button = tk.Button(buttons_frame, text="Next Move", command=lambda: next_move())
                next_move_button.pack(side="left", padx=5)

                play_button = tk.Button(buttons_frame, text="Play Moves", command=play_moves)
                play_button.pack(side="left", padx=5)

                def next_move():
                    nonlocal current_move_index
                    if current_move_index < len(solvealg):
                        if solvealg[current_move_index] not in ['U', 'U\'', 'D', 'D\'', 'L', 'L\'', 'R', 'R\'', 'F', 'F\'', 'B', 'B\'']:
                            current_move_index += 1
                        move = solvealg[current_move_index]
                        self.make_move(move)
                        current_move_index += 1
                        if current_move_index >= len(solvealg):
                            move_label.config(text=move_label.cget("text") + "\n\n\nCube Solved!")
                            next_move_button.pack_forget()
                            play_button.pack_forget()

                move_window.geometry("+{}+{}".format(
                    int(self.root.winfo_screenwidth() / 2 - move_window.winfo_reqwidth() / 2),
                    int(self.root.winfo_screenheight() / 2 - move_window.winfo_reqheight() / 2)
                ))

                move_window.mainloop()
        else:
            print("No valid solution")

    def reset_action(self):
        """Config for reset button
        Resets cube faces by creating a fresh new cube
        
        """
        print("Reset button clicked")
        self.cube = Cube()
        self.cubestate = self.cube.get_cubestate()
        self.update_faces()


if __name__ == "__main__":
    simandsolve = SNS()