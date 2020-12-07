from PIL import Image
import numpy as np
import random

im = Image.open("mazes/maze-3.png")
pix = im.load()
print(pix[9, 8])

def find_ends(img):
    img = np.array(img)
    # for color image
    start = (254, 0, 0)
    end = (0, 9, 254)
    
    Ys, Xs = np.where(np.all(img==start, axis=2))
    Ye, Xe = np.where(np.all(img==end, axis=2))
    
    start_loc = (Xs[0], Ys[0])
    end_loc = (Xe[0], Ye[0])
    return start_loc, end_loc

def show(im):
    imB = im.resize((600,600))  
    imB.show()

def search(start, end, img, pix):
    isFound = False
    current = start
    array = np.array(img)
    path = []
    intersects = []
    while isFound is False:
        possible = []
        surroundings = [(current[0]-1, current[1]),
                        (current[0]+1, current[1]),
                        (current[0], current[1]-1),
                        (current[0], current[1]+1)]


        for move in surroundings:
            if end == move:
                isFound = True
            if ((pix[move] >= (200, 200, 200) or pix[move] == (0, 9, 254)) and pix[move] != (255, 255, 0) and move != start):
                possible.append(move)

        
        if len(possible) >= 2:
            if current not in intersects:
                intersects.append(current)
        if len(possible) == 0:
            intersects_reversed = intersects[::-1]
            for i in intersects_reversed:
                if i != current:
                    current = i
                    intersects.pop(intersects.index(i))
                    
                    break
            path = path[:path.index(current)]
            
            
        else:
            current = random.choice(possible)
        path.append(current)
        array[current[1], current[0]] = (255, 255, 0)
        img=Image.fromarray(array)
        pix = img.load()
    for p in path:
        array[p[1], p[0]] = (0, 255, 0)
    img=Image.fromarray(array)
    img.save('image.png')

start, end = find_ends(im)
search(start, end, im, pix)