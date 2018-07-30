from PyQt5 import QtCore,QtGui,QtWidgets
srC=super
srq=str
srx=print
srP=len
srX=int
srR=QtWidgets.QApplication
srU=QtWidgets.QTableWidgetItem
srt=QtWidgets.QComboBox
srG=QtWidgets.QLineEdit
srw=QtWidgets.QPushButton
srv=QtWidgets.QTableWidget
srk=QtWidgets.QLabel
sre=QtWidgets.QMainWindow
srn=QtCore.Qt
srM=QtCore.QCoreApplication
srh=QtCore.QMetaObject
src=QtCore.QRect
import sys
srg=sys.exit
srQ=sys.argv
import pymysql
sra=pymysql.connect
import FormMain
srD='db_saw_python'
srl=''
sro='root'
srN='127.0.0.1'
class RtoijjU(sre):
 def __init__(srT):
  super().__init__()
  srT.srJ(srT)
 def srJ(srT,srB):
  srB.setObjectName("RtoijjU")
  srB.resize(444,361)
  srT.label=srk(srB)
  srT.label.setGeometry(src(20,50,121,16))
  srT.label.setObjectName("label")
  srT.label_2=srk(srB)
  srT.label_2.setGeometry(src(20,20,121,16))
  srT.label_2.setObjectName("label_2")
  srT.xxDghj=srv(srB)
  srT.xxDghj.setGeometry(src(20,110,401,201))
  srT.xxDghj.setObjectName("xxDghj")
  srT.xxDghj.setColumnCount(0)
  srT.xxDghj.setRowCount(0)
  srT.amRtUo=srw(srB)
  srT.amRtUo.setGeometry(src(20,320,75,23))
  srT.amRtUo.setObjectName("amRtUo")
  srT.oppTri=srw(srB)
  srT.oppTri.setGeometry(src(100,320,75,23))
  srT.oppTri.setObjectName("oppTri")
  srT.iuoEdRt=srw(srB)
  srT.iuoEdRt.setGeometry(src(180,320,75,23))
  srT.iuoEdRt.setObjectName("iuoEdRt")
  srT.xsDcf=srw(srB)
  srT.xsDcf.setGeometry(src(350,320,75,23))
  srT.xsDcf.setObjectName("xsDcf")
  srT.label_3=srk(srB)
  srT.label_3.setGeometry(src(20,80,121,16))
  srT.label_3.setObjectName("label_3")
  srT.oWerrT=srG(srB)
  srT.oWerrT.setGeometry(src(160,80,261,20))
  srT.oWerrT.setObjectName("oWerrT")
  srT.uRTIo=srt(srB)
  srT.uRTIo.setGeometry(src(160,20,261,22))
  srT.uRTIo.setObjectName("uRTIo")
  srT.uRTIo.addItem("")
  srT.uRTIo.setItemText(0,"")
  srT.aaSSdFF=srt(srB)
  srT.aaSSdFF.setGeometry(src(160,50,261,22))
  srT.aaSSdFF.setObjectName("aaSSdFF")
  srT.aaSSdFF.addItem("")
  srT.aaSSdFF.setItemText(0,"")
  srT.amRtUo.clicked.connect(srT.srL)
  srT.oppTri.clicked.connect(srT.sru)
  srT.xsDcf.clicked.connect(srT.srp)
  srT.iuoEdRt.clicked.connect(srT.srI)
  srT.srF(srB)
  srh.connectSlotsByName(srB)
 def srF(srT,srB):
  srV=srM.translate
  srB.setWindowTitle(srV("RtoijjU","Data Nilai Alternatif Kriteria"))
  srT.label.setText(srV("RtoijjU","Kriteria"))
  srT.label_2.setText(srV("RtoijjU","Alternatif"))
  srT.amRtUo.setText(srV("RtoijjU","Insert"))
  srT.oppTri.setText(srV("RtoijjU","Update"))
  srT.iuoEdRt.setText(srV("RtoijjU","Clear"))
  srT.xsDcf.setText(srV("RtoijjU","Delete"))
  srT.label_3.setText(srV("RtoijjU","Nilai"))
  srT.sry()
  srT.srb()
  srT.srW()
  srT.show()
 def sry(srT):
  db=sra(srN,sro,srl,srD)
  srE=db.cursor()
  srz="SELECT * FROM alternatif"
  srT.list_id_alternatif=[]
  srT.uRTIo.clear()
  try:
   srE.execute(srz)
   srj=srE.fetchall()
   i=0
   for srY in srj:
    srT.list_id_alternatif.append(srq(srY[0]))
    srT.uRTIo.addItem(srY[1])
    i=i+1
  except:
   srx("Error: unable to fetch data")
  db.close()
 def srb(srT):
  db=sra(srN,sro,srl,srD)
  srE=db.cursor()
  srz="SELECT * FROM kriteria"
  srT.list_id_kriteria=[]
  srT.aaSSdFF.clear()
  try:
   srE.execute(srz)
   srj=srE.fetchall()
   i=0
   for srY in srj:
    srT.list_id_kriteria.append(srq(srY[0]))
    srT.aaSSdFF.addItem(srY[1])
    i=i+1
  except:
   srx("Error: unable to fetch data")
  db.close()
 def srW(srT):
  db=sra(srN,sro,srl,srD)
  srE=db.cursor()
  srz="SELECT alternatif_kriteria.*, alternatif.nama_alternatif, kriteria.nama_kriteria FROM alternatif_kriteria LEFT JOIN alternatif ON alternatif.id_alternatif = alternatif_kriteria.id_alternatif LEFT JOIN kriteria ON alternatif_kriteria.id_kriteria = kriteria.id_kriteria"
  try:
   srE.execute(srz)
   srj=srE.fetchall()
   srT.xxDghj.setColumnCount(4)
   srT.xxDghj.setRowCount(srP(srj)) 
   srT.xxDghj.setHorizontalHeaderLabels(('Id','Alternatif','Kriteria','Nilai'))
   i=0
   srT.vheader=[]
   for srY in srj:
    srT.vheader.append('')
    srT.xxDghj.setItem(i,0,srU(srq(srY[0])))
    srT.xxDghj.setItem(i,1,srU(srY[4]))
    srT.xxDghj.setItem(i,2,srU(srY[5]))
    srT.xxDghj.setItem(i,3,srU(srq(srY[3])))
    i=i+1
   srT.id_alternatif_kriteria=""
   srT.xxDghj.setVerticalHeaderLabels(srT.vheader)
   srT.xxDghj.cellClicked.connect(srT.srO)
  except:
   srx("Error: unable to fetch data")
  db.close()
 def srO(srT,srY,column):
  srT.id_alternatif_kriteria=srT.xxDghj.item(srX(srY),0).text()
  srS=srT.uRTIo.findText(srT.xxDghj.item(srX(srY),1).text(),srn.MatchFixedString)
  if srS>=0:
   srT.uRTIo.setCurrentIndex(srS)
  srS=srT.aaSSdFF.findText(srT.xxDghj.item(srX(srY),2).text(),srn.MatchFixedString)
  if srS>=0:
   srT.aaSSdFF.setCurrentIndex(srS)
  srT.oWerrT.setText(srT.xxDghj.item(srX(srY),3).text())
 def srL(srT):
  db=sra(srN,sro,srl,srD)
  srE=db.cursor()
  srz="insert into alternatif_kriteria(id_alternatif,             id_kriteria, nilai)             values ('%s', '%s', '%s')"% (srT.list_id_alternatif[srT.uRTIo.currentIndex()],srT.list_id_kriteria[srT.aaSSdFF.currentIndex()],srT.oWerrT.text())
  try:
   srE.execute(srz)
   db.commit()
  except:
   db.rollback()
  db.close()
  srT.srI()
  srT.srW()
 def sru(srT):
  db=sra(srN,sro,srl,srD)
  srE=db.cursor()
  srz="update alternatif_kriteria set id_alternatif = '%s', id_kriteria = '%s',             nilai = '%s' where id_alternatif_kriteria = '%s'"% (srT.list_id_alternatif[srT.uRTIo.currentIndex()],srT.list_id_kriteria[srT.aaSSdFF.currentIndex()],srT.oWerrT.text(),srT.id_alternatif_kriteria)
  try:
   srE.execute(srz)
   db.commit()
  except:
   db.rollback()
  db.close()
  srT.srI()
  srT.srW()
 def srp(srT):
  db=sra(srN,sro,srl,srD)
  srE=db.cursor()
  srz="delete from alternatif_kriteria where id_alternatif_kriteria = '%s'"% (srT.id_alternatif_kriteria)
  try:
   srE.execute(srz)
   db.commit()
  except:
   db.rollback()
  db.close()
  srT.srI()
  srT.srW()
 def srI(srT):
  srT.uRTIo.setCurrentIndex(0)
  srT.aaSSdFF.setCurrentIndex(0)
  srT.oWerrT.setText("")
