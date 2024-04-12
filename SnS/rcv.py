# rcv.py
# A program using OpenCV to scan a Rubik's Cube and detect its colors
# Joey Goetz

import cv2 as cv
import numpy as np

colorslist = ['red','blue','orange','green','yellow', 'white']
colorboxlist = [(0,0,255),(255,0,0),(0,165,255),(0,255,0),(0,255,255),(255,255,255)]
colors = {
    'red': [145, 130, 30],
    'blue': [80, 175, 75],
    'orange': [0, 140, 90],
    'green': [50, 140, 40],
    'yellow': [10, 90, 80],
    'white': [100, 100, 255]
    }

def main():
    """Initializes an OpenCV video capture using the device's webcam
    Waits for user to press either ESC to close or SPACE to take a photo
    Takes faces in the order Front-Right-Back-Left-Bottom-Top

    """
    cap = cv.VideoCapture(0)
    img_counter = 0
    color_counter = 0
    cubes = []
    while True:
        ret, frame = cap.read()
        hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.rectangle(frame, (225,125), (425,325), colorboxlist[color_counter], 3)
        cv.imshow('RCV', frame)
        k = cv.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            cube = frame.copy()
            cubes.append(cube)
            print(f"{colorslist[img_counter]} side taken")
            color_calibrater(cube, colorslist[img_counter])
            img_counter += 1
            if img_counter >= 6:
                cuboid_positions = cuboid_analyzer(cubes)
                print(cuboid_positions)
                cv.destroyAllWindows()
                break
            color_counter += 1
    if cuboid_positions:
        return cuboid_positions

def color_calibrater(face, color):
    """Initializes the HSV color ranges for each color by scannign the
    center square of each face
    
    """
    if color != "white":
        h = []
        s = []
        v = []
        image = cv.cvtColor(face, cv.COLOR_BGR2HSV)
        for i in range(215, 236):
            for j in range(315, 336):
                hsv = image[i][j]
                h.append(hsv[0])
                s.append(hsv[1])
                v.append(hsv[2])
        colors[color] = [round(sum(h)/len(h)), round(sum(s)/len(s)), round(sum(v)/len(v))]

def color_averager(face, y, x):
    """Averages the color of a single cuboid by compiling and averaging
    the centermost 30 pixels
    
    """
    h = []
    s = []
    v = []
    for i in range(y-10, y+11):
        for j in range(x-10, x+11):
            hsv = face[i][j]
            h.append(hsv[0])
            s.append(hsv[1])
            v.append(hsv[2])
    return [round(sum(h)/len(h)), round(sum(s)/len(s)), round(sum(v)/len(v))]

def color_clusters(facelist):
    """A simple clustering algorithm that classifies colors by grouping
    together the 9 most alike cuboids on all the faces
    
    """
    colorlist = []
    color_counts = {color: 0 for color in colors}
    for i, face in enumerate(facelist):
        face_colors = []
        for j, cuboid in enumerate(face):
            closest_color = None
            if i == 5 and j == 4:
                face_colors.append('white')
            else:
                min_distance = float('inf')
                for color, hsv_values in colors.items():
                    distance = np.linalg.norm(np.array(cuboid) - np.array(hsv_values))
                    if distance < min_distance and color_counts[color] < 9:
                        min_distance = distance
                        closest_color = color
                if closest_color is not None:
                    face_colors.append(closest_color)
                    color_counts[closest_color] += 1
        colorlist.append(face_colors)
        print(color_counts)
    return colorlist

def cuboid_analyzer(cubes):
    """Grabs the HSV value for each cuboid and compiles a facelist of each
    of these values to be classified
    
    """
    facelist = []
    colorlist = []
    while True:
        facelist = []
        for cube in cubes:
            image = cube[128:322, 228:422]
            hsvimage = cv.cvtColor(image, cv.COLOR_BGR2HSV)
            top_left = color_averager(hsvimage, 25, 25)
            mid_left = color_averager(hsvimage, 97, 25)
            bot_left = color_averager(hsvimage, 169, 25)
            top_middle = color_averager(hsvimage, 25, 97)
            mid_middle = color_averager(hsvimage, 97, 97)
            bot_middle = color_averager(hsvimage, 169, 97)
            top_right = color_averager(hsvimage, 25, 169)
            mid_right = color_averager(hsvimage, 97, 169)
            bot_right = color_averager(hsvimage, 169, 169)
            cuboids = [top_left, top_middle, top_right,
                    mid_left, mid_middle, mid_right,
                    bot_left, bot_middle, bot_right]
            facelist.append(cuboids)
        colorlist = color_clusters(facelist)
        return colorlist


if __name__ == "__main__":
    main()
