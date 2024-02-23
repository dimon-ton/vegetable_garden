from machine import ADC, Pin
import time



soil = ADC(0)

soil_pin = 5
soil_plug = Pin(soil_pin, Pin.OUT)



while True:
     
    soil_plug.value(1)
    time.sleep(2)
    print(soil.read())
    soil_plug.value(0)
    time.sleep(2)
 
    
