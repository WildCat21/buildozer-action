from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
from urllib.request import *
from datetime import date
import sys, os, time, random, json
from deta import Deta    
        
class main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ava = AvA(self)
        self.shop = market(self)
        self.inlog = login(self)
        self.mmen = menu(self)
        self.inlog.gogo()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.inlog)
        self.stack.addWidget(registrer(self))
        self.stack.addWidget(self.ava)
        self.stack.addWidget(self.mmen)
        self.stack.addWidget(self.shop)
        self.stack.addWidget(message(self))
        self.stack.addWidget(casino(self))
        
        layout = QGridLayout()
        layout.addWidget(self.stack, 0, 0)
        
        self.setLayout(layout)
        self.show()
        
    def logout(self):
        self.mmen.stopmsg()
        try:
            os.remove("user.cvd")
            msgBox = QMessageBox()
            msgBox.setText("Du wurdest erfolgreich ausgeloggt.")
            msgBox.exec_()
            self.login()
        except:
            msgBox = QMessageBox()
            msgBox.setText("44: Fehler")
            msgBox.setInformativeText("Ein Fehler ist aufgetreten. Eventuell bist du nicht angemeldet. Falls dieser Fehler weiterhin besteht, sende uns den Felercode per Mail an cows.vs.ducks@gmail.com.")
            msgBox.exec_()

    def belohnung(self):
        try:
            datei = open("belohnung.cvd", "r")
            gd = datei.read()
            datei.close()
        except:
            gd = date.today()
        if str(gd) != str(date.today()) or not os.path.isfile("belohnung.cvd"):
            belo = random.randint(10, 100)
            datei = open("user.cvd", "r")
            uss = datei.read()
            datei.close()
            deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
            users = deta.Base("user")
            user = users.get(uss) # the user
            mon = user["moneten"]
            moni = int(mon)
            moni += belo
            users.update({"moneten": moni}, uss)
            try:
                os.remove("belohnung.cvd")
            except:
                pass
            datei = open("belohnung.cvd", "a")
            datei.write(str(date.today()))
            datei.close()
            msgBox = QMessageBox()
            msgBox.setText("Du hast deine Tägliche Belohnung von " + str(belo) + " Moneten erhalten.")
            msgBox.exec_()
        else:
            msgbox = QMessageBox()
            msgbox.setText("Du hast dir heute schon deine Belohnung abgeholt. Versuche es morgen nochmal.")
            msgbox.exec()
        
    def login(self):
        self.mmen.stopmsg()
        self.showNormal()
        self.setGeometry(20, 20, 120, 95)
        self.stack.setCurrentIndex(0)
        self.ava.botstop()
        self.inlog.gogo()
    
    def registrer(self):
        self.showNormal()
        self.setGeometry(20, 20, 120, 95)
        self.stack.setCurrentIndex(1)
        self.ava.botstop()
        
    def game(self):
        self.showFullScreen()
        self.mmen.stopmsg()
        self.ava.go()
        self.stack.setCurrentIndex(2)
        
    def menug(self):
        self.showNormal()
        self.setGeometry(20, 20, 120, 95)
        self.shop.stopstore()
        self.mmen.gomsg()
        self.stack.setCurrentIndex(3)
        self.ava.botstop()
        self.inlog.sstop()
        
    def store(self):
        self.showNormal()
        self.setGeometry(20, 20, 120, 95)
        self.shop.gostore()
        self.stack.setCurrentIndex(4)
        self.ava.botstop()
        
    def mesge(self):
        self.showNormal()
        self.setGeometry(20, 20, 120, 95)
        self.stack.setCurrentIndex(5)
        
    def cassino(self):
        self.showNormal()
        self.setGeometry(20, 20, 120, 95)
        self.stack.setCurrentIndex(6)
        
