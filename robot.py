import time
from smbus import SMBus
from adafruit_servokit import ServoKit  # Set channels to the number of servo channels on your kit.
import serial
serialPort = serial.Serial(port = "/dev/ttyS0", baudrate=38400,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

def ultrasonic_read(address):
    i2c_bus = SMBus(1)
    i2c_bus.write_byte_data(address, 0, 0x51)  # Tell sensor to scan in mm

    high = i2c_bus.read_byte_data(address, 2)  # Read the high byte of the value
    #print(high) # print the value of High byte

    low = i2c_bus.read_byte_data(address, 3)  # Read the low byte of the value
    #print(low) # print the value of low byte

    current_value = high * 256 + low
    return current_value


def forward_1(duty): # (motor, duty, direction)
    F_duty = '((' + 'AF' + str(int(abs(duty))) + '))'
    serialPort.write(str.encode(F_duty))

def backward_1(duty):
    R_duty = '((' + 'AR' + str(int(abs(duty))) + '))'
    serialPort.write(str.encode(R_duty))




address_1 = 70
address_2 = 71

sensor1 = ultrasonic_read(address_1)
sensor2 = ultrasonic_read(address_2)

serialPort.write(b'((AF50))') #Both motors forward at 50% duty cycle
if sensor1 == 0 or sensor2 == 0:
    time.sleep(6)
    serialPort.write(b'((AR40))') #Both motors in reverse at 40% duty cycle
    time.sleep(2)
    serialPort.write(b'((AR000))') # Stop both motors







