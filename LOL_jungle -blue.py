# -*- coding: cp936 -*-
import win32api

import win32con

import ctypes ,ctypes.wintypes,win32gui
import threading
import time

time.sleep(10)
#win32api.keybd_event(17,0,0,0)  #ctrl键位码是17

#win32api.keybd_event(86,0,0,0)  #v键位码是86

#win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键

#win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

def press_q():
   win32api.keybd_event(81,0,0,0)  #q键位码是81
   time.sleep(1)
   win32api.keybd_event(81,0,win32con.KEYEVENTF_KEYUP,0)
   time.sleep(1)
def press_w():
   time.sleep(1)
   win32api.keybd_event(87,0,0,0)  #w键位码是81
   time.sleep(1)
   win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)
   time.sleep(1)
def press_e():
   win32api.keybd_event(69,0,0,0)  #e键位码是81
   win32api.keybd_event(69,0,win32con.KEYEVENTF_KEYUP,0)
def press_r():
   win32api.keybd_event(82,0,0,0)  #r键位码是81
   win32api.keybd_event(82,0,win32con.KEYEVENTF_KEYUP,0)

def mouse_move(x,y):
   win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0);
def mouse_set(x,y):
   win32api.SetCursorPos((x,y))
def mouse_lclick():
    win32api.mouse_event (win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0 )
    time.sleep(0.2)
    win32api.mouse_event (win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0 )
def mouse_rclick():
    win32api.mouse_event (win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0 )
    time.sleep(0.2)
    win32api.mouse_event (win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0 )
def q_beat():
   mouse_set(540, 691)
   time.sleep(0.1)
   mouse_lclick()
   time.sleep(0.1)
   mouse_set(920, 385)
   time.sleep(0.1)
   mouse_lclick()
def q_beat3():
   mouse_set(540, 691)
   time.sleep(0.1)
   mouse_lclick()
   time.sleep(0.1)
   mouse_set(694, 402)
   time.sleep(0.1)
   mouse_lclick()
def q_beat4():
   mouse_set(540, 691)
   time.sleep(0.1)
   mouse_lclick()
   time.sleep(0.1)
   mouse_set(651, 414)
   time.sleep(0.1)
   mouse_lclick()
def q_beat6():
   mouse_set(540, 691)
   time.sleep(0.1)
   mouse_lclick()
   time.sleep(0.1)
   mouse_set(694, 402)
   time.sleep(0.1)
   mouse_lclick()
def w_beat():
   mouse_set(589, 691)
   mouse_lclick()
def e_beat():
   mouse_set(638, 691)
   mouse_lclick()

def come_back():
   mouse_set(924, 720)
   mouse_lclick()
   time.sleep(15)
def kill_them(x):
   if x==1 :
      q_beat()
   elif x==3:
      q_beat3()
   elif x==4:
      q_beat4()
   elif x==6:
      q_beat6()
   #time.sleep(0.1)
   #w_beat()
   time.sleep(0.1)
   e_beat()
def kill(x,y):
    for i in range(y):
        kill_them(x)
        time.sleep(2)
def goto_StoneMan():
    mouse_set(1274,724)
    mouse_rclick()
    mouse_rclick()
    mouse_lclick()
    time.sleep(25)
    mouse_set(829, 405)
    mouse_rclick()
    
def goto_F4():
    mouse_set(1259,690)
    time.sleep(0.1)
    mouse_rclick()
    mouse_rclick()
    time.sleep(0.1)
    mouse_lclick()
    time.sleep(10)
    mouse_set(694, 402)
    time.sleep(0.1)
    mouse_rclick()
    
def goto_wolf():
    mouse_set(1223,678)
    time.sleep(0.1)
    mouse_rclick()
    mouse_rclick()
    time.sleep(0.1)
    mouse_lclick()
    time.sleep(12)
    mouse_set(651, 414)
    time.sleep(0.1)
    mouse_rclick()
def goto_hama():
    mouse_set(1201,655)
    time.sleep(0.1)
    mouse_rclick()
    mouse_rclick()
    time.sleep(0.1)
    mouse_lclick()
    time.sleep(10)
    mouse_set(705, 374)
    time.sleep(0.1)
    mouse_rclick()
def shengji():
   mouse_set(544,650)
   time.sleep(0.1)
   mouse_lclick()
   time.sleep(0.1)
   mouse_set(590,650)
   time.sleep(0.1)
   mouse_lclick()
   time.sleep(0.1)
   mouse_set(632,650)
   time.sleep(0.1)
   mouse_lclick()
   time.sleep(0.1)
#mouse_set(500,500)
#mouse_rclick()

EXIT = False
class Hotkey(threading.Thread):
 
    def run(self):
        global EXIT
        user32 = ctypes.windll.user32
        if not user32.RegisterHotKey(None, 99, win32con.MOD_WIN, win32con.VK_F3):
            raise RuntimeError
        try:
            msg = ctypes.wintypes.MSG()
            print msg
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        EXIT = True
                        return
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)

            
while True:
    shengji()
    
    goto_StoneMan()
    #time.sleep(1)
    w_beat()
    kill(1,6)
    shengji()
    time.sleep(3)
    goto_F4()
    w_beat()
    kill(3,8)
    shengji()
    time.sleep(3)
    goto_wolf()
    w_beat()
    kill(4,8)
    shengji()
    time.sleep(3)
    goto_hama()
    w_beat()
    kill(4,6)
    time.sleep(3)
    come_back()
    #time.sleep(5)

#time.sleep(5)

