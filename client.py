import Tkinter as tk
import socket

s = socket.socket()
s.connect((raw_input("Connect to: "), 4263))

BTN_0 = (1, 256)
BTN_1 = (1, 257)
BTN_2 = (1, 258)
BTN_3 = (1, 259)
BTN_4 = (1, 260)
BTN_8 = (1, 264)
ABS_X = (3, 0)
ABS_Y = (3, 1)

def emit(t, v):
	msg = str(t[0])+":"+str(t[1])+":"+str(v)+"\n"
	print msg
	s.send(msg)

def onEnter(event):
	emit(BTN_8,1)
def onEnterRel(event):
	emit(BTN_8,0)
def onCtrl(ev):
	emit(BTN_1,1)
def onCtrlRel(ev):
	emit(BTN_1,0)
def onShift(ev):
	emit(BTN_0,1)
def onShiftRel(ev):
	emit(BTN_0,0)
def onTrig(ev):
	r = None
	if ev.keysym.lower() == "z":
		r = BTN_2
	if ev.keysym.lower() == "x":
		r = BTN_3
	if ev.keysym.lower() == "c":
		r = BTN_4
	if not (r == None):
		t = 0
		if ev.type == "2":
			t = 1
		emit(r, t)
	print r
	print ev.keysym.lower()
xvl = 0
xvr = 0
yvu = 0
yvd = 0
ra = 32767
def onDir(ev):
	global xvl, xvr, yvu, yvd
	print ev.keycode
	if ev.keycode == 111 or ev.keycode == 8320768:
		yvu=1
	if ev.keycode == 113 or ev.keycode == 8124162:
		xvl=1
	if ev.keycode == 114 or ev.keycode == 8189699:
		xvr=1
	if ev.keycode == 116 or ev.keycode == 8255233:
		yvd=1
	emit(ABS_X, (xvr-xvl)*ra)
	emit(ABS_Y, (yvd-yvu)*ra)
def onDirRel(ev):
	global xvl, xvr, yvu, yvd
	if ev.keycode == 111 or ev.keycode == 8320768:
		yvu=0
	if ev.keycode == 113 or ev.keycode == 8124162:
		xvl=0
	if ev.keycode == 114 or ev.keycode == 8189699:
		xvr=0
	if ev.keycode == 116 or ev.keycode == 8255233:
		yvd=0
	emit(ABS_X, (xvr-xvl)*ra)
	emit(ABS_Y, (yvd-yvu)*ra)
root = tk.Tk()
root.geometry('300x200')
root.bind('<KeyPress-Return>', onEnter)
root.bind('<KeyRelease-Return>', onEnterRel)
root.bind('<KeyPress-Control_L>', onCtrl)
root.bind('<KeyRelease-Control_L>', onCtrlRel)
root.bind('<KeyPress-Shift_L>', onShift)
root.bind('<KeyRelease-Shift_L>', onShiftRel)
root.bind('<KeyPress-Left>', onDir)
root.bind('<KeyRelease-Left>', onDirRel)
root.bind('<KeyPress-Right>', onDir)
root.bind('<KeyRelease-Right>', onDirRel)
root.bind('<KeyPress-Up>', onDir)
root.bind('<KeyRelease-Up>', onDirRel)
root.bind('<KeyPress-Down>', onDir)
root.bind('<KeyRelease-Down>', onDirRel)
root.bind('<KeyPress-Z>', onTrig)
root.bind('<KeyPress-X>', onTrig)
root.bind('<KeyPress-C>', onTrig)
root.bind('<KeyPress-z>', onTrig)
root.bind('<KeyPress-x>', onTrig)
root.bind('<KeyPress-c>', onTrig)
root.bind('<KeyRelease-Z>', onTrig)
root.bind('<KeyRelease-X>', onTrig)
root.bind('<KeyRelease-C>', onTrig)
root.bind('<KeyRelease-z>', onTrig)
root.bind('<KeyRelease-x>', onTrig)
root.bind('<KeyRelease-c>', onTrig)
root.mainloop()
