# Grundlagen: Bearbeitungs- und Prüfstand

Stand: 23.11.2026. Ausgangscommit: `9604b21dc88902bc46f62b4037c712ae342cfcb7`.

## Umfang der Änderung

Kapitel 2 wurde eigenständig neu formuliert und auf die drei vorgesehenen Maßnahmen ausgerichtet. Der allgemeine Anlagenaufbau sowie SPS-, PROFINET- und IO-Link-Grundlagen bleiben erhalten. Die langen FUP-/SCL-Vergleiche und die alten Projektziele wurden aus dem Grundlagenkapitel entfernt. Hinzugekommen sind RS232, CBX100, Ethernet-Switching, IPv4, TCP, serieller Geräteserver, Datenpufferung, Socket-Kommunikation und Energieführungsketten. Zwei Tabellen und zwei erläuterte Berechnungsansätze unterstützen die Darstellung.

Nur `content/02_Grundlagen.tex`, ergänzende Einträge in `content/literature.bib` und diese Prüfnotizen sind Teil der Änderung. Einleitung, Umsetzungskapitel, Hauptdatei, Vorgängerarchiv und bestehende Literaturdatensätze wurden nicht verändert. Die PDF unter `build/` stammt weiterhin aus dem alten Stand.

## Quellenbasis

Die neuen externen Belege wurden beim jeweiligen Hersteller, Fachverband, der DGUV/BGHM, dem RFC Editor beziehungsweise in der offiziellen Python-Dokumentation eingesehen. Das Abrufdatum bezeichnet den tatsächlichen Recherchetag. Veröffentlichungsdaten wurden nur eingetragen, wenn sie aus dem Dokument oder der zugehörigen Publikationsseite hervorgehen. Es wurden keine Normausgaben als selbst eingesehene Volltexte ausgegeben.

| Abschnitt | Wesentliche Belege | Einordnung |
|---|---|---|
| Anlagenaufbau | `vorgaenger_grundlagen_archiv`, Querverweis auf Kapitel 3 | Archivtext am Ausgangscommit; eigene aktuelle Bestandsaufnahme getrennt davon |
| SPS und PROFINET | `siemens_zyklus_2014`, `pi_profinet_2018` | Zyklus/Prozessabbild und Trennung von PROFINET-RT und TCP/IP |
| IO-Link | `iolink_system_2018`, `ifm_iolink_technik`, `ifm_al1100_datenblatt_2024` | Punkt-zu-Punkt, Datenarten, IODD, AL1100, 20-m-Grenze |
| Sicherheit | `ifa_report_2025`, `bghm_nothalt`, `ifm_oy5100`, `pilz_pnoz_s4_grundlagen` | Wirkungskette, PL/Kategorie, Einordnung des Messlichtgitters und Relaisfunktionen |
| RS232 und CBX100 | `ti_rs232_2002`, `adi_rs232_2001`, `datalogic_cbx100_grundlagen` | Elektrische Pegel, Zeichenrahmen, Haupt-/Hilfsschnittstelle |
| Netzwerk | `cisco_switching`, `rfc1122`, `rfc1918`, `rfc9293` | Switching, Schichten, Adressierung und Bytestrom |
| Konverter und Anwendung | `usr410s_grundlagen`, `python_socket_howto`, `python_socket_api` | Betriebsarten, Paketierung, Datenabgrenzung, Socket-Verhalten |
| Leitungsführung | `igus_befuellung`, IO-Link-Systembeschreibung | Biegeradius, Beweglichkeit, Zugentlastung und zulässige Verbindungslänge |

Die Zahlenrechnung für 8N1 bei 19 200 Bd, das Empfangsbeispiel mit CR und die Zerlegung der Latenz sind eigene Erläuterungen. Sie werden nicht als gemessene Projektergebnisse dargestellt. Insbesondere ist CR damit noch nicht als tatsächlicher Scanner-Terminator bestätigt.

## Noch am Projekt abzugleichen

