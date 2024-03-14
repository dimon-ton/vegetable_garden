# main.py -- put your code here!

from machine import ADC, Pin
import time
from time import sleep, sleep_ms

class Relay():
    def __init__(self, ePin):
        self.pin = ePin
        self.r = Pin(self.pin, Pin.OUT)
        self.r.value(1)
        
    def switch(self, status=''):
        self.status = status
        if self.status == 'ON':
            self.r.value(0)
        elif status == 'OFF':
            self.r.value(1)
        
        return self.r.value()
    

        

class PushButton:
    def __init__(self, ePin):
        self.pin = ePin
        self.push_button = Pin(self.pin, Pin.IN, Pin.PULL_UP)
        
        
    def getData(self):
            self.button_value = self.push_button.value()
            if self.button_value == 0:
                return self.button_value
            else:
                return self.button_value

class SoilSensor:
    def __init__(self,soil_pin):
        self.soil = ADC(0)
        self.soil_pin = soil_pin # pin for moisture sensor default --> 5
        self.soil_plug = Pin(self.soil_pin, Pin.OUT)
        self.soil_plug.value(0) # turn off moisture sensor
        
        
    def extract_data(self):
    
        '''
            I want to loop for reading soil moisture value in 20 loops because I need still value from the sensor.
        '''
        for i in range(20):
            
            self.soil_plug.value(1) # turn on soil moisture sensor
            time.sleep(2) # wait for soil moisture sensor preparing to read value
            
    #         print(soil.read())
            self.soil_value = self.soil.read() # read and keep the value in variable
            
            self.soil_plug.value(0) # turn off soil moisture sensor
            
        return self.soil_value
        

relay01 = Relay(4)
pushB = PushButton(12)
    

status_relay_array = ["ON", "OFF"]

relay_switch = 1
relay_status = 1

# button
button_status = 1
last_button_status = 1
button_pressed = False
mode = "OFF"

while True:

    
    button_status = pushB.getData()
    

    if button_status != last_button_status:
        time.sleep_ms(20)
        
        button_status = pushB.getData()
        
        if button_status == 0:
            button_pressed = True
        else:
            button_pressed = False
            
    if button_pressed and not last_button_status:
        
        
        if mode == 'OFF':
            mode = 'ON'
        elif mode == 'ON':
            mode = 'AUTO'
        else:
            mode = 'OFF'

        # Update relay status accordingly
        if mode == 'ON':
            relay01.switch('ON')
        elif mode == 'OFF':
            relay01.switch('OFF')
        
        
        print("Mode:", mode)
        
        
#         if not relay01.switch():
#             msg = "OFF"
#         else:
#             msg = "ON"
# 
#         relay01.switch(msg)



        sleep(0.5)
 
   
    last_button_status = button_status
        
                
        


'''
 web for viewing ESP8266 Pinout
 https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/05/ESP8266-NodeMCU-kit-12-E-pinout-gpio-pin.png?w=817&quality=100&strip=all&ssl=1

'''




     

    
