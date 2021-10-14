# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 13:05:33 2017

@author: Aaron Au
"""
#PYTHON 2.7


import pygame
from newportESP import ESP

#CONSTANTS
#==============================================================================
#Controller Defintions
axisCon = {'x' : 0, 'y' : 1, 'z' : 0, 'r' : 1}; #Axis x, y, Hat 0 (0,z)
buttonsCon = {'fineJog' : 4, 'corseJog' : 5, 'serial' : 7, 'home' : 6, 'stop' : 1, 'enable' : 0, 'angled': 2};
threshold = {'joystick' : 0.15, 'trigger' : 0.5};
distances = [0.00125, 0.0025, 0.005, 0.01, 0.02, 0.04];

xyzSerial = 'COM4';
rSerial = None;

#ESP300 Defintions
axisEsp = {'x' : '1', 'y' : '2', 'z' : '3', 'r' : None};
location = {'x' : 0, 'y' : 0, 'z' : 0};

#VARIABLES
#==============================================================================
xyzESP = ESP(xyzSerial);
xAxis = xyzESP.axis(axisEsp['x']);
yAxis = xyzESP.axis(axisEsp['y']);
zAxis = xyzESP.axis(axisEsp['z']);

jogDistance = distances[0];
clock = pygame.time.Clock();
notDone = True;
multiplier = {'x' : 1, 'y' : -1, 'z' : 1, 'r' : 1};

def toggleESP():
    if xyzESP.ser.isOpen():
        #CLOSE ESP
        xyzESP.ser.close();
        print('ESP Closed');
    else:
        #OPEN ESP
        xyzESP.ser.open();
        xAxis.on();
        yAxis.on();
        zAxis.on();

        print('ESP Open');

toggleESP();

pygame.init();
screen = pygame.display.set_mode([100,20])
pygame.joystick.init();

if (pygame.joystick.get_count() < 1):
    print('No Joystick Found')
else:    
    while notDone:
        
        joystick = pygame.joystick.Joystick(0);
        joystick.init();        
        
        command = ""; #Empty Command        
        if xyzESP.ser.isOpen():
            if joystick.get_button(buttonsCon['enable']) and joystick.get_button(buttonsCon['angled']): #X and Z move together
                #X Axis Movement
                x_axis = joystick.get_axis(axisCon['x']);
                if abs(x_axis) >= threshold['joystick'] :
                    xAxis.move_by(x_axis*multiplier['x']*jogDistance, True);
                    zAxis.move_by((-1)*x_axis*multiplier['x']*jogDistance, True);
                #Y Axis Movement
                y_axis = joystick.get_axis(axisCon['y']);
                if abs(y_axis) >= threshold['joystick']:
                    yAxis.move_by(y_axis*multiplier['y']*jogDistance, True);
                #Z Axis Movement
                z_axis = joystick.get_hat(axisCon['z'])[1];
                if z_axis != 0:
                    zAxis.move_by(z_axis*multiplier['z']*jogDistance, True);
                    xAxis.move_by(z_axis*multiplier['z']*jogDistance, True);
                r_axis = joystick.get_hat(axisCon['z'])[0];
                '''if r_axis != 0 and rSerial != None:
                    command = command + axisEsp['r'] + 'pr' + str.format("{0:.5f}", r_axis*multiplier['r']*jogDistance) + ';';'''
            elif joystick.get_button(buttonsCon['enable']):
                #X Axis Movement
                x_axis = joystick.get_axis(axisCon['x']);
                if abs(x_axis) >= threshold['joystick'] :
                    xAxis.move_by(x_axis*multiplier['x']*jogDistance, True);
                #Y Axis Movement
                y_axis = joystick.get_axis(axisCon['y']);
                if abs(y_axis) >= threshold['joystick']:
                    yAxis.move_by(y_axis*multiplier['y']*jogDistance, True);
                #Z Axis Movement
                z_axis = joystick.get_hat(axisCon['z'])[1];
                if z_axis != 0:
                    zAxis.move_by(location['z']+z_axis*multiplier['z']*jogDistance, True)
                r_axis = joystick.get_hat(axisCon['z'])[0];
                '''if r_axis != 0 and rSerial != None:
                    command = command + axisEsp['r'] + 'pr' + str.format("{0:.5f}", r_axis*multiplier['r']*jogDistance) + ';';'''
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                notDone = False;
            if event.type == pygame.JOYBUTTONDOWN:
                '''if joystick.get_button(buttonsCon['home']) and joystick.get_button(buttonsCon['enable']):
                    command = axisEsp['x']+'OR;'+axisEsp['y']+'OR;'+axisEsp['z']+'OR;'''
                if joystick.get_button(buttonsCon['stop']) and xyzESP.ser.isOpen():
                    xAxis.off();
                    yAxis.off();
                    zAxis.off();
                #Serial Toggle
                if joystick.get_button(buttonsCon['serial']):
                    toggleESP();
                
                #Jog Distances
                if joystick.get_button(buttonsCon['fineJog']):
                    index = distances.index(jogDistance);
                    if index > 0:
                        jogDistance = distances[index-1];
                    print (jogDistance);
                if joystick.get_button(buttonsCon['corseJog']):
                    index = distances.index(jogDistance);
                    if index < len(distances)-1:
                        jogDistance = distances[index+1];
                    print (jogDistance);
        
        pygame.display.flip();
        #clock.tick(2);

pygame.quit();
