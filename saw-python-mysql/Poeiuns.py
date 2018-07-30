from PyQt5 import QtCore,QtGui,QtWidgets
gDG=super
ghD=len
ghM=str
ghz=print
ghW=float
ghS=range
gDo=QtWidgets.QApplication
gDH=QtWidgets.QTableWidgetItem
gDp=QtWidgets.QLabel
gDr=QtWidgets.QPushButton
gDd=QtWidgets.QTableWidget
gDw=QtWidgets.QMainWindow
gDe=QtCore.QCoreApplication
gDK=QtCore.QMetaObject
gDQ=QtCore.QRect
import sys
gDN=sys.exit
gDB=sys.argv
import pymysql
gDT=pymysql.connect
import FormMain
gDq='db_saw_python'
gDP=''
gDV='root'
gDf='127.0.0.1'
class Poeiuns(gDw):
 def __init__(gDM):
  super().__init__()
  gDM.gDX(gDM)
 def gDX(gDM,gDh):
  gDh.setObjectName("Poeiuns")
  gDh.resize(872,657)
  gDM.mShEwK=gDd(gDh)
  gDM.mShEwK.setGeometry(gDQ(20,40,401,91))
  gDM.mShEwK.setObjectName("mShEwK")
  gDM.mShEwK.setColumnCount(0)
  gDM.mShEwK.setRowCount(0)
  gDM.iOOrTEd=gDr(gDh)
  gDM.iOOrTEd.setGeometry(gDQ(350,10,75,23))
  gDM.iOOrTEd.setObjectName("iOOrTEd")
  gDM.label=gDp(gDh)
  gDM.label.setGeometry(gDQ(20,10,161,16))
  gDM.label.setObjectName("label")
  gDM.label_2=gDp(gDh)
  gDM.label_2.setGeometry(gDQ(20,140,161,16))
  gDM.label_2.setObjectName("label_2")
  gDM.apROPE=gDd(gDh)
  gDM.apROPE.setGeometry(gDQ(20,160,401,61))
  gDM.apROPE.setObjectName("apROPE")
  gDM.apROPE.setColumnCount(0)
  gDM.apROPE.setRowCount(0)
  gDM.FQWert=gDd(gDh)
  gDM.FQWert.setGeometry(gDQ(20,250,401,61))
  gDM.FQWert.setObjectName("FQWert")
  gDM.FQWert.setColumnCount(0)
  gDM.FQWert.setRowCount(0)
  gDM.basOPER=gDd(gDh)
  gDM.basOPER.setGeometry(gDQ(20,340,401,61))
  gDM.basOPER.setObjectName("basOPER")
  gDM.basOPER.setColumnCount(0)
  gDM.basOPER.setRowCount(0)
  gDM.oPRTEyt=gDd(gDh)
  gDM.oPRTEyt.setGeometry(gDQ(20,440,401,61))
  gDM.oPRTEyt.setObjectName("oPRTEyt")
  gDM.oPRTEyt.setColumnCount(0)
  gDM.oPRTEyt.setRowCount(0)
  gDM.URKBDH=gDd(gDh)
  gDM.URKBDH.setGeometry(gDQ(20,540,401,101))
  gDM.URKBDH.setObjectName("URKBDH")
  gDM.URKBDH.setColumnCount(0)
  gDM.URKBDH.setRowCount(0)
  gDM.label_3=gDp(gDh)
  gDM.label_3.setGeometry(gDQ(20,230,161,16))
  gDM.label_3.setObjectName("label_3")
  gDM.label_4=gDp(gDh)
  gDM.label_4.setGeometry(gDQ(20,320,161,16))
  gDM.label_4.setObjectName("label_4")
  gDM.label_5=gDp(gDh)
  gDM.label_5.setGeometry(gDQ(20,420,161,16))
  gDM.label_5.setObjectName("label_5")
  gDM.label_6=gDp(gDh)
  gDM.label_6.setGeometry(gDQ(20,520,161,16))
  gDM.label_6.setObjectName("label_6")
  gDM.label_7=gDp(gDh)
  gDM.label_7.setGeometry(gDQ(450,250,161,16))
  gDM.label_7.setObjectName("label_7")
  gDM.label_8=gDp(gDh)
  gDM.label_8.setGeometry(gDQ(450,10,161,16))
  gDM.label_8.setObjectName("label_8")
  gDM.label_9=gDp(gDh)
  gDM.label_9.setGeometry(gDQ(450,520,191,16))
  gDM.label_9.setObjectName("label_9")
  gDM.idihkjsd=gDd(gDh)
  gDM.idihkjsd.setGeometry(gDQ(450,40,401,61))
  gDM.idihkjsd.setObjectName("idihkjsd")
  gDM.idihkjsd.setColumnCount(0)
  gDM.idihkjsd.setRowCount(0)
  gDM.iorDTfj=gDd(gDh)
  gDM.iorDTfj.setGeometry(gDQ(450,540,201,101))
  gDM.iorDTfj.setObjectName("iorDTfj")
  gDM.iorDTfj.setColumnCount(0)
  gDM.iorDTfj.setRowCount(0)
  gDM.label_10=gDp(gDh)
  gDM.label_10.setGeometry(gDQ(450,110,161,16))
  gDM.label_10.setObjectName("label_10")
  gDM.yurSKRT=gDd(gDh)
  gDM.yurSKRT.setGeometry(gDQ(450,400,201,101))
  gDM.yurSKRT.setObjectName("yurSKRT")
  gDM.yurSKRT.setColumnCount(0)
  gDM.yurSKRT.setRowCount(0)
  gDM.UiRToNG=gDd(gDh)
  gDM.UiRToNG.setGeometry(gDQ(450,130,401,111))
  gDM.UiRToNG.setObjectName("UiRToNG")
  gDM.UiRToNG.setColumnCount(0)
  gDM.UiRToNG.setRowCount(0)
  gDM.zzSSxxFR=gDd(gDh)
  gDM.zzSSxxFR.setGeometry(gDQ(450,270,201,91))
  gDM.zzSSxxFR.setObjectName("zzSSxxFR")
  gDM.zzSSxxFR.setColumnCount(0)
  gDM.zzSSxxFR.setRowCount(0)
  gDM.label_12=gDp(gDh)
  gDM.label_12.setGeometry(gDQ(450,380,161,16))
  gDM.label_12.setObjectName("label_12")
  gDM.gDF(gDh)
  gDK.connectSlotsByName(gDh)
 def gDF(gDM,gDh):
  gDz=gDe.translate
  gDh.setWindowTitle(gDz("Poeiuns","SPK Analisa xcdxbbxSAW"))
  gDM.iOOrTEd.setText(gDz("Poeiuns","Perhitungan"))
  gDM.label.setText(gDz("Poeiuns","Hasil Analisa Produk"))
  gDM.label_2.setText(gDz("Poeiuns","Alternatif"))
  gDM.label_3.setText(gDz("Poeiuns","Kriteria"))
  gDM.label_4.setText(gDz("Poeiuns","Kepentingan"))
  gDM.label_5.setText(gDz("Poeiuns","Cost Benefit"))
  gDM.label_6.setText(gDz("Poeiuns","Alternatif Kriteria"))
  gDM.label_7.setText(gDz("Poeiuns","Hasil Belum Dirangking)"))
  gDM.label_8.setText(gDz("Poeiuns","Pembagi"))
  gDM.label_9.setText(gDz("Poeiuns","Rangking Alternatif Produk Terbaik"))
  gDM.label_10.setText(gDz("Poeiuns","Normalisasi"))
  gDM.label_12.setText(gDz("Poeiuns","Hasil Rangking Nilai Terbaik"))
  gDM.iOOrTEd.clicked.connect(gDM.gDY)
  gDM.show()
  gDh.resize(442,150)
  gDM.Poeiuns=gDh
  gDM.gDy()
 def gDI(gDM,data,gDW):
  gDW.setColumnCount(ghD(data[0]))
  gDW.setRowCount(ghD(data)) 
  hh=[]
  i=0
  vh=[]
  for gDS in data[0]:
   hh.append('')
  for gDn in data:
   vh.append('')
   j=0
   for gDS in gDn:
    gDW.setItem(i,j,gDH(ghM(gDS)))
    j=j+1
   i=i+1
  gDW.setHorizontalHeaderLabels(hh)
  gDW.setVerticalHeaderLabels(vh)
 def gDb(gDM,data,gDW):
  gDW.setColumnCount(ghD(data))
  gDW.setRowCount(1)
  hh=[]
  i=0
  vh=['']
  for gDn in data:
   hh.append('')
   gDW.setItem(0,i,gDH(ghM(gDn)))
   i=i+1
  gDW.setHorizontalHeaderLabels(hh)
  gDW.setVerticalHeaderLabels(vh)
 def gDc(gDM,data,gDW):
  gDW.setColumnCount(1)
  gDW.setRowCount(ghD(data)) 
  hh=['']
  i=0
  vh=[]
  for gDn in data:
   vh.append('')
   gDW.setItem(i,0,gDH(ghM(gDn)))
   i=i+1
  gDW.setHorizontalHeaderLabels(hh)
  gDW.setVerticalHeaderLabels(vh)
 def gDy(gDM):
  gDu=[] 
  gDU=[] 
  db=gDT(gDf,gDV,gDP,gDq)
  gDk=db.cursor()
  gDJ="SELECT * FROM alternatif"
  try:
   gDk.execute(gDJ)
   gDv=gDk.fetchall()
   for gDn in gDv:
    gDu.append(gDn[1])
    gDU.append(ghM(gDn[0]))
  except:
   ghz("Error: unable to fetch data")
  db.close()
  gDR=[] 
  gDl=[] 
  gDL=[] 
  gDC=[] 
  db=gDT(gDf,gDV,gDP,gDq)
  gDk=db.cursor()
  gDJ="SELECT * FROM kriteria"
  try:
   gDk.execute(gDJ)
   gDv=gDk.fetchall()
   for gDn in gDv:
    gDR.append(gDn[1])
    gDl.append(gDn[3])
    gDL.append(ghW(gDn[2]))
    gDC.append(ghM(gDn[0]))
  except:
   ghz("Error: unable to fetch data")
  db.close()
  gDA=[] 
  for i in ghS(ghD(gDu)):
   gDA.append([])
   for j in ghS(ghD(gDR)):
    gDA[i].append(0)
    db=gDT(gDf,gDV,gDP,gDq)
    gDk=db.cursor()
    gDJ="SELECT * FROM alternatif_kriteria WHERE `id_alternatif` = '%s' AND `id_kriteria` = '%s'"%(gDU[i],gDC[j])
    try:
     gDk.execute(gDJ)
     gDv=gDk.fetchall()
     for gDn in gDv:
      gDA[i][j]=ghW(gDn[3])
    except:
     ghz("Error: unable to fetch data")
    db.close()
  gDx=[]
  for i in ghS(ghD(gDR)):
   gDx.append(0) 
   for j in ghS(ghD(gDu)):
    if gDl[i]=='cost':
     if j==0:
      gDx[i]=gDA[j][i]
     else:
      if gDx[i]>gDA[j][i]:
       gDx[i]=gDA[j][i]
    else: 
     if j==0:
      gDx[i]=gDA[j][i]
     else:
      if gDx[i]<gDA[j][i]:
       gDx[i]=gDA[j][i]
  gDa=[]
  for i in ghS(ghD(gDu)):
   gDa.append([])
   for j in ghS(ghD(gDR)):
    gDa[i].append(0)
    if gDl[j]=='cost':
     gDa[i][j]=gDx[j]/gDA[i][j]
    else:
     gDa[i][j]=gDA[i][j]/gDx[j]
  gDj=[]
  for i in ghS(ghD(gDu)):
   gDj.append(0)
   for j in ghS(ghD(gDR)):
    gDj[i]=gDj[i]+(gDa[i][j]*gDL[j])
  gDs=[]
  gDi=[]
  for i in ghS(ghD(gDu)):
   gDi.append(gDj[i])
   gDs.append(gDu[i])
  for i in ghS(ghD(gDu)):
   for j in ghS(ghD(gDu)):
    if j>i:
     if gDi[j]>gDi[i]:
      gDO=gDi[i]
      gDE=gDs[i]
      gDi[i]=gDi[j]
      gDs[i]=gDs[j]
      gDi[j]=gDO
      gDs[j]=gDE
  gDM.gDb(gDu,gDM.apROPE)
  gDM.gDb(gDR,gDM.FQWert)
  gDM.gDb(gDl,gDM.oPRTEyt)
  gDM.gDb(gDL,gDM.basOPER)
  gDM.gDI(gDA,gDM.URKBDH)
  gDM.gDb(gDx,gDM.idihkjsd)
  gDM.gDI(gDa,gDM.UiRToNG)
  gDM.gDc(gDj,gDM.zzSSxxFR)
  gDM.gDc(gDi,gDM.yurSKRT)
  gDM.gDc(gDs,gDM.iorDTfj)
  gDM.mShEwK.setColumnCount(3)
  gDM.mShEwK.setRowCount(ghD(gDs)) 
  hh=['Ranking','Alternatif','Nilai']
  i=0
  vh=[]
  for gDn in gDs:
   vh.append('')
   gDM.mShEwK.setItem(i,0,gDH(ghM(i+1)))
   gDM.mShEwK.setItem(i,1,gDH(ghM(gDs[i])))
   gDM.mShEwK.setItem(i,2,gDH(ghM(gDi[i])))
   i=i+1
  gDM.mShEwK.setHorizontalHeaderLabels(hh)
  gDM.mShEwK.setVerticalHeaderLabels(vh)
 def gDY(gDM):
  gDM.Poeiuns.resize(872,657)
