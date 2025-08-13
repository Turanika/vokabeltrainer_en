# Vokabeltrainer

Ein  Vokabeltrainer in Python mit grafischer Oberfläche (Tkinter), der Vokabeln aus einer CSV-Datei lädt und einzeln anzeigt.  
Der Nutzer kann durch die Wörter blättern, sie mischen und die Übersetzung anzeigen lassen.

## Funktionen

- Lädt Vokabeln aus einer frei wählbaren CSV-Datei
- Blättern zwischen Vokabeln (Vor/Zurück)
- Mischen der Reihenfolge
- Übersetzung auf Knopfdruck anzeigen
- Einfache grafische Oberfläche mit Tkinter

## Installation

1. **Python 3** muss installiert sein  
2. Repository klonen oder ZIP-Datei herunterladen und entpacken
3. Falls benötigt, zusätzliches Modul `tkinter` sicherstellen (meist bereits in Python enthalten)

## Nutzung

Starte das Programm mit:

```
python en_vok_train.py
```
Beim Start kannst du eine eigene CSV-Datei auswählen.
Beispielhafte Datei: example_vocab.csv

## Format der CSV-Datei

Die erste relevante Zeile muss die Zielsprache enthalten, z.B.:

```
:Russisch
````
Die Sprache wird nach dem : erkannt

Danach folgen die Vokabelpaare im Format **Ausgangssprache,Zielsprache** (bzw. korrekte Übersetzung), wie hier:

````
:Russisch 

House,Дом

Car,Машина

Chair,Стул
````
## Tipp

Du kannst beliebige CSV-Dateien mit deinen eigenen Vokabeln erstellen und verwenden.

## Tests

Falls du Unit- oder Integrationstests verwenden möchtest, kannst du sie mit folgendem Befehl ausführen:
```
python -m unittest en_vok_unittest.py
python -m unittest test_integ.py
```