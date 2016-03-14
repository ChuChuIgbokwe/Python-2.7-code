#!/usr/bin/env python
"""
Created on Sat Feb  7 22:30:17 2015

@author: chu-chu
"""

import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('mp2_data.dat')
groundtruth_u_i = data[0:,0]
groundtruth_v_i = data[0:,1]
noisy_u_i = data[0:,2]
noisy_v_i = data[0:,3]


def constant_vel_kf():
    '''
    Kalman filter using a constant velocity model
    '''
    sz =  len(groundtruth_u_i)
    T = 1 #sample time
    F = np.matrix([[1,0,T,0],[0,1,0,T],[0,0,1,0],[0,0,0,1]])
    H = np.matrix([[1,0,0,0],[0,1,0,0]])
    Q = np.matrix(np.eye(F.shape[0]))
    ra = 1000.0**2
    R = np.matrix([[ra, 0.0],[0.0, ra]])
    I = np.matrix(np.eye(F.shape[0]))
    P = np.diag([1000.0, 1000.0, 1000.0, 1000.0])
#    initialize empty lists
    xt = []
    yt = []
    dxt= []
    dyt= []

    for i in range(sz):
        # PREDICT x, P based on motion
        x = np.matrix([groundtruth_u_i[i],groundtruth_v_i[i],10,10]).T
        z = np.matrix([noisy_u_i[i],noisy_v_i[i]]).T
        x = F*x
        P = F*P*F.T + Q

        y = z - H * x #error
        S = H * P * H.T + R  # residual convariance
        K = P * H.T * np.linalg.pinv(S)    # Kalman gain
        x = x + K*y
        #convert to list so you can append it to initialised empty lists
        x = np.array(x).reshape(-1,).tolist()
        P = (I - K*H)*P

        xt.append(x[0])
        yt.append(x[1])
        dxt.append(x[2])
        dyt.append(x[3])

    plt.figure(1)
    plt.title('Kalman Filter Constant Velocity Model')
    plt.ylabel('Y-Axis')
    plt.xlabel('X-Axis')
    plt.plot(groundtruth_u_i,groundtruth_v_i, '-b', label='Groundtruth')
    plt.plot(noisy_u_i,noisy_v_i, '-g', label='Noisy Observations')
    plt.plot(xt,yt, '-r', label='Kalman Filter')
    plt.legend(loc='upper left')
    plt.show()


def constant_acceleration_kf():
    '''
    Kalman filter using a constant acceleration model
    '''
    sz =  len(groundtruth_u_i)
    T = 1 #sample time
    F = np.matrix([[1,0,T,0,(T**2/2),0],[0,1,0,T,0,(T**2/2)],[0,0,1,0,T,0],[0,0,0,1,0,T],[0,0,0,0,1,0],[0,0,0,0,0,1]])
    H = np.matrix([[1,0,0,0,0,0],[0,1,0,0,0,0]])
    Q = np.matrix(np.eye(F.shape[0]))*10000
    ra = 1000.0**2 #originally 10.0
    R = np.matrix([[ra, 0.0],[0.0, ra]])
    R = np.matrix(np.eye(2))*1000**2
    I = np.matrix(np.eye(F.shape[0]))
    P = np.diag([1000.0, 1000.0, 1000.0, 1000.0,1000.0,1000.0])
    xt = []
    yt = []
    dxt= []
    dyt= []
    ddxt = [] #acceleration x
    ddyt = [] #acceleration y
    prediction_x = []
    prediction_y = []
    for i in range(sz):
        # PREDICT x, P based on motion
        x = np.matrix([groundtruth_u_i[i],groundtruth_v_i[i],10,10,10,10]).T
        z = np.matrix([noisy_u_i[i],noisy_v_i[i]]).T
        x = F*x
        P = F*P*F.T + Q
        # UPDATE x, P based on measurement m
        # distance between measured and current position-belief
        y = z - H * x #error
        S = H * P * H.T + R  # residual convariance
        K = P * H.T * np.linalg.pinv(S)    # Kalman gain
        x = x + K*y
        #convert to list so you can append it to initialised empty lists
        x = np.array(x).reshape(-1,).tolist()
        P = (I - K*H)*P

        xt.append(x[0])
        yt.append(x[1])
        dxt.append(x[2])
        dyt.append(x[3])
        ddxt.append(x[4])
        ddyt.append(x[5])

    plt.figure(2)
    plt.title('Kalman Filter Constant Acceleration Model')
    plt.ylabel('Y-Axis')
    plt.xlabel('X-Axis')
    plt.plot(groundtruth_u_i,groundtruth_v_i, '-b', label='Groundtruth')
    plt.plot(noisy_u_i,noisy_v_i, '-g', label='Noisy Observations')
    plt.plot(xt,yt, '-r', label='Kalman Filter')
    plt.legend(loc='upper left')
    plt.show()


def main():
    constant_vel_kf()
    constant_acceleration_kf()


if __name__ == '__main__':
    main()