# -*- coding: utf-8 -*-
import win32api
import win32con
import ctypes ,ctypes.wintypes,win32gui
import time
import pythoncom
import pyHook
from PyQt4 import QtCore, QtGui
import time,os

class Keythread(QtCore.QThread):
    #daemon=True    #保证主进程结束时子进程也结束
    def __init__ (self):
        super(Keythread, self).__init__(None)
        
    def onKeyboardEvent(self,event):
        # 监听键盘事件
        if event.Key == 'M':
            #event.set()
            self.emit(QtCore.SIGNAL("clos"))
        #print "Key:", event.Key
    def run(self):
        
        hm = pyHook.HookManager()
        hm.KeyDown = self.onKeyboardEvent
        hm.HookKeyboard()
        print "Im Runing"
        pythoncom.PumpMessages()
        return True   




class Mythread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
    def run(self):
        time.sleep(10)     
        while True:
            self.shengji()
            self.goto_StoneMan()
            #time.sleep(1)
            self.w_beat()
            self.kill(1,6)
            self.shengji()
            time.sleep(3)
            self.goto_F4()
            self.w_beat()
            self.kill(3,8)
            self.shengji()
            time.sleep(3)
            self.goto_wolf()
            self.w_beat()
            self.kill(4,8)
            self.shengji()
            time.sleep(3)
            self.goto_hama()
            self.w_beat()
            self.kill(4,6)
            time.sleep(3)
            self.come_back()
    def press_q(self):
       win32api.keybd_event(81,0,0,0)  #q键位码是81
       time.sleep(1)
       win32api.keybd_event(81,0,win32con.KEYEVENTF_KEYUP,0)
       time.sleep(1)
    def press_w(self):
       time.sleep(1)
       win32api.keybd_event(87,0,0,0)  #w键位码是81
       time.sleep(1)
       win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)
       time.sleep(1)
    def press_e(self):
       win32api.keybd_event(69,0,0,0)  #e键位码是81
       win32api.keybd_event(69,0,win32con.KEYEVENTF_KEYUP,0)
    def press_r(self):
       win32api.keybd_event(82,0,0,0)  #r键位码是81
       win32api.keybd_event(82,0,win32con.KEYEVENTF_KEYUP,0)

    def mouse_move(self,x,y):
       win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0);
    def mouse_set(self,x,y):
       win32api.SetCursorPos((x,y))
    def mouse_lclick(self):
        win32api.mouse_event (win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0 )
        time.sleep(0.2)
        win32api.mouse_event (win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0 )
    def mouse_rclick(self):
        win32api.mouse_event (win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0 )
        time.sleep(0.2)
        win32api.mouse_event (win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0 )
    def q_beat(self):
       self.mouse_set(540, 691)
       time.sleep(0.1)
       self.mouse_lclick()
       time.sleep(0.1)
       self.mouse_set(920, 385)
       time.sleep(0.1)
       self.mouse_lclick()
    def q_beat3(self):
       self.mouse_set(540, 691)
       time.sleep(0.1)
       self.mouse_lclick()
       time.sleep(0.1)
       self.mouse_set(694, 402)
       time.sleep(0.1)
       self.mouse_lclick()
    def q_beat4(self):
       self.mouse_set(540, 691)
       time.sleep(0.1)
       self.mouse_lclick()
       time.sleep(0.1)
       self.mouse_set(651, 414)
       time.sleep(0.1)
       self.mouse_lclick()
    def q_beat6(self):
       self.mouse_set(540, 691)
       time.sleep(0.1)
       self.mouse_lclick()
       time.sleep(0.1)
       self.mouse_set(694, 402)
       time.sleep(0.1)
       self.mouse_lclick()
    def w_beat(self):
       self.mouse_set(589, 691)
       self.mouse_lclick()
    def e_beat(self):
       self.mouse_set(638, 691)
       self.mouse_lclick()

    def come_back(self):
       self.mouse_set(924, 720)
       self.mouse_lclick()
       time.sleep(15)
    def kill_them(self,x):
       if x==1 :
          self.q_beat()
       elif x==3:
          self.q_beat3()
       elif x==4:
          self.q_beat4()
       elif x==6:
          self.q_beat6()
       #time.sleep(0.1)
       #w_beat()
       time.sleep(0.1)
       e_beat()
    def kill(self,x,y):
        for i in range(y):
            self.kill_them(x)
            time.sleep(2)
    def goto_StoneMan(self):
        self.mouse_set(1274,724)
        self.mouse_rclick()
        self.mouse_rclick()
        self.mouse_lclick()
        time.sleep(25)
        self.mouse_set(829, 405)
        self.mouse_rclick()
        
    def goto_F4(self):
        self.mouse_set(1259,690)
        time.sleep(0.1)
        self.mouse_rclick()
        self.mouse_rclick()
        time.sleep(0.1)
        self.mouse_lclick()
        time.sleep(10)
        self.mouse_set(694, 402)
        time.sleep(0.1)
        self.mouse_rclick()
        
    def goto_wolf(self):
        self.mouse_set(1223,678)
        time.sleep(0.1)
        self.mouse_rclick()
        self.mouse_rclick()
        time.sleep(0.1)
        self.mouse_lclick()
        time.sleep(12)
        self.mouse_set(651, 414)
        time.sleep(0.1)
        self.mouse_rclick()
    def goto_hama(self):
        self.mouse_set(1201,655)
        time.sleep(0.1)
        self.mouse_rclick()
        self.mouse_rclick()
        time.sleep(0.1)
        self.mouse_lclick()
        time.sleep(10)
        self.mouse_set(705, 374)
        time.sleep(0.1)
        self.mouse_rclick()
    def shengji(self):
       self.mouse_set(544,650)
       time.sleep(0.1)
       self.mouse_lclick()
       time.sleep(0.1)
       self.mouse_set(590,650)
       time.sleep(0.1)
       self.mouse_lclick()
       time.sleep(0.1)
       self.mouse_set(632,650)
       time.sleep(0.1)
       self.mouse_lclick()
       time.sleep(0.1)