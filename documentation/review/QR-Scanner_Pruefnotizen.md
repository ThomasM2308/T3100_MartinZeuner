# Kapitel 5 (QR-Scanner): Bearbeitungs- und Prüfstand

Stand: 23.11.2026. Branch: `QR-Scanner_Dokument_bearbeitet`, abgezweigt von `studienarbeit/grundlagen-ueberarbeitung` (Commit `fa013e2`).

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

- Aussagen über das Verhalten bei falscher Baudrate („sechsfache Abtastrate“) sind eigene Erklärung, keine Herstellerangabe.
- Die Befunde FB 6 und CSV/SPS-Bestand sollten in Kapitel 7 (Ausblick) aufgegriffen werden: Fehler-OB bzw. Bereichsprüfung in FB 6, Abgleich CSV ↔ `DB_Lagerbestand`.
- KI-Nutzung: Rohfassung mit Claude erstellt (Kommentar im Kopf der Datei) – im KI-Anhang offenlegen.

## Prüfung

- Alle Zitierschlüssel existieren in `literature.bib`, alle `\ref`-Ziele existieren im Projekt.
- Klammern und Umgebungen geschlossen.
- Probesatz des Kapitels allein (pdfLaTeX, gleiche Seitenränder, 12 pt, 1,5-zeilig; ohne biblatex/ngerman, die im Container fehlen): fehlerfrei, ca. 6,5 Seiten. Ein Gesamtlauf mit `Projektarbeit.tex` steht aus.
