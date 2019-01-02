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


        fieldStop = Field(1.250, 8.700, fieldI_cons, 0)
        fieldI = Field(1.250, 8.700, fieldI_cons, fieldStop)
        fieldH = Field(1.250, 6.000, fieldH_cons, fieldI)
        fieldG = Field(1.760, 5.300, fieldG_cons, fieldH)
        fieldF = Field(1.750, 4.300, fieldF_cons, fieldG)
        fieldE = Field(0.500, 3.900, fieldE_cons, fieldF)
        fieldD = Field(0.500, 3.200, fieldD_cons, fieldE)
        fieldC = Field(1.760, 2.500, fieldC_cons, fieldD)
        fieldB = Field(1.750, 1.600, fieldB_cons, fieldC)
        fieldA = Field(0.500, 0.500, fieldA_cons, fieldB)

        # for i in range(1000):
        robo_pos = [0.5, 0.5, 0]

        khangai = Robot(robo_pos, fieldA)

        vel = Vector(0,0)
        last_vel = Vector(0,0)
        accel = Vector(0,0)

        accel_factor = 1

        # xPos = []
        # yPos = []
        mass = 10

        # i = 0
        # file_name = "data_set/dataSet" + str(i) + ".csv"
        # f = open(file_name, "w")

        # f.writelines("time, x, y\n")

        t = 0.00

        then = time()
        while khangai.getField() != fieldStop :

                if time() - then > 0.01 :
                        dt = time() - then
                        then = time()

                        vel += accel*dt
                        robo_pos[0] = calPos(robo_pos[0], vel.x, accel.x, dt)
                        robo_pos[1] = calPos(robo_pos[1], vel.y, accel.y, dt)

                        vel = khangai.run(robo_pos, 1.2, dt)

                        accel = accel_factor*(vel - last_vel)/dt
                        last_vel = vel
                        # print(accel)

                        # line = str(t) + ", " + str(robo_pos[1]) + ", " + str(robo_pos[0]) + "\n"
                        # f.writelines(line)
                        t += dt
                        # print(robo_pos)

                        # xPos.append(robo_pos[0])
                        # yPos.append(robo_pos[1])
                        x = robo_pos[1]
                        y = robo_pos[0]

                        currentAxis.add_patch(Rectangle((x - .41, y - .39), 0.82, 0.78,alpha=1, fill=None))

                        plt.scatter(x, y, s=1, color='black')
                        plt.pause(0.005)
        
        # f.close()
        print("Time Taken : " + str(t))
        # plt.plot(yPos, xPos, label='Simple Movement')
        plt.show()


if __name__=="__main__":
   main()
