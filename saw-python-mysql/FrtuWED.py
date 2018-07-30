from PyQt5 import QtCore,QtGui,QtWidgets
weA=super
weC=print
weM=QtWidgets.QApplication
wek=QtWidgets.QMessageBox
weY=QtWidgets.QPushButton
wem=QtWidgets.QLabel
wej=QtWidgets.QLineEdit
wel=QtWidgets.QMainWindow
weL=QtCore.QCoreApplication
weG=QtCore.QMetaObject
weo=QtCore.QRect
import sys
weH=sys.exit
wec=sys.argv
import pymysql
weQ=pymysql.connect
import FormMain
weB='db_saw_python'
weP=''
wes='root'
wei='127.0.0.1'
weS='admin'
class FrtuWED(wel):
 def __init__(weD):
  super().__init__()
  weD.wep(weD)
 def wep(weD,weJ):
  weJ.setObjectName("FrtuWED")
  weJ.resize(293,177)
  weD.xDDFGh=wej(weJ)
  weD.xDDFGh.setGeometry(weo(130,20,141,20))
  weD.xDDFGh.setObjectName("xDDFGh")
  weD.label=wem(weJ)
  weD.label.setGeometry(weo(20,20,61,16))
  weD.label.setObjectName("label")
  weD.label_2=wem(weJ)
  weD.label_2.setGeometry(weo(20,50,91,16))
  weD.label_2.setObjectName("label_2")
  weD.oBgdHi=weY(weJ)
  weD.oBgdHi.setGeometry(weo(20,140,75,23))
  weD.oBgdHi.setObjectName("oBgdHi")
  weD.LLmGdh=weY(weJ)
  weD.LLmGdh.setGeometry(weo(200,140,75,23))
  weD.LLmGdh.setObjectName("LLmGdh")
  weD.uEEfRt=wej(weJ)
  weD.uEEfRt.setGeometry(weo(130,50,141,20))
  weD.uEEfRt.setInputMask("")
  weD.uEEfRt.setObjectName("uEEfRt")
  weD.label_3=wem(weJ)
  weD.label_3.setGeometry(weo(20,110,101,16))
  weD.label_3.setObjectName("label_3")
  weD.eWWTRE=wej(weJ)
  weD.eWWTRE.setGeometry(weo(130,80,141,20))
  weD.eWWTRE.setObjectName("eWWTRE")
  weD.label_4=wem(weJ)
  weD.label_4.setGeometry(weo(20,80,91,16))
  weD.label_4.setObjectName("label_4")
  weD.RTOide=wej(weJ)
  weD.RTOide.setGeometry(weo(130,110,141,20))
  weD.RTOide.setInputMask("")
  weD.RTOide.setObjectName("RTOide")
  weD.oBgdHi.clicked.connect(weD.weq)
  weD.LLmGdh.clicked.connect(weD.wea)
  weD.weE(weJ)
  weG.connectSlotsByName(weJ)
 def weE(weD,weJ):
  wet=weL.translate
  weJ.setWindowTitle(wet("FrtuWED","Ganti Password"))
  weD.label.setText(wet("FrtuWED","Username"))
  weD.label_2.setText(wet("FrtuWED","Password Lama"))
  weD.oBgdHi.setText(wet("FrtuWED","Update"))
  weD.LLmGdh.setText(wet("FrtuWED","Cancel"))
  weD.label_3.setText(wet("FrtuWED","Konfirmasi Password"))
  weD.label_4.setText(wet("FrtuWED","Password Baru"))
  weD.show()
  weD.xDDFGh.setText(weS)
 def weq(weD):
  db=weQ(wei,wes,weP,weB)
  weg=db.cursor()
  wen="SELECT * FROM `login` WHERE `username` = '%s' AND `password` = '%s'"%(weS,weD.uEEfRt.text()) 
  weg.execute(wen)
  weK=weg.fetchall()
  if weK:
   if weD.eWWTRE.text()==weD.RTOide.text():
    web=weQ(wei,wes,weP,weB)
    weh=web.cursor()
    wex="update login set password = '%s'                              where username = '%s'"% (weD.eWWTRE.text(),weS)
    try:
     weh.execute(wex)
     web.commit()
    except:
     web.rollback()
    web.close()
    weD.close()
   else:
    weN=wek()
    weN.setIcon(wek.Information)
    weN.setText("Password Baru Tidak Sama")
    weN.setWindowTitle("Peringatan")
    weN.setStandardButtons(wek.Ok)
    wer=weN.exec_()
  else:
   weN=wek()
   weN.setIcon(wek.Information)
   weN.setText("Password Lama Salah")
   weN.setWindowTitle("Peringatan")
   weN.setStandardButtons(wek.Ok)
   wer=weN.exec_()
   weC("gagal")
  db.close()
 def wea(weD):
  weD.close()
