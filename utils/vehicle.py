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
        self.x1, self.y1 = min(x0+w, x_limit), min(y0+h, y_limit)
        self.x_cg, self.y_cg = (self.x0+self.x1)/2, (self.y0+self.y1)/2
        self.vx, self.vy = vx, vy
        self.ax, self.ay = 1 , 0

        self.slope = 1.6
        self.trajectory_box = [(self.x0, self.y0, self.x1, self.y1)]

        while 0<= self.x0 <=x_limit and 0<=self.y0<=y_limit and \
            0 <= self.x1 <= x_limit and 0 <= self.y1 <= y_limit and\
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
