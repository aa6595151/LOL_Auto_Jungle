# -*- coding: utf-8 -*-
import threading
import pythoncom
import pyHook
#from LOL_jungle import press

class Mythread(threading.Thread):
    daemon=True    #保证主进程结束时子进程也结束
    def __init__ (self):
        threading.Thread.__init__(self)
    def onKeyboardEvent(self,event):
        # 监听键盘事件
        global press
        if event.Key == 'M':
            #event.set()
            print "22222222"
            press.clear()
        #print "Key:", event.Key
    def run(self):
        
        hm = pyHook.HookManager()
        hm.KeyDown = self.onKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()
        return True   
   
# pr=Mythread()
# pr.start()
# press=threading.Event()
# press.set()
# while True:
    # if not press.isSet():
        # print "hahah"
        
        # break