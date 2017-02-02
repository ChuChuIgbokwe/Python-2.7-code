# Please only modify the indicated area below!

from math import *
import random
import matplotlib.pyplot as plt

landmarks = [[20.0, 20.0],
             [80.0, 80.0],
             [120.0, 34.0],
             [80.0, 64.7],
             [25.0, 87.0],
             [72.5, 80.0],
             [10.8, 77.0],
             [80.0, 80.0],
             [92.0, 33.0],
             [64.2, 44.4],
             [13.9, 12.8],
             [80.0, 20.0]]
world_size = 100.0


class robot:
    def __init__(self):
        self.x = random.random() * world_size
        self.y = random.random() * world_size
        self.orientation = random.random() * 2.0 * pi
        self.forward_noise = 0.0;
        self.turn_noise = 0.0;
        self.sense_noise = 0.0;

    def set(self, new_x, new_y, new_orientation):
        '''

        :param new_x:
        :param new_y:
        :param new_orientation:
        :return:
        '''
        if new_x < 0 or new_x >= world_size:
            raise ValueError, 'X coordinate out of bound'
        if new_y < 0 or new_y >= world_size:
            raise ValueError, 'Y coordinate out of bound'
        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise ValueError, 'Orientation must be in [0..2pi]'
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)

    def set_noise(self, new_f_noise, new_t_noise, new_s_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.forward_noise = float(new_f_noise);
        self.turn_noise = float(new_t_noise);
        self.sense_noise = float(new_s_noise);

    def sense(self):
        '''

        :return:
        '''
        Z = []
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            Z.append(dist)
        return Z

    def move(self, turn, forward):
        '''

        :param turn:
        :param forward:
        :return:
        '''
        if forward < 0:
            raise ValueError, 'Robot cant move backwards'

        # turn, and add randomness to the turning command
        orientation = self.orientation + float(turn) + random.gauss(0.0, self.turn_noise)
        orientation %= 2 * pi

        # move, and add randomness to the motion command
        dist = float(forward) + random.gauss(0.0, self.forward_noise)
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)
        x %= world_size  # cyclic truncate
        y %= world_size

        # set particle
        res = robot()
        res.set(x, y, orientation)
        res.set_noise(self.forward_noise, self.turn_noise, self.sense_noise)
        return res

    def Gaussian(self, mu, sigma, x):
        '''

        :param mu:
        :param sigma:
        :param x:
        :return:
        '''
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))

    def measurement_prob(self, measurement):
        '''

        :param measurement:
        :return:
        '''
        # calculates how likely a measurement should be

        prob = 1.0;
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            prob *= self.Gaussian(dist, self.sense_noise, measurement[i])
        return prob

    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))


def eval(r, p):
    '''

    :param r:
    :param p:
    :return:
    '''
    sum = 0.0;
    for i in range(len(p)):  # calculate mean error
        dx = (p[i].x - r.x + (world_size / 2.0)) % world_size - (world_size / 2.0)
        dy = (p[i].y - r.y + (world_size / 2.0)) % world_size - (world_size / 2.0)
        err = sqrt(dx * dx + dy * dy)
        sum += err
    return sum / float(len(p))


