import mraa
import time




def temp():
    x = mraa.Gpio(26)
    x.dir(mraa.DIR_OUT)
    ads1115 = mraa.I2c(0)
    ads1115.address(0x48)
    #for i in range(0, 10):
    ads1115.writeWordReg(1, 0x83C1)
    raw = ads1115.readWordReg(0)
    analogValue = ((raw&0xff00)>>8)+((raw&0x00ff)<<8)
    dat=(85 * analogValue) /4096                                 
    celsius = dat
    fahrenheit = celsius * 9.0/5.0 + 32.0;
        #print "%d degrees Celsius, or %d degrees Fahrenheit" \
            #% (celsius, fahrenheit)
        #time.sleep(1)
    return fahrenheit     
