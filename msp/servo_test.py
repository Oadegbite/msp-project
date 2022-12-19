from adafruit_servokit import ServoKit

myKit = ServoKit(channels=16)



MAX_ANGLE = 180

next_angle = 0

step = 30

def move_servo(servo, new_angle):	
	myKit.servo[servo].angle=new_angle
	print(f"current_angle:{myKit.servo[0].angle}")


move_servo(0, next_angle)

while next_angle < MAX_ANGLE:
	next_angle += step
	move_servo(0, next_angle)




