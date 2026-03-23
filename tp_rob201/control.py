""" A set of robotics control functions """

import random
import numpy as np


def reactive_obst_avoid(lidar, rotationHistory, iteration):
    """
    Simple obstacle avoidance
    lidar : placebot object with lidar data
    """
    # TODO for TP1

    laser_dist = lidar.get_sensor_values()  #liste de taille 361, en face c'est donc laser_dist[180]
                                            #l'ordre de grandeur est de 100 pour 2cm environ
    speed = 0.0
    rotation_speed = 0.0

    command = {"forward": speed,
               "rotation": rotation_speed}
    
    isObstacle=False
    minDist=min(laser_dist[135:225])    #on prend le minimum dans un cône de vision de 90°
    angleMin=np.argmin(laser_dist)

    if minDist < 50 :
        isObstacle=True
    else :
        isObstacle=False

    if not isObstacle :
        command["forward"]=0.5
        command["rotation"]=0
    else : 
        command["forward"]=0
        if(angleMin<180) :  #on tourne dans le sens opposé par rapport au mur
            command["rotation"]=0.5
            rotationHistory+=0.5
        else :
            command["rotation"]=-0.5
            rotationHistory-=0.5
        iteration+=1
    return command


def potential_field_control(lidar, current_pose, goal_pose):
    """
    Control using potential field for goal reaching and obstacle avoidance
    lidar : placebot object with lidar data
    current_pose : [x, y, theta] nparray, current pose in odom or world frame
    goal_pose : [x, y, theta] nparray, target pose in odom or world frame
    Notes: As lidar and odom are local only data, goal and gradient will be defined either in
    robot (x,y) frame (centered on robot, x forward, y on left) or in odom (centered / aligned
    on initial pose, x forward, y on left)
    """
    # TODO for TP2

    command = {"forward": 0,
               "rotation": 0}

    return command
