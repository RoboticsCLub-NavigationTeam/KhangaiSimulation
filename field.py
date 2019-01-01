import math


class Field:
        
        def __init__(self, xc, yc, constraint, next):
                self.xc = xc
                self.yc = yc
                self.constraint = constraint
                self.next = next

        def nextFieldReached(self, state):
                return (self.next.constraint(state))

        def angleOfAttack(self, state):
                dx = self.next.xc - state[0]
                dy = self.next.yc - state[1]
                return math.atan2(dy, dx)


def fieldA_cons(state):
        x = state[0]
        y = state[1]
        if (x > 0 and x < 0.100 and y > 0 and y < 0.100):
                return True

        return False


def fieldB_cons(state):
        x = state[0]
        y = state[1]
        if (x > 1.500 and x < 2.000 and y > 1.500 and y < 1.800):
                return True

        return False


def fieldC_cons(state):
        x = state[0]
        y = state[1]
        if (x > 1.500 and x < 2.000 and y > 2.300 and y < 2.800):
                return True

        return False


def fieldD_cons(state):
        x = state[0]
        y = state[1]
        if (x > 0.300 and x < 0.800 and y > 3.100 and y < 3.500):
                return True

        return False


def fieldE_cons(state):
        x = state[0]
        y = state[1]
        if (x > 0.300 and x < 0.800 and y > 3.450 and y < 3.950):
                return True

        return False


def fieldF_cons(state):
        x = state[0]
        y = state[1]
        if (x > 1.500 and x < 2.000 and y > 4.050 and y < 4.550):
                return True

        return False


def fieldG_cons(state):
        x = state[0]
        y = state[1]
        if (x > 1.500 and x < 2.000 and y > 5.050 and y < 5.550):
                return True

        return False


def fieldH_cons(state):
        x = state[0]
        y = state[1]
        if (x > 1.225 and x < 1.280 and y > 5.800 and y < 6.250):
                return True

        return False


def fieldI_cons(state):
        x = state[0]
        y = state[1]
        if (x > 1.225 and x < 1.280 and y > 8.500 and y < 9.000):
                return True

        return False
