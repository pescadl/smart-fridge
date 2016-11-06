import mraa
import time

x = mraa.Gpio(35)
x.dir(mraa.DIR_OUT)
x.write(1)