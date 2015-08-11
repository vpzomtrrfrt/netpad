port = 4263

import socket, threading, uinput

btns = [
	uinput.BTN_JOYSTICK,
	uinput.BTN_0,
	uinput.BTN_1,
	uinput.BTN_2,
	uinput.BTN_3,
	uinput.BTN_4,
	uinput.BTN_8,
	uinput.ABS_X,
	uinput.ABS_Y
]

def listenthread(c):
	dev = uinput.Device(btns)
	f = c.makefile()
	while True:
		l = f.readline()
		s = l.split(':')
		print l
		if len(s)==3:
			dev.emit((int(s[0]), int(s[1])), int(s[2]))
		else:
			print l+" is not valid"
			c.close()
			break

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))
s.listen(5)
while True:
	c, a = s.accept()
	print str(a)+" has connected"
	t = threading.Thread(target=listenthread,args=(c,))
	t.daemon = True
	t.start()
