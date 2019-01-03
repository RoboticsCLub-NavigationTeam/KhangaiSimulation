from random import randint
from time import time

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from field import *
from robot import *
from vector import Vector

noise = np.random.normal(0, 0.01, 100)

def calPos(x, vx, ax, t):
        index = randint(0, 99)
        return (x + vx*t + 0.5*ax*t*t) + noise[index]



def main():
        
        # plt.show()

        plt.xlim(0, 9)
        plt.ylim(0, 2.5)
        currentAxis = plt.gca()
        currentAxis.set_aspect('equal', adjustable='box')

        # Plotting Poles
        plt.scatter(2.000, 1.250, s=10, color='red')
        plt.scatter(3.500, 1.250, s=10, color='red')
        plt.scatter(5.000, 1.250, s=10, color='red')
        # Plotting Bridge (Lower Side)
        plt.scatter(6.500, 0.725, s=10, color='red')
        plt.scatter(7.000, 0.725, s=10, color='red')
        plt.scatter(7.500, 0.725, s=10, color='red')
        plt.scatter(8.000, 0.725, s=10, color='red')
        # Plotting Bridge (Upper Side)
        plt.scatter(6.500, 1.725, s=10, color='red')
        plt.scatter(7.000, 1.725, s=10, color='red')
        plt.scatter(7.500, 1.725, s=10, color='red')
        plt.scatter(8.000, 1.725, s=10, color='red')


        fieldStop2 = Field(8.700, 1.250, fieldI_cons, 0)
        fieldStop = Field(8.700, 1.250, fieldI_cons, fieldStop2)
        fieldI = Field(8.700, 1.250, fieldI_cons, fieldStop)
        fieldH = Field(6.000, 1.250, fieldH_cons, fieldI)
        fieldG = Field(5.300, 1.760, fieldG_cons, fieldH)
        fieldF = Field(4.300, 1.750, fieldF_cons, fieldG)
        fieldE = Field(3.900, 0.500, fieldE_cons, fieldF)
        fieldD = Field(3.200, 0.500, fieldD_cons, fieldE)
        fieldC = Field(2.500, 1.760, fieldC_cons, fieldD)
        fieldB = Field(1.600, 1.750, fieldB_cons, fieldC)
        fieldA = Field(0.500, 0.500, fieldA_cons, fieldB)

        # for i in range(1000):
        robo_pos = [0.5, 0.5, 0]
        robo_dim = [0.65, 0.65]

        khangai = Robot(robo_pos, fieldA)

        vel = Vector(0,0)
        last_vel = Vector(0,0)
        accel = Vector(0,0)

        robo_speed = 3
        accel_factor = 1

        # xPos = []
        # yPos = []
        mass = 10

        # i = 0
        # file_name = "data_set/dataSet" + str(i) + ".csv"
        # f = open(file_name, "w")

        # f.writelines("time, x, y\n")

        t = 0.00
        w = robo_dim[0]
        h = robo_dim[1]

        x = robo_pos[0]
        y = robo_pos[1]

        then = time()
        while khangai.getField() != fieldStop :

                if time() - then > 0.01 :
                        dt = time() - then
                        then = time()

                        vel += accel*dt
                        x = calPos(x, vel.x, accel.x, dt)
                        y = calPos(y, vel.y, accel.y, dt)
                        robo_pos[0] = x
                        robo_pos[1] = y
                        t += dt

                        vel = khangai.run(robo_pos, robo_speed, dt)

                        accel = accel_factor*(vel - last_vel)/dt
                        last_vel = vel

                        currentAxis.add_patch(Rectangle((x - w/2.0, y - h/2.0), w, h,alpha=1, fill=None))

                        plt.scatter(x, y, s=1, color='black')
                        plt.pause(0.005)
        
        # f.close()
        print("Time Taken : " + str(t))
        # plt.plot(yPos, xPos, label='Simple Movement')
        plt.show()


if __name__=="__main__":
   main()
