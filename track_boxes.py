import sys
import numpy as np
from kalmanFilter import kf
from motionModel import constantVelocity
from vehicle import Vehicle

from matplotlib import pyplot as plt
import numpy as np
from numpy import random
import cv2


image_width = 1280
image_height = 720

img = 255 * np.ones((image_height, image_width, 3), dtype=np.int8)
# plt.imshow(img)
# plt.show()

traj = []
v1 = Vehicle(200, 500, 100, 100, image_width, image_height, 10, 5)
traj.append( v1.trajectory_box )

v2 = Vehicle(600, 550, 100, 100, image_width, image_height, 0, 15)
traj.append(v2.trajectory_box )

max_count = max(len(traj[0]), len(traj[1]))

for frame_idx in range(max_count):
    boxes = []
    for vh_idx in range(2):
        if frame_idx < len(traj[vh_idx]):
            boxes.append(traj[vh_idx][frame_idx])
        else:
            boxes.append(traj[vh_idx][-1])

    for b in boxes:
        cv2.rectangle(img, (b[0:2]), (b[2:4]), (255, 0, 0), thickness=2)

    plt.clf()
    plt.imshow(img)
    plt.pause(0.5)




