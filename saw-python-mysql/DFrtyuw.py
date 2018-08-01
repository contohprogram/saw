from PyQt5 import QtCore,QtGui,QtWidgets
ocQ=super
ocD=len
ocW=str
ocf=print
ocj=int
ocC=QtWidgets.QApplication
wek=QtWidgets.QMessageBox
och=QtWidgets.QTableWidgetItem
ocK=QtWidgets.QComboBox
ocq=QtWidgets.QPushButton
ocH=QtWidgets.QTableWidget
ocN=QtWidgets.QLabel
ocY=QtWidgets.QLineEdit
ocl=QtWidgets.QMainWindow
ocO=QtCore.Qt
ocX=QtCore.QCoreApplication
ocy=QtCore.QMetaObject
ocU=QtCore.QRect
import sys
ocr=sys.exit
ocw=sys.argv
import pymysql
ocL=pymysql.connect
import FormMain
ocS='db_saw_python'
ocT=''
ocM='root'
ocJ='127.0.0.1'
class DFrtyuw(ocl):
 def __init__(ocm):
  super().__init__()
  ocm.ocn(ocm)
 def ocn(ocm,ocu):
  ocu.setObjectName("DFrtyuw")
  ocu.resize(444,361)
  ocm.txRmt=ocY(ocu)
  ocm.txRmt.setGeometry(ocU(160,20,261,20))
  ocm.txRmt.setObjectName("txRmt")
  ocm.label=ocN(ocu)
  ocm.label.setGeometry(ocU(20,20,121,16))
  ocm.label.setObjectName("label")
  ocm.rtAAb=ocH(ocu)
  ocm.rtAAb.setGeometry(ocU(20,120,401,191))
  ocm.rtAAb.setObjectName("rtAAb")
  ocm.rtAAb.setColumnCount(0)
  ocm.rtAAb.setRowCount(0)
  ocm.inRtbs=ocq(ocu)
  ocm.inRtbs.setGeometry(ocU(20,320,75,23))
  ocm.inRtbs.setObjectName("inRtbs")
  ocm.updRpt=ocq(ocu)
  ocm.updRpt.setGeometry(ocU(100,320,75,23))
  ocm.updRpt.setObjectName("updRpt")
  ocm.cRlte=ocq(ocu)
  ocm.cRlte.setGeometry(ocU(180,320,75,23))
  ocm.cRlte.setObjectName("cRlte")
  ocm.tfrGts=ocq(ocu)
  ocm.tfrGts.setGeometry(ocU(350,320,75,23))
  ocm.tfrGts.setObjectName("tfrGts")
  ocm.cGrtos=ocK(ocu)
  ocm.cGrtos.setGeometry(ocU(160,80,261,22))
  ocm.cGrtos.setObjectName("cGrtos")
  ocm.cGrtos.addItem("")
  ocm.cGrtos.setItemText(0,"")
  ocm.cGrtos.addItem("")
  ocm.cGrtos.addItem("")
  ocm.label_3=ocN(ocu)
  ocm.label_3.setGeometry(ocU(20,50,121,16))
  ocm.label_3.setObjectName("label_3")
  ocm.jjUrts=ocY(ocu)
  ocm.jjUrts.setGeometry(ocU(160,50,261,20))
  ocm.jjUrts.setObjectName("jjUrts")
  ocm.label_2=ocN(ocu)
  ocm.label_2.setGeometry(ocU(20,80,121,16))
  ocm.label_2.setObjectName("label_2")
  ocm.inRtbs.clicked.connect(ocm.ocE)
  ocm.updRpt.clicked.connect(ocm.ocv)
  ocm.tfrGts.clicked.connect(ocm.ocg)
  ocm.cRlte.clicked.connect(ocm.ocF)
  ocm.ocI(ocu)
  ocy.connectSlotsByName(ocu)
 def ocI(ocm,ocu):
  oci=ocX.translate
  ocu.setWindowTitle(oci("DFrtyuw","Data Kriteria"))
  ocm.label.setText(oci("DFrtyuw","Nama Kriteria"))
  ocm.inRtbs.setText(oci("DFrtyuw","Insert"))
  ocm.updRpt.setText(oci("DFrtyuw","Update"))
  ocm.cRlte.setText(oci("DFrtyuw","Clear"))
  ocm.tfrGts.setText(oci("DFrtyuw","Delete"))
  ocm.cGrtos.setItemText(1,oci("DFrtyuw","cost"))
  ocm.cGrtos.setItemText(2,oci("DFrtyuw","benefit"))
  ocm.label_3.setText(oci("DFrtyuw","Kepentingan"))
  ocm.label_2.setText(oci("DFrtyuw","Cost Benefit"))
  ocm.oce()
  ocm.show()
 def oce(ocm):
  db=ocL(ocJ,ocM,ocT,ocS)
  ocR=db.cursor()
  ocx="SELECT * FROM kriteria" 
  try:
   ocR.execute(ocx)
   ocA=ocR.fetchall()
   ocm.rtAAb.setColumnCount(4)
   ocm.rtAAb.setRowCount(ocD(ocA)) 
   ocm.rtAAb.setHorizontalHeaderLabels(('Id Kriteria','Nama Kriteria','Kepentingan','Cost Benefit'))
   i=0
   ocm.vheader=[]
   for ocV in ocA:
    ocm.vheader.append('')
    ocm.rtAAb.setItem(i,0,och(ocW(ocV[0])))
    ocm.rtAAb.setItem(i,1,och(ocV[1]))
    ocm.rtAAb.setItem(i,2,och(ocW(ocV[2])))
    ocm.rtAAb.setItem(i,3,och(ocV[3]))
    i=i+1
   ocm.id_kriteria=""
   ocm.rtAAb.setVerticalHeaderLabels(ocm.vheader)
   ocm.rtAAb.cellClicked.connect(ocm.ocp)
  except:
   ocf("Error: unable to fetch data")
  db.close()
 def ocp(ocm,ocV,column):
  ocm.id_kriteria=ocm.rtAAb.item(ocj(ocV),0).text()
  ocm.txRmt.setText(ocm.rtAAb.item(ocj(ocV),1).text())
  ocm.jjUrts.setText(ocm.rtAAb.item(ocj(ocV),2).text())
  ocd=ocm.cGrtos.findText(ocm.rtAAb.item(ocj(ocV),3).text(),ocO.MatchFixedString)
  if ocd>=0:
   ocm.cGrtos.setCurrentIndex(ocd)
 def ocE(ocm):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  ocm.oce()
 def ocv(ocm):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  ocm.ocF()
  ocm.oce()
 def ocg(ocm):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  ocm.oce()
 def ocF(ocm):
  ocm.txRmt.setText("")
  ocm.jjUrts.setText("")
  ocm.cGrtos.setCurrentIndex(0)