class menu(QWidget):
    def __init__(self, main, parent=None):
        super().__init__(parent)
        ly = QVBoxLayout()
        ly.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(
            """
            QPushButton {
                border: 4px solid;
                border-radius: 10px;
                border-color: #ffa126;
                min-height: 50px;
                max-width: 350px;
            }
            QPushButton:hover {
                border: 4px solid;
                border-color: #ffa126;
                background-color: #cf7500;
                border-style: inset;
            }
            QPushButton:pressed {
                border: 4px solid;
                border-color: #ffa126;
                background-color: #ffa126;
                border-style: inset;
            }
            """
        )

        #colors = ["rgb(40, 166, 212)", "rgb(18, 250, 95)", "rgb(61, 217, 245)", "rgb(240, 53, 218)"]
      
        logout = QPushButton("Logout")
        logout.clicked.connect(main.logout)
        ly.addWidget(logout)
        
        avag = QPushButton("Alpha vs. Alpha")
        avag.clicked.connect(main.game)
        #avag.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        ly.addWidget(avag)
        
        acc = QPushButton("Einstellungen (bald)")
        #acc.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        ly.addWidget(acc)

        msg = QPushButton("</> Nachrichten")
        msg.clicked.connect(main.mesge)
        #msg.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        ly.addWidget(msg)
        
        bel = QPushButton("tägliche Belohnung abholen")
        bel.clicked.connect(main.belohnung)
        #bel.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        ly.addWidget(bel)
        
        cas = QPushButton("Casino")
        cas.clicked.connect(main.cassino)
        #cas.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        #ly.addWidget(cas)
        
        store = QPushButton("Market")
        store.clicked.connect(main.store)
        #store.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        ly.addWidget(store)

        self.new = QLabel()
        ly.addWidget(self.new)
        
        self.setLayout(ly)
        
    def gomsg(self):
        self.chec = QTimer()
        self.chec.timeout.connect(self.checkmsg)
        self.chec.start(5000)

    def stopmsg(self):
        self.chec.stop()
        
    def checkmsg(self):
        datei = open("user.cvd", "r")
        uss = datei.read()
        datei.close()
        deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
        users = deta.Base("user")
        user = users.get(uss) # the user
        mes = user["msg"]
        try:
            datei = open("lastmsg.cvd", "r")
            lastmsg = datei.read()
            datei.close()
        except:
            lastmsg = ""
        if mes != "" and mes != lastmsg:
            self.new.setText("Du hast eine neue </> Nachricht.")
            msgbox = QMessageBox()
            msgbox.setText("Du hast eine neue </> Nachricht. Drücke im Menü  auf </> Nachrichten, um sie anzuzeigen.")
            msgbox.exec()
            try:
                os.remove("lastmsg.cvd")
            except:
                pass
            datei = open("lastmsg.cvd", "a")
            lastmsg = datei.write(mes)
            datei.close()
        else:
            self.new.setText("")
        
class casino(QWidget):
    def __init__(self, main, parent=None):
        super().__init__(parent)
        ly = QVBoxLayout()
        
        ba = QPushButton("Zurück")
        ba.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        ba.clicked.connect(main.menug)
        ly.addWidget(ba)
        
        lb = QLabel("Das ist das Casino. Du kannst hier einen Betrag eingeben, den du einsetzen willst.\nDas wird eine zufällige Zahl zwischen 0 und 10 generiert. Wenn es eine 10 ist,\nbekommst du das Doppelte zurück, und wenn es eine 0 ist, bekommst du nichts zurück.\nZwischen drinnen bekommst du immer mehr.")
        ly.addWidget(lb)
        
        self.betr = QSpinBox()
        self.betr.setMaximum(1000000)
        ly.addWidget(self.betr)
        
        bt = QPushButton("los!!!")
        bt.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        bt.clicked.connect(self.go)
        ly.addWidget(bt)
        
        self.setLayout(ly)
        
    def go(self):
        num = int(self.betr.value())
        zuf = random.randint(0, 10)
        datei = open("user.cvd", "r")
        uss = datei.read()
        datei.close()
        deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
        users = deta.Base("user")
        user = users.get(uss) # the user
        mon = user["moneten"]
        moni = int(mon)
        moni -= num
        if moni >= 0:
            users.update({"moneten": moni}, uss)
            num = num / 10 * 2 * zuf
            msgbox = QMessageBox()
            msgbox.setText("Du hast " + str(num) + " Moneten bekommen.")
            msgbox.exec()
            deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
            users = deta.Base("user")
            user = users.get(uss) # the user
            mon = user["moneten"]
            moni = int(mon)
            moni += num
            users.update({"moneten": moni}, uss)
        else:
            msgbox = QMessageBox()
            msgbox.setText("Du hast leider nicht genug Moneten.")
            msgbox.exec()
        
