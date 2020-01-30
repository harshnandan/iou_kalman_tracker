import cv2
import numpy as np
from matplotlib import pyplot as plt
import random

def iou(bbox1, bbox2):
    """
    Calculates the intersection-over-union of two bounding boxes.
    :param bbox1: (numpy.array, list of floats): bounding box in format x1,y1,x2,y2.
    :param bbox2: (numpy.array, list of floats): bounding box in format x1,y1,x2,y2.
    :return: (int) intersection-over-onion of bbox1, bbox2
    """

    bbox1 = [float(x) for x in bbox1]
    bbox2 = [float(x) for x in bbox2]

    (x0_1, y0_1, x1_1, y1_1) = bbox1
    (x0_2, y0_2, x1_2, y1_2) = bbox2

    # get the overlap rectangle
    overlap_x0 = max(x0_1, x0_2)
    overlap_y0 = max(y0_1, y0_2)
    overlap_x1 = min(x1_1, x1_2)
    overlap_y1 = min(y1_1, y1_2)

    # check if there is an overlap
    if overlap_x1 - overlap_x0 <= 0 or overlap_y1 - overlap_y0 <= 0:
        return 0

    # if yes, calculate the ratio of the overlap to each ROI size and the unified size
    size_1 = (x1_1 - x0_1) * (y1_1 - y0_1)
    size_2 = (x1_2 - x0_2) * (y1_2 - y0_2)
    size_intersection = (overlap_x1 - overlap_x0) * (overlap_y1 - overlap_y0)
    size_union = size_1 + size_2 - size_intersection

    return size_intersection / size_union


def box_cg(box):
    """
    Returns the cg of a box
    :param box: (numpy.array, list of floats): bounding box in format x1,y1,x2,y2.
    :return:
    """
    return [((box[0] + box[2]) / 2), ((box[1] + box[3]) / 2)]


def generate_boxes(image_width, image_height, dt, visualize_traj=False):
    traj = []
    v1 = Vehicle(200, 500, 100, 100, image_width, image_height, 10, 5)
    traj.append(v1.trajectory_box)

    v2 = Vehicle(600, 550, 100, 100, image_width, image_height, 0, 15)
    traj.append(v2.trajectory_box)

    max_count = max(len(traj[0]), len(traj[1]))

    boxes_traj = []
    timestamp = dt
    for frame_idx in range(max_count):
        boxes = [timestamp]
        for vh_idx in range(2):
            if frame_idx < len(traj[vh_idx]):
                boxes.append(traj[vh_idx][frame_idx])
            else:
                boxes.append(traj[vh_idx][-1])
        if random.random() > 0.6:
            boxes_traj.append(boxes)
        timestamp += dt
    if visualize_traj:
        img = 255 * np.ones((image_height, image_width, 3), dtype=np.int8)
        for frame_idx in range(max_count):
            for b in boxes_traj[frame_idx]:
                cv2.rectangle(img, (b[0:2]), (b[2:4]), (255, 0, 0), thickness=2)

            plt.clf()
            plt.imshow(img)
            plt.pause(1)

    return boxes_traj


class Vehicle:

    def __init__(self, x0, y0, w, h, x_limit, y_limit, vx, vy):
        """
        Initialize vehicle parameter

        :param x0: (int8) initial x position as image pixel
        :param y0: initial y position as image pixel
        :param w: box width in pixel
        :param h: box height in pixel
        :param x_limit: max x-pixel limit for box
        :param y_limit: max y-pixel limit for box
        :param vx: x-velocity
        :param vy: y-velocity
        """

        self.x0, self.y0 = x0, y0
        self.w, self.h = w, h
        self.x1, self.y1 = min(x0 + w, x_limit), min(y0 + h, y_limit)
        self.x_cg, self.y_cg = (self.x0 + self.x1) / 2, (self.y0 + self.y1) / 2
        self.vx, self.vy = vx, vy
        self.ax, self.ay = 1, 0

        self.slope = 1.6
        self.trajectory_box = [(self.x0, self.y0, self.x1, self.y1)]

        while 0 <= self.x0 <= x_limit and 0 <= self.y0 <= y_limit and \
                0 <= self.x1 <= x_limit and 0 <= self.y1 <= y_limit and \
                self.w > 20 and self.h > 20:
            self.vx += self.ax
            self.vy += self.ay

            self.x0 += self.vx
            self.y0 -= self.vy
            self.w -= 1
            self.h -= 1
            self.x1 = self.x0 + self.w
            self.y1 = self.y0 + self.h

            self.trajectory_box.append((self.x0, self.y0, self.x1, self.y1))
