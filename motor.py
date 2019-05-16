import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

p = GPIO.PWM(11,50)
q = GPIO.PWM(13	,50)
r = GPIO.PWM(15,50)
s = GPIO.PWM(16	,50)

p.start(0)
q.start(0)
r.start(0)
s.start(0)

try:
	while True:
		for i in range(100):
			p.ChangeDutyCycle(i)
			r.ChangeDutyCycle(i)
			time.sleep(0.02)
		for i in range(100):
			p.ChangeDutyCycle(100-i)
			r.ChangeDutyCycle(100-i)
			time.sleep(0.02)

		p.ChangeDutyCycle(0)
		r.ChangeDutyCycle(0)

		for i in range(100):
			q.ChangeDutyCycle(i)
			s.ChangeDutyCycle(i)
			time.sleep(0.02)
		for i in range(100):
			q.ChangeDutyCycle(100-i)
			s.ChangeDutyCycle(100-i)
			time.sleep(0.02)
		
		q.ChangeDutyCycle(0)
		s.ChangeDutyCycle(0)

except KeyboardInterrupt:
	GPIO.cleanup()
	p.stop()
	q.stop()
	r.stop()
	s.stop()
	pass
	