class message(QWidget):
    def __init__(self, main, parent=None):
        super().__init__(parent)
        ly = QVBoxLayout()
        
        ba = QPushButton("Zurück")
        ba.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        ba.clicked.connect(main.menug)
        ly.addWidget(ba)
        lb = QLabel("Hier kannst du Nachrichten von uns bekommen.")
        ly.addWidget(lb)
        pltz = QLabel()
        ly.addWidget(pltz)
        
        self.msgs = QLabel()
        ly.addWidget(self.msgs)
        
        relo = QPushButton("neu laden")
        relo.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        relo.clicked.connect(self.reload)
        ly.addWidget(relo)

        self.setLayout(ly)
        
    def reload(self):
        datei = open("user.cvd", "r")
        uss = datei.read()
        datei.close()
        deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
        users = deta.Base("user")
        user = users.get(uss) # the user
        mes = user["msg"]
        self.msgs.setText(mes)
        try:
            os.remove("lastmsg")
        except:
            pass
        datei = open("lastmsg.cvd", "a")
        datei.write(mes)
        datei.close()
        
class market(QWidget):
    def __init__(self, main, parent=None):
        super().__init__(parent)
               
        ly = QVBoxLayout()
        
        mon = 0
        self.monn = QLabel(str(mon) + " m")
        ly.addWidget(self.monn)
        
        self.timeeeer = QTimer()
        self.timeeeer.timeout.connect(self.getmon)
        self.timeeeer.start(2000)

        back = QPushButton("Zurück")
        back.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        back.clicked.connect(main.menug)
        ly.addWidget(back)
        
        waff1 = QLabel("Waffen")
        ly.addWidget(waff1)
        
        self.waff = QListWidget()
        ly.addWidget(self.waff)
        
        tr1 = QLabel("Tränke")
        ly.addWidget(tr1)
        
        self.tr = QListWidget()
        ly.addWidget(self.tr)
        
        cha1 = QLabel("Charaktere")
        ly.addWidget(cha1)
        
        self.cha = QListWidget()
        ly.addWidget(self.cha)
        
        wtz = QLabel("Witze")
        ly.addWidget(wtz)
        
        self.wtz1 = QListWidget()
        ly.addWidget(self.wtz1)
        
        self.tr.itemClicked.connect(self.trank)
        self.wtz1.itemClicked.connect(self.witz)
        
        self.tr.addItem("Herztrank(4 Herzen)" + "   preis: 200 m")
        
        a = urlopen("https://raw.githubusercontent.com/Cows-vs-Ducks/game/main/ww.json").read().decode()
        self.witze = json.loads(a)
        i = 0
        for witz1 in self.witze:
            i += 1
            self.wtz1.addItem(str(i) + "   preis: 10 m")
        
        self.setLayout(ly)

    def gostore(self):
        self.timeeeer = QTimer()
        self.timeeeer.timeout.connect(self.getmon)
        self.timeeeer.start(2000)

    def stopstore(self):
        self.timeeeer.stop()
        
    def trank(self, item):
        tr = item.text().replace("   preis: 200 m", "")
        if tr == "Herztrank(4 Herzen)":
            datei = open("user.cvd", "r")
            uss = datei.read()
            datei.close()
            deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
            users = deta.Base("user")
            user = users.get(uss) # the user
            mon = user["moneten"]
            moni = int(mon)
            moni -= 200
            if moni >= 0:
                tr = user["tränke"]
                tri = str(tr) + "1"
                users.update({"tränke": tri}, uss)
                users.update({"moneten": moni}, uss)
                msgbox = QMessageBox()
                msgbox.setText("Du hast dir einen Herztrank gekauft! Jetzt hast du im nächsten Spiel 4 Herzen.")
                msgbox.exec()
            else:
                msgbox = QMessageBox()
                msgbox.setText("Du hast leider nicht genug Moneten.")
                msgbox.exec()
        else:
            msgbox = QMessageBox()
            msgbox.setText("Ein Fehler ist aufgetreten. Bitte probiere es nochmal. Falls dieser Fehler weiterhin auftritt, sende uns eine Mail an cows.vs.ducks@gmail.com.")
            msgbox.exec()
        

    def getmon(self):
        try:
            datei = open("user.cvd", "r")
            uss = datei.read()
            datei.close()
            deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
            users = deta.Base("user")
            user = users.get(uss) # the user
            mon = user["moneten"]
            self.monn.setText(str(mon) + " m")
        except:
            pass
        
    def witz(self, item):
        wt = item.text().replace("   preis: 10 m", "")
        #print(self.witze[wt])
        datei = open("user.cvd", "r")
        uss = datei.read()
        datei.close()
        deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
        users = deta.Base("user")
        user = users.get(uss) # the user
        mon = user["moneten"]
        moni = int(mon)
        moni -= 10
        if moni >= 0:
            users.update({"moneten": moni}, uss)
            msgbox = QMessageBox()
            msgbox.setText(self.witze[wt])
            msgbox.setWindowTitle("Dein Witz")
            msgbox.exec()
        else:
            msgbox = QMessageBox()
            msgbox.setText("Du hast leider nicht genug Moneten.")
            msgbox.exec()
        
class login(QWidget):
    def __init__(self, main, parent=None):
        super().__init__(parent)
        
        llly = QGridLayout()
        self.main = main
        
        
        us = QLabel("Benutzername *")
        self.us1 = QLineEdit()
        ps = QLabel("Passwort *")
        self.ps1 = QLineEdit()
        fe = QPushButton("login")
        pfff = QLabel("* Pflichtfelder")
        rg = QPushButton("Noch kein Konto?")
        pltz = QLabel()
        
        rg.setStyleSheet("border: None; color: blue;")
        fe.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')
        
        rg.clicked.connect(main.registrer)
        fe.clicked.connect(self.logii)
        
        llly.addWidget(us, 0, 1)
        llly.addWidget(self.us1, 1, 1)
        llly.addWidget(ps, 2, 1)
        llly.addWidget(self.ps1, 3, 1)
        llly.addWidget(pltz, 4, 1)
        llly.addWidget(fe, 5, 0)
        llly.addWidget(pfff, 5, 1)
        llly.addWidget(rg, 5, 2)
        
        self.setLayout(llly)

    def gogo(self):
        self.chekc = QTimer()
        self.chekc.timeout.connect(self.check)
        self.chekc.start(1000)

    def sstop(self):
        self.chekc.stop()

    def check(self):
        if os.path.isfile("user.cvd"):
            main.menug(self.main)
        else:
            pass
        
    def logii(self):
        passwwd = self.ps1.text()
        ussee = self.us1.text()
        deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
        users = deta.Base("user")
        user = users.get(ussee)
        try:
            password = user["passwort"]
            ban = user["bann"]
            if password == passwwd and not ban == "1":
                try:
                    os.remove("user.cvd")
                except:
                    pass
                datei = open("user.cvd", "a")
                datei.write(ussee)
                datei.close()
                msgBox = QMessageBox()
                msgBox.setText("Willkommen zurück, " + ussee)
                msgBox.setInformativeText("Du wurdest erfolgreich angemeldet.")
                msgBox.exec_()
                main.menug(self.main)
                
            else:
                msgBox = QMessageBox()
                msgBox.setText("41: Du konntest nicht angemeldet werden.")
                msgBox.setInformativeText("Dein Passwort ist falsch oder dein Konto wurde deaktiviert. Wenn das Problem weiterhin besteht oder wenn du dein Passwort vergessen hasst, sende uns den Fehlercode per Mail an cows.vs.ducks@gmail.com. Wir senden dir dann dein Passwort an die E-Mail-Adressse, die du bei der Registrierung angegeben hast.")
                msgBox.exec_()
        except:
            msgBox = QMessageBox()
            msgBox.setText("42: Du konntest nicht angemeldet werden.")
            msgBox.setInformativeText("Der Benutzername wurde nicht in unserer Datenbank gefunden. Falls dieser Fehler weiterhin besteht, sende uns den Fehlercode und deinen Benutzernamen per Mail an cows.vs.ducks@gmail.com.")
            msgBox.exec_()

class registrer(QWidget): 
    def __init__(self, main, parent=None): 
        super().__init__(parent)
        
        ly = QGridLayout()
        self.main = main
        
        lvn = QLabel("Vorname")
        self.vn = QLineEdit()
        lnn = QLabel("Nachname")
        self.nn = QLineEdit()
        lag = QLabel("Alter")
        self.ag = QLineEdit()
        lgb = QLabel("Geburtsdatum (tt.mm.jjjj)")
        self.gb = QLineEdit()
        
        lus = QLabel("Benutzername *")
        self.us = QLineEdit()
        lem = QLabel("E-Mail-Adresse *")
        self.em = QLineEdit()
        lps = QLabel("Passwort *")
        self.ps = QLineEdit()
        lpss = QLabel("Passwort wiederholen *")
        self.pss = QLineEdit()
        
        fertig = QPushButton("registrieren")
        pf = QLabel("* Pflichtfelder")
        log = QPushButton("Du hast schon ein Konto?")
        
        log.setStyleSheet("border: None; color: blue;")
        fertig.setStyleSheet('font: 75 10pt "Microsoft YaHei UI"; font-weight: bold; color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:9px; }')

        fertig.clicked.connect(self.regg)
        log.clicked.connect(main.login)

        plttzz = QLabel()
        
        ly.addWidget(fertig, 8, 0)
        ly.addWidget(pf, 8, 1)
        ly.addWidget(log, 8, 2)
        
        ly.addWidget(lvn, 0, 0)
        ly.addWidget(self.vn, 1, 0)
        ly.addWidget(lnn, 2, 0)
        ly.addWidget(self.nn, 3, 0)
        ly.addWidget(lag, 4, 0)
        ly.addWidget(self.ag, 5, 0)
        ly.addWidget(lgb, 6, 0)
        ly.addWidget(self.gb, 7, 0)
        
        ly.addWidget(lus, 0, 3)
        ly.addWidget(self.us, 1, 3)
        ly.addWidget(lem, 2, 3)
        ly.addWidget(self.em, 3, 3)
        ly.addWidget(lps, 4, 3)
        ly.addWidget(self.ps, 5, 3)
        ly.addWidget(lpss, 6, 3)
        ly.addWidget(self.pss, 7, 3)
        
        self.setLayout(ly)
        

    def regg(self):
        vn = self.vn.text()
        nn = self.nn.text()
        ag = self.ag.text()
        gb = self.gb.text()
        us = self.us.text()
        em = self.em.text()
        ps = self.ps.text()
        pss = self.pss.text()

        if em != "" and em != "" and ps != "" and pss == ps:
            try:
                deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
                users = deta.Base("user")
                users.insert({"key": us,
                              "vorname": vn,
                              "nachname": nn,
                              "alter": ag,
                              "geburtsdatum": gb,
                              "benutzername": us,
                              "email": em,
                              "passwort": ps,
                              "moneten": "0",
                              "level": "1",
                              "waffen": "1",
                              "tränke": "",
                              "status": "gamer",
                              "msg": "",
                              "bann": "0",
                })
                """
                allusers = deta.Base("alluser")
                allusers.insert({"key": us,
                              "level": "1",
                               "moneten": "0"
                })
                """
            except:
                msgBox = QMessageBox()
                msgBox.setText("40: Du konntest nicht registriert werden.")
                msgBox.setInformativeText("Stelle sicher, dass du mit dem Internet verbunden bist. Wenn ja, ist der Benutzername schon vergeben. Wenn das Problem weiterhin besteht, sende uns den Fehlercode und den Benutzernamen, den du haben willst per Mail an cows.vs.ducks@gmail.com.")
                msgBox.exec_()
        
            msgBoxr = QMessageBox()
            msgBoxr.setText("Du wurdest erfolgreich registriert.")
            msgBoxr.exec_()
            
            main.login(self.main)
            
        else:
            msgBox = QMessageBox()
            msgBox.setText("43: Du konntest nicht registriert werden.")
            msgBox.setInformativeText("Vielleicht hast du das Passwort nicht korrekt wiederholt oder du hast nicht alle Pflichtfelder ausgefüllt. Wenn alles stimmt, und dieser Fehler weiterhin auftritt, sende uns den Fehlercode per Mail an cows.vs.ducks@gmail.com.")
            msgBox.exec_()
        

class Hearth(QWidget):
    def __init__(self, main, parent=None):
        super().__init__(parent)

        self.ly = QGridLayout()
        self.main = main

        self.bothearth1 = QSvgWidget("heart.svg", self)
        self.bothearth1.setFixedSize(10, 10)
        self.ly.addWidget(self.bothearth1, 0, 7)

        self.bothearth2 = QSvgWidget("heart.svg", self)
        self.bothearth2.setFixedSize(10, 10)
        self.ly.addWidget(self.bothearth2, 0, 8)

        self.bothearth3 = QSvgWidget("heart.svg", self)
        self.bothearth3.setFixedSize(10, 10)
        self.ly.addWidget(self.bothearth3, 0, 9)

        platzhalter = QLabel()
        self.ly.addWidget(platzhalter, 0, 5)

        self.userhearth1 = QSvgWidget("heart.svg", self)
        self.userhearth1.setFixedSize(10, 10)
        self.ly.addWidget(self.userhearth1, 0, 1)

        self.userhearth2 = QSvgWidget("heart.svg", self)
        self.userhearth2.setFixedSize(10, 10)
        self.ly.addWidget(self.userhearth2, 0, 2)
        
        self.userhearth3 = QSvgWidget("heart.svg", self)
        self.userhearth3.setFixedSize(10, 10)
        self.ly.addWidget(self.userhearth3, 0, 3)
        
    def gogogo(self):
        datei = open("user.cvd", "r")
        uss = datei.read()
        datei.close()
        deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
        users = deta.Base("user")
        user = users.get(uss) # the user
        tr = user["tränke"]
        trs = list(str(tr))
        if "1" in trs:
            trs.remove("1")
            upd = "".join(trs)
            users.update({"tränke": str(upd)}, uss)
            self.herzen = 4
            self.userhearth4 = QSvgWidget("heart.svg", self)
            self.userhearth4.setFixedSize(50, 50)
            self.ly.addWidget(self.userhearth4, 0, 4)
        else:
            self.herzen = 3

        self.herruser = 3
        self.herrbot = self.herzen

        self.setLayout(self.ly)
        self.show()
        
    def reseth(self):
        self.herrbot = 3
        self.herruser = self.herzen

    def lesshearthbot(self):
        if self.herruser == 3:
            self.bothearth3.move(1000000, 1000000)
            self.herruser = 2
        elif self.herruser == 2:
            self.bothearth2.move(1000000, 1000000)
            self.herruser = 1
        elif self.herruser == 1:
            self.bothearth1.move(1000000, 1000000)
            moe = random.randint(1, 3)
            msgbox = QMessageBox()
            if moe == 1:
                msgbox.setText("Du hast Gewonnen!!! Dafür bekommst du 100 Moneten.")
            elif moe == 2:
                msgbox.setText("Herzlichen Glückwunsch, du hast gewonnen und bekommst 100 Moneten")
            elif moe == 3:
                msgbox.setText("Du hast gewonnen. Als Belohnung bekommst du 100 Moneten.")
            else:
                msgbox.setText("Ein Fehler ist aufgetreten. Aber du hast Gewonnen!")
            msgbox.setWindowTitle("Gewonnen")
            msgbox.exec()
            datei = open("user.cvd", "r")
            uss = datei.read()
            datei.close()
            deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
            users = deta.Base("user")
            user = users.get(uss) # the user
            mon = user["moneten"]
            moni = int(mon)
            moni += 100
            users.update({"moneten": moni}, uss)
            main.menug(self.main)


    def lesshearthuser(self):
        if self.herrbot == 4:
            self.userhearth4.move(1000000, 1000000)
            self.herrbot = 3
        elif self.herrbot == 3:
            self.userhearth3.move(1000000, 1000000)
            self.herrbot = 2
        elif self.herrbot == 2:
            self.userhearth2.move(1000000, 1000000)
            self.herrbot = 1
        elif self.herrbot == 1:
            self.userhearth1.move(1000000, 1000000)
            msgbox = QMessageBox()
            msgbox.setText("Du hast leider verloren. Probiere es doch einfach nochmal!")
            msgbox.setWindowTitle("Verloren")
            msgbox.exec()
            main.menug(self.main)

class AvA(QWidget):
    def __init__(self, main, parent=None):
        super().__init__(parent)

        self.main = main
        ly = QHBoxLayout()
        self.hearthh = Hearth(self.main)
        self.pltz = QLabel()
        ly.addWidget(self.hearthh)
        ly.addWidget(self.pltz)
        #ly.addWidget(self.pltz)

        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.white))
        self.setPalette(palette)

        fileh1 = open("height.cvd", "r")
        self.height = fileh1.read()
        fileh1.close()
        filew1 = open("width.cvd", "r")
        self.width = filew1.read()
        filew1.close()

        self.actutime = 4
        #self.herr = 3
        
        self.ball = QWidget(self)
        self.ball.setStyleSheet("background-color:black;border-radius:12px")
        self.ball.resize(25, 25)
        self.ball.move(1000000, 1000000)

        self.botball = QWidget(self)
        self.botball.setStyleSheet("background-color:black;border-radius:12px")
        self.botball.resize(25, 25)
        self.botball.move(1000000, 1000000)
        
        self.botzu = random.randint(0, 10)
        self.boti = 0
        
        self.stepw = int(self.width) / 20
        self.steph = int(self.height) / 15
        
        self.keyUp = "16777235"
        self.keyDown = "16777237"
        self.keyLeft = "16777234"
        self.keyRight = "16777236"
        
        self.cowx = 0
        self.cowy = int(self.height) / 2
        self.duckx = int(self.width) - 200
        self.ducky = int(self.height) / 2

        self.waffe = "1"
        
        self.pic = QSvgWidget("cow.svg", self) # Cow
        self.pic.setFixedSize(175 / 2, 100)
        self.pic.move(self.cowx, self.cowy)
        
        self.pic2 = QSvgWidget("cow.svg", self) # Duck
        self.pic2.setFixedSize(175 / 2, 100)
        self.pic.move(self.duckx, self.ducky)
        
        self.timeeer = QTimer()
        self.timeeer.timeout.connect(self.moveduckback)
        self.timeeer.start(7000)
        
        self.setLayout(ly)
        self.showFullScreen()
        #self.setGeometry(0, 0, int(self.width), int(self.height))
        
    def go(self):
        self.botshoot = QTimer()
        self.botshoot.timeout.connect(self.shootbot)
        self.botshoot.start(4000)
        self.hearthh.gogogo()
        
    def botstop(self):
        try:
            self.hearthh.reseth()
            self.botshoot.stop()
        except:
            pass

    def moveduckback(self):
        self.duckx = int(self.width) - 200
        self.ducky = int(self.height) / 2
        self.pic2.move(self.duckx, self.ducky)

    def closeEvent(self, event):
        msgbox = QMessageBox()
        msgbox.setText("Bist du sicher, dass du das Spiel abbrechen willst?")
        msgbox.setWindowTitle("Abbrechen?")
        msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        rv = msgbox.exec()
        if rv == QMessageBox.Cancel:
            event.ignore()
        else:
            event.accept()
        
    def keyPressEvent(self, event):
        if str(event.key()) == self.keyRight:
            self.right()
        elif str(event.key()) == self.keyDown:
            self.down()
        elif str(event.key()) == self.keyLeft:
            self.left()
        elif str(event.key()) == self.keyUp:
            self.up()
        else:
            pass
        
        event.accept()

    def mousePressEvent(self, event):
        self.shootx = event.x()
        self.shooty = event.y()
        #self.timer = QTimer()
        #self.timer.timeout.connect(self.botaus)
        #self.timer.setSingleShot(True)
        #self.timer.start(1000)
        self.shootuser()
        self.botaus()
        event.accept()
        
    def botaus(self):
        if self.boti >= self.botzu:
            self.botzu = random.randint(0, 10)
            self.boti = 0
        else:
            if self.shootx <= self.duckx + 175 / 2 and self.shooty <= self.ducky + 100 and self.shootx >= self.duckx and self.shooty >= self.ducky:
                for x in range(0, 4):
                    self.botup()
            
                self.timer = QTimer()
                self.timer.timeout.connect(self.botback)
                self.timer.setSingleShot(True)
                self.timer.start(2000)
                self.boti += 1
            
            else:
                pass
    
    def botback(self):
        for x in range(0, 4):
            self.botdown()

    def botdown(self):
        self.ducky += self.steph
        self.duckx = self.duckx
        self.pic2.move(self.duckx, self.ducky)
        
    def botup(self):
        self.ducky -= self.steph
        self.duckx = self.duckx
        self.pic2.move(self.duckx, self.ducky)
        
    def checkuser(self):
        if self.shootx <= self.duckx + 175 / 2 and self.shooty <= self.ducky + 100 and self.shootx >= self.duckx and self.shooty >= self.ducky:
            print("getroffen")
            #self.ball.move(1000000, 1000000)
            self.hearthh.lesshearthbot()
            return True
        else:
            #self.ball.move(1000000, 1000000)
            return False

    def checkbot(self):
        if self.shootx <= self.cowx + 175 / 2 and self.shooty <= self.cowy + 100 and self.shootx >= self.cowx and self.shooty >= self.cowy:
            print("getroffen")
            self.ball.move(1000000, 1000000)
            self.hearthh.lesshearthuser()
        else:
            self.ball.move(1000000, 1000000)

    def shootuser(self):
        user = "user"
        treffer = False
        i = 0
        self.shootsx = 4
        self.shootsy = self.shooty / self.shootx * 4
        self.shootffx = self.cowx
        self.shootffy = self.cowy
        if user == "user":
            if self.actutime - time.time() >= 3 or self.actutime == 4:
                if self.waffe == "1":
                    while not i >= 100 and not treffer:
                        self.shootffx += self.shootsx
                        self.shootffy += self.shootsy
                        self.shootanim1 = QPropertyAnimation(self.ball, b"pos")
                        self.shootanim1.setDuration(50)
                        self.shootanim1.setStartValue(QPoint(self.shootffx - self.shootsx, self.shootffy - self.shootsy))
                        self.shootanim1.setEndValue(QPointF(self.shootffx, self.shootffy))
                        self.shootanim1.start()
                        treffer = self.checkuser()
                        i += 1
            else:
                pass

    def shootbot(self):
        self.shootx = self.cowx + 25
        self.shooty = self.cowy + 25
        self.shootanim2 = QPropertyAnimation(self.botball, b"pos")
        self.shootanim2.setDuration(1000)
        self.shootanim2.setStartValue(QPoint(self.duckx, self.ducky))
        self.shootanim2.setEndValue(QPointF(self.shootx, self.shooty))
        self.shootanim2.start()
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkbot)
        self.timer.setSingleShot(True)
        self.timer.start(1000)
        
    def right(self):
        self.cowxt = self.cowx + self.stepw
        self.cowy = self.cowy
        if self.cowxt <= int(self.width) - 100:
            self.cowx = self.cowxt
            self.pic.move(self.cowx, self.cowy)
    
    def down(self):
        self.cowyt = self.cowy + self.steph
        self.cowx = self.cowx
        if self.cowyt <= int(self.height) - 200:
            self.cowy = self.cowyt
            self.pic.move(self.cowx, self.cowy)
    
    def left(self):
        self.cowxt = self.cowx - self.stepw
        self.cowy = self.cowy
        if self.cowxt >= 0:
            self.cowx = self.cowxt
            self.pic.move(self.cowx, self.cowy)
    
    def up(self):
        self.cowyt = self.cowy - self.steph
        self.cowx = self.cowx
        if self.cowyt >= 0:
            self.cowy = self.cowyt
            self.pic.move(self.cowx, self.cowy)

app = QApplication([])

app.setStyle("Fusion")

palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)
try:
    os.remove("width.cvd")
    os.remove("height.cvd")
except:
    pass
filew = open("width.cvd", "a")
filew.write(str(app.desktop().width()))
filew.close()
fileh = open("height.cvd", "a")
fileh.write(str(app.desktop().height()))
fileh.close()
mainw = main()
mainw.setWindowTitle("Cows vs. Ducks")
mainw.setWindowIcon(QIcon("cvd-icon.png"))
mainw.show()
sys.exit(app.exec_())
