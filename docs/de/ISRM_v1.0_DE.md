# ISRM v1.0 — Offizielle deutsche Übersetzung

**Intelligent Systems Reference Model (ISRM)**  
**Originator:** Marcel Reitz — Altenbuch, Deutschland  
**Initiale Entwicklung:** 2026  
**Veröffentlichung v1.0:** 3. Oktober 2026  
**Kanonische DOI:** 10.5281/zenodo.23115842  
**Lizenz:** CC BY 4.0

> **Sprachstatus:** Dies ist die offizielle deutschsprachige Übersetzung der öffentlich veröffentlichten ISRM-v1.0-Fassung. Sie dient der deutschsprachigen Nutzung, Diskussion und Standardisierungsarbeit. Bei inhaltlichen Abweichungen oder Auslegungsfragen ist die über die DOI veröffentlichte englische v1.0 die maßgebliche Referenz. Diese Übersetzung ist keine DIN-Norm, kein Norm-Entwurf und keine DIN SPEC.

## 1. Anwendungsbereich

ISRM ist ein technologieunabhängiges Referenzmodell für intelligente und zielgerichtete Systeme. Es beschreibt funktionale Verantwortlichkeiten und Informationsflüsse, durch die Ziele oder Ereignisse sowie wahrgenommene Informationen und Kontext in Entscheidungen, kontrollierte Handlungen und beobachtbare Wirkungen überführt werden.

Das Modell ist auf Software-Agenten, deterministische Automatisierung, autonome Systeme, Robotik, cyber-physische Systeme, Multi-Agenten-Systeme, Human-in-the-Loop-Systeme und zukünftige Systemklassen anwendbar, sofern eine sinnvolle funktionale Zuordnung möglich ist.

## 2. Systemgrenze und Umwelt

Die **Umwelt (W)** liegt außerhalb der ISRM-Systemgrenze. Wirkungen werden durch Execution in die Umwelt eingebracht; Signale und Ereignisse aus der Umwelt werden durch Perception aufgenommen. Ein anderes ISRM-System kann Bestandteil dieser Umwelt sein. Die Umwelt wird in v1.0 nicht als funktionale Ebene modelliert.

## 3. Formale Kurznotation

`S = { I, P, C, R, D, E ; G, T, A }`

Dabei stehen **I** für Intent, **P** für Perception, **C** für Context, **R** für Cognition, **D** für Decision, **E** für Execution, **G** für Control, **T** für Trust und **A** für Adaptation. **W** bezeichnet die externe Umwelt.

## 4. Funktionale Ebenen

| Ebene | Funktion | Verantwortung |
|---|---|---|
| **L6** | **Intent** | Gewünschte Ergebnisse, Ziele, Aufgaben, Randbedingungen, Prioritäten und ereignisabgeleitete Ziele |
| **L5** | **Perception** | Transformation von Signalen und Ereignissen in nutzbare Beobachtungen |
| **L4** | **Context** | Aufgabenrelevanter Zustand aus Beobachtungen, Wissen, Gedächtnis, Systemzustand, Annahmen und Unsicherheit |
| **L3** | **Cognition** | Erzeugen, Bewerten und Verfeinern von Interpretationen, Plänen und Kandidatenhandlungen |
| **L2** | **Decision** | Auswahl, Ablehnung, Zurückstellung oder Eskalation unter Autorität, Policy und Risiko |
| **L1** | **Execution** | Überführung autorisierter Handlungen in konkrete Ausführungsversuche und Ergebnisrückmeldung |

### L6 — Intent
Intent repräsentiert gewünschte Ergebnisse, Ziele, Aufgaben, Randbedingungen, Prioritäten und aus Ereignissen abgeleitete Ziele. Intent ist eine funktionale Verantwortung, aber nicht zwingend der erste Eintrittspunkt jeder Verarbeitung.

### L5 — Perception
Perception transformiert Signale, Daten und Ereignisse in für das System nutzbare Beobachtungen. Perception kann unter Kontrolle des Control Plane Intent erzeugen, verfeinern, aussetzen oder beenden.

### L4 — Context
Context bildet den aufgabenrelevanten Zustand aus Beobachtungen, Wissensreferenzen, Gedächtnis, Systemzustand, zeitlichem Geltungsbereich, Annahmen und Unsicherheit.

### L3 — Cognition
Cognition erzeugt, bewertet und verfeinert Interpretationen, Pläne und Kandidatenhandlungen. Die Bezeichnung beschreibt eine funktionale Verantwortung und setzt weder menschliche Kognition noch ein bestimmtes KI-Verfahren voraus.

### L2 — Decision
Decision wählt Kandidatenhandlungen aus, lehnt sie ab, stellt sie zurück oder eskaliert sie. Entscheidungen werden durch Autorität, Policy, Risiko, Unsicherheit und weitere Control-Anforderungen begrenzt.

### L1 — Execution
Execution übersetzt autorisierte Handlungen in konkrete Ausführungsversuche gegenüber Zielsystemen bzw. der Umwelt und erzeugt einen Ausführungsnachweis einschließlich Fehlern, Teilwirkungen und gegebenenfalls Rollback- oder Kompensationsinformationen.

## 5. Querschnittsebenen

**Control Plane (G):** Autorität, Governance, Policy und Safety. Es begrenzt insbesondere Entscheidungs- und Ausführungsbefugnisse und kontrolliert sicherheits- oder autoritätsrelevante Anpassungen.

**Trust Plane (T):** Identität, Authentifizierung, Integrität, Security, Provenienz, Verantwortlichkeit und Audit. Es ermöglicht die Zuordnung wesentlicher Informationen und Handlungen zu vertrauensrelevanten Nachweisen.

**Adaptation Plane (A):** Evaluation, Lernen, Optimierung und kontrollierte verhaltensändernde Updates. Verhaltensändernde Anpassungen werden versioniert; sicherheits-, autoritäts- oder policyrelevante Anpassungen unterliegen Control- und Trust-Prüfungen.

## 6. Betriebs- und Anpassungszyklen

**Betriebszyklus:** Perception → Context → Cognition → Decision → Execution → Environment → Perception.

**Anpassungszyklus:** Outcome → Evaluation → Adaptation Proposal → Control/Trust Checks → Approved Change → Versioned System State.

Eine Verarbeitungsepisode kann über **Intent** oder **Perception** beginnen. ISRM unterstützt damit zielgetriebene und ereignisgetriebene Aktivierung.

## 7. Processing Episode

Eine **Processing Episode (PE)** ist die nachvollziehbare Einheit einer Systemaktivität:

`PE = {activation, IO*, OO*, CS*, CA*, DR*, AA*, ER*, AR*, parent?, children*}`

Sie bindet Aktivierungsquelle, aktive Intents, Beobachtungen und Kontext, Kandidatenhandlungen, Entscheidungen, Ausführungsversuche und resultierende Beobachtungen. Eine PE kann Kindepisoden erzeugen oder Teil einer übergeordneten Episode sein.

## 8. Kanonische Informationsobjekte

- **Intent Object (IO):** Ziel-ID, Quelle, Zielsetzung, Randbedingungen, Priorität, Autoritätsreferenz, Gültigkeit, Unsicherheit/Ambiguität.
- **Observation Object (OO):** Quelle, Wert/Ereignis, Zeit/Ordnung, Konfidenz/Unsicherheit, Provenienz, Integrität.
- **Context State (CS):** relevante Beobachtungen, Wissensreferenzen, Gedächtnis/Zustand, zeitlicher Geltungsbereich, Annahmen, Unsicherheit.
- **Candidate Action (CA):** vorgeschlagene Wirkung, Begründungsreferenz, erwartetes Ergebnis, Vorbedingungen, Kosten/Risiko, erforderliche Autorität, Reversibilität.
- **Decision Record (DR):** ausgewählte, abgelehnte oder zurückgestellte Kandidaten, Entscheidungsgrundlage, Autorität, Policy-Prüfungen, Unsicherheit und Eskalation.
- **Authorized Action (AA):** begrenzte Operation, Ziel, Parameter, Autorisierungsreferenz, Gültigkeit sowie Idempotenz-/Transaktionssemantik.
- **Execution Record (ER):** versuchte Operation, Zeitpunkt, Ziel, Status, Teilwirkungszustand, Evidenz und Fehler/Rollback.
- **Adaptation Record (AR):** bewertetes Ergebnis, Lernsignal, vorgeschlagene/akzeptierte Änderung, Geltungsbereich, Freigabe/Policy und Versionsübergang.