1. **Vorgängerarbeit:** Vollständige Autorennamen, genaue Titel, Abgabejahre und Seitenzahlen müssen aus den Originalarbeiten ergänzt werden. Bis dahin zitiert Kapitel 2 den tatsächlich verfügbaren archivierten Grundlagenauszug mit festem Commit-Link. Die vorhandenen unvollständigen T3100-/T3200-Literatureinträge wurden nicht mit Vermutungen ergänzt.
2. **Konverter:** Der USR-TCP232-410s wird als Herstellerbeispiel erläutert. Bestellvariante (gegebenenfalls Händlerzusatz HB), Firmware und zugehörige Anleitung sind vor der konkreten Parametrierung abzugleichen. Werkseinstellungen, Portnummern oder IP-Adressen wurden nicht als bereits feststehende Projektwerte übernommen.
3. **Scanneranschluss:** Prüfen, ob bisher die Hauptschnittstelle oder die interne RS232-Hilfsschnittstelle der CBX100 verwendet wird. Ein Umklemmen auf eine andere Schnittstelle setzt einen Abgleich der Scannerparameter voraus.
4. **Sicherheitsrelais:** Für die Grundlagen wurde die zugängliche Pilz-Anleitung 21396-EN-17 verwendet. Der bereits vorhandene Eintrag `pilz_pnoz_s4` nennt dagegen 21396-EN-23; dessen URL war bei dieser Recherche nicht abrufbar. Dieser Eintrag wurde wegen der Verweise aus Kapitel 4 nicht stillschweigend ersetzt. Vor der Ausarbeitung von Kapitel 4 die zur verbauten Bestellnummer passende Anleitung heranziehen.
5. **Abgrenzung Sicherheit:** Der neue Text erklärt keinen erreichten Performance Level und keine validierte Personenschutzfunktion. Das OY5100 wird entsprechend der Herstellerbezeichnung als messendes Lichtgitter beschrieben. Die Funktionsbeobachtung im SPS-Programm ist davon getrennt zu beurteilen.
6. **Abgleich mit Kapitel 4 bei dessen späterer Bearbeitung:** Im vorhandenen Text sind Horizontal- und Vertikalmotor den Kontakten 13/14 und 23/24 widersprüchlich zugeordnet. Außerdem wird die fehlende IP54-Einhausung dort allein mit dem Prototypstatus toleriert. Kapitel 2 übernimmt diese Begründung nicht und benennt stattdessen die Herstellervorgabe. Änderungen an Kapitel 4 waren ausdrücklich nicht Teil dieses Schritts.
7. **KI-Nutzung:** Die Neufassung entstand mit Unterstützung von ChatGPT, einschließlich Quellenrecherche und sprachlicher Ausarbeitung. Die Autoren müssen den Inhalt fachlich prüfen. Bei der späteren Überarbeitung des KI-Anhangs ist diese tatsächliche Nutzung zu ergänzen; der vorhandene Anhang wurde hier nicht verändert.

## Prüfung

- Alle 21 in Kapitel 2 verwendeten Quellenschlüssel sind in `literature.bib` definiert; keine doppelten Schlüssel.
- Alle internen Verweise des neuen Kapitels haben ein Ziel im Projekt.
- LaTeX-Umgebungen und geschweifte Klammern des Kapitels wurden auf Abschluss geprüft.
- Keine alten Platzhalter, hart eingetippten Literaturziffern oder ungeklärten Messwerte im neuen Kapitel.
- Die bisherigen Literatureinträge wurden bytegetreu erhalten und um 21 Einträge ergänzt.
- Ein lokaler PDF-Prüflauf war **nicht erfolgreich abschließbar**: Auf dem ausführenden Rechner ist Tectonic vorhanden, aber kein pdfLaTeX/Biber. Die Vorlage ist auf pdfLaTeX/Biber eingestellt. Auch ein isolierter, nur temporär für Tectonic angepasster Kapitellauf scheiterte an fehlenden TeX-Paketen (`l3backend-xetex.def`, `blx-bibtex.def`); deren Download war wegen fehlender DNS-/Netzwerkverbindung nicht möglich. Daher liegt noch keine visuelle Satzprüfung vor. Die eigentliche Projektvorlage wurde für diese Versuche nicht verändert.

Für die abschließende Satzprüfung in einer vollständigen TeX-Installation im Ordner `documentation`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error Projektarbeit.tex
biber Projektarbeit
pdflatex -interaction=nonstopmode -halt-on-error Projektarbeit.tex
pdflatex -interaction=nonstopmode -halt-on-error Projektarbeit.tex
```

Dabei sind bestehende Warnungen aus den noch nicht überarbeiteten Kapiteln von Problemen der Neufassung zu unterscheiden. Eine neue Gesamt-PDF sollte erst nach diesem Lauf den bisherigen Build ersetzen.
