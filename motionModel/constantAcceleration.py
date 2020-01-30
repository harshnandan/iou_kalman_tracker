import numpy as np


class ConstantAccelerationModel:

    def __init__(self, dims):
        """
        Initialize the parameters of constant velocity motion model
        """
        self.dims = int(dims)
        dt = 0.0
        self.x = np.zeros((3*dims, 1))
        # state transition matrix
        self.F = np.vstack((
                            np.hstack((np.eye(dims), dt*np.eye(dims), (dt**2)/2*np.eye(dims))),
                            np.hstack((np.zeros((dims, dims)), np.eye(dims), dt*np.eye(dims))),
                            np.hstack((np.zeros((dims, 2 * dims)), np.eye(dims)))
                            ))
        # process covariance matrix
        self.P = np.vstack((
                            np.hstack((10*np.eye(dims), np.zeros((dims, 2*dims)))),
                            np.hstack((np.zeros((dims, dims)), 1000*np.eye(dims), np.zeros((dims, dims)) )),
                            np.hstack((np.zeros((dims, 2*dims)), 2000*np.eye(dims) )),
                            ))
        # input
        self.u = np.zeros((3*dims, 1))
        # observation
        self.H = np.hstack((np.eye(dims), np.zeros((dims, 2*dims))))
        # observation noise
        self.R = 1 * np.eye(dims)

    def set_init_state(self, state):
        """
        Update the observable state of motion model
        :param state: Update the state vector
        :return: None
        """
        for i in range(len(state)):
            self.x[i] = state[i]

    def update_F(self, dt):
        """
        Update the time increment in state transition matrix
        :param dt: current time increment
        :return: None
        """
        # state transition matrix
        self.F = np.vstack((
                            np.hstack((np.eye(self.dims), dt * np.eye(self.dims), (dt ** 2) / 2 * np.eye(self.dims))),
                            np.hstack((np.zeros((self.dims, self.dims)), np.eye(self.dims), dt*np.eye(self.dims))),
                            np.hstack((np.zeros((self.dims, 2 * self.dims)), np.eye(self.dims)))
                            ))
