# UART Serial Bus Output Demo - Simple output program for testing serial connection
# Author: Alex Bowen (Orbit Development, LLC)
#
# OpenMV Cam Tutorial : https://docs.openmv.io/openmvcam/tutorial/index.html
#
# OpenMV H7 Plus Datasheet : https://cdn.sparkfun.com/assets/a/3/f/d/9/OpenMV-H7_Datasheet.pdf
#       UART(1) : (TX, RX) = (P1, P0)
#       UART(3) : (TX, RX) = (P4, P5)
#
# pyb.UART Documentation : https://docs.openmv.io/library/pyb.UART.html

from pyb import UART
import time

clock = time.clock()
uart = pyb.UART(3, 9600)  # UART(3) on pins P4 (TX) and P5 (RX), baudrate 9600
#uart = pyb.UART(1, 9600)  # UART(1) on pins P1 (TX) and P0 (RX), baudrate 9600


print_interval = 1 # Print to UART every [print_interval] seconds


while True:
    clock.tick()

    uart.write("test\n")    # In the production program, the camera will simply write
                            # a string with the most recent count number to the serial line
                            # for us to read and process in the node firmware.

    time.sleep(print_interval) # Pause execution
