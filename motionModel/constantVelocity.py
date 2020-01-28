import numpy as np


class constantVelocityModel:

    def __init__(self, dims=2):
        """
        Initialize the parameters of constant velocity motion model
        """
        dt = 0.0
        # state transition matrix
        self.F = np.vstack((
                            np.hstack((np.eye(dims), dt*np.eye(dims))),
                            np.hstack((np.zeros((dims, dims)), np.eye(dims)))
                            ))
        # process covariance matrix
        self.P = np.vstack((
                            np.hstack((10*np.eye(dims), np.zeros((dims, dims)))),
                            np.hstack((np.zeros((dims, dims)), 1000*np.eye(dims)))
                            ))
        # input
        self.u = np.zeros((2*dims, 1))
        # observation
        self.H = np.hstack((np.eye(dims), np.zeros(dims, dims)))
        # observation noise
        self.R = 1 * np.eye(dims)

    def set_state(self, state):
        """
        Update the observable state of motion model
        :param state: Update the state vector
        :return: None
        """
        pass

    def update_F(selfself, dt):
        """
        Update the time increment in state transition matrix
        :param dt: current time increment
        :return: None
        """
        # state transition matrix
        self.F = np.vstack((
                            np.hstack((np.eye(dims), dt*np.eye(dims))),
                            np.hstack((np.zeros((dims, dims)), np.eye(dims)))
                            ))