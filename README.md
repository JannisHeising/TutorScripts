## Erstellen der Namensliste

In Müsli, gehe zur Teilnehmer und kopiere den Text vom ersten Namen zum letzten. Das wird die Studiengänge der Teilnehmer beinhalten, aber das ist nicht schlimm. Diesen Text dann in eine Textdatei einfügen, am Besten im Ordner des derzeitigen Übungszettels oder einen Ordner drüber.


## unzip.py

Dieses Skript erledigt drei Dinge:

1. Entzippen der zip-Datei mit allen (!) Abgaben.
2. Löschen derjenigen Abgaben, deren Nachname nicht in der Namensliste auftaucht.
3. Falls eine Abgabe eine einzelne zip-Datei ist, entzippen dieser (+löschen der zip-Datei).

Achtung: Wenn mehrere Abgaben mit dem gleichen Nachnamen übrigbleiben, muss man manuell schauen, welches die richtige ist. Vornamen werden ignoriert, weil sie manchmal auf Moodle und Müsli unterschiedliche Formatierungen haben.


## create-score.py

Erstellt eine JSON-Datei, in die die Punkte eingetragen werden können, um sie vom nächsten Skript (semi-)automatisch in Müsli eintragen zu lassen.


## enter-score.py

Dieses Skript trägt die Punkte aus der JSON-Datei in eine html-Datei ein. Hierzu kann man folgendermaßen vorgehen:

1. Gehe in Müsli zur Punktetabelle des derzeitigen Übungszettels.
2. Inspiziere den HTML-Code (Rechtsklich -> Inspect).
3. Suche (Strg + F) nach grading-table und wähle das zweite Ergebnis (<table id="grading-table" ...>).
4. Rechtsklick darauf -> Copy Outer HTML.
5. Füge den kopierten Text in eine Textdatei ein.

(Man kann jeden beliebigen HTML-Teil kopieren, solange das Element mit id="grading-table" vollständig enthalten ist.)

Nun kann man das Skript ausführen. Anschließend kann man den veränderten Text wieder in Müsli einfügen, und zwar wieder nach Schritt 1-4, nur am Ende Paste Outer HTML (statt Copy).