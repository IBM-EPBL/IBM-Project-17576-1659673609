import random as r                                 #importing random module as r for generating random values from 0 to 99

class Measurement:                                 #created a Measurement class for reusability and cleaniness of code
    def __init__(self, temperature, humidity):     #Passed two methods temperature and humidity
        self.temperature = temperature
        self.humidity = humidity

while(True):                                       #while loop for continuous monitoring of temperature and humidity value

    random_temp_value = int(r.randint(0,99))       #Generating value from 0 to 99 for temperature
    random_hum_value = int(r.randint(0,99))        #Generating value from 0 to 99 for humidity

    class_init = Measurement(random_temp_value , random_hum_value)  #calling class Measurement with two arguments


    if(class_init.temperature >= 40 or class_init.humidity >= 70):  #Control flow  
        print("Alarm is HIGH!!")                                    # Alarm is HIGH!! when both the condition are true
    else:
        print("Alarm is LOW")                                       #Alarm is LOW when both the condition are false