from PyQt5 import QtCore,QtGui,QtWidgets
sPo=super
sPL=len
sPJ=str
sPg=print
sPG=int
sPQ=QtWidgets.QApplication
sPd=QtWidgets.QTableWidgetItem
sPm=QtWidgets.QPushButton
sPt=QtWidgets.QTableWidget
sPn=QtWidgets.QLabel
sPj=QtWidgets.QTextEdit
sPN=QtWidgets.QLineEdit
sPb=QtWidgets.QMainWindow
sPp=QtCore.QCoreApplication
sPq=QtCore.QMetaObject
sPH=QtCore.QRect
import sys
sPM=sys.exit
sPK=sys.argv
import pymysql
sPB=pymysql.connect
sPx='db_saw_python'
sPw=''
sPe='root'
sPz='127.0.0.1'
class FGGhrts(sPb):
 def __init__(sPy):
  super().__init__()
  sPy.sPr(sPy)
 def sPr(sPy,sPf):
  sPf.setObjectName("FGGhrts")
  sPf.resize(444,361)
  sPy.tNNP=sPN(sPf)
  sPy.tNNP.setGeometry(sPH(160,20,261,20))
  sPy.tNNP.setObjectName("tNNP")
  sPy.dtPPr=sPj(sPf)
  sPy.dtPPr.setGeometry(sPH(160,50,261,61))
  sPy.dtPPr.setObjectName("dtPPr")
  sPy.label=sPn(sPf)
  sPy.label.setGeometry(sPH(20,20,121,16))
  sPy.label.setObjectName("label")
  sPy.label_2=sPn(sPf)
  sPy.label_2.setGeometry(sPH(20,50,47,13))
  sPy.label_2.setObjectName("label_2")
  sPy.AttrbT=sPt(sPf)
  sPy.AttrbT.setGeometry(sPH(20,130,401,181))
  sPy.AttrbT.setObjectName("AttrbT")
  sPy.AttrbT.setColumnCount(0)
  sPy.AttrbT.setRowCount(0)
  sPy.trNss=sPm(sPf)
  sPy.trNss.setGeometry(sPH(20,320,75,23))
  sPy.trNss.setObjectName("trNss")
  sPy.bUdddlt=sPm(sPf)
  sPy.bUdddlt.setGeometry(sPH(100,320,75,23))
  sPy.bUdddlt.setObjectName("bUdddlt")
  sPy.cCdltt=sPm(sPf)
  sPy.cCdltt.setGeometry(sPH(180,320,75,23))
  sPy.cCdltt.setObjectName("cCdltt")
  sPy.tdDDlb=sPm(sPf)
  sPy.tdDDlb.setGeometry(sPH(350,320,75,23))
  sPy.tdDDlb.setObjectName("tdDDlb")
  sPy.trNss.clicked.connect(sPy.sPT)
  sPy.bUdddlt.clicked.connect(sPy.sPu)
  sPy.tdDDlb.clicked.connect(sPy.sPR)
  sPy.cCdltt.clicked.connect(sPy.sPA)
  sPy.sPF(sPf)
  sPq.connectSlotsByName(sPf)
 def sPF(sPy,sPf):
  sPl=sPp.translate
  sPf.setWindowTitle(sPl("Form","Data Alternatif"))
  sPy.label.setText(sPl("Form","Nama Alternatif Produk"))
  sPy.label_2.setText(sPl("Form","Deskripsi"))
  sPy.trNss.setText(sPl("Form","Insert"))
  sPy.bUdddlt.setText(sPl("Form","Update"))
  sPy.cCdltt.setText(sPl("Form","Clear"))
  sPy.tdDDlb.setText(sPl("Form","Delete"))
  sPy.sPC()
  sPy.show()
 def sPC(sPy):
  db=sPB(sPz,sPe,sPw,sPx)
  sPY=db.cursor()
  sPU="SELECT * FROM alternatif" 
  try:
   sPY.execute(sPU)
   sPD=sPY.fetchall()
   sPy.AttrbT.setColumnCount(3)
   sPy.AttrbT.setRowCount(sPL(sPD))
   sPy.AttrbT.setHorizontalHeaderLabels(('Id Alternatif','Nama Alternatif','Deskripsi'))
   i=0
   sPy.vheader=[]
   for sPX in sPD:
    sPy.vheader.append('')
    sPy.AttrbT.setItem(i,0,sPd(sPJ(sPX[0])))
    sPy.AttrbT.setItem(i,1,sPd(sPX[1]))
    sPy.AttrbT.setItem(i,2,sPd(sPX[2]))
    i=i+1
   sPy.id_alternatif=""
   sPy.AttrbT.setVerticalHeaderLabels(sPy.vheader)
   sPy.AttrbT.cellClicked.connect(sPy.sPv)
  except:
   sPg("Error: unable to fetch data")
  db.close()
 def sPv(sPy,sPX,column):
  sPy.id_alternatif=sPy.AttrbT.item(sPG(sPX),0).text()
  sPy.tNNP.setText(sPy.AttrbT.item(sPG(sPX),1).text())
  sPy.dtPPr.setText(sPy.AttrbT.item(sPG(sPX),2).text())
 def sPT(sPy):
  db=sPB(sPz,sPe,sPw,sPx)
  sPY=db.cursor()
  sPU="insert into alternatif(nama_alternatif,             deskripsi)             values ('%s', '%s')"% (sPy.tNNP.text(),sPy.dtPPr.toPlainText())
  try:
   sPY.execute(sPU)
   db.commit()
  except:
   db.rollback()
  db.close()
  sPy.sPA()
  sPy.sPC()
 def sPu(sPy):
  db=sPB(sPz,sPe,sPw,sPx)
  sPY=db.cursor()
  sPU="update alternatif set nama_alternatif = '%s',             deskripsi = '%s' where id_alternatif = '%s'"% (sPy.tNNP.text(),sPy.dtPPr.toPlainText(),sPy.id_alternatif)
  try:
   sPY.execute(sPU)
   db.commit()
  except:
   db.rollback()
  db.close()
  sPy.sPA()
  sPy.sPC()
 def sPR(sPy):
  db=sPB(sPz,sPe,sPw,sPx)
  sPY=db.cursor()
  sPU="delete from alternatif where id_alternatif = '%s'"% (sPy.id_alternatif)
  try:
   sPY.execute(sPU)
   db.commit()
  except:
   db.rollback()
  db.close()
  sPy.sPA()
  sPy.sPC()
 def sPA(sPy):
  sPy.tNNP.setText("")
  sPy.dtPPr.setText("")
