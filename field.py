import math
import matplotlib.pyplot as plt
import numpy as np

# Algorithm on Wikipedia : https://en.wikipedia.org/wiki/Spline_(mathematics)
def cubic_spline(p):
        a = [None]*3
        b = [None]*3
        d = [None]*3
        u = [None]*3
        h = [None]*2

        for i in range(3):
                a[i] = p[i][1]

        for i in range(2):
                if p[i+1][0] == p[i][0]:
                        p[i+1][0] += 0.001
                        pass

                h[i] = p[i+1][0] - p[i][0]

        alpha = 3.0*(a[2] - a[1])/h[1] - 3.0*(a[1] - a[0])/h[0]

        c = [None]*3
        l = [None]*3
        z = [None]*3

        l[0] = 1
        u[0] = z[0] = 0

        l[1] = 2*(p[2][0] - p[0][0]) - h[0]*u[0]
        u[1] = h[1]/l[1]
        z[1] = (alpha - h[0]*z[0])/l[1]

        l[2] = 1
        z[2] = c[2] = 0

        for j in range(1,-1,-1):
                c[j] = z[j] - u[j]*c[j+1]
                b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3.0
                d[j] = (c[j+1] - c[j])/(3*h[j])
        
        return [a[0], b[0], c[0], d[0]]


def cubic_theta(p, v, h, dt):
        xp = p[0][0]
        yp = p[0][1]
        x2 = p[2][0]
        x1 = p[1][0]
        coeff = cubic_spline(p)
        a = coeff[0]
        b = coeff[1]
        c = coeff[2]
        d = coeff[3]

        P = lambda x : (a + b*(x-xp) + c*(x-xp)**2 + d*(x-xp)**3)
        
        # x_lst = [x/1000.0 for x in range(int(xp*1000), int(x2*1000))]
        # x = np.array(x_lst)
        # y = P(x)
        # plt.plot(x,y)
        # plt.show()

        r = v*dt
        del_x = 0
        del_y = 0
        while del_x**2 + del_y**2 < r**2 :
                del_x += h
                del_y = P(xp + del_x) - yp
                # print(del_x, del_y)

        # input()
        return math.atan2(del_y, del_x)


class Field:
        
        def __init__(self, xc, yc, constraint, next):
                self.xc = xc
                self.yc = yc
                self.constraint = constraint
                self.next = next

        def nextFieldReached(self, state):
                return (self.next.constraint(state))

        def angleOfAttack(self, state, vel, dt):

                p0 = [state[0], state[1]]
                p1 = [self.next.xc, self.next.yc]
                p2 = [self.next.next.xc, self.next.next.yc]

                p = [p0, p1, p2]
                theta = cubic_theta(p, vel, 0.001, dt)

                dx = self.next.xc - state[0]
                dy = self.next.yc - state[1]
                # print(dx, dy)
                # return math.atan2(dy, dx)
                return theta


def fieldA_cons(state):
        x = state[0]
        y = state[1]
        if (y > 0 and y < 0.100 and x > 0 and x < 0.100):
                return True

        return False


def fieldB_cons(state):
        x = state[0]
        y = state[1]
        if (y > 1.500 and y < 2.000 and x > 1.500 and x < 1.800):
                return True

        return False


def fieldC_cons(state):
        x = state[0]
        y = state[1]
        if (y > 1.500 and y < 2.000 and x > 2.300 and x < 2.800):
                return True

        return False


def fieldD_cons(state):
        x = state[0]
        y = state[1]
        if (y > 0.300 and y < 0.600 and x > 3.100 and x < 3.500):
                return True

        return False


def fieldE_cons(state):
        x = state[0]
        y = state[1]
        if (y > 0.300 and y < 0.800 and x > 3.700 and x < 4.450):
                return True

        return False


def fieldF_cons(state):
        x = state[0]
        y = state[1]
        if (y > 1.600 and y < 2.000 and x > 4.050 and x < 4.550):
                return True

        return False


def fieldG_cons(state):
        x = state[0]
        y = state[1]
        if (y > 1.600 and y < 2.000 and x > 5.050 and x < 5.550):
                return True

        return False


def fieldH_cons(state):
        x = state[0]
        y = state[1]
        if (y > 1.200 and y < 1.280 and x > 5.700 and x < 6.30):
                return True

        return False


def fieldI_cons(state):
        x = state[0]
        y = state[1]
        if (y > 1.200 and y < 1.280 and x > 8.400 and x < 9.000):
                return True

        return False
