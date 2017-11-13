
import curses
from .fieldpad import FieldPad

import signal

class Screen:
    
    
    def __init__(self, display, stdscr):
        self.display = display
        curses.curs_set(0)
        self.stdscr = stdscr
        #self.height, self.width = self.stdscr.getmaxyx()
        self.setWins()
        signal.signal(signal.SIGWINCH, self.updateSize)
    
    def _limitHeight(self, h, y):
        return min(h + y, self.height) - y
    
    def setWins(self):
        height, width = self.height, self.width = self.stdscr.getmaxyx()
        
        sideW = 20
        sideX = width-sideW
        msgH = max(3, min(height // 5, 6))
        msgY = height - msgH
        healthY = 0
        healthH = self._limitHeight(2, healthY)
        groundY = healthY + healthH
        groundH = self._limitHeight(7, groundY)
        invY = groundY + groundH
        invH = self._limitHeight(12, invY)
        infoY = invY + invH
        infoH = self._limitHeight(20, infoY)
        
        self.windows = {
            "field": self.makeWin(0, 0, sideX - 1, msgY),#curses.newwin(msgY, sideX - 1, 0, 0),
            "msg": self.makeWin(0, msgY, sideX - 1, msgH),#curses.newwin(msgH, sideX - 1, msgY, 0),
            "health": self.makeWin(sideX, healthY, sideW, healthH),#curses.newwin(healthH, sideW, healthY, sideX),
            "ground": self.makeWin(sideX, groundY, sideW, groundH),#curses.newwin(groundH, sideW, groundY, sideX),
            "inventory": self.makeWin(sideX, invY, sideW, invH),#curses.newwin(invH, sideW, invY, sideX),
            "info": self.makeWin(sideX, infoY, sideW, infoH)#curses.newwin(infoH, sideW, infoY, sideX)
        }
    
    def makeWin(self, x, y, width, height):
        if width < 1 or height < 1:
            #raise Exception("too small"+str((x, y, width, height)))
            return None
        return curses.newwin(height, width, y, x)
    
    
    def updateSize(self, *args):
        curses.endwin()
        curses.initscr()
        self.setWins()
        #self.height, self.width = self.stdscr.getmaxyx()
        self.stdscr.clear()
        self.update(True)
    
    def update(self, force=False):
        d = self.display
        d.fieldPad.update(self.windows["field"], force)
        d.messagePad.update(self.windows["msg"], force)
        d.healthPad.update(self.windows["health"], force)
        d.groundPad.update(self.windows["ground"], force)
        d.inventoryPad.update(self.windows["inventory"], force)
        d.infoPad.update(self.windows["info"], force)
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
