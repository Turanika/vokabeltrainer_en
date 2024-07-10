# Autor: TH
# Datum: 10.07.2024


# Dieses Programm ist ein Vokabeltrainer, der Englisch-Wörter mit ihren Entsprechungen in einer
# Fremdsprache (hier: Russisch) anzeigt. Der Benutzer kann durch die Vokabeln blättern, sie mischen und die Übersetzung 
# einer Vokabel anzeigen. Die Vokabeln werden aus einer auf dem PC gespeicherten CSV-Datei geladen.

import random
import tkinter as tk
import tkinter.filedialog
import os

class VokabelTrainer:
    # Intitialisierung der Hauptklasse des Vokabeltrainers.
    # Argumente:
    # root -- Das Hauptfenster des Tkinter-GUIs.
    # woerterbuch -- Ein Wörterbuch, das englische Wörter als Schlüssel und ihre Fremdsprachenübersetzungen als Werte enthält.
    # sprache -- Die Fremdsprache, in die die Wörter übersetzt werden:
    def __init__(self, root, woerterbuch, sprache):
        self.root = root
        
        # Dimension (Geometry) des Fensters ermitteln und als Mindestgröße verwenden:
        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
        
        self.woerterbuch = woerterbuch
        self.sprache = sprache
        self.keys = list(woerterbuch.keys())
        self.index = 0

        # Erstellen und Positionieren der GUI-Elemente
        self.label_vokabel = tk.Label(root, text="", font=('Helvetica', 18))
        self.label_vokabel.pack(pady=20)

        self.button_zurueck = tk.Button(root, text="Zurück", command=self.vorherige_vokabel)
        self.button_zurueck.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_weiter = tk.Button(root, text="Weiter", command=self.naechste_vokabel)
        self.button_weiter.pack(side=tk.RIGHT, padx=10, pady=10)

        self.button_mischen = tk.Button(root, text="Vokabeln mischen", command=self.vokabeln_mischen())
        self.button_mischen.pack(side=tk.LEFT, padx=10, pady=10)

        self.button_antwort = tk.Button(root, text="Antwort anzeigen", command=self.antwort_anzeigen)
        self.button_antwort.pack(side=tk.LEFT, padx=10, pady=10)

        self.vokabel_anzeigen()  # Zeigt die erste Vokabel an

    def vorherige_vokabel(self):
        # Zeigt die vorherige Vokabel an
        self.index -= 1
        if self.index < 0:
            self.index = len(self.keys) - 1
        self.vokabel_anzeigen()

    def naechste_vokabel(self):
        # Zeigt die nächste Vokabel an
        self.index += 1
        if self.index >= len(self.keys):
            self.index = 0
        self.vokabel_anzeigen()

    def antwort_anzeigen(self):
        # Zeigt die Übersetzung der aktuellen Vokabel an
        if self.index < len(self.keys):
            vokabel_englisch = self.keys[self.index]
            vokabel_fremdsprache = self.woerterbuch[vokabel_englisch]
            self.label_vokabel.config(text=f"{vokabel_englisch} in {self.sprache}: {vokabel_fremdsprache}")

    def vokabel_anzeigen(self):
        # Zeigt die aktuelle Vokabel ohne Übersetzung an
        if self.index < len(self.keys):
            vokabel_englisch = self.keys[self.index]
            self.label_vokabel.config(text=f"{vokabel_englisch} in {self.sprache}")

    def vokabeln_mischen(self):
        # Mischt die Reihenfolge der Vokabeln
        random.shuffle(self.keys)
        self.index = 0
        self.vokabel_anzeigen()

def main():
    # Hauptfunktion, die den Vokabeltrainer startet
    root = tk.Tk()

    # Dateiauswahldialog aufrufen
    vokabel_file_path = tkinter.filedialog.askopenfilename(
        initialfile="vokabel_en_kons.csv",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    # GUI-Objekt ausblenden, damit die Konsole wieder in den Vordergrund kommt
    root.withdraw()

    # Überprüfen, ob eine Datei ausgewählt wurde
    if not vokabel_file_path or not os.path.exists(vokabel_file_path):
        print("Keine gültige Datei ausgewählt. Programm wird beendet.")
        return

    # Vokabeln aus der Datei ins Wörterbuch einlesen
    with open(vokabel_file_path, 'r', encoding='utf-8') as vokabel_file:
        zeilen = vokabel_file.readlines()

    woerterbuch = {}
    sprache = ""

    for zeile in zeilen:
        if zeile.startswith(":"):
            sprache = zeile[1:].strip('\n')  # Sprache aus der Datei auslesen
        elif not zeile.startswith(('#', '\n', ':')):
            vokabel_englisch, vokabel_fremdsprache = zeile.strip().split(",", 1)
            woerterbuch[vokabel_englisch.strip()] = vokabel_fremdsprache.strip()

    # Start des Vokabeltrainers
    trainer = VokabelTrainer(root, woerterbuch, sprache)
    root.deiconify()  # GUI bzw. das zuvor durch .withrdaw() ausgeblendete Fenster wieder anzeigen
    root.mainloop()

if __name__ == "__main__":
    main()
