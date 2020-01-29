import numpy as np

''' A generic Kalman filter which uses an arbitrary linear model specified by the user'''
class KalmanFilter:

    def __init__(self, init_state, time_stamp, motion_model):
        """
        Initialize the kalman filter
        :param init_state: the initial measurement is set as the initial state
        :param time_stamp: the time stamp of the first measurement
        :param motion_model: motion model object
        """
        dt = time_stamp / 1000
        self.time_stamp = [time_stamp]
        self.motion_model = motion_model

        self.motion_model.update_F(dt)
        self.motion_model.set_state(init_state)

    def predict(self, time_stamp):
        """
        Performs the prediction step of kalman filter
        :param time_stamp: Time stamp at which prediction is asked for
        :return: None
        """
        self.time_stamp += [time_stamp]
        dt = (self.time_stamp[-1] - self.time_stamp[-2]) / 1000
        self.motion_model.update_F(dt)

        self.motion_model.x = np.matmul(self.motion_model.F, self.motion_model.x) + self.u
        self.motion_model.P = np.matmul(np.matmul(self.motion_model.F, self.motion_model.P), self.motion_model.F.transpose())

    def update(self, z_measured):
        """
        Performs measurement update
        :param z_measured: position measurement
        :return: None
        """
        # measurement update
        z = np.array([[x], [y]], dtype=np.float32)
        err = z - np.matmul(self.motion_model.H, self.motion_model.x)
        S = np.matmul(np.matmul(self.motion_model.H, self.motion_model.P),
                      self.motion_model.H.transpose()) + self.motion_model.R
        S_inv = np.linalg.inv(S)
        K = np.matmul(np.matmul(self.motion_model.P, self.motion_model.H.transpose()), S_inv)

        self.motion_model.x = self.motion_model.x + np.matmul(K, err)
        self.motion_model.P = np.matmul(np.eye(self.motion_model.x.shape[0]) -
                                    np.matmul(K, self.motion_model.H), self.motion_model.P)