def visualization(robot, step, p, pr, weights):
    """ Visualization
    :param robot:   the current robot object
    :param step:    the current step
    :param p:       list with particles
    :param pr:      list of resampled particles
    :param weights: particle weights
    """

    plt.figure("Robot in the world", figsize=(15., 15.))
    plt.title('Particle filter, step ' + str(step))

    # draw coordinate grid for plotting
    grid = [0, world_size, 0, world_size]
    plt.axis(grid)
    plt.grid(b=True, which='major', color='0.75', linestyle='--')
    plt.xticks([i for i in range(0, int(world_size), 5)])
    plt.yticks([i for i in range(0, int(world_size), 5)])

    # draw particles
    for ind in range(len(p)):

        # particle
        circle = plt.Circle((p[ind].x, p[ind].y), 1., facecolor='#ffb266', edgecolor='#994c00', alpha=0.5)
        plt.gca().add_patch(circle)

        # particle's orientation
        arrow = plt.Arrow(p[ind].x, p[ind].y, 2*cos(p[ind].orientation), 2*sin(p[ind].orientation), alpha=1., facecolor='#994c00', edgecolor='#994c00')
        plt.gca().add_patch(arrow)


    # draw resampled particles
    for ind in range(len(pr)):

        # particle
        circle = plt.Circle((pr[ind].x, pr[ind].y), 1., facecolor='#66ff66', edgecolor='#009900', alpha=0.5)
        plt.gca().add_patch(circle)

        # particle's orientation
        arrow = plt.Arrow(pr[ind].x, pr[ind].y, 2*cos(pr[ind].orientation), 2*sin(pr[ind].orientation), alpha=1., facecolor='#006600', edgecolor='#006600')
        plt.gca().add_patch(arrow)

    # fixed landmarks of known locations
    for lm in landmarks:
        circle = plt.Circle((lm[0], lm[1]), 1., facecolor='#cc0000', edgecolor='#330000')
        plt.gca().add_patch(circle)

    # robot's location
    circle = plt.Circle((robot.x, robot.y), 1., facecolor='#6666ff', edgecolor='#0000cc')
    plt.gca().add_patch(circle)

    # robot's orientation
    arrow = plt.Arrow(robot.x, robot.y, 2*cos(robot.orientation), 2*sin(robot.orientation), alpha=0.5, facecolor='#000000', edgecolor='#000000')
    plt.gca().add_patch(arrow)
    # plt.show()
    # plt.savefig("output/figure_" + str(step) + ".jpg")
    plt.savefig("/home/chu-chu/PycharmProjects/technical_interview/particle_filter_output/figure_" + str(step) + ".png")
    plt.close()


def main():

    ### introduction to the robot class

    # create a robot
    myrobot = robot()
    print myrobot

    # set noise parameters
    myrobot.set_noise(5., .1, 5.)

    # set robot's initial position and orientation
    myrobot.set(30., 50., pi/2.)
    print myrobot

    # clockwise turn and move
    myrobot = myrobot.move(-pi/2., 15.)
    print myrobot

    print myrobot.sense()

    # clockwise turn again and move
    myrobot = myrobot.move(-pi/2., 10.)
    print myrobot

    print myrobot.sense()

    print ''
    print ''

    ### introduction to the robot class
    # create a robot for the particle filter demo
    myrobot = robot()
    myrobot = myrobot.move(0.1, 5.0)
    z = myrobot.sense()

    print 'z = ', z
    print 'myrobot = ', myrobot

    # create a set of particles
    n = 1000  # number of particles
    p = []    # list of particles

    for i in range(n):
        x = robot()
        x.set_noise(0.05, 0.05, 5.0)
        p.append(x)

    steps = 50  # particle filter steps

    for t in range(steps):
        # move the robot and sense the environment after that
        myrobot = myrobot.move(0.1, 5.)
        z = myrobot.sense()
        # now we simulate a robot motion for each of these particles
        p2 = [p[i].move(0.1,5.0) for i in range(n)]
        # p2 = []
        # for i in range(n):
        #     p2.append( p[i].move(0.1, 5.) )
        p = p2
        # generate particle weights depending on robot's measurement
        w = [p[i].measurement_prob(z) for i in range(n)]

        # for i in range(n):
        #     w.append(p[i].measurement_prob(z))

        # resampling with a sample probability proportional to the importance weight
        p3 = []

        index = int(random.random() * n)
        beta = 0.0
        mw = max(w)

        for i in range(n):
            beta += random.random() * 2.0 * mw

            while beta > w[index]:
                beta -= w[index]
                index = (index + 1) % n

            p3.append(p[index])

        # here we get a set of co-located particles
        p = p3
        print 'Step = ', t, ', Evaluation = ', eval(myrobot, p)
        # visualize the current step
        visualization(myrobot, t, p2, p3, w)


    print 'p = ', p


if __name__ == "__main__":
    main()