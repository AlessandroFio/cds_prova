import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTabWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QCheckBox,
    QScrollArea
    )

from PyQt6.QtCore import Qt
import art_cds_new

class PostoDiBlocco(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(1000, 800)
        self.setWindowTitle("Posto di Blocco")
        
        self.setUpPostoDiBlocco()
        self.show() # Inizializza l'interfaccia utente

    def setUpPostoDiBlocco(self):
        # pagina sx
        self.tab_bar=QTabWidget()
        #persona
        self.persona_tab = QWidget()
        self.persona_tab.setObjectName("Tab")
        #veicolo
        self.veicolo_scroll = QScrollArea()
        self.veicolo_scroll.setWidgetResizable(True)
        
        self.veicolo_tab =QWidget()
        self.veicolo_tab.setObjectName("Tab")
        self.veicolo_scroll.setWidget(self.veicolo_tab)
        #velocità
        self.velocità_tab = QWidget()
        self.velocità_tab .setObjectName("Tab")


        self.tab_bar.addTab(self.persona_tab, "Persona")
        #self.tab_bar.addTab(self.veicolo_tab, "Veicolo")
        self.tab_bar.addTab(self.veicolo_scroll,"Veicolo")
        self.tab_bar.addTab(self.velocità_tab, "Velocità")

        self.personaTab()
        self.veicoloTab()
        self.velocitàTab()

        # Pagina dx
        self.side_widget = QWidget()
        self.side_widget.setObjectName("intestazione1")
        self.side_widget.setMinimumWidth(200)
        self.sanzioneWidget()

        # Definisci il layout principale
        
        main_h_box=QHBoxLayout()
        main_h_box.addWidget(self.tab_bar)
        main_h_box.addWidget(self.side_widget)
        self.setLayout(main_h_box)

        # Imposta lo stile del widget
        self.setStyleSheet("""
    QWidget#Tab{
    }
    QWidget#intestazione1{
        font-size:20px;
        font-weight: bold;
    }

    QLabel#intestazione2{
        font-size: 15px;
        font-weight: bold;
        color: #333;
    }
    QLabel#intestazione3{
        font-size: 13px;
        font-weight: normal;
        color: #333;
    }
    QLabel#spiegazione{
        font-size: 10px;
        color: #777;
    }
    QLabel#subtitle{
            font-size:15px;
            font-weight: normal
    }
""")            

    def personaTab(self):
        tab_documenti_persona_layout =QLabel("Documenti della Persona")
        tab_documenti_persona_layout.setObjectName("intestazione2")
        
        # GUIDA REQUISITI D'ETA' art 115
        self.patente_requisiti_checkboxes=[]
        
        patente_requisiti = QVBoxLayout()

        patente_art115 = QLabel('Requisiti per la guida dei veicoli')
        patente_art115.setObjectName("subtitle")

        art115_04 = QCheckBox("Guida ciclomotore senza avere l'età prevista")
        art115_04.setProperty("Ipotesi", "115-4")
        self.patente_requisiti_checkboxes.append(art115_04)
        art115_05 = QCheckBox("Guida di veicoli senza aver compiuto i previsti 16 anni")
        art115_05.setProperty("Ipotesi", "115-5")
        self.patente_requisiti_checkboxes.append(art115_05)
        art115_06 = QCheckBox("Guida di veicoli senza aver compiuto i previsti 18 anni")
        art115_06.setProperty("Ipotesi", "115-6")
        self.patente_requisiti_checkboxes.append(art115_06)
        art115_07 = QCheckBox("Guida di veicoli senza aver compiuto i previsti 21 anni")
        art115_07.setProperty("Ipotesi", "115-7")
        self.patente_requisiti_checkboxes.append(art115_07)
        art115_09 = QCheckBox("Guida di veicoli senza aver compiuto i previsti 24 anni")
        art115_09.setProperty("Ipotesi", "115-9")
        self.patente_requisiti_checkboxes.append(art115_09)
        art115_10 = QCheckBox("Guida di veicolo oltre l'età massima")
        art115_10.setProperty("Ipotesi", "115-10")
        self.patente_requisiti_checkboxes.append(art115_10)
        art115_11 = QCheckBox("Incauto affidamento")
        art115_11.setProperty("Ipotesi", "115-11")
        self.patente_requisiti_checkboxes.append(art115_11)
        art115_13 = QCheckBox("Guida accompagnata autorizzata senza contrassegno o trasportando persone")
        art115_13.setProperty("Ipotesi", "115-13")
        self.patente_requisiti_checkboxes.append(art115_13)
        art115_14 = QCheckBox("Minore, autorizzato alla guida accompagnata, che supera i limiti di velocità")
        art115_14.setProperty("Ipotesi", "115-14")
        self.patente_requisiti_checkboxes.append(art115_14)
        art115_15 = QCheckBox("Minore autorizzato alla guida accompagnata senza avere l'accompagnatore al fianco")
        art115_15.setProperty("Ipotesi", "115-15")
        self.patente_requisiti_checkboxes.append(art115_15)
        #art115_16 = QCheckBox("Esercitazione in autostrada di minore autorizzato alla guida accompagnata")

        patente_requisiti.addWidget(patente_art115)
        patente_requisiti.addWidget(art115_04)
        patente_requisiti.addWidget(art115_05)
        patente_requisiti.addWidget(art115_06)
        patente_requisiti.addWidget(art115_07)
        patente_requisiti.addWidget(art115_09)
        patente_requisiti.addWidget(art115_10)
        patente_requisiti.addWidget(art115_11)
        patente_requisiti.addWidget(art115_13)
        patente_requisiti.addWidget(art115_14)
        patente_requisiti.addWidget(art115_15)
        # patente_requisiti.addWidget(art115_16)
        
        # STATO della PERSONA
        tab_stato_persona_layout = QLabel("Stato della Persona")
        tab_stato_persona_layout.setObjectName("intestazione2")

        # Aggiungi bottone 
        tab_persona_botton = QPushButton("Aggiorna Dati Persona")

        # Aggiungi la funzione per il bottone
        tab_persona_botton.clicked.connect(self.update_persona_data)
       
        # Definisci il layout per la tabella della persona
        self.persona_tab.setLayout(QVBoxLayout())   
        self.persona_tab.layout().addWidget(tab_documenti_persona_layout)
        self.persona_tab.layout().addSpacing(5)
        self.persona_tab.layout().addLayout(patente_requisiti)
        self.persona_tab.layout().addStretch(1)
        self.persona_tab.layout().addWidget(tab_stato_persona_layout)
        self.persona_tab.layout().addSpacing(5)
        #self.persona_tab.layout().addLayout(box_etilometro)
        self.persona_tab.layout().addSpacing(10)
        self.persona_tab.layout().addStretch(1)
        self.persona_tab.layout().addWidget(tab_persona_botton, alignment=Qt.AlignmentFlag.AlignRight| Qt.AlignmentFlag.AlignBottom)

    def update_persona_data(self):
        # Funzione per aggiornare i dati della persona
        testo = ""
        for element in self.patente_requisiti_checkboxes:
            if element.isChecked():
                data_value = element.property("Ipotesi")
                #print(data_value)
                for chiave in art_cds_new.dizionario_art_cds:
                    if chiave == data_value:
                        testo += f"<br><span style = 'font-size : 12px ; font-weight : italic; color: blue'> ipotesi: {data_value}</span><br>"
                        testo += f"<span style = 'font-size : 15px; font-weight : bold'>{art_cds_new.dizionario_art_cds[chiave]["art"]} </span><br>"
                        if art_cds_new.dizionario_art_cds[chiave]["sanzioni accessorie"]:
                            lista_s ='; '.join(art_cds_new.dizionario_art_cds[chiave]["sanzioni accessorie"])
                            testo += f"<span style = 'color: green'>{lista_s} </span><br>"
                        else:
                            testo += "<span style = 'color: green'> Nessuno </span><br>"
                        if art_cds_new.dizionario_art_cds[chiave]["art correlati"]:
                            lista ='; '.join(art_cds_new.dizionario_art_cds[chiave]["art correlati"])
                            testo += f"<span style = 'color: red'>{lista} </span><br>"
                        else:
                            testo += "<span style = 'color: red'> Nessuno </span><br>"
        self.display_persona_label.setText(testo)
                        #print(art_cds.dizionario_art_cds[chiave]["art correlati"])
        self.update()



    def veicoloTab(self):
        #lista dei checkbox
        self.veicoli_checkboxes=[]

        # Definisci i documenti
        tab_documenti_veicolo_layout = QLabel("Documenti del Veicolo")
        tab_documenti_veicolo_layout.setObjectName("intestazione2")
        
        # Definsci l'assenza dei documenti con un checkBox
        # REVISIONE
        revisione =QVBoxLayout()

        revisione_art80 = QLabel("Revisione")
        revisione_art80.setObjectName("subtitle")

        art80_01 = QCheckBox("Circolazione con veicolo sena revisione")
        art80_01.setProperty("Ipotesi", "80-1")
        self.veicoli_checkboxes.append(art80_01)
        art80_02 = QCheckBox("Circolazione con veicolo non sottoposto a revisione singola straoirdinaria")
        art80_02.setProperty("Ipotesi", "80-2")
        self.veicoli_checkboxes.append(art80_02)
        art80_03 = QCheckBox("Circolazione con veicolo la cui revisione è stata ripetutamente omessa")
        art80_03.setProperty("Ipotesi", "80-3")
        self.veicoli_checkboxes.append(art80_03)
        art80_04 = QCheckBox("Circolazione con veicolo sopseso dalla circolazione 1° infrazione")
        art80_04.setProperty("Ipotesi", "80-4")
        self.veicoli_checkboxes.append(art80_04)
        art80_05 = QCheckBox("Circolazione con veicolo sospeso dalla circolazione -reiterazione della violazione")
        art80_05.setProperty("Ipotesi", "80-5")
        self.veicoli_checkboxes.append(art80_05)
        art80_17 = QCheckBox("Esibizione di falsa attestazione di revisione")
        art80_17.setProperty("Ipotesi", "80-8")
        self.veicoli_checkboxes.append(art80_17)

        revisione.addWidget(revisione_art80)
        revisione.addWidget(art80_01)
        revisione.addWidget(art80_02)
        revisione.addWidget(art80_03)
        revisione.addWidget(art80_04)
        revisione.addWidget(art80_05)
        revisione.addWidget(art80_17)

        # DOCUMENTO DI CIRCOLAZIONE art 93-95
        documento_di_circolazione = QVBoxLayout()

        doc_di_circolazione_art93 = QLabel("Documento di cirocalzione")
        doc_di_circolazione_art93.setObjectName("subtitle")

        art93_01 = QCheckBox("Circolazione con veicolo non immatricolato senza documento di circolazione (conducente)")
        art93_01.setProperty("Ipotesi", "93-1")
        self.veicoli_checkboxes.append(art93_01)
        art93_02 = QCheckBox("Consentire la circolazione con veicolo non immatricolato (proprietario)")
        art93_02.setProperty("Ipotesi", "93-2")
        self.veicoli_checkboxes.append(art93_02)
        art93_03 = QCheckBox("Traino di rimorchio con caratteristiche non indicate nel documento di circolazione")
        art93_03.setProperty("Ipotesi", "93-3")
        self.veicoli_checkboxes.append(art93_03)
        art95_01 = QCheckBox("Circolazione senza avere con sé l'estratto del cdocumento  di circolazione")
        art95_01.setProperty("Ipotesi", "95-1")
        self.veicoli_checkboxes.append(art95_01)

        documento_di_circolazione.addWidget(doc_di_circolazione_art93)
        documento_di_circolazione.addWidget(art93_01)
        documento_di_circolazione.addWidget(art93_02)
        documento_di_circolazione.addWidget(art93_03)
        documento_di_circolazione.addWidget(art95_01)

        

        # Definisci se l'assicurazione è scaduta con un radio button e inserire la data di scadenza

        tab_stato_veicolo_layout= QLabel("Stato del Veicolo")
        tab_stato_veicolo_layout.setObjectName("intestazione2")

        #TARGHE 100 - 102
        targhe =QVBoxLayout()

        targhe_art100 = QLabel("Targhe")
        targhe_art100.setObjectName("subtitle")
        art100_01 = QCheckBox("Autoveicolo senza targa di immatricolaizone")
        art100_01.setProperty("Ipotesi", "100-1")
        self.veicoli_checkboxes.append(art100_01)
        art100_02 = QCheckBox("Motoveicolo senza targa fi immatricolazione")
        art100_02.setProperty("Ipotesi", "100-2")
        self.veicoli_checkboxes.append(art100_02)
        art100_03 = QCheckBox("Rimorchio sena targa posteriore")
        art100_03.setProperty("Ipotesi", "100-3")
        self.veicoli_checkboxes.append(art100_03)
        art100_04 = QCheckBox("Rimorchio o carrello appendice senza targa ripetitrice")
        art100_04.setProperty("Ipotesi", "100-4")
        self.veicoli_checkboxes.append(art100_04)
        art100_05 = QCheckBox("targa non rifrangente")
        art100_05.setProperty("Ipotesi", "100-5")
        self.veicoli_checkboxes.append(art100_05)
        art100_06 = QCheckBox("Collocazione o installazione irregolare di targa")
        art100_06.setProperty("Ipotesi", "100-6")
        self.veicoli_checkboxes.append(art100_06)
        art100_07 = QCheckBox("Targa con distintivi, iscrizioni e sigle vietate")
        art100_07.setProperty("Ipotesi", "100-7")
        self.veicoli_checkboxes.append(art100_07)
        art100_08 = QCheckBox("Targa auto-costruita per motoveicoli durante le gare autorizzate non avente le caratteristiche richieste")
        art100_08.setProperty("Ipotesi", "100-8")
        self.veicoli_checkboxes.append(art100_08)
        art100_09 = QCheckBox("Veicolo avente targa non propria o contraffatta - 1° infrazione")
        art100_09.setProperty("Ipotesi", "100-9")
        self.veicoli_checkboxes.append(art100_09)
        art100_10 = QCheckBox("Veicolo avente targa non propria o contraffatta - Reiterazione")
        art100_10.setProperty("Ipotesi", "100-10")
        self.veicoli_checkboxes.append(art100_10)
        #art100_11 = QCheckBox("Falsificazione, alterazione, manomissione di targhe")
        
        art100_12 = QCheckBox("Uso di targa falsa, manomessa o alterata")
        art100_12.setProperty("Ipotesi", "100-12")
        self.veicoli_checkboxes.append(art100_12)
        art100_13 = QCheckBox("Infrazioni reiterate di mancanza o uso imporprio della targa di motoveicoli, autoveicoli o rimorchi")   
        art100_13.setProperty("Ipotesi", "100-13")
        self.veicoli_checkboxes.append(art100_13)
        art102_02 = QCheckBox("Circolazione con targa autocostruita senza denunciare la perdita dell'originale")
        art102_02.setProperty("Ipotesi", "102-2")
        self.veicoli_checkboxes.append(art102_02)
        art102_03 = QCheckBox("Circolazione oltre i termini con targa autocostruita")
        art102_03.setProperty("Ipotesi", "102-3")
        self.veicoli_checkboxes.append(art102_03)
        art102_04 = QCheckBox("Circolazione con targa illeggibile")
        art102_04.setProperty("Ipotesi", "102-4")
        self.veicoli_checkboxes.append(art102_04)

        targhe.addWidget(targhe_art100)
        targhe.addWidget(art100_01)
        targhe.addWidget(art100_02)
        targhe.addWidget(art100_03)
        targhe.addWidget(art100_04)
        targhe.addWidget(art100_05)
        targhe.addWidget(art100_06)
        targhe.addWidget(art100_07)
        targhe.addWidget(art100_08)
        targhe.addWidget(art100_09)
        targhe.addWidget(art100_10)
        #targhe.addWidget(art100_11)
        targhe.addWidget(art100_12)
        targhe.addWidget(art100_13)
        targhe.addWidget(art102_02)
        targhe.addWidget(art102_03)
        targhe.addWidget(art102_04)


        # Aggiungi bottone
        tab_veicolo_botton = QPushButton("Aggiorna Dati Veicolo")

        # Aggiungi la funzione per il bottone
        tab_veicolo_botton.clicked.connect(self.update_veicolo_data)

        # Definisci il layout per la tabella del veicolo
        self.veicolo_tab.setLayout(QVBoxLayout())
        
        self.veicolo_tab.layout().addWidget(tab_documenti_veicolo_layout)
        self.veicolo_tab.layout().addSpacing(5)
        self.veicolo_tab.layout().addLayout(revisione)
        self.veicolo_tab.layout().addSpacing(5)
        self.veicolo_tab.layout().addLayout(documento_di_circolazione)
        self.veicolo_tab.layout().addSpacing(5)
        #self.veicolo_tab.layout().addLayout(targhe)
        self.veicolo_tab.layout().addStretch(1)
        self.veicolo_tab.layout().addWidget(tab_stato_veicolo_layout) 
        self.veicolo_tab.layout().addSpacing(5)
        self.veicolo_tab.layout().addLayout(targhe)
        self.veicolo_tab.layout().addSpacing(5)
        self.veicolo_tab.layout().addStretch(1)
        self.veicolo_tab.layout().addWidget(tab_veicolo_botton, alignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
    def update_veicolo_data(self):
        testo = ""
        for element in self.veicoli_checkboxes:
            if element.isChecked():
                data_value = element.property("Ipotesi")
                #print(data_value)
                for chiave in art_cds_new.dizionario_art_cds:
                    if chiave == data_value:
                        testo += f"<br><span style = 'font-size : 12px ; font-weight : italic; color: blue'> ipotesi: {data_value}</span><br>"
                        testo += f"<span style = 'font-size : 15px; font-weight : bold'>{art_cds_new.dizionario_art_cds[chiave]["art"]} </span><br>"
                        if art_cds_new.dizionario_art_cds[chiave]["sanzioni accessorie"]:
                            lista_s ='; '.join(art_cds_new.dizionario_art_cds[chiave]["sanzioni accessorie"])
                            testo += f"<span style = 'color: green'>{lista_s} </span><br>"
                        else:
                            testo += "<span style = 'color: green'> Nessuno </span><br>"
                        if art_cds_new.dizionario_art_cds[chiave]["art correlati"]:
                            lista ='; '.join(art_cds_new.dizionario_art_cds[chiave]["art correlati"])
                            testo += f"<span style = 'color: red'>{lista} </span><br>"
                        else:
                            testo += "<span style = 'color: red'> Nessuno </span><br>"
        self.display_veicolo_label.setText(testo)     
        self.update()   

    def velocitàTab(self):
        # lista checkbox selezionati
        self.velocità_checkboxes =[]

        vel = QLabel("Superamento dei limiti di velocità")
        vel.setObjectName("subtitle")

        # Limiti di velocità
        velocità = QVBoxLayout()

        velocità_limiti = QLabel("Limiti")
        velocità_limiti.setObjectName("subtitle")

        art117_01 = QCheckBox("Violazione limiti di velocità per neopatentati")
        art117_01.setProperty("Ipotesi", "117-01")
        self.velocità_checkboxes.append(art117_01)
        art141_01 = QCheckBox("Circolazione a velocità non adeguata")
        art141_01.setProperty("Ipotesi", "141-1")
        self.velocità_checkboxes.append(art141_01)
        art142_07 = QCheckBox("Superamento dei limiti di velocità non oltre 10 km/h")
        art142_07.setProperty("Ipotesi", "142-1")
        self.velocità_checkboxes.append(art142_07)
        art142_08 = QCheckBox("Superamento dei limiti di velocità di oltre 10 km/h ma non oltre 40 km/h")
        art142_08.setProperty("Ipotesi", "142-3")
        self.velocità_checkboxes.append(art142_08)
        art142_09 = QCheckBox("Superamento dei limiti di velocità di oltre 40 km/h ma non oltre 60 km/h")
        art142_09.setProperty("Ipotesi", "142-5")
        self.velocità_checkboxes.append(art142_09)
        art142_09bis = QCheckBox("Supermanto dei limiti di velocità di oltre 60 km/h")
        art142_09bis.setProperty("Ipotesi", "142-9")
        self.velocità_checkboxes.append(art142_09bis)



        velocità.addWidget(art117_01)
        velocità.addWidget(art141_01)
        velocità.addWidget(art142_07)
        velocità.addWidget(art142_08)
        velocità.addWidget(art142_09)
        velocità.addWidget(art142_09bis)

        # Bottone aggiorna i dati
        tab_velocità_button = QPushButton("Aggiorna Dati Velocità")

        tab_velocità_button.clicked.connect(self.update_velocita_data)


        self.velocità_tab.setLayout(QVBoxLayout())
        self.velocità_tab.layout().addWidget(vel)
        self.velocità_tab.layout().addLayout(velocità)
        self.velocità_tab.layout().addStretch(1)
        self.velocità_tab.layout().addWidget(tab_velocità_button, alignment = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

    def update_velocita_data(self):
        #print("aggiornato")
        testo = ""
        for element in self.velocità_checkboxes:
            if element.isChecked():
                data_value = element.property("Ipotesi")
                #print(data_value)
                for chiave in art_cds_new.dizionario_art_cds:
                    if chiave == data_value:
                        testo += f"<br><span style = 'font-size : 12px ; font-weight : italic; color: blue'> ipotesi: {data_value}</span><br>"
                        testo += f"<span style = 'font-size : 15px; font-weight : bold'>{art_cds_new.dizionario_art_cds[chiave]["art"]} </span><br>"
                        if art_cds_new.dizionario_art_cds[chiave]["art correlati"]:
                            lista ='; '.join(art_cds_new.dizionario_art_cds[chiave]["art correlati"])
                            testo += f"<span style = 'color: red'>{lista} </span><br>"
                        else:
                            testo += "<span style = 'color: red'> Nessuno </span><br>"
        self.display_velocità_label.setText(testo)     
        self.update()

    def sanzioneWidget(self):
        sanzione_lable=QLabel("ART Infranti")
        sanzione_lable.setObjectName("intestazione1")
        

        self.display_persona_label = QLabel("")
        self.display_persona_label.setWordWrap(True)
        
        self.display_veicolo_label = QLabel("")
        self.display_veicolo_label.setWordWrap(True)

        self.display_velocità_label = QLabel("")
        self.display_velocità_label.setWordWrap(True)        



        # Layout per il widget laterale
        self.side_widget.setLayout(QVBoxLayout())
        self.side_widget.layout().addWidget(sanzione_lable)
        #self.side_widget.layout().addSpacing(10)
        #self.side_widget.layout().addWidget(persona_label)
        self.side_widget.layout().addWidget(self.display_persona_label)
        #self.side_widget.layout().addSpacing(2)
        #self.side_widget.layout().addWidget(veicolo_label)
        self.side_widget.layout().addWidget(self.display_veicolo_label)
        #self.side_widget.layout().addSpacing(2)
        self.side_widget.layout().addWidget(self.display_velocità_label)
        self.side_widget.layout().addStretch(1)

  

# Funzione principale per eseguire l'applicazione       
if __name__=="__main__":
    app=QApplication(sys.argv)
    window = PostoDiBlocco()
    sys.exit(app.exec())
