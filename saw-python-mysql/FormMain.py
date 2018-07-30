from PyQt5 import QtCore,QtGui,QtWidgets
enT=super
enF=True
enw=False
enf=QtWidgets.QApplication
enO=QtWidgets.QAction
enV=QtWidgets.QStatusBar
enY=QtWidgets.QMenu
eng=QtWidgets.QMenuBar
end=QtWidgets.QWidget
enz=QtWidgets.QMainWindow
enA=QtCore.QCoreApplication
enD=QtCore.QMetaObject
enW=QtCore.QRect
import sys
enc=sys.exit
eno=sys.argv
from FGGhrts import *
from RtoijjU import *
from DFrtyuw import *
from ZxDFgrt import *
from FrtuWED import *
from SdEktrw import *
from Poeiuns import *
enk='127.0.0.1'
env='root'
ent=''
enb='db_saw_python'
enq=''
class FormMain(enz):
 def __init__(eni):
  super().__init__()
  eni.enl(eni)
 def enl(eni,enx):
  enx.setObjectName("FormMain")
  enx.resize(800,520)
  eni.centralwidget=end(enx)
  eni.centralwidget.setObjectName("centralwidget")
  enx.setCentralWidget(eni.centralwidget)
  eni.reWTGS=eng(enx)
  eni.reWTGS.setGeometry(enW(0,0,800,21))
  eni.reWTGS.setObjectName("reWTGS")
  eni.iRuWSED=enY(eni.reWTGS)
  eni.iRuWSED.setObjectName("iRuWSED")
  eni.KJDLWE=enY(eni.reWTGS)
  eni.KJDLWE.setObjectName("KJDLWE")
  eni.KEdFTG=enY(eni.reWTGS)
  eni.KEdFTG.setObjectName("KEdFTG")
  eni.uRtDFG=enY(eni.reWTGS)
  eni.uRtDFG.setObjectName("uRtDFG")
  enx.setMenuBar(eni.reWTGS)
  eni.lksafdE=enV(enx)
  eni.lksafdE.setObjectName("lksafdE")
  enx.setStatusBar(eni.lksafdE)
  eni.zzzzxDFR=enO(enx)
  eni.zzzzxDFR.setObjectName("zzzzxDFR")
  eni.lkOrDERD=enO(enx)
  eni.lkOrDERD.setObjectName("lkOrDERD")
  eni.kkRtonss=enO(enx)
  eni.kkRtonss.setObjectName("kkRtonss")
  eni.enLdRE=enO(enx)
  eni.enLdRE.setObjectName("enLdRE")
  eni.enOerTY=enO(enx)
  eni.enOerTY.setObjectName("enOerTY")
  eni.RRUTdfrWE=enO(enx)
  eni.RRUTdfrWE.setObjectName("RRUTdfrWE")
  eni.eniAs=enO(enx)
  eni.eniAs.setObjectName("eniAs")
  eni.RRUTdfr=enO(enx)
  eni.RRUTdfr.setObjectName("RRUTdfr")
  eni.bRDfGRT=enO(enx)
  eni.bRDfGRT.setObjectName("bRDfGRT")
  eni.iRuWSED.addAction(eni.zzzzxDFR)
  eni.iRuWSED.addAction(eni.lkOrDERD)
  eni.iRuWSED.addAction(eni.kkRtonss)
  eni.KJDLWE.addAction(eni.enLdRE)
  eni.KJDLWE.addAction(eni.enOerTY)
  eni.KJDLWE.addAction(eni.RRUTdfrWE)
  eni.KEdFTG.addAction(eni.eniAs)
  eni.KEdFTG.addAction(eni.RRUTdfr)
  eni.reWTGS.addAction(eni.iRuWSED.menuAction())
  eni.reWTGS.addAction(eni.KJDLWE.menuAction())
  eni.reWTGS.addAction(eni.KEdFTG.menuAction())
  eni.reWTGS.addAction(eni.uRtDFG.menuAction())
  eni.uRtDFG.addAction(eni.bRDfGRT)
  eni.enLdRE.triggered.connect(eni.enI)
  eni.RRUTdfrWE.triggered.connect(eni.enJ)
  eni.enOerTY.triggered.connect(eni.eny)
  eni.RRUTdfr.triggered.connect(eni.enC)
  eni.eniAs.triggered.connect(eni.enE)
  eni.zzzzxDFR.triggered.connect(eni.enm)
  eni.lkOrDERD.triggered.connect(eni.enB)
  eni.kkRtonss.triggered.connect(eni.enQ)
  eni.bRDfGRT.triggered.connect(eni.enU)
  eni.ena(enx)
  enD.connectSlotsByName(enx)
 def ena(eni,enx):
  enS=enA.translate
  enx.setWindowTitle(enS("FormMain","SPK Metode SAW dengan Python dan MySQL- http://contohprogram.com"))
  eni.iRuWSED.setTitle(enS("FormMain","Utility"))
  eni.KJDLWE.setTitle(enS("FormMain","Data"))
  eni.KEdFTG.setTitle(enS("FormMain","Analisa"))
  eni.uRtDFG.setTitle(enS("FormMain","Keluar"))
  eni.zzzzxDFR.setText(enS("FormMain","Login"))
  eni.lkOrDERD.setText(enS("FormMain","Logout"))
  eni.kkRtonss.setText(enS("FormMain","Ganti Password"))
  eni.enLdRE.setText(enS("FormMain","Data Alternatif"))
  eni.enOerTY.setText(enS("FormMain","Data Kriteria"))
  eni.RRUTdfrWE.setText(enS("FormMain","Data Alternatif Kriteria"))
  eni.eniAs.setText(enS("FormMain","Metode SAW (Statis)"))
  eni.RRUTdfr.setText(enS("FormMain","Analisa SPK Metode SAW"))
  eni.bRDfGRT.setText(enS("FormMain","Keluar"))
  eni.zzzzxDFR.setEnabled(enF)
  eni.kkRtonss.setEnabled(enw)
  eni.lkOrDERD.setEnabled(enw)
  eni.enLdRE.setEnabled(enw)
  eni.enOerTY.setEnabled(enw)
  eni.RRUTdfrWE.setEnabled(enw)
  eni.show()
 def enI(eni):
  eni.FGGhrts=FGGhrts()
  eni.FGGhrts.show()
 def eny(eni):
  eni.DFrtyuw=DFrtyuw()
  eni.DFrtyuw.show()
 def enm(eni):
  eni.ZxDFgrt=ZxDFgrt()
  eni.ZxDFgrt.fMain=eni
  eni.ZxDFgrt.show()
 def enB(eni):
  FormMain.username_login=''
  eni.zzzzxDFR.setEnabled(enF)
  eni.kkRtonss.setEnabled(enw)
  eni.lkOrDERD.setEnabled(enw)
  eni.enLdRE.setEnabled(enw)
  eni.enOerTY.setEnabled(enw)
  eni.RRUTdfrWE.setEnabled(enw)
 def enQ(eni):
  eni.FrtuWED=FrtuWED()
  eni.FrtuWED.show()
 def enJ(eni):
  eni.RtoijjU=RtoijjU()
  eni.RtoijjU.show()
 def enC(eni):
  eni.Poeiuns=Poeiuns()
  eni.Poeiuns.show()
 def enE(eni):
  eni.SdEktrw=SdEktrw()
  eni.SdEktrw.show()
 def enU(eni):
  eni.close()
if __name__=='__main__':
 enL=enf(eno)
 ex=FormMain()
 enc(enL.exec())