## 9. Kanonische Übergänge

- **T6-5:** Intent-to-Perception/Context
- **T5-4:** Perception-to-Context
- **T4-3:** Context-to-Cognition
- **T3-2:** Cognition-to-Decision
- **T2-1:** Decision-to-Execution
- **T1-W:** Execution-to-Environment
- **TW-5:** Environment-to-Perception

## 10. Grundprinzipien

1. **P1 — Funktionale Dekomposition**
2. **P2 — Geschlossener Regel-/Rückkopplungsbetrieb**
3. **P3 — Rekursive Komposition**
4. **P4 — Ebenenübergreifende Kontrolle**
5. **P5 — Implementierungsunabhängigkeit**
6. **P6 — Explizite Systemgrenze**
7. **P7 — Optionale Realisierung**
8. **P8 — Nachvollziehbare Agency**
9. **P9 — Erhalt von Unsicherheit**
10. **P10 — Begrenzte Autorität**

## 11. Kernregeln von v1.0

- Intent ist eine funktionale Ebene, jedoch kein zwingender erster Eintrittspunkt.
- Mehrere Processing Episodes können gleichzeitig aktiv sein.
- Konfligierende Entscheidungen werden innerhalb Decision unter Vorgaben des Control Plane arbitriert. Ist keine sichere Arbitration möglich, muss das System zurückstellen, ablehnen oder eskalieren.
- Materielle Unsicherheit muss in relevanten Observation Objects, Context States, Candidate Actions und Decision Records darstellbar bleiben.
- Verhaltensändernde Adaptation muss bei C3 durch einen unterscheidbaren Versionsübergang nachvollziehbar sein.
- Autorität darf entlang von Übergängen nur erhalten oder reduziert werden, sofern kein ausdrücklich autorisiertes Ereignis zur Änderung der Autorität vorliegt.
- Eine Candidate Action wird nicht allein dadurch zu einer Authorized Action, dass Cognition sie vorgeschlagen hat.
- Ein Ausführungsergebnis muss von angenommenem Erfolg unterscheidbar bleiben, wenn keine Bestätigung vorliegt.
- Bei konkurrierenden Wirkungen sollte Execution geeignete Idempotenz-, Locking-, Transaktions- oder Kompensationssemantik bereitstellen.

## 12. Rekursive Komposition und Delegation

Jedes ISRM-System kann Teil der Umwelt eines anderen Systems und gleichzeitig selbst vollständiges ISRM-System sein. Eine Ausführung oder Nachricht von System A kann in System B zur Wahrnehmung werden und dort Intent erzeugen oder verfeinern.

Die Autorität von System B darf die von System A delegierte Autorität nicht überschreiten, sofern B nicht über eine davon unabhängige, ausdrücklich autorisierte Befugnis verfügt.

## 13. Fehlerklassen

- **Intent:** Ambiguität, Konflikt, Unerfüllbarkeit, fehlende Autorisierung, Goal Drift.
- **Perception:** Verlust, Korruption, Spoofing, Fehlklassifikation, Synchronisationsfehler.
- **Context:** veralteter Zustand, Auslassung, Poisoning, falsches Gedächtnis, Scope Leakage.
- **Cognition:** ungültige Schlussfolgerung, halluzinierte Fähigkeit, Nichtterminierung, fehlerhaftes Kausalmodell.
- **Decision:** unsichere Wahl, Policy-Verstoß, Autoritätsausweitung, unterlassene Zurückstellung.
- **Execution:** Teilwirkung, Duplikat, Timeout, falsches Ziel, Rollback-Fehler, unbekannter Ausführungszustand.
- **Control:** fehlende Autorisierung, Policy-Konflikt, unsichere Freigabe, unbegrenzte Delegation.
- **Trust:** Identitäts-/Provenienzfehler, Manipulation, Audit-Lücken, Geheimnisoffenlegung.
- **Adaptation:** Drift, unsicheres Lernen, nicht freigegebene Änderung, Regression.
- **Boundary:** unbeobachtete Wirkung, angenommener Erfolg, Umwelt-Mismatch.

## 14. Konformitätsklassen

- **C0 — Mappable:** System und Systemgrenze lassen sich auf die ISRM-Verantwortlichkeiten abbilden.
- **C1 — Traceable:** C0 plus Rekonstruktion wesentlicher IO/OO/CS/DR/AA/ER für deklarierte folgenreiche Handlungen.
- **C2 — Controlled:** C1 plus explizite Autoritäts-/Policy-Prüfungen, begrenzte Ausführung, Fehlerbehandlung und Eskalation.
- **C3 — Adaptive-Controlled:** C2 plus evaluierte, versionierte, auditierbare und durch Control/Trust begrenzte verhaltensändernde Anpassungen.

Eine Konformitätsaussage sollte System und Grenze, beanspruchte Klasse, anwendbare, zusammengeführte, verteilte oder nicht vorhandene Verantwortlichkeiten, die Menge folgenreicher Handlungen, relevante Plane-Mechanismen und bekannte Einschränkungen benennen.

## 15. Nicht-Ziele

ISRM:
- definiert weder Bewusstsein noch Sentienz oder AGI;
- bewertet keine Systeme nach einem Intelligenzgrad;
- schreibt keine konkrete KI-, Software-, Hardware- oder Kommunikationsarchitektur vor;
- ersetzt weder OSI/TCP-IP noch Safety-, Security-, Datenschutz-, Rechts- oder Domänenstandards;
- definiert in v1.0 kein universelles Wire Protocol und keine universelle Ethik;
- verlangt nicht, dass funktionale Ebenen als getrennte Softwarekomponenten realisiert werden.

## 16. Validierungsstatus

Die interne v1.0-Prüfung umfasste drei Referenzimplementierungen: einen deterministischen Controller, einen Tool-nutzenden Software-Agenten und ein rekursives Multi-Agenten-System.

- **69 / 69** anwendbare Referenzimplementierungs-Testausführungen: PASS
- **60 / 60** Edge-Case-Testausführungen: PASS
- **50.000 Zufallsiterationen je getesteter Invariantenfamilie:** keine beobachtete Verletzung

Die Ergebnisse stützen die interne Konsistenz und Implementierbarkeit der getesteten Modellteile. Sie sind **keine unabhängige Zertifizierung** und beweisen weder Vollständigkeit, Neuheit, Safety, Security, Rechtskonformität noch Eignung als nationale oder internationale Norm.

## 17. Vorarbeiten und Positionierung

ISRM beansprucht **nicht** die Erfindung von Feedback-Regelung, Wahrnehmungs-Handlungs-Schleifen, kognitiven Architekturen, Delegation, Schichtenarchitekturen, Governance, Provenienz oder Lernen.

Zu relevanten Vorarbeiten und Vergleichspunkten gehören insbesondere Sense–Plan–Act, OODA, BDI, MAPE-K, NIST RCS/4D-RCS sowie bestehende Standards und Frameworks zu KI-Terminologie, Lifecycle, Governance und Risikomanagement.

Der vorgeschlagene Beitrag von ISRM liegt in der integrierten Referenzstruktur aus sechs funktionalen Verantwortlichkeiten, expliziter externer Umweltgrenze, drei Querschnittsebenen, rekursiver Komposition, Processing Episodes, kanonischen Informationsobjekten, autoritätserhaltenden Übergängen und Konformitätsklassen.

## 18. Standardisierungsstatus

ISRM v1.0 ist ein **offenes Pre-Standard-Referenzmodell** und keine DIN-, EN-, ISO/IEC- oder IEEE-Norm. Eine mögliche zukünftige Norm würde durch das jeweilige konsensbasierte Standardisierungsverfahren entwickelt und könnte von ISRM v1.0 abweichen.

## 19. Zitierung

Bitte die kanonische Veröffentlichung zitieren:

```text
Reitz, Marcel (2026).
ISRM v1.0 — Intelligent Systems Reference Model:
A Technology-Neutral Reference Model for Intelligent and Goal-Directed Systems.
Zenodo. https://doi.org/10.5281/zenodo.23115842
```

**Bevorzugte Herkunftsangabe:**  
Originator: Marcel Reitz — Altenbuch, Deutschland. Initiale Entwicklung: 2026.

---

**ISRM v1.0 · Offizielle deutsche Übersetzung · DOI 10.5281/zenodo.23115842 · Marcel Reitz · 2026**
