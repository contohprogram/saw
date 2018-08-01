from PyQt5 import QtCore,QtGui,QtWidgets
umH=super
umk=None
umi=False
umS=True
umt=print
umc=QtWidgets.QApplication
umU=QtWidgets.QMessageBox
umB=QtWidgets.QPushButton
umL=QtWidgets.QLabel
umb=QtWidgets.QLineEdit
umK=QtWidgets.QMainWindow
umX=QtCore.QCoreApplication
umY=QtCore.QMetaObject
umT=QtCore.QRect
import sys
umh=sys.exit
umR=sys.argv
import pymysql
umP=pymysql.connect
import FormMain
umG='admin'
umF='db_saw_python'
umr=''
umJ='root'
umN='127.0.0.1'
class ZxDFgrt(umK):
 def __init__(ume):
  super().__init__()
  ume.uma(ume)
  ume.fMain=umk
 def uma(ume,umz):
  umz.setObjectName("ZxDFgrt")
  umz.resize(293,130)
  ume.tUt=umb(umz)
  ume.tUt.setGeometry(umT(90,20,181,20))
  ume.tUt.setObjectName("tUt")
  ume.label=umL(umz)
  ume.label.setGeometry(umT(20,20,61,16))
  ume.label.setObjectName("label")
  ume.label_2=umL(umz)
  ume.label_2.setGeometry(umT(20,50,47,13))
  ume.label_2.setObjectName("label_2")
  ume.blN=umB(umz)
  ume.blN.setGeometry(umT(20,80,75,23))
  ume.blN.setObjectName("blN")
  ume.bXX=umB(umz)
  ume.bXX.setGeometry(umT(200,80,75,23))
  ume.bXX.setObjectName("bXX")
  ume.tPPp=umb(umz)
  ume.tPPp.setGeometry(umT(90,50,181,20))
  ume.tPPp.setInputMask("")
  ume.tPPp.setObjectName("tPPp")
  ume.labelPesan=umL(umz)
  ume.labelPesan.setGeometry(umT(20,110,251,16))
  ume.labelPesan.setText("username : admin, password : 123")
  ume.labelPesan.setObjectName("labelPesan")
  ume.blN.clicked.connect(ume.umf)
  ume.bXX.clicked.connect(ume.umn)
  ume.umv(umz)
  umY.connectSlotsByName(umz)
 def umv(ume,umz):
  umE=umX.translate
  umz.setWindowTitle(umE("ZxDFgrt","Login"))
  ume.label.setText(umE("ZxDFgrt","Username"))
  ume.label_2.setText(umE("ZxDFgrt","Password"))
  ume.blN.setText(umE("ZxDFgrt","Login"))
  ume.bXX.setText(umE("ZxDFgrt","Exit"))
  ume.show()
 def umf(ume):
  db=umP(umN,umJ,umr,umF)
  umg=db.cursor()
  umO="SELECT * FROM `login` WHERE `username` = '%s' AND `password` = '%s'"%(ume.tUt.text(),ume.tPPp.text()) 
  umg.execute(umO)
  umw=umg.fetchall()
  if umw:
   umG=umw[0][0]
   ume.fMain.zzzzxDFR.setEnabled(umi)
   ume.fMain.kkRtonss.setEnabled(umS)
   ume.fMain.lkOrDERD.setEnabled(umS)
   ume.fMain.enLdRE.setEnabled(umS)
   ume.fMain.enOerTY.setEnabled(umS)
   ume.fMain.RRUTdfrWE.setEnabled(umS)

   ume.close()
  else:
   umj=umU()
   umj.setIcon(umU.Information)
   umj.setText("Login Gagal")
   umj.setWindowTitle("Peringatan")
   umj.setStandardButtons(umU.Ok)
   ums=umj.exec_()
   umt("gagal")
  db.close()
 def umn(ume):
  ume.close()
