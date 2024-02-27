from machine import ADC, Pin
import time

class Relay:
    def __init__(self, ePin, status='OFF')
        self.pin = ePin
        self.status = status
        self.relay = Pin(self.pin, Pin.OUT)
        
    def switch(self):
        if self.status == 'ON':
            self.relay.value(0)
        else
            self.relay.value(1)
        end if
        

class PushButton:
    def __init__(self, ePin):
        self.pin = ePin
        self.push_button = Pin(self.pin, Pin.IN)
        
    def getData(self):
        while True:
            self.button_value = self.push_button.value()
            if self.button_value == 0:
                print("button pressed")
            sleep(0.2)


relay = Relay(4, 'ON')
relay.switch

'''
 web for viewing ESP8266 Pinout
 https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/05/ESP8266-NodeMCU-kit-12-E-pinout-gpio-pin.png?w=817&quality=100&strip=all&ssl=1

'''
soil = ADC(0) # read analog value through AO pin


# set pin to turn on or off soil moisture sensor
soil_pin = 5 # pin for moisture sensor
soil_plug = Pin(soil_pin, Pin.OUT)




def extract_data:
    
    '''
    I want to loop for reading soil moisture value in 20 loops because I need still value from the sensor.
'''
    for i in range(20):
        
        soil_plug.value(1) # turn on soil moisture sensor
        time.sleep(2) # wait for soil moisture sensor preparing to read value
        
#         print(soil.read())
        soil_value = soil.read() # read and keep the value in variable
        
        soil_plug.value(0) # turn off soil moisture sensor
        
    return soil_value
        
     
    
    

