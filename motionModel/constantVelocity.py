import numpy as np


def constantVelocityModel(self, dt):
    
    self.F = np.array([[1., 0., dt, 0.],
                       [0, 1., 0., dt],
                       [0., 0., 1., 0.],
                       [0., 0., 0., 1.]], dtype=np.float32)  # state transition matrix

    self.P = np.array([[10., 0., 0., 0.],
                       [0., 10., 0., 0.],
                       [0., 0., 1000., 0.],
                       [0., 0., 0., 1000.]], dtype=np.float32)  # process covariance matrix

    self.u = np.array([[0.], [0.], [0.], [0.]], dtype=np.float32)
    self.H = np.array([[1., 0., 0., 0.], [0., 1., 0., 0.]], dtype=np.float32)
    self.R = np.array([[1., 0.], [0., 1.]], dtype=np.float32)