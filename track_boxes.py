from kalmanFilter import kf
from motionModel import constantVelocity
from utils import helper
import numpy as np


# constant velocity model
cv_model = constantVelocity.ConstantVelocityModel(2)


# image parameters
image_width = 1280
image_height = 720
img = 255 * np.ones((image_height, image_width, 3), dtype=np.int8)

trajectories = helper.generate_boxes(image_width, image_height, True)




