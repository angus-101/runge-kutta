# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:05:08 2019

@author: angus
"""

###############################################################################

import matplotlib.pyplot as plt                                                 # Imports.
import numpy as np

###############################################################################

G = 6.67e-11                                                                    # Constants.
EarthMass = 5.972e24
EarthRadius = 6371000
EarthMoonDist = 384400000
MoonRadius = 1737100
MoonMass = 7.34767309e22

###############################################################################

def f1(v_x):                                                                    # Defining the functions for the orbits.
    
    return v_x    

def f2(v_y):                                                                    # f1 and f2 apply for both part a and part b.
    
    return v_y

def f3(x, y):                                                                   # f3 and f4 apply for only part a.
    
    num = -G * PlanetMass * x
    r = (x ** 2 + y ** 2) ** (3 / 2)
    
    return num / r

def f4(x, y):
    
    num = -G * PlanetMass * y
    r = (x ** 2 + y ** 2) ** (3 / 2)
    
    return num / r

def f5(x, y):                                                                   # f5 and f6 apply for only part b.
    
    num = -G * EarthMass * x
    r = (x ** 2 + y ** 2) ** (3 / 2) 
    num_m = - G * MoonMass * (x - EarthMoonDist)
    r_m = ((x - EarthMoonDist) ** 2 + y ** 2) ** (3 / 2)
    
    return num / r + num_m / r_m

def f6(x, y):
    
    num = -G * EarthMass * y
    r = (x ** 2 + y ** 2) ** (3 / 2) 
    num_m = - G * MoonMass * y
    r_m = ((x - EarthMoonDist) ** 2 + y ** 2) ** (3 / 2)
    
    return num / r + num_m / r_m

###############################################################################

def valueCheckPosFloat(value):                                                  # This function checks that the user has input a positive float when they're meant to.
    
    while value.isalpha() or float(value) <= 0:
        
        print("You require a positive float!")
        value = input("Please enter a positive float: ")
    
    value = float(value)
    
    return value

###############################################################################

def orbit1(delta_t):                                                            # Defining the function that calculates the k values for part a.
    
    n = 0                                                                       # Variable to be incremented with each cycle of the loop.
    StartPoint = '0'
    StartPoint = False                                                          # Boolean that says if the rocket has reached the beginning of its orbit.

    while StartPoint == False:
        
        k_1_x.append(f1(v_x[n]))
        k_1_y.append(f2(v_y[n]))
        k_1_v_x.append(f3(x[n], y[n]))
        k_1_v_y.append(f4(x[n], y[n]))
        
        k_2_x.append(f1(v_x[n] + delta_t * k_1_v_x[n] / 2))
        k_2_y.append(f2(v_y[n] + delta_t * k_1_v_y[n] / 2))
        k_2_v_x.append(f3(x[n] + delta_t * k_1_x[n] / 2, y[n] + delta_t * k_1_y[n] / 2))
        k_2_v_y.append(f4(x[n] + delta_t * k_1_x[n] / 2, y[n] + delta_t * k_1_y[n] / 2))
        
        k_3_x.append(f1(v_x[n] + delta_t * k_2_v_x[n] / 2))
        k_3_y.append(f2(v_y[n] + delta_t * k_2_v_y[n] / 2))
        k_3_v_x.append(f3(x[n] + delta_t * k_2_x[n] / 2, y[n] + delta_t * k_2_y[n] / 2))
        k_3_v_y.append(f4(x[n] + delta_t * k_2_x[n] / 2, y[n] + delta_t * k_2_y[n] / 2))
        
        k_4_x.append(f1(v_x[n] + delta_t * k_3_v_x[n]))
        k_4_y.append(f2(v_y[n] + delta_t * k_3_v_y[n]))
        k_4_v_x.append(f3(x[n] + delta_t * k_3_x[n], y[n] + delta_t * k_3_y[n]))
        k_4_v_y.append(f4(x[n] + delta_t * k_3_x[n], y[n] + delta_t * k_3_y[n]))
        
        x.append(x[n] + delta_t / 6 * (k_1_x[n] + 2 * k_2_x[n] + 2 * k_3_x[n] + k_4_x[n]))
        y.append(y[n] + delta_t / 6 * (k_1_y[n] + 2 * k_2_y[n] + 2 * k_3_y[n] + k_4_y[n]))
        v_x.append(v_x[n] + delta_t / 6 * (k_1_v_x[n] + 2 * k_2_v_x[n] + 2 * k_3_v_x[n] + k_4_v_x[n]))
        v_y.append(v_y[n] + delta_t / 6 * (k_1_v_y[n] + 2 * k_2_v_y[n] + 2 * k_3_v_y[n] + k_4_v_y[n]))
        time.append(time[n] + delta_t)
        
        speed.append(np.sqrt(v_x[n] ** 2 + v_y[n] ** 2))
        r.append(np.sqrt(x[n] ** 2 + y[n] ** 2))
        KE.append(1/2 * RocketMass * speed[n] ** 2)
        PE.append(-G * PlanetMass * RocketMass / r[n])
        energy.append(KE[n] + PE[n])
        
        if r[-1] <= PlanetRadius:                                               # Condition for checking if the rocket hits the planet's surface.
                
            print()
            print("-" * 28 + " YOU CRASHED " + "-" * 29)
            print()
            print("-" * 70)
            break
            
        if x[-1] < 0 and y[-2] > 0 and y[-1] < 0 or time[-1] > 5e5 * delta_t:   # Condition for if the rocket has reached the start point.
                                                                                # There is also a time condition for if the rocket escapes the planet's gravity.
            StartPoint = True
    
        n += 1
                   
    time.pop()
        
    plt.plot(time, KE, label = 'Kinetic energy')                                # Plotting KE, PE, and total energy versus time graphs.
    plt.plot(time, PE, label = 'Potential energy')
    plt.plot(time, energy, label = 'Total energy')     
    
    plt.xlabel("Time / s")
    plt.ylabel("Energy / J")
    plt.legend()
    plt.show()
        
    return(x, y, v_x, v_y, time, speed, r, KE, PE, energy)
    
def orbit2(delta_t):                                                            # Defining the function that calculates the k values for part b.
    
    n = 0
    StartPoint = '0'
    StartPoint = False

    while StartPoint == False:
        
        k_1_x.append(f1(v_x[n]))
        k_1_y.append(f2(v_y[n]))
        k_1_v_x.append(f5(x[n], y[n]))
        k_1_v_y.append(f6(x[n], y[n]))
        
        k_2_x.append(f1(v_x[n] + delta_t * k_1_v_x[n] / 2))
        k_2_y.append(f2(v_y[n] + delta_t * k_1_v_y[n] / 2))
        k_2_v_x.append(f5(x[n] + delta_t * k_1_x[n] / 2, y[n] + delta_t * k_1_y[n] / 2))
        k_2_v_y.append(f6(x[n] + delta_t * k_1_x[n] / 2, y[n] + delta_t * k_1_y[n] / 2))
        
        k_3_x.append(f1(v_x[n] + delta_t * k_2_v_x[n] / 2))
        k_3_y.append(f2(v_y[n] + delta_t * k_2_v_y[n] / 2))
        k_3_v_x.append(f5(x[n] + delta_t * k_2_x[n] / 2, y[n] + delta_t * k_2_y[n] / 2))
        k_3_v_y.append(f6(x[n] + delta_t * k_2_x[n] / 2, y[n] + delta_t * k_2_y[n] / 2))
        
        k_4_x.append(f1(v_x[n] + delta_t * k_3_v_x[n]))
        k_4_y.append(f2(v_y[n] + delta_t * k_3_v_y[n]))
        k_4_v_x.append(f5(x[n] + delta_t * k_3_x[n], y[n] + delta_t * k_3_y[n]))
        k_4_v_y.append(f6(x[n] + delta_t * k_3_x[n], y[n] + delta_t * k_3_y[n]))
        
        x.append(x[n] + delta_t / 6 * (k_1_x[n] + 2 * k_2_x[n] + 2 * k_3_x[n] + k_4_x[n]))
        y.append(y[n] + delta_t / 6 * (k_1_y[n] + 2 * k_2_y[n] + 2 * k_3_y[n] + k_4_y[n]))
        v_x.append(v_x[n] + delta_t / 6 * (k_1_v_x[n] + 2 * k_2_v_x[n] + 2 * k_3_v_x[n] + k_4_v_x[n]))
        v_y.append(v_y[n] + delta_t / 6 * (k_1_v_y[n] + 2 * k_2_v_y[n] + 2 * k_3_v_y[n] + k_4_v_y[n]))
        time.append(time[n] + delta_t)
        
        speed.append(np.sqrt(v_x[n] ** 2 + v_y[n] ** 2))
        r.append(np.sqrt(x[n] ** 2 + y[n] ** 2))
        r_m.append(np.sqrt((x[n] - EarthMoonDist) ** 2 + y[n] ** 2))            # Another array for storing the distance between the rocket and the centre of the moon.
        KE.append(1/2 * RocketMass * speed[n] ** 2)
        PE_Earth.append(-G * EarthMass * RocketMass / r[n])
        PE_Moon.append(-G * MoonMass * RocketMass / (r[n] + EarthMoonDist))
        PE.append(PE_Earth[n] + PE_Moon[n])
        energy.append(KE[n] + PE[n])
        
        if r[-1] <= EarthRadius or r_m[-1] <= MoonRadius:
                
            print()
            print("-" * 28 + " YOU CRASHED " + "-" * 29)
            print()
            print("-" * 70)
            break
          
        if x[-1] < 0 and y[-2] > 0 and y[-1] < 0 or time[-1] > 5e5 * delta_t:
                
            StartPoint = True
    
        n += 1
        
    time.pop()
        
    plt.plot(time, KE, label = 'Kinetic energy')        
    plt.plot(time, PE, label = 'Potential energy')
    plt.plot(time, energy, label = 'Total energy')     
    
    plt.xlabel("Time / s")
    plt.ylabel("Energy / J")
    plt.legend()
    plt.show()
        
    return(x, y, v_x, v_y, time, speed, r, KE, PE, energy)
    
###############################################################################
    
def Planet(PlanetRadius):                                                       # Function that plots the planet.
                                                                                # The planet is actually a series of dense concentric cirlces, but looks solid.
    radius = 0

    while radius <= PlanetRadius:                                               # Each circle is constructed for a given radius, then the radius is incremented.
            
        angle = 0
            
        while angle <= 2 * np.pi:
                
            Planet_x.append(radius * np.sin(angle))
            Planet_y.append(radius * np.cos(angle))
            angle += 0.1
                
        radius += 5000
        
    return(Planet_x, Planet_y)
        
def EarthMoon(EarthRadius, MoonRadius, EarthMoonDist):                          # The same fucntion, but plots the Earth and the Moon.
        
    radius = 0
    
    while radius <= EarthRadius:
            
        angle = 0
            
        while angle <= 2 * np.pi:
                
            Earth_x.append(radius * np.sin(angle))
            Earth_y.append(radius * np.cos(angle))
            angle += 0.1
                
            radius += 5000
    
    
    radius = 0
        
    while radius <= MoonRadius:
            
        angle = 0
            
        while angle <= 2 * np.pi:
                
            Moon_x.append(radius * np.sin(angle) + EarthMoonDist)
            Moon_y.append(radius * np.cos(angle))
            angle += 0.1
                
        radius += 500                                                           # Smaller increment because the Moon is smaller than the Earth.
            
    return(Earth_x, Earth_y, Moon_x, Moon_y)
    
###############################################################################

MyInput = '0'                                                                   # Menu system for ease of use.
while MyInput != 'q':
    
###############################################################################
    
    k_1_x = []                                                                  # Defining the arrays that store the k values, position and velocity values, and other variables.
    k_1_y = []
    k_1_v_x = []
    k_1_v_y = []
    
    k_2_x = []
    k_2_y = []
    k_2_v_x = []
    k_2_v_y = []
    
    k_3_x = []
    k_3_y = []
    k_3_v_x = []
    k_3_v_y = []
    
    k_4_x = []
    k_4_y = []
    k_4_v_x = []
    k_4_v_y = []
    
    r = []
    r_m = []
    x = []
    y = [0]
    v_x = [0]
    v_y = []
    time = [0]
    
    Planet_x = []
    Planet_y = []
    Earth_x = []
    Earth_y = []
    Moon_x = []
    Moon_y = []
    
    KE = []
    PE_Earth = []
    PE_Moon = []
    PE = []
    energy = []
    speed = []
    
###############################################################################
    
    print()                                                                     # Brief descriptions of what each section does.
    print("-" * 70)
    print()
    print("Option 'a' simulates a planet, whos radius and mass are input by the")
    print("user. They are then asked to provide an initial distance and")
    print("velocity of a rocket, and the trajectory of the rocket is plotted.")
    print()
    print("Option 'b' simulates the Earth and the Moon. The user is asked for")
    print("an initial height and velocity, and the orbit is plotted.")
    print()
    print("-" * 70)
    
    MyInput = input("Please choose option a, b, or q, to quit: ")               # The user enters their section choice here.
    print()
    print("You entered the choice: " + MyInput)
    print()
    print("-" * 70)
    
###############################################################################
    
    if MyInput == 'a':
        
        PlanetRadius = input("Enter the planet's radius in m (Earth = 6,371,000 m): ")
        PlanetRadius = valueCheckPosFloat(PlanetRadius)                         # User input variables and variable checks.
        
        PlanetMass = input("Enter the planet's mass in kg (Earth = 5.972e24 kg): ")
        PlanetMass = valueCheckPosFloat(PlanetMass)
        
        RocketMass = input("Enter the rocket's mass in kg (~2e6 kg): ")
        RocketMass = valueCheckPosFloat(RocketMass)
                
        x0 = input("Enter the rocket's initial distance from the surface of the planet in m: ")
        x0 = valueCheckPosFloat(x0)
        x0 += PlanetRadius
        x.append(-x0)
        
        print()
        CircOrbVel = np.sqrt(G * PlanetMass / abs(x[0]))                        # Calculations of the escape velocity and velocity needed for a circular orbit.
        EscVel = np.sqrt(2 * G * PlanetMass / abs(x[0]))
        print("For a circular orbit at this radius, you need a velocity of " + str(round(CircOrbVel, 1)) + " m/s,")
        print("while the escape velocity is " + str(round(EscVel, 1)) + " m/s.")
        
        v0 = input("Enter the rocket's initial speed in m/s: ")
        v0 = valueCheckPosFloat(v0)
        v_y.append(-v0)
        
        delta_t = input("Enter the timestep in s (~" + str(round(x0 / 7e5, 2)) + "s): ")
        delta_t = valueCheckPosFloat(delta_t)
        print()
        print("-" * 70)
        
        orbit1(delta_t)                                                         # Calling the above defined functions.
            
        Planet(PlanetRadius)
        
        plt.plot(Planet_x, Planet_y, color = 'b', label = 'Your planet')        # Plotting the planet and rocket path.
        plt.plot(x, y, color = 'black', label = "Rocket's path")
        plt.xlabel("x coordinate")
        plt.ylabel("y coordinate")
        plt.axis('equal')   
        plt.legend()
        plt.show()
        
###############################################################################

    elif MyInput == 'b':
        
        RocketMass = input("Enter the rocket's mass in kg (~2e6 kg): ")
        RocketMass = valueCheckPosFloat(RocketMass)
        
        x0 = input("Enter the rocket's initial distance from the surface of the Earth in m: ")
        x0 = valueCheckPosFloat(x0)
        x0 += EarthRadius
        x.append(-x0)
        
        v0 = input("Enter the rocket's initial speed in m/s (7570 m/s for a figure of 8 orbit at 7000 km): ")
        v0 = valueCheckPosFloat(v0)
        v_y.append(-v0)
        
        delta_t = input("Enter the timestep in s (~" + str(round(x0 / 7e5, 2)) + "s): ")
        delta_t = valueCheckPosFloat(delta_t)
        print()
        print("-" * 70)
        
        orbit2(delta_t)
        
        EarthMoon(EarthRadius, MoonRadius, EarthMoonDist)
        
        plt.plot(Earth_x, Earth_y, color = 'b', label = 'Earth')
        plt.plot(Moon_x, Moon_y, color = 'lightslategrey', label = 'Moon')
        plt.plot(x, y, color = 'black', label = "Rocket's path", lw = 0.4)
        plt.xlabel("x coordinate")
        plt.ylabel("y coordinate")
        plt.axis('equal')
        plt.legend()
        plt.show()
        
        print()
        MoonMin = round((min(r_m) - MoonRadius) / 1000, 1)                      # Calculating the distance of closest approach to the Moon.
        TimeTakenS = int(time[-1])
        TimeTakenH = int(time[-1] / 3600)
        TimeTakenM = int(((time[-1] / 3600) % 1) * 60)
        remainder = int(time[-1] % 60)
        print("The distance of closest approach to the moon was " + str(MoonMin) + " km.")
        print("The time taken for the orbit was " + str(TimeTakenS) + " s, or " + str(TimeTakenH))
        print("hours, " + str(TimeTakenM) + " minutes, " + str(remainder) + " seconds.")
        
###############################################################################
        
    elif MyInput != 'q':        
         
        print()
        print("-" * 21 + " PLEASE ENTER A VALID INPUT " + "-" * 21)
        
###############################################################################

print()    
print("-" * 26 + " CLOSING PROGRAM " + "-" * 27)
print()
print("-" * 70)

###############################################################################
        
        

    


























