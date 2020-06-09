from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QPropertyAnimation,QRect
from PyQt5.QtWidgets import QApplication, QMainWindow,QAction,QDialog,QWidget,QAction
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import math
import sys
import random

#for playing of gamish sounds sha...
#from pygame import mixer

#import for the maingame window
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Intro(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('intro.ui', self)
    
class Popup(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('popup.ui', self)
    
class Board(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('board.ui', self)
        self.b = 0
class Result(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('result.ui', self)


class Game(QMainWindow):#n_c QWidget
    def __init__(self):
        super().__init__()
        
        ui = (1,1)
        rui = random.choice(ui)
        if rui == 1:
            loadUi('nc_c.ui', self)
        if rui == 2:
            loadUi('n_c.ui', self)
        self.setWindowTitle("2017 © Nuts And Crosses")


        #adding the music fellas
        QTimer.singleShot(2000,self.plaY)
        
        
        self.begin.clicked.connect(self.AddBoard)
        self.vector = ([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
        self.begin.mine = 1
        self.err=0
        self.howto.clicked.connect(self.How_to)
        self.true_play = 0 # making sure that a user can never play twice
        self.win = 0
        self.loss = 0
        self.draw=0
        self.easy.setChecked(True)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)
    def plaY(self):
        #################################################
        #mixer.init()                                   #
        #mixer.music.load("04. already there.mp3")      #
        #mixer.music.play()                             #
        #################################################
        pass
    def Style(self):
        a = (1,2,3,4)
        style = random.choice(a)
    def How_to(self):
        self.stackedWidget.setCurrentIndex(1)
        self.play_1.clicked.connect(self.AddBoard)
    def BoardRestart(self):
        self.win = 0
        self.loss = 0
        self.draw=0
        QTimer.singleShot(0,self.Restart)
    def Animate(self):
        if self.easy.isChecked()==True:
            v= 1000
        if self.medium.isChecked()==True:
            v = 500
        if self.hard.isChecked()==True:
            v = 250
        if self.advanced.isChecked()==True:
            v = 250
        self.one = QPropertyAnimation(self.board.one,b"geometry")
        self.one.setDuration(v)#initially 500
        self.one.setStartValue(QRect(0,0,0,0))
        self.one.setEndValue(QRect(24, 63, 104, 104))
        self.one.start()

        self.one_2 = QPropertyAnimation(self.board.one_2,b"geometry")
        self.one_2.setDuration(v)
        self.one_2.setStartValue(QRect(512,280,0,0))
        self.one_2.setEndValue(QRect(24, 171, 104, 104))
        self.one_2.start()

        self.two = QPropertyAnimation(self.board.two,b"geometry")
        self.two.setDuration(v)
        self.two.setStartValue(QRect(413,400,0,0))
        self.two.setEndValue(QRect(131, 62, 104, 104))
        self.two.start()

        self.two_2 = QPropertyAnimation(self.board.two_2,b"geometry")
        self.two_2.setDuration(v)
        self.two_2.setStartValue(QRect(300,200,0,0))
        self.two_2.setEndValue(QRect(132, 170, 104, 104))
        self.two_2.start()

        self.three = QPropertyAnimation(self.board.three,b"geometry")
        self.three.setDuration(v)
        self.three.setStartValue(QRect(1500,80,0,0))
        self.three.setEndValue(QRect(238, 61, 104, 104))
        self.three.start()

        self.three_2 = QPropertyAnimation(self.board.three_2,b"geometry")
        self.three_2.setDuration(v)
        self.three_2.setStartValue(QRect(1089,10,0,0))
        self.three_2.setEndValue(QRect(239, 168, 104, 104))
        self.three_2.start()
        

        self.four = QPropertyAnimation(self.board.four,b"geometry")
        self.four.setDuration(v)
        self.four.setStartValue(QRect(240,550,0,0))
        self.four.setEndValue(QRect(346, 60, 104, 104))
        self.four.start()

        self.four_2 = QPropertyAnimation(self.board.four_2,b"geometry")
        self.four_2.setDuration(v)
        self.four_2.setStartValue(QRect(270,1000,0,0))
        self.four_2.setEndValue(QRect(347, 167, 104, 104))
        self.four_2.start()

        self.one_3 = QPropertyAnimation(self.board.one_3,b"geometry")
        self.one_3.setDuration(v)
        self.one_3.setStartValue(QRect(345,432,0,0))
        self.one_3.setEndValue(QRect(24, 278, 104, 104))
        self.one_3.start()

        self.one_4 = QPropertyAnimation(self.board.one_4,b"geometry")
        self.one_4.setDuration(v)
        self.one_4.setStartValue(QRect(200,112,0,0))
        self.one_4.setEndValue(QRect(25, 386, 104, 104))
        self.one_4.start()

        self.two_3 = QPropertyAnimation(self.board.two_3,b"geometry")
        self.two_3.setDuration(v)
        self.two_3.setStartValue(QRect(1000,500,0,0))
        self.two_3.setEndValue(QRect(132, 278, 104, 104))
        self.two_3.start()

        self.two_4 = QPropertyAnimation(self.board.two_4,b"geometry")
        self.two_4.setDuration(v)
        self.two_4.setStartValue(QRect(500,1000,0,0))
        self.two_4.setEndValue(QRect(133, 385, 104, 104))
        self.two_4.start()

        self.three_3 = QPropertyAnimation(self.board.three_3,b"geometry")
        self.three_3.setDuration(v)
        self.three_3.setStartValue(QRect(1000,500,0,0))
        self.three_3.setEndValue(QRect(239, 276, 104, 104))
        self.three_3.start()

        self.three_4 = QPropertyAnimation(self.board.three_4,b"geometry")
        self.three_4.setDuration(v)
        self.three_4.setStartValue(QRect(500,1000,0,0))
        self.three_4.setEndValue(QRect(241, 384, 104, 104))
        self.three_4.start()

        self.four_3 = QPropertyAnimation(self.board.four_3,b"geometry")
        self.four_3.setDuration(v)
        self.four_3.setStartValue(QRect(1000,500,0,0))
        self.four_3.setEndValue(QRect(347, 276, 104, 104))
        self.four_3.start()

        self.four_4 = QPropertyAnimation(self.board.four_4,b"geometry")
        self.four_4.setDuration(v)
        self.four_4.setStartValue(QRect(500,1000,0,0))
        self.four_4.setEndValue(QRect(349, 384, 104, 104))
        self.four_4.start()
      
    def AddBoard(self):
        self.speed = 1 
        self.true_play=0
        self.board = Board()
        self.Style()
        self.board.back.clicked.connect(self.Home)
        self.stackedWidget.addWidget(self.board)
        self.stackedWidget.setCurrentIndex(2)
        self.board.win.setText(str(self.win))
        self.board.loss.setText(str(self.loss))
        self.board.draw.setText(str(self.draw))
        ## animation
        self.Animate()
        ## End of animation
        self.board.win.setAlignment(Qt.AlignCenter)
        self.board.loss.setAlignment(Qt.AlignCenter)
        self.board.draw.setAlignment(Qt.AlignCenter)
        
        self.hold_comp = 1
        self.board.restart.clicked.connect(self.Restart)
        if self.err==0:
            self.I()
            self.err+=1
        self.pf()
        self.vector = ([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
        
        
        try:
            self.result.close()
        except:
            pass
        self.board.levels.setAlignment(Qt.AlignCenter)
        if self.easy.isChecked()==True:
            self.board.levels.setText("<font color=blue><b>Level</font></b>:<font color=green><b> easy</font></b>")
            self.speed = 1000
        if self.medium.isChecked()==True:
            self.board.levels.setText("<font color=blue><b>Level</font></b>:<font color=brown><b> Medium</font></b>")
            self.speed = 500
        if self.hard.isChecked()==True:
            self.board.levels.setText("<font color=blue><b>Level</font></b>: <font color=red><b>Hard</font></b>")
            self.speed = 1 
        if self.advanced.isChecked()==True:
            self.board.levels.setText("<font color=blue><b>Level</font></b>: <font color=red><b>Advanced</font></b>")
            self.speed = 1 
    def p(self):#p for popup
        self.previewWindow =Popup()
        flags = Qt.Popup
        self.previewWindow.setWindowFlags(flags)
 
        ##adding the pop up
        _init_pos = (self.geometry())
        n = str(_init_pos)
        u,l = n.split("(")
        a,b = l.split(")")
        List = list(a)
        fi,se,th,fo =a.split(" ")
        fi_pop = list(fi)
        fi_pop.pop()
        fi_real = "".join(fi_pop)
        first = int(fi_real)
        se_pop = list(se)
        se_pop.pop()
        se_real = "".join(se_pop)
        second = int(se_real)
        th_pop = list(th)
        th_pop.pop()
        th_real = "".join(th_pop)
        third = int(th_real)
        fo_pop = list(fo)
        fo_real ="".join(fo_pop)
        fourth = int(fo_real)
        self.previewWindow.setGeometry(first+180, second+200, third-242, fourth+542)
        self.previewWindow.show()

        #self.previewWindow.nut.clicked.connect(self.previewWindow.close)
        #self.previewWindow.cross.clicked.connect(self.Home)
    def I(self):#I for intro
        self.intro =Intro()
        flags = Qt.Popup
        self.intro.setWindowFlags(flags)
 
        ##adding the pop up
        _init_pos = (self.geometry())
        n = str(_init_pos)
        u,l = n.split("(")
        a,b = l.split(")")
        List = list(a)
        fi,se,th,fo =a.split(" ")
        fi_pop = list(fi)
        fi_pop.pop()
        fi_real = "".join(fi_pop)
        first = int(fi_real)
        se_pop = list(se)
        se_pop.pop()
        se_real = "".join(se_pop)
        second = int(se_real)
        th_pop = list(th)
        th_pop.pop()
        th_real = "".join(th_pop)
        third = int(th_real)
        fo_pop = list(fo)
        fo_real ="".join(fo_pop)
        fourth = int(fo_real)
        self.intro.setGeometry(first+10, second+30, third-242, fourth+542)
        self.intro.show()
        #self.previewWindow.nut.clicked.connect(self.previewWindow.close)
        #self.previewWindow.cross.clicked.connect(self.Home)
    def  Home(self):
        self.stackedWidget.removeWidget(self.board)
        self.stackedWidget.setCurrentIndex(0)
        self.true_play=0
        self.win = 0
        self.loss = 0
        self.draw=0
        
       
    def Restart(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.removeWidget(self.board)
        self.true_play=0
        self.AddBoard()
        self.plaY()
    def pf(self):#the functions to be carrie out on the board
        #self.board.one.clicked.connect(self.One)
        self.board.one.clicked.connect(self.One)
        self.board.two.clicked.connect(self.Two)
        self.board.three.clicked.connect(self.Three)
        self.board.four.clicked.connect(self.Four)

        self.board.one_2.clicked.connect(self.One_2)
        self.board.two_2.clicked.connect(self.Two_2)
        self.board.three_2.clicked.connect(self.Three_2)
        self.board.four_2.clicked.connect(self.Four_2)

        self.board.one_3.clicked.connect(self.One_3)
        self.board.two_3.clicked.connect(self.Two_3)
        self.board.three_3.clicked.connect(self.Three_3)
        self.board.four_3.clicked.connect(self.Four_3)

        self.board.one_4.clicked.connect(self.One_4)
        self.board.two_4.clicked.connect(self.Two_4)
        self.board.three_4.clicked.connect(self.Three_4)
        self.board.four_4.clicked.connect(self.Four_4)
    def R(self):#R stands for result
        #Adding a frame like stuff informing the player that he or she has won
        self.result = Result()
        flags = Qt.Drawer
        self.result.setWindowFlags(flags)
 
        ##adding the pop up and setting the geometry to the middle of the screen
        _init_pos = (self.geometry())
        n = str(_init_pos)
        u,l = n.split("(")
        a,b = l.split(")")
        List = list(a)
        fi,se,th,fo =a.split(" ")
        fi_pop = list(fi)
        fi_pop.pop()
        fi_real = "".join(fi_pop)
        first = int(fi_real)
        se_pop = list(se)
        se_pop.pop()
        se_real = "".join(se_pop)
        second = int(se_real)
        th_pop = list(th)
        th_pop.pop()
        th_real = "".join(th_pop)
        third = int(th_real)
        fo_pop = list(fo)
        fo_real ="".join(fo_pop)
        fourth = int(fo_real)
        self.result.setGeometry(first+10, second+30, third-242, fourth+542)
        self.result.setWindowTitle("Results")
        self.result.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.result.show()
    def Pause_Music(self):
        print()
    def CHECK(self):
        #vertical checker
        if self.vector[0][0]==2 and self.vector[1][0]==2 and self.vector[2][0]==2 and self.vector[3][0]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.true_play=1
                self.hold_comp = 2
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][0]==1 and self.vector[1][0]==1 and self.vector[2][0]==1 and self.vector[3][0]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.true_play=1
                self.hold_comp = 2
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][1]==2 and self.vector[1][1]==2 and self.vector[2][1]==2 and self.vector[3][1]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][1]==1 and self.vector[1][1]==1 and self.vector[2][1]==1 and self.vector[3][1]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][2]==2 and self.vector[1][2]==2 and self.vector[2][2]==2 and self.vector[3][2]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][2]==1 and self.vector[1][2]==1 and self.vector[2][2]==1 and self.vector[3][2]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][3]==2 and self.vector[1][3]==2 and self.vector[2][3]==2 and self.vector[3][3]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][3]==1 and self.vector[1][3]==1 and self.vector[2][3]==1 and self.vector[3][3]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        ###################################################Horizontal Checker#########################
        elif self.vector[0][0]==2 and self.vector[0][1]==2 and self.vector[0][2]==2 and self.vector[0][3]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][0]==1 and self.vector[0][1]==1 and self.vector[0][2]==1 and self.vector[0][3]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                QTimer.singleShot(3000,self.Restart)
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[1][0]==2 and self.vector[1][1]==2 and self.vector[1][2]==2 and self.vector[1][3]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[1][0]==1 and self.vector[1][1]==1 and self.vector[1][2]==1 and self.vector[1][3]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[2][0]==2 and self.vector[2][1]==2 and self.vector[2][2]==2 and self.vector[2][3]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[2][0]==1 and self.vector[2][1]==1 and self.vector[2][2]==1 and self.vector[2][3]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[3][0]==2 and self.vector[3][1]==2 and self.vector[3][2]==2 and self.vector[3][3]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[3][0]==1 and self.vector[3][1]==1 and self.vector[3][2]==1 and self.vector[3][3]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        #vertice checker
        elif self.vector[0][0]==2 and self.vector[1][1]==2 and self.vector[2][2]==2 and self.vector[3][3]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][0]==1 and self.vector[1][1]==1 and self.vector[2][2]==1 and self.vector[3][3]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][3]==2 and self.vector[1][2]==2 and self.vector[2][1]==2 and self.vector[3][0]==2:
            if self.player_id == 2:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        elif self.vector[0][3]==1 and self.vector[1][2]==1 and self.vector[2][1]==1 and self.vector[3][0]==1:
            if self.player_id == 1:
                self.R()
                self.result.screen.setText("Congractu!!!! awesome\nyou have won.....")
                self.hold_comp = 2
                self.true_play=1
                self.win+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
            else:
                self.R()
                self.result.screen.setText("Loss...! bahaha")
                self.true_play=1
                self.loss+=1
                self.result.restart.clicked.connect(self.Restart)
                self.board.win.setText(str(self.win))
                self.board.loss.setText(str(self.loss))
                self.board.draw.setText(str(self.draw))
                self.Pause_Music()
        #checking is all the boxes are fill and still no winner
        elif self.vector[0][0]>0 and self.vector[0][1]>0 and self.vector[0][2]>0 and self.vector[0][3]>0\
        and self.vector[1][0]>0 and self.vector[1][1]>0 and self.vector[1][2]>0 and self.vector[1][3]>0\
        and self.vector[2][0]>0 and self.vector[2][1]>0 and self.vector[2][2]>0 and self.vector[2][3]>0\
        and self.vector[3][0]>0 and self.vector[3][1]>0 and self.vector[3][2]>0 and self.vector[3][3]>0:
            self.R()
            self.result.screen.setText("<font color=green><b>Game Draw</b><font>")
            self.result.restart.clicked.connect(self.Restart)
            self.true_play=1
            self.draw+=1
            self.board.win.setText(str(self.win))
            self.board.loss.setText(str(self.loss))
            self.board.draw.setText(str(self.draw))
            self.Pause_Music()
                


        
    def One(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut1)
                self.previewWindow.cross.clicked.connect(self.renderCross1)
                
            else:
                if self.vector[0][0]>0:
                    pass
                else:
                    if self.player == 'nut':
                        
                        self.board.one.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[0][0] = self.player_id
                        self.true_play+=1
                        
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                        
                    else:
                        self.board.one.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[0][0] = self.player_id
                        self.true_play+=1
                       
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                
    def Two(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut2)
                self.previewWindow.cross.clicked.connect(self.renderCross2)
                
                
            else:
                if self.vector[0][1]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.two.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[0][1] = self.player_id
                        self.true_play+=1
                        
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.two.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[0][1] = self.player_id
                        self.true_play+=1
                       
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
            
    def Three(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut3)
                self.previewWindow.cross.clicked.connect(self.renderCross3)
                
            else:
                if self.vector[0][2]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.three.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[0][2] = self.player_id
                        self.true_play+=1
                        
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.three.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[0][2] = self.player_id
                        self.true_play+=1
                        
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
    def Four(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut4)
                self.previewWindow.cross.clicked.connect(self.renderCross4)
                
            else:
                if self.vector[0][3]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.four.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[0][3] = self.player_id
                        self.true_play+=1
                        
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.four.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[0][3] = self.player_id
                        self.true_play+=1
                       
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()

    def One_2(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut12)
                self.previewWindow.cross.clicked.connect(self.renderCross12)
                
            else:
                if self.vector[1][0]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.one_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[1][0] = self.player_id
                        self.true_play+=1
                      
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.one_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[1][0] = self.player_id
                        self.true_play+=1
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
    def Two_2(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut22)
                self.previewWindow.cross.clicked.connect(self.renderCross22)
                
            else:
                if self.vector[1][1]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.two_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[1][1] = self.player_id
                        self.true_play+=1
                        
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.two_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[1][1] = self.player_id
                        self.true_play+=1
                    
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
    def Three_2(self):
            if self.true_play%2==0:
                if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
                and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
                and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
                and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                    self.p()
                    self.previewWindow.nut.clicked.connect(self.renderNut32)
                    self.previewWindow.cross.clicked.connect(self.renderCross32)
                    
                else:
                    if self.vector[1][2]>0:
                        pass
                    else:
                        if self.player == 'nut':
                            self.board.three_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                             background-image: url(:/newPrefix/textEdit.png);""")
                            self.vector[1][2] = self.player_id
                            self.true_play+=1
                    
                            try:
                                QTimer.singleShot(self.speed,self.ComputerPlay)
                            except:
                                pass
                            self.CHECK()
                        else:
                            self.board.three_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                             background-image: url(:/newPrefix/textEdit_2.png);""")
                            self.vector[1][2] = self.player_id
                            self.true_play+=1
                      
                            try:
                                QTimer.singleShot(self.speed,self.ComputerPlay)
                            except:
                                pass
                            self.CHECK()
                    
    def Four_2(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut42)
                self.previewWindow.cross.clicked.connect(self.renderCross42)
                
            else:
                if self.vector[1][3]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.four_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[1][3] = self.player_id
                        self.true_play+=1
             
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.four_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[1][3] = self.player_id
                        self.true_play+=1
               
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()

    def One_3(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut13)
                self.previewWindow.cross.clicked.connect(self.renderCross13)
               
            else:
                if self.vector[2][0]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.one_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[2][0] = self.player_id
                        self.true_play+=1
                    
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.one_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[2][0] = self.player_id
                        self.true_play+=1
                 
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    
    def Two_3(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut23)
                self.previewWindow.cross.clicked.connect(self.renderCross23)
               
                
            else:
                if self.vector[2][1]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.two_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[2][1] = self.player_id
                        self.true_play+=1
                    
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.two_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[2][1] = self.player_id
                        self.true_play+=1
                  
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
    def Three_3(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut33)
                self.previewWindow.cross.clicked.connect(self.renderCross33)
                
            else:
                if self.vector[2][2]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.three_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[2][2] = self.player_id
                        self.true_play+=1
           
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.three_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[2][2] = self.player_id
                        self.true_play+=1
             
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
    def Four_3(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut43)
                self.previewWindow.cross.clicked.connect(self.renderCross43)
                
            else:
                if self.vector[2][3]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.four_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[2][3] = self.player_id
                        self.true_play+=1
                    
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.four_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[2][3] = self.player_id
                        self.true_play+=1
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()

    def One_4(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut14)
                self.previewWindow.cross.clicked.connect(self.renderCross14)
              
            else:
                if self.vector[3][0]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.one_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[3][0] = self.player_id
                        self.true_play+=1
                        
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.one_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[3][0] = self.player_id
                        self.true_play+=1
                       
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
    def Two_4(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut24)
                self.previewWindow.cross.clicked.connect(self.renderCross24)
              
            else:
                if self.vector[3][1]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.two_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[3][1] = self.player_id
                        self.true_play+=1
                    
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.two_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[3][1] = self.player_id
                        self.true_play+=1
                
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
    def Three_4(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut34)
                self.previewWindow.cross.clicked.connect(self.renderCross34)
                
            else:
                if self.vector[3][2]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.three_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[3][2] = self.player_id
                        self.true_play+=1
               
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.three_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[3][2] = self.player_id
                        self.true_play+=1

                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
    def Four_4(self):
        if self.true_play%2==0:
            if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                self.p()
                self.previewWindow.nut.clicked.connect(self.renderNut44)
                self.previewWindow.cross.clicked.connect(self.renderCross44)
            else:
                if self.vector[3][3]>0:
                    pass
                else:
                    if self.player == 'nut':
                        self.board.four_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
                                                         background-image: url(:/newPrefix/textEdit.png);""")
                        self.vector[3][3] = self.player_id
                        self.true_play+=1
               
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
                    else:
                        self.board.four_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                         background-image: url(:/newPrefix/textEdit_2.png);""")
                        self.vector[3][3] = self.player_id
                        self.true_play+=1
               
                        try:
                            QTimer.singleShot(self.speed,self.ComputerPlay)
                        except:
                            pass
                        self.CHECK()
    def renderNut1(self):
        self.board.one.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[0][0]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross1(self):
        self.board.one.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[0][0]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
        
    def renderNut2(self):
        self.board.two.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[0][1]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross2(self):
        self.board.two.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[0][1]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()

    def renderNut3(self):
        self.board.three.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[0][2]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross3(self):
        self.board.three.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[0][2]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut4(self):
        self.board.four.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[0][3]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross4(self):
        self.board.four.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[0][3]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut12(self):
        self.board.one_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[1][0]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross12(self):
        self.board.one_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[1][0]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut22(self):
        self.board.two_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[1][1]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross22(self):
        self.board.two_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[1][1]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut32(self):
        self.board.three_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[1][2]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross32(self):
        self.board.three_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[1][2]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut42(self):
        self.board.four_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[1][3]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross42(self):
        self.board.four_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[1][3]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut13(self):
        self.board.one_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[2][0]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross13(self):
        self.board.one_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[2][0]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
        
    def renderNut23(self):
        self.board.two_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[2][1]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross23(self):
        self.board.two_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[2][1]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut33(self):
        self.board.three_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[2][2]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross33(self):
        self.board.three_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[2][2]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut43(self):
        self.board.four_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[2][3]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross43(self):
        self.board.four_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.vector[2][3]=self.player_id
        self.true_play+=1
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut14(self):
        self.board.one_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.true_play+=1
        self.vector[3][0]=self.player_id
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross14(self):
        self.board.one_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.true_play+=1
        self.board.one.n = 2
        self.vector[3][0]=self.player_id
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut24(self):
        self.board.two_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.true_play+=1
        self.Computer = "cross"
        self.board.one.n = 1
        self.vector[3][1]=self.player_id
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross24(self):
        self.board.two_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.board.one.n = 2
        self.true_play+=1
        self.vector[3][1]=self.player_id
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut34(self):
        self.board.three_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.true_play+=1
        self.board.one.n = 1
        self.vector[3][2]=self.player_id
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross34(self):
        self.board.three_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.true_play+=1
        self.board.one.n = 2
        self.vector[3][2]=self.player_id
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderNut44(self):
        self.board.four_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
 background-image: url(:/newPrefix/textEdit.png);""")
        self.player = "nut"
        self.player_id = 1
        self.computer_id = 2
        self.Computer = "cross"
        self.board.one.n = 1
        self.true_play+=1
        self.vector[3][3]=self.player_id
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()
    def renderCross44(self):
        self.board.four_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
 background-image: url(:/newPrefix/textEdit_2.png);""")
        self.player = "cross"
        self.Computer = "nut"
        self.player_id = 2
        self.computer_id = 1
        self.true_play+=1
        self.board.one.n = 2
        self.vector[3][3]=self.player_id
        self.previewWindow.close()
        QTimer.singleShot(self.speed,self.ComputerPlay)
        #self.ComputerPlay()

    
    
    
    def ComputerPlay(self):
        if (self.hold_comp%2)!=0:
            self.list =[]
            if self.vector[0][0]==0:
                self.list.append(1)
            if self.vector[0][1]==0:
                self.list.append(2)
            if self.vector[0][2]==0:
                self.list.append(3)
            if self.vector[0][3]==0:
                self.list.append(4)


            if self.vector[1][0]==0:
                self.list.append(5)
            if self.vector[1][1]==0:
                self.list.append(6)
            if self.vector[1][2]==0:
                self.list.append(7)
            if self.vector[1][3]==0:
                self.list.append(8)


            if self.vector[2][0]==0:
                self.list.append(9)
            if self.vector[2][1]==0:
                self.list.append(10)
            if self.vector[2][2]==0:
                self.list.append(11)
            if self.vector[2][3]==0:
                self.list.append(12)

            if self.vector[3][0]==0:
                self.list.append(13)
            if self.vector[3][1]==0:
                self.list.append(14)
            if self.vector[3][2]==0:
                self.list.append(15)
            if self.vector[3][3]==0:
                self.list.append(16)
            
            rand = random.choice(self.list)
           
            ### try to make the computer
            ### make the game immpossible to win.  :)....:) kikiki
            comp = self.computer_id
            user = self.player_id
            if self.easy.isChecked()==True:
                ease = (1,2,3)#Increses this by ease = (1,2,3...) for easier play.. :)
            if self.medium.isChecked()==True:
                ease=(1,2)
            if self.hard.isChecked()==True:
                ease= (1,1)
            if self.advanced.isChecked()==True:
                ease = (1,1)
            easeR = random.choice(ease)
            ####################################rows#####################################
            #adding ultimate toughness for the app when advanced radiobutton is checked
            if self.advanced.isChecked()==True:
                if self.vector[0][0]==self.player_id and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                    rand = 16
                if self.vector[0][0]==0 and self.vector[0][1]==self.player_id and self.vector[0][2]==0 and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                    rand = 14
                if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==self.player_id and self.vector[0][3]==0\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                    rand = 15
                if self.vector[0][0]==0 and self.vector[0][1]==0 and self.vector[0][2]==0 and self.vector[0][3]==self.player_id\
            and self.vector[1][0]==0 and self.vector[1][1]==0 and self.vector[1][2]==0 and self.vector[1][3]==0\
            and self.vector[2][0]==0 and self.vector[2][1]==0 and self.vector[2][2]==0 and self.vector[2][3]==0\
            and self.vector[3][0]==0 and self.vector[3][1]==0 and self.vector[3][2]==0 and self.vector[3][3]==0:
                    rand = 16
            #later jhoor...........
            
           
            if easeR==1:
                 #row one
                if self.vector[0][0] == self.player_id and self.vector[0][1]==self.player_id\
                and self.vector[0][2]==self.player_id and self.vector[0][3]==0:
                    rand=4
                if self.vector[0][0] == self.player_id and self.vector[0][1]==self.player_id\
                and self.vector[0][2]==0 and self.vector[0][3]==self.player_id:
                    rand=3
                if self.vector[0][0] == self.player_id and self.vector[0][1]==0\
                and self.vector[0][2]==self.player_id and self.vector[0][3]==self.player_id:
                    rand=2
                if self.vector[0][0] == 0 and self.vector[0][1]==self.player_id\
                and self.vector[0][2]==self.player_id and self.vector[0][3]==self.player_id:
                    rand=1
                
                #row 2
                if self.vector[1][0] == self.player_id and self.vector[1][1]==self.player_id\
                and self.vector[1][2]==self.player_id and self.vector[1][3]==0:
                    rand=8
                if self.vector[1][0] == self.player_id and self.vector[1][1]==self.player_id\
                and self.vector[1][2]==0 and self.vector[1][3]==self.player_id:
                    rand=7
                if self.vector[1][0] == self.player_id and self.vector[1][1]==0\
                and self.vector[1][2]==self.player_id and self.vector[1][3]==self.player_id:
                    rand=6
                if self.vector[1][0] ==0 and self.vector[1][1]==self.player_id\
                and self.vector[1][2]==self.player_id and self.vector[1][3]==self.player_id:
                    rand=5
                # row 3
                if self.vector[2][0] == self.player_id and self.vector[2][1]==self.player_id\
                and self.vector[2][2]==self.player_id and self.vector[2][3]==0:
                    rand=12
                if self.vector[2][0] == self.player_id and self.vector[2][1]==self.player_id\
                and self.vector[2][2]==0 and self.vector[2][3]==self.player_id:
                    rand=11
                if self.vector[2][0] == self.player_id and self.vector[2][1]==0\
                and self.vector[2][2]==self.player_id and self.vector[2][3]==self.player_id:
                    rand=10
                if self.vector[2][0] == 0 and self.vector[2][1]==self.player_id\
                and self.vector[2][2]==self.player_id and self.vector[2][3]==self.player_id:
                    rand=9
                #row 4
                if self.vector[3][0] == self.player_id and self.vector[3][1]==self.player_id\
                and self.vector[3][2]==self.player_id and self.vector[3][3]==0:
                    rand=16
                if self.vector[3][0] == self.player_id and self.vector[3][1]==self.player_id\
                and self.vector[3][2]==0 and self.vector[3][3]==self.player_id:
                    rand=15
                if self.vector[3][0] == self.player_id and self.vector[3][1]==0\
                and self.vector[3][2]==self.player_id and self.vector[3][3]==self.player_id:
                    rand=14
                if self.vector[3][0] == 0 and self.vector[3][1]==self.player_id\
                and self.vector[3][2]==self.player_id and self.vector[3][3]==self.player_id:
                    rand=13
                ##############################################columns############################
                #coloumn 1
                if self.vector[0][0] == self.player_id and self.vector[1][0]==self.player_id\
                and self.vector[2][0]==self.player_id and self.vector[3][0]==0:
                    rand=13
                if self.vector[0][0] == self.player_id and self.vector[1][0]==self.player_id\
                and self.vector[2][0]==0 and self.vector[3][0]==self.player_id:
                    rand=9
                if self.vector[0][0] == self.player_id and self.vector[1][0]==0\
                and self.vector[2][0]==self.player_id and self.vector[3][0]==self.player_id:
                    rand=5
                if self.vector[0][0] ==0 and self.vector[1][0]==self.player_id\
                and self.vector[2][0]==self.player_id and self.vector[3][0]==self.player_id:
                    rand=1
                #column 2
                if self.vector[0][1] == self.player_id and self.vector[1][1]==self.player_id\
                and self.vector[2][1]==self.player_id and self.vector[3][1]==0:
                    rand=14
                if self.vector[0][1] == self.player_id and self.vector[1][1]==self.player_id\
                and self.vector[2][1]==0 and self.vector[3][1]==self.player_id:
                    rand=10
                if self.vector[0][1] == self.player_id and self.vector[1][1]==0\
                and self.vector[2][1]==self.player_id and self.vector[3][1]==self.player_id:
                        rand=6
                if self.vector[0][1] == 0 and self.vector[1][1]==self.player_id\
                and self.vector[2][1]==self.player_id and self.vector[3][1]==self.player_id:
                    rand=2
                #column 3
                if self.vector[0][2] == self.player_id and self.vector[1][2]==self.player_id\
                and self.vector[2][2]==self.player_id and self.vector[3][2]==0:
                    rand=15
                if self.vector[0][2] == self.player_id and self.vector[1][2]==self.player_id\
                and self.vector[2][2]==0 and self.vector[3][2]==self.player_id:
                    rand=11
                if self.vector[0][2] == self.player_id and self.vector[1][2]==0\
                and self.vector[2][2]==self.player_id and self.vector[3][2]==self.player_id:
                    rand=7
                if self.vector[0][2] == 0 and self.vector[1][2]==self.player_id\
                and self.vector[2][2]==self.player_id and self.vector[3][2]==self.player_id:
                    rand=3
                #Column 4
                if self.vector[0][3] == self.player_id and self.vector[1][3]==self.player_id\
                and self.vector[2][3]==self.player_id and self.vector[3][3]==0:
                    rand=16
                if self.vector[0][3] == self.player_id and self.vector[1][3]==self.player_id\
                and self.vector[2][3]==0 and self.vector[3][3]==self.player_id:
                    rand=12
                if self.vector[0][3] == self.player_id and self.vector[1][3]==0\
                and self.vector[2][3]==self.player_id and self.vector[3][3]==self.player_id:
                    rand=8
                if self.vector[0][3] ==0 and self.vector[1][3]==self.player_id\
                and self.vector[2][3]==self.player_id and self.vector[3][3]==self.player_id:
                    rand=4
                #######################################Vertices########################################
                #the right vertice
                if self.vector[0][0]==self.player_id and self.vector[1][1]==self.player_id\
                and self.vector[2][2]==self.player_id and self.vector[3][3]==0:
                    rand=16
                if self.vector[0][0]==self.player_id and self.vector[1][1]==self.player_id\
                and self.vector[2][2]==0 and self.vector[3][3]==self.player_id:
                    rand=11
                if self.vector[0][0]==self.player_id and self.vector[1][1]==0\
                and self.vector[2][2]==self.player_id and self.vector[3][3]==self.player_id:
                    rand=6
                if self.vector[0][0]==0 and self.vector[1][1]==self.player_id\
                and self.vector[2][2]==self.player_id and self.vector[3][3]==self.player_id:
                    rand=1
                ### the left vertice
                if self.vector[0][3]==self.player_id and self.vector[1][2]==self.player_id\
                and self.vector[2][1]==self.player_id and self.vector[3][0]==0:
                    rand=13
                if self.vector[0][3]==self.player_id and self.vector[1][2]==self.player_id\
                and self.vector[2][1]==0 and self.vector[3][0]==self.player_id:
                    rand=10
                if self.vector[0][3]==self.player_id and self.vector[1][2]==0\
                and self.vector[2][1]==self.player_id and self.vector[3][0]==self.player_id:
                    rand=7
                if self.vector[0][3]==0 and self.vector[1][2]==self.player_id\
                and self.vector[2][1]==self.player_id and self.vector[3][0]==self.player_id:
                    rand=4
                #immpossibility archieved

    #===========================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Making the computer win when allowed to or given the chance
             #row one
            
            if self.vector[0][0] == self.computer_id and self.vector[0][1]==self.computer_id\
            and self.vector[0][2]==self.computer_id and self.vector[0][3]==0:
                rand=4
            if self.vector[0][0] == self.computer_id and self.vector[0][1]==self.computer_id\
            and self.vector[0][2]==0 and self.vector[0][3]==self.computer_id:
                rand=3
            if self.vector[0][0] == self.computer_id and self.vector[0][1]==0\
            and self.vector[0][2]==self.computer_id and self.vector[0][3]==self.computer_id:
                rand=2
            if self.vector[0][0] == 0 and self.vector[0][1]==self.computer_id\
            and self.vector[0][2]==self.computer_id and self.vector[0][3]==self.computer_id:
                rand=1
            
            #row 2
            if self.vector[1][0] == self.computer_id and self.vector[1][1]==self.computer_id\
            and self.vector[1][2]==self.computer_id and self.vector[1][3]==0:
                rand=8
            if self.vector[1][0] == self.computer_id and self.vector[1][1]==self.computer_id\
            and self.vector[1][2]==0 and self.vector[1][3]==self.computer_id:
                rand=7
            if self.vector[1][0] == self.computer_id and self.vector[1][1]==0\
            and self.vector[1][2]==self.computer_id and self.vector[1][3]==self.computer_id:
                rand=6
            if self.vector[1][0] ==0 and self.vector[1][1]==self.computer_id\
            and self.vector[1][2]==self.computer_id and self.vector[1][3]==self.computer_id:
                rand=5
            # row 3
            if self.vector[2][0] == self.computer_id and self.vector[2][1]==self.computer_id\
            and self.vector[2][2]==self.computer_id and self.vector[2][3]==0:
                rand=12
            if self.vector[2][0] == self.computer_id and self.vector[2][1]==self.computer_id\
            and self.vector[2][2]==0 and self.vector[2][3]==self.computer_id:
                rand=11
            if self.vector[2][0] == self.computer_id and self.vector[2][1]==0\
            and self.vector[2][2]==self.computer_id and self.vector[2][3]==self.computer_id:
                rand=10
            if self.vector[2][0] == 0 and self.vector[2][1]==self.computer_id\
            and self.vector[2][2]==self.computer_id and self.vector[2][3]==self.computer_id:
                rand=9
            #row 4
            if self.vector[3][0] == self.computer_id and self.vector[3][1]==self.computer_id\
            and self.vector[3][2]==self.computer_id and self.vector[3][3]==0:
                rand=16
            if self.vector[3][0] == self.computer_id and self.vector[3][1]==self.computer_id\
            and self.vector[3][2]==0 and self.vector[3][3]==self.computer_id:
                rand=15
            if self.vector[3][0] == self.computer_id and self.vector[3][1]==0\
            and self.vector[3][2]==self.computer_id and self.vector[3][3]==self.computer_id:
                rand=14
            if self.vector[3][0] == 0 and self.vector[3][1]==self.computer_id\
            and self.vector[3][2]==self.computer_id and self.vector[3][3]==self.computer_id:
                rand=13
            ##############################################columns############################
            #coloumn 1
            if self.vector[0][0] == self.computer_id and self.vector[1][0]==self.computer_id\
            and self.vector[2][0]==self.computer_id and self.vector[3][0]==0:
                rand=13
            if self.vector[0][0] == self.computer_id and self.vector[1][0]==self.computer_id\
            and self.vector[2][0]==0 and self.vector[3][0]==self.computer_id:
                rand=9
            if self.vector[0][0] == self.computer_id and self.vector[1][0]==0\
            and self.vector[2][0]==self.computer_id and self.vector[3][0]==self.computer_id:
                rand=5
            if self.vector[0][0] ==0 and self.vector[1][0]==self.computer_id\
            and self.vector[2][0]==self.computer_id and self.vector[3][0]==self.computer_id:
                rand=1
            #column 2
            if self.vector[0][1] == self.computer_id and self.vector[1][1]==self.computer_id\
            and self.vector[2][1]==self.computer_id and self.vector[3][1]==0:
                rand=14
            if self.vector[0][1] == self.computer_id and self.vector[1][1]==self.computer_id\
            and self.vector[2][1]==0 and self.vector[3][1]==self.computer_id:
                rand=10
            if self.vector[0][1] == self.computer_id and self.vector[1][1]==0\
            and self.vector[2][1]==self.computer_id and self.vector[3][1]==self.computer_id:
                    rand=6
            if self.vector[0][1] == 0 and self.vector[1][1]==self.computer_id\
            and self.vector[2][1]==self.computer_id and self.vector[3][1]==self.computer_id:
                rand=2
            #column 3
            if self.vector[0][2] == self.computer_id and self.vector[1][2]==self.computer_id\
            and self.vector[2][2]==self.computer_id and self.vector[3][2]==0:
                rand=15
            if self.vector[0][2] == self.computer_id and self.vector[1][2]==self.computer_id\
            and self.vector[2][2]==0 and self.vector[3][2]==self.computer_id:
                rand=11
            if self.vector[0][2] == self.computer_id and self.vector[1][2]==0\
            and self.vector[2][2]==self.computer_id and self.vector[3][2]==self.computer_id:
                rand=7
            if self.vector[0][2] == 0 and self.vector[1][2]==self.computer_id\
            and self.vector[2][2]==self.computer_id and self.vector[3][2]==self.computer_id:
                rand=3
            #Column 4
            if self.vector[0][3] == self.computer_id and self.vector[1][3]==self.computer_id\
            and self.vector[2][3]==self.computer_id and self.vector[3][3]==0:
                rand=16
            if self.vector[0][3] == self.computer_id and self.vector[1][3]==self.computer_id\
            and self.vector[2][3]==0 and self.vector[3][3]==self.computer_id:
                rand=12
            if self.vector[0][3] == self.computer_id and self.vector[1][3]==0\
            and self.vector[2][3]==self.computer_id and self.vector[3][3]==self.computer_id:
                rand=8
            if self.vector[0][3] ==0 and self.vector[1][3]==self.computer_id\
            and self.vector[2][3]==self.computer_id and self.vector[3][3]==self.computer_id:
                rand=4
            #######################################Vertices########################################
            #the right vertice
            if self.vector[0][0]==self.computer_id and self.vector[1][1]==self.computer_id\
            and self.vector[2][2]==self.computer_id and self.vector[3][3]==0:
                rand=16
            if self.vector[0][0]==self.computer_id and self.vector[1][1]==self.computer_id\
            and self.vector[2][2]==0 and self.vector[3][3]==self.computer_id:
                rand=11
            if self.vector[0][0]==self.computer_id and self.vector[1][1]==0\
            and self.vector[2][2]==self.computer_id and self.vector[3][3]==self.computer_id:
                rand=6
            if self.vector[0][0]==0 and self.vector[1][1]==self.computer_id\
            and self.vector[2][2]==self.computer_id and self.vector[3][3]==self.computer_id:
                rand=1
            ### the left vertice
            if self.vector[0][3]==self.computer_id and self.vector[1][2]==self.computer_id\
            and self.vector[2][1]==self.computer_id and self.vector[3][0]==0:
                rand=13
            if self.vector[0][3]==self.computer_id and self.vector[1][2]==self.computer_id\
            and self.vector[2][1]==0 and self.vector[3][0]==self.computer_id:
                rand=10
            if self.vector[0][3]==self.computer_id and self.vector[1][2]==0\
            and self.vector[2][1]==self.computer_id and self.vector[3][0]==self.computer_id:
                rand=7
            if self.vector[0][3]==0 and self.vector[1][2]==self.computer_id\
            and self.vector[2][1]==self.computer_id and self.vector[3][0]==self.computer_id:
                rand=4

                
            
            

            
            ####applying the choosen values to the game board..... :)
            if rand==1:
                if self.Computer=='cross':
                    self.board.one.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[0][0]=self.computer_id
                    self.true_play+=1
                else:
                    self.board.one.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[0][0]= self.computer_id
                    self.true_play+=1
                
            if rand==2:
                if self.Computer=='cross':
                    self.board.two.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[0][1]=self.computer_id
                    self.true_play+=1
                else:
                    self.board.two.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[0][1]= self.computer_id
                    self.true_play+=1
                    
            if rand==3:
                if self.Computer=='cross':
                    self.board.three.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[0][2]=self.computer_id
                    self.true_play+=1
                else:
                    self.board.three.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[0][2]= self.computer_id
                    self.true_play+=1
                    
            if rand==4:
                if self.Computer=='cross':
                    self.board.four.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[0][3]=self.computer_id
                    self.true_play+=1
                    
                else:
                    self.board.four.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[0][3]= self.computer_id
                    self.true_play+=1
               
            if rand==5:
                if self.Computer=='cross':
                    self.board.one_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[1][0]=self.computer_id
                    self.true_play+=1
                 
                else:
                    self.board.one_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[1][0]= self.computer_id
                    self.true_play+=1
                
            if rand==6:
                if self.Computer=='cross':
                    self.board.two_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[1][1]=self.computer_id
                    self.true_play+=1
                    
                else:
                    self.board.two_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[1][1]= self.computer_id
                    self.true_play+=1
                   
            if rand==7:
                if self.Computer=='cross':
                    self.board.three_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[1][2]=self.computer_id
                    self.true_play+=1
                   
                else:
                    self.board.three_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[1][2]= self.computer_id
                    self.true_play+=1
                 
            if rand==8:
                if self.Computer=='cross':
                    self.board.four_2.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[1][3]=self.computer_id
                    self.true_play+=1
                
                else:
                    self.board.four_2.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[1][3]= self.computer_id
                    self.true_play+=1
                   
            if rand==9:
                if self.Computer=='cross':
                    self.board.one_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[2][0]=self.computer_id
                    self.true_play+=1
                    
                else:
                    self.board.one_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[2][0]= self.computer_id
                    self.true_play+=1
                  
            if rand==10:
                if self.Computer=='cross':
                    self.board.two_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[2][1]=self.computer_id
                    self.true_play+=1
                
                else:
                    self.board.two_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[2][1]= self.computer_id
                    self.true_play+=1
                 
            if rand==11:
                if self.Computer=='cross':
                    self.board.three_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[2][2]=self.computer_id
                    self.true_play+=1
             
                else:
                    self.board.three_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[2][2]= self.computer_id
                    self.true_play+=1
      
            if rand==12:
                if self.Computer=='cross':
                    self.board.four_3.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[2][3]=self.computer_id
                    self.true_play+=1
                
                else:
                    self.board.four_3.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[2][3]= self.computer_id
                    self.true_play+=1
               
            if rand==13:
                if self.Computer=='cross':
                    self.board.one_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[3][0]=self.computer_id
                    self.true_play+=1
                    
                else:
                    self.board.one_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[3][0]= self.computer_id
                    self.true_play+=1
                   
            if rand==14:
                if self.Computer=='cross':
                    self.board.two_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[3][1]=self.computer_id
                    self.true_play+=1
                 
                else:
                    self.board.two_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[3][1]= self.computer_id
                    self.true_play+=1
                  
            if rand==15:
                if self.Computer=='cross':
                    self.board.three_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[3][2]=self.computer_id
                    self.true_play+=1
                    
                else:
                    self.board.three_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[3][2]= self.computer_id
                    self.true_play+=1
             
            if rand==16:
                if self.Computer=='cross':
                    self.board.four_4.setStyleSheet("""image: url(:/newPrefix/cross.png);
                                                 background-image: url(:/newPrefix/textEdit_2.png);""")
                    self.vector[3][3]=self.computer_id
                    self.true_play+=1
              
                else:
                    self.board.four_4.setStyleSheet("""image: url(:/newPrefix/nut.png);
     background-image: url(:/newPrefix/textEdit.png);""")
                    self.vector[3][3]= self.computer_id
                    self.true_play+=1
                
            self.CHECK()
img = random.randint(1,1)
if img == 1:
    import img
else:
    import img_1
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Game() 
    MainWindow.show()
    sys.exit(app.exec_())
        
