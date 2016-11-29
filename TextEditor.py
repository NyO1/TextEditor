from PyQt4.QtGui import *
import os


app = QApplication([])      # Crea un'applicazione Qt
window = QWidget()          # Crea una finestra (ma non e' visibile)
window.resize(500, 300)     # Imposta dimensione e titolo della finestra
window.setWindowTitle('My Python Text Editor')
layout = QVBoxLayout()      # Crea il layout per la finestra
tlayout = QHBoxLayout()     # Crea il layout per la toolbar
button_open = QPushButton('Open')    # Crea i tre bottoni
button_save = QPushButton('Save')
button_exit = QPushButton('Exit')
tlayout.addWidget(button_open)       # Li aggiunge al layout della toolbar
tlayout.addWidget(button_save)
tlayout.addWidget(button_exit)
textedit = QTextEdit('')             # Crea un'area per editare testo
layout.addLayout(tlayout)   # Aggiunge il layout della toolbar a quello della finestra
layout.addWidget(textedit)  # Aggiunge l'area per editare al layout della finestra
layout.addWidget(label)
window.setLayout(layout)    # Imposta il layout della finestra



def open_callback():    # Definisce la callback per aprire un file
    filename = QFileDialog.getOpenFileName(window)
    if not filename: return    # L'utente ha scelto "Cancel"
    with open(filename, 'U') as f:
        textedit.setText(f.read().decode('utf8'))
    

def save_callback():    # Definisce la callback per salvare il file
    filename = QFileDialog.getSaveFileName(window)
    if not filename: return    # L'utente ha scelto "Cancel"
    with open(filename, 'w') as f:
        f.write(textedit.toPlainText().toUtf8())
        


# Imposta le callback dei tre bottoni in risposta all'evento clicked 
button_open.clicked.connect(open_callback) 
button_save.clicked.connect(save_callback)
button_exit.clicked.connect(app.exit)
window.show()               # Mostra la finestra
app.exec_()                 # Lancia l'interazione con l'utente