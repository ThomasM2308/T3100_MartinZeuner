# Kapitel 5 (QR-Scanner): Bearbeitungs- und Prüfstand

Ursprünglicher Stand: 23.11.2026. Branch: `QR-Scanner_Dokument_bearbeitet`, abgezweigt von `studienarbeit/grundlagen-ueberarbeitung` (Commit `fa013e2`).

## Umfang der Änderung

- `content/05_QR-Scanner.tex`: Gerüst durch ausformulierten Text ersetzt (Zielumfang laut Gerüst ca. 6 Seiten; Probesatz des Kapitels allein ergab knapp 7 Seiten inkl. Gleitobjekte).
- `content/literature.bib`: ein neuer Eintrag `usr410s_quickstart` (Werkseinstellungen des Konverters). Bestehende Einträge unverändert.
- Diese Prüfnotizen.

Andere Kapitel, die Hauptdatei und der KI-Anhang wurden nicht verändert.

## Herkunft der Angaben

| Aussage im Kapitel | Grundlage |
|---|---|
| Matrix 200, Variante 212-100, 10–30 V DC | Typenschild-Foto `scanner_matrix200_typenschild.jpg` (Gerüstnotiz) |
| CBX100 führt Versorgung, serielle Schnittstelle, Trigger auf Klemmen | `datalogic_cbx100_grundlagen` (wie in Kapitel 2) – **Abschnitt im Handbuch nachtragen** |
| Altes Programm: COM3, 19 200 Bd, 8N1 (Default), `LON`, Ziffernfilter, kein Reconnect, Bit auch bei unbekanntem Code, Warten ohne Timeout | Code der Vorgänger (`Scanner.py`, `Studienarbeit2_Threading.py`, `Auslagern.py`) |
| USB-RS232-Adapter als COM10; COM3 nicht vorhanden | Inbetriebnahme 23.11.2026, Terminalausgabe „Verfügbare Ports: COM10, COM4, COM5“ (COM4/5 = Bluetooth) |
| DHCP am USB-Ethernet-Adapter, keine IPv4, snap7-Timeout; danach 192.168.0.50/24 ohne Gateway, Ping auf SPS ok | Inbetriebnahme 23.11.2026 (Windows-Einstellungen, Terminal) |
| `LON` bei 9 600–115 200 Bd, Parität N/E: keine Daten | Suchskript `scanner_suche.py`, mehrere Läufe |
| Auslösung über HMI „Scannen“ / SPS-Trigger | Beobachtung; Hinweis der Studierenden, dass ein Triggerkabel zur SPS führt – **Leitung und Scanner-Einstellung noch bestätigen** |
| Etiketten enthalten Klartext (`Buche`) | Terminalausgabe `Rohdaten: Buche` |
| Werkseinstellungen USR-TCP232-410S | `usr410s_quickstart` (Herstellerkurzanleitung) |
| Einzelnes unlesbares Zeichen bei 115 200 Bd, danach 19 200 Bd ok | Terminalausgabe `Rohdaten: 'à'`, danach erfolgreiche Scans |
| Kein Nullmodem nötig | gleiche Leitung wie am USB-Adapter funktionierte |
| FB 6, Zeile 52: `_ue` statt `_auftr`, Bereichslängenfehler, STOP | TIA-Diagnosepuffer und FB 6 (Projekt 260705_T3_3200), Korrektur durch die Studierenden geladen |
| 20-s-Zeitgrenze, Vormerken neuer Scans, Sperre nur pro Zugriff | Code `Studienarbeit2_Threading.py` (T3X00), mit simulierter SPS geprüft, danach an der Anlage bestätigt |
| Adressen .2/.4/.20 | TIA-Netzsicht (Gerüstnotiz 05.11.2026) |

## Offene Punkte (im PDF rot markiert)

1. Triggerleitung SPS → CBX100 und Trigger-Modus des Scanners bestätigen (Handbuch/Konfiguration).
2. Haupt- oder Hilfsschnittstelle der CBX100 für die RS232-Leitung angeben (vgl. Prüfnotiz 3 zu Kapitel 2).
3. Spannungsversorgung des Konverters (Netzteil oder 24 V vom Gestell) und Montageort angeben.
4. Zugangsdaten der Weboberfläche: geändert? Im Dokument keine Passwörter nennen.
5. Abschlusszeichen messen (`scanner_tcp_test.py`, HEX-Ausgabe) und in 5.4 eintragen.
6. Test 7 (Netzwerkkabel ziehen) und Test 8 (Dauerbetrieb) durchführen und eintragen.
7. Abstimmung der FB-6-Korrektur mit dem Betreuer bestätigen.
8. Verweis auf den digitalen Anhang (Code-ZIP) anpassen.
9. Bibliografische Angaben `schaal_zorko_t3200` (Vornamen, Titel) ergänzen; Handbuch Matrix 200 (`datalogic_matrix200`) ist noch ein TODO-Eintrag und wird im Kapitel bewusst nicht zitiert.
10. Montage des Scanners auf der Einschubplatte (Gerüstnotiz) – falls umgesetzt, in 5.1/5.4 oder als Foto ergänzen.

## Hinweise für die Überarbeitung

- Die ursprüngliche Erklärung der falschen Baudrate („sechsfache Abtastrate“) wurde am 25.11.2026 durch eine Beschreibung der nicht übereinstimmenden Bitzeiten ersetzt. Aus dem einzelnen unlesbaren Zeichen lässt sich kein genauer interner Abtastvorgang ableiten.
- Die Befunde FB 6 und CSV/SPS-Bestand sollten in Kapitel 7 (Ausblick) aufgegriffen werden: Fehler-OB bzw. Bereichsprüfung in FB 6, Abgleich CSV ↔ `DB_Lagerbestand`.
- KI-Nutzung: Rohfassung mit Claude erstellt (Kommentar im Kopf der Datei) – im KI-Anhang offenlegen.

## Prüfung

- Alle Zitierschlüssel existieren in `literature.bib`, alle `\ref`-Ziele existieren im Projekt.
- Klammern und Umgebungen geschlossen.
- Probesatz des Kapitels allein (pdfLaTeX, gleiche Seitenränder, 12 pt, 1,5-zeilig; ohne biblatex/ngerman, die im Container fehlen): fehlerfrei, ca. 6,5 Seiten. Ein Gesamtlauf mit `Projektarbeit.tex` steht aus.


## Redaktionelle Überarbeitung vom 25.11.2026

Kapitel 5 wurde mit ChatGPT sprachlich und strukturell an die Grundlagen angepasst. Die fachliche Basis bilden ausschließlich die vorhandene Kapitelversion und die oben aufgeführten Prüfnotizen. Es wurden keine neuen Anlagenversuche durchgeführt; die externe Python-Anwendung und das TIA-Projekt wurden bei dieser Überarbeitung nicht ausgeführt oder erneut geprüft.

- Der Adressplan bleibt als einzige Tabelle im Haupttext erhalten. Variantenvergleich und Konverterparameter werden zusammenhängend erläutert.
- Die nummerierte Fehlerliste wurde in die Beschreibung der Referenzinbetriebnahme integriert. Die Argumentation folgt Ausgangszustand, Auswahl, Umsetzung, Prüfung und Bewertung.
- Das Prüfprotokoll und der unveränderte Codeausschnitt stehen in `content/103_Anhang_QR-Scanner.tex`. Die Hauptdatei bindet diesen Anhang nach Kapitel 7 ein. Die bisherigen Labels `tab:qr_test` und `lst:qr_read` bleiben erhalten; die nicht mehr benötigten Labels `tab:qr_varianten` und `tab:qr_konfig` entfallen.
- Die Korrektur in FB 6 wird als Behebung eines bestehenden Fehlers gegenüber der verworfenen Verlagerung der Scannerverarbeitung in die SPS abgegrenzt. Eine Abstimmung mit dem Betreuer wird nicht als erfolgt dargestellt.
- Der Empfang nach Betätigung des HMI wird als Beobachtung dokumentiert; Triggerleitung und Scannerparametrierung bleiben zu bestätigen. Aus dem Ausbleiben von Daten auf `LON` wird keine allgemeine Aussage über die Unterstützung des Befehls abgeleitet.
- Bei DHCP ist von einer fehlenden geeigneten Adresse für das Anlagennetz die Rede, nicht pauschal vom Fehlen jeglicher IPv4-Adresse.
- Die Ruhezeit von 0,3 s wird als Ersatz für ein Abschlusszeichen beschrieben. Der Empfangstimeout von 0,2 s, der Wiederverbindungsabstand von 2 s und das Auftragszeitfenster von 20 s bleiben unverändert.
- Die bestehende Filterregel wird ausdrücklich erläutert: Gemischte alphanumerische Codes werden auf ihre Ziffern reduziert. Eine beliebige Klartextunterstützung wird nicht behauptet.
- Der Versuch mit falscher Baudrate wird im Prüfprotokoll als fehlgeschlagener Empfang mit anschließender Ursachenklärung dokumentiert, nicht als von vornherein erfolgreich erwarteter Fehler.
- Alle offenen Anschlussangaben, die digitalen Codeunterlagen, der Wiederverbindungstest und der Dauertest bleiben offen. Die Inhalte und bibliografischen Einträge der übrigen Kapitel wurden nicht redaktionell verändert.
- Der bestehende KI-Anhang ist weiterhin ein markierter Vorgänger-Platzhalter. Die Nutzung von Claude für die Rohfassung und von ChatGPT für diese Überarbeitung ist vor Abgabe dort zutreffend zu ergänzen.

### Prüfung der überarbeiteten Fassung

- Vollständiger Build mit pdfLaTeX und Biber (TeX Live 2026) erfolgreich; Literatur und Querverweise nach Folgeläufen aufgelöst. Gesamtfassung: 55 PDF-Seiten.
- Kapitel 5 umfasst die Druckseiten 29–36 (acht Seiten); Anhang A die Seiten 42–43 (zwei Seiten). Alle zehn Seiten wurden als Bilder auf Lesbarkeit, Umbrüche und überstehende Elemente geprüft.
- Im überarbeiteten Kapitel und seinem Anhang gibt es im abschließenden LaTeX-Lauf keine Overfull- oder Underfull-Meldungen. Der Prüfbericht im Anhang verwendet linksbündige Tabellenzellen.
- Alle Zitierschlüssel und Querverweise der beiden bearbeiteten Inhaltsdateien geprüft; der Codeauszug wurde zeichengetreu aus der Ausgangsfassung übernommen. Bibliografie unverändert.
- Außerhalb des Änderungsumfangs bleiben bestehende Warnungen: fehlende Abbildungsziele `fig:ventil` und `fig:not_halt` in Kapitel 4 sowie überbreite Stellen unter anderem in Vorgänger-Platzhaltern, den Grundlagen und im Literaturverzeichnis. Diese wurden nicht stillschweigend mitbearbeitet.
- Keine erneute Funktionsprüfung von Python-Code, SPS oder Anlage. Die im Kapitel dokumentierten Versuchsergebnisse sind Angaben aus dem vorhandenen Projektstand, keine Ergebnisse dieser redaktionellen Prüfung.
