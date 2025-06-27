# M.A.S.K.

## Machine-Learning Assisted Skeleton Kinect Tracking

**Author:** Marty Lauterbach
**Project:** MKI-Projekt SoSe 2025
**Institution:** Reutlingen University in cooperation with Filmakademie Baden-Württemberg

![FAWB Logo](_documentation/images/FAWB.svg)

*Complete documentation automatically generated from LaTeX sources*

## Table of Contents

- [Projektvision und Ergebnisse](#projektvision-und-ergebnisse)
- [Projektkontext und Kooperation](#projektkontext-und-kooperation)
- [Machbarkeitsstudie](#machbarkeitsstudie)
- [Anforderungen und Designentscheidungen](#anforderungen-und-designentscheidungen)
- [Entwicklungsweg](#entwicklungsweg)
- [Systemarchitektur und Innovation](#systemarchitektur-und-innovation)
- [Produktionsnachweis](#produktionsnachweis)
- [Zentrale Erkenntnisse](#zentrale-erkenntnisse)
- [Fazit und Beiträge](#fazit-und-beiträge)
- [Vollständiges Code-Repository](#vollständiges-code-repository)
- [Team und Kommunikation](#team-und-kommunikation)
- [Danksagung](#danksagung)

## Projektvision und Ergebnisse

subsection*Dokumentationsstruktur
Diese Dokumentation folgt einem chronologisch-logischen Aufbau, der den Leser vom **großen Bild zum Detail** führt:
- **Projektüberblick:** Vision, Kooperationskontext und Machbarkeitsstudie
- **Technische Umsetzung:** Anforderungen, Entwicklungsweg und finale Systemarchitektur  
- **Praxisvalidierung:** Produktionsnachweis in der realen Filmproduktion
- **Erkenntnisse:** Zentrale Learnings und Projektbeiträge
- **Technische Dokumentation:** Code-Repository und Teamkommunikation
subsection*Projektvision
M.A.S.K. (Machine-Learning Assisted Skeleton Kinect Tracking) entstand aus einer interdisziplinären Kooperation zwischen der Filmakademie Baden-Württemberg und der Hochschule Reutlingen. Das Projekt entwickelte ein kostengünstiges, robustes Motion-Capture-System für die cinematographische Tanzproduktion *Echoes of the Mind*.
Die zentrale Herausforderung bestand in der Entwicklung eines Tracking-Systems, das unter intensiver Beamerbeleuchtung und bei komplexen Bewegungssequenzen zuverlässig funktioniert. Herkömmliche RGB-basierte Tracking-Verfahren zeigen unter diesen Produktionsbedingungen reduzierte Genauigkeit. Zur Lösung wurde eine spezifische Adaptation entwickelt, die Consumer-Hardware und Open-Source-Software kombiniert.
Die Entwicklung durchlief mehrere iterative Phasen: Ein ursprünglich geplanter Dual-Source-Ansatz wurde zugunsten einer vereinfachten MediaPipe-basierten Lösung modifiziert. Die finale Infrarot-Adaptation entstand aus spezifischen Produktionsanforderungen und bewährte sich unter realen Studiobedingungen.
Das resultierende System basiert auf einer modularen Architektur mit TouchDesigner-Containern, die flexible Integration in bestehende Produktions-Workflows ermöglichen. Die Implementation verarbeitet Kamera-Streams in Echtzeit, extrahiert Skelettdaten über MediaPipe und stellt strukturierte Koordinaten für Visualisierungssysteme bereit. Spezialisierte Python-Skripte ermöglichen die direkte Integration in TouchDesigner für ParticleGPU-Effekte, Zustandsmaschinen und Trigger-Logiken.
Das M.A.S.K.-System wurde erfolgreich in einer professionellen Filmproduktion validiert und demonstriert die Wirksamkeit kostengünstiger Motion-Capture-Lösungen für spezialisierte Anwendungen. Die modulare Systemarchitektur ermöglicht Reproduzierbarkeit und Erweiterung für ähnliche interdisziplinäre Projekte.
Hervorgebracht wurden zusätzlich Schwierigkeiten bei der Verarbeitung von teilweise verdeckten Performern. Wenn die grundlegenden RGB-Daten nicht ausreichend schlüssig für das MediaPipe-Modell waren, folgte das System einen GIGO-Prinzip: Garbage In, Garbage Out. Das System konnte dann keine sinnvollen Skelettdaten mehr extrahieren. Die finale Infrarot-Adaptation ermöglichte es, in Momenten wo der Beamer auf dem Tänzer ein Problem war, auch bei partieller Sichtbarkeit präzisere Tracking-Daten zu generieren.
Die Entwicklung verdeutlicht das Potenzial interdisziplinärer Kooperationen zwischen technischen Hochschulen und Kunsthochschulen für praxisorientierte Lösungsansätze in der Creative Technology.
**Open Source:** raggedright Der vollständige Quellcode, inklusive TouchDesigner-Projekten und Python-Skripten, sowie dem LaTex dieser Dokumentation, ist verfügbar unter:
`https://github.com/mklemmingen/MASK`
**Behind-The-Scenes Video:** Visualisierungen, Debug-Overlays und Setup der Infrarot-Pipeline unter:
urlhttps://youtu.be/2jvziSgExTw

---

## Projektkontext und Kooperation

## Interdisziplinäre Hochschul-Kooperation

Mitte Januar 2025 entwickelte sich eine Kooperation zwischen der Filmakademie Baden-Württemberg Ludwigsburg und der Hochschule Reutlingen. Als einziger Entwickler der Hochschule Reutlingen übernahm ich die vollständige technische Entwicklungsverantwortung für ein Motion-Capture-System, das in Kooperation mit den Designerinnen Maja Litzke und Rahel Fundinger der Filmakademie realisiert werden sollte.
Diese Konstellation bot die seltene Gelegenheit, als Solo-Entwickler ein komplettes System von der Konzeption bis zur Produktionsreife zu entwickeln, während gleichzeitig intensive interdisziplinäre Zusammenarbeit zwischen technischer Entwicklung und künstlerischer Vision stattfand.

## Das Kernprojekt Echoes of the Mind

Das Kernprojekt Echoes of the Mind ist eine cinematographische Umsetzung eines interpretativen Tanzes, der komplexe emotionale Zustände wie Overthinking und Anxiety durch dynamische, responsive Visualisierungen darstellt. Diese werden mittels Beamer-Projektion direkt auf und um den Performer projiziert, wodurch eine immersive Symbiose zwischen Tanz und digitaler Kunst entsteht.
}

![Echoesofthemind Startbild](_documentation/images/docupictures/EchoesOfTheMind_startbild.png)

*MoodBoard-Startbild des Projektes glqq Echoes of the Mindgrqq*
**Künstlerische Vision:**
raggedright Das Projekt visualisiert innere emotionale Prozesse durch externe Projektionen, die direkt auf die Körperbewegungen des Performers reagieren. Die Choreographie thematisiert mentale Überlastung und Angstzustände, wobei die technischen Visualisierungen diese psychischen Zustände räumlich und zeitlich erfahrbar machen.
}

![Echoesofthemind Mood](_documentation/images/docupictures/EchoesOfTheMind_mood.png)

*Künstlerische Vision: Emotionale Visualisierungskonzepte für glqq Echoes of the Mindgrqq*

## Technische Anforderungsanalyse

Der beschriebene Projektkontext definiert spezifische technische Anforderungen für das Motion-Capture-System: variable Beleuchtungsbedingungen durch Beamer-Projektionen, schnelle und komplexe Bewegungssequenzen sowie potenzielle Teilverdeckungen des Performers während der Choreographie.
**Spezifische Herausforderungen des Projekts:**
- **Echtzeit-Responsivität:** raggedright Visualisierungen müssen unmittelbar auf Bewegungsänderungen reagieren, ohne wahrnehmbare Verzögerung
- **Präzise Körper-Mapping:** raggedright Projektionen sollen exakt auf spezifische Körperregionen (Kopf, Hände, Torso) ausgerichtet werden: Auch bei **Partieller Sichtbarkeit:** Tänzer verdecken oft Körperteile - Standard-Kinect verliert dann das Skelett
- **Beleuchtungskompatibilität:** raggedright Das System muss unter intensiver Beamer-Beleuchtung funktionieren, sowie unter geringer Lichtverfügbarkeit.
- **Multiple Kamerawinkel:** Verschiedene Szenen erfordern Top-Down-, Front- und Seitenperspektiven
- **Schnelle Setup-Wechsel:** Mehrere Visualisierungsmodi müssen innerhalb der Produktionszeit umschaltbar sein
**Produktionskontext:**
raggedright Die Filmproduktion war für Mai 2025 im professionellen Albrecht-Ade-Studio der Filmakademie Ludwigsburg geplant. Dies definierte einen festen Zeitrahmen von vier Monaten für Entwicklung, Testing und Produktionsreife des M.A.S.K.-Systems.

## Professionelle Arbeitsteilung

**Kreative Führung - Filmakademie Ludwigsburg:**
- **Maja Litzke \& Rahel Fundinger:** Künstlerische Vision und Choreographie-Entwicklung
- **Productions-\infrastruktur:** Bereitstellung von professionellem Studio, Beamer-Equipment und Kamera-Hardware
- **Visual Design:** Definition ästhetischer Anforderungen und emotionaler Zielstellungen
- **Workflow-Integration:** Einbindung in bestehende TouchDesigner-Produktionspipelines
**Technische Vollverantwortung - Hochschule Reutlingen:**
- **Marty Lauterbach (Solo-Developer):** Eigenständige Entwicklung der kompletten Motion-Capture-Pipeline
- **System-\Architektur:** Design und Implementation der MediaPipe-TouchDesigner-\Integration
- **Entwicklung:** Infrarot-basierte Tracking-Lösung unter Produktionsbedingungen
- **Performance-Engineering:** Optimierung für Real-time-Anforderungen und Produktionsumgebung

## Kooperationsmanagement

Da sich bei diesem Projekt zwei Hochschulen zu einem interdisziplinären Team zusammenfanden, wurde gemeinsam ein agiler Entwicklungsansatz gewählt. In regelmäßigen Sprint-Meetings definierten die Filmakademie-Partner die künstlerischen und choreographischen Anforderungen, während ich die technischen Möglichkeiten und Limitierungen kommunizierte. Diese bidirektionale Abstimmung ermöglichte sowohl technische Optimierungen als auch kreative Anpassungen basierend auf den jeweiligen Fachkompetenzen.
**Kommunikationsstruktur:**
raggedright Regelmäßige Online-Kommunikation ermöglichte kontinuierliche Abstimmung zwischen den Standorten Reutlingen und Ludwigsburg. Zusätzlich fanden vier Online-Meetings statt, um komplexe technische und künstlerische Entscheidungen gemeinsam zu treffen.
**Iterative Anforderungsentwicklung:**
raggedright Die Anforderungen entwickelten sich iterativ basierend auf choreographischen Erkenntnissen und technischen Möglichkeiten. Dies erforderte flexible Systemarchitektur und agile Entwicklungsmethoden, um auf Änderungen reagieren zu können.

## M.A.S.K. als technisches Backbone

M.A.S.K. wurde als technisches Backbone entwickelt, um die künstlerische Vision zu realisieren. Das System musste spezifische Voraussetzungen erfüllen, damit die kreativen Visualisierungen den gewünschten künstlerischen Effekt erzielen können. Durch präzises Skelett-Tracking mittels Kinect V2 und MediaPipe reagieren die projizierten Visualisierungen in Echtzeit auf Bewegungen, Position und emotionale Ausdruckskraft des Performers.
**Systemintegration:**
raggedright Das entwickelte System musste sich gut in bestehende TouchDesigner-Workflows der Filmakademie integrieren, ohne bestehende Produktionsprozesse zu unterbrechen. Dies erforderte modulare Architektur und standardisierte Schnittstellen.
**Evaluierungsmetriken:**
Der Projekterfolg wurde anhand folgender Kriterien gemessen:
- Zuverlässige Tracking-Performance während der gesamten Produktionszeit
- Kurze Setup-Zeiten pro Visualisierungsmodus
- Nahtlose Integration in den Filmproduktions-Workflow
- Künstlerische Zufriedenheit mit der Responsivität der Visualisierungen

---

## Machbarkeitsstudie

Einschätzung der Machbarkeit des M.A.S.K.-Projekts (Stand: März 2025) unter Anwendung des TELOS-Frameworks nach Hall (2013)footnoteHall, J.A. *Accounting Information Systems, 8th Edition*. Brooks/Cole, 2013..

## Technologisch

**Technische Realisierbarkeit:**
raggedright Das Projekt ist technisch umsetzbar. Die Kernkomponenten TouchDesigner, MediaPipe und Kinect V2 sind etablierte Technologien mit dokumentierter Kompatibilität. Studien wie Babouras et al. (2024)footnoteBabouras, A., Abdelnour, P., Fevens, T. et al. "Comparing novel smartphone pose estimation frameworks with the Kinect V2 for knee tracking during athletic stress tests." *International Journal of Computer Assisted Radiology and Surgery* 19, 1321–1328 (2024). bestätigen die Zuverlässigkeit der Kinect V2-MediaPipe-Kombination für bewegungsbasierte Anwendungen.
**Technologie-Zugang:**
raggedright Das interdisziplinäre Team verfügt über die erforderliche Hardware (Kinect V2) und nutzt TouchDesigner 2023.11 in der kostenlosen Bildungsversion. Die Filmakademie Ludwigsburg stellt zusätzliche Studioinfrastruktur bereit.
**Stakeholder-Akzeptanz:**
raggedright Die Technologiewahl wurde gemeinsam mit der Filmakademie getroffen, wodurch hohe Akzeptanz und aktive Unterstützung gewährleistet sind.

## Economic

**Finanzierung:**
raggedright Das Projekt wird im Rahmen des regulären Studiums durchgeführt, ohne externe Finanzierung. Die einzigen Kosten entstehen durch die Kinect V2-Hardware (ca. 90€), die privat beschafft wurde. TouchDesigner und MediaPipe sind kostenfrei verfügbar.

## Legal

**Lizenzrechtliche Aspekte:**
- MediaPipe: Apache License 2.0footnote{urlhttps://github.com/google-ai-edge/mediapipe/blob/master/LICENSE}
- Kinect V2 (libfreenect2): Open-Source-Lizenzfootnote{urlhttps://zenodo.org/records/50641}
- TouchDesigner: Nicht-kommerzielle Bildungslizenzfootnote{urlhttps://derivative.ca/UserGuide/Licensing}
Alle verwendeten Technologien sind für nicht-kommerzielle Bildungsprojekte frei nutzbar.

## Operational

**Implementierungsanforderungen:**
- Entwicklung einer synchronisierten Datenfusion zwischen Kinect V2 und MediaPipe
- Implementation regelbasierter Trigger für Visualisierungssteuerung
- Integration in die bestehende TouchDesigner-Pipeline der Filmakademie
- Koordination zwischen beiden Standorten (Reutlingen/Ludwigsburg)
**Projektmanagement:**
raggedright Regelmäßige Online-Meetings und punktuelle Präsenztreffen ermöglichen effektive Zusammenarbeit zwischen den Projektteams.

## Scheduling

**Zeitplanung:**
- **Projektlaufzeit:** Januar bis Mai 2025
- **Prototyp-Ziel:** Mitte April 2025
- **Finaler Einsatz:** Filmproduktion Mai 2025
- **Ressourcenallokation:** 2 feste Projekttage pro Woche
**Risikomanagement:**
raggedright Der modulare Entwicklungsansatz ermöglicht eine stufenweise Implementierung und reduziert das Risiko von Zeitüberschreitungen. Parallele Studienverpflichtungen wurden durch Workload-Anpassungen in anderen Modulen kompensiert.

---

## Anforderungen und Designentscheidungen

## Änderungsverlauf

### Technische Infrastruktur der Filmakademie

- **Hardware:** NVIDIA RTX 3080, AMD Ryzen 9750
- **Software:** TouchDesigner 2023.11
- **Tracking:** Kinect V2 mit RGB- und Tiefensensor
- **Studiodimensionen:** 383 m² (21m × 15m)
}

![Mediapipenodes](_documentation/images/docupictures/mediapipeNODES.png)

*MediaPipe Skeleton-Nodes, die die Basis für die Skelett-Visualisierung bilden*

## Funktionale Anforderungen

**Kern-Tracking-Funktionalität:**
- **FA-01:** Einfachpersonen-Erkennung und -Verfolgung im Kinect-Sichtfeld
- **FA-02:** Echtzeit-Verarbeitung der Positionsdaten für regelbasierte Trigger
- **FA-05:** Native TouchDesigner-Integration für Visualisierungssteuerung
- **FA-06:** Modulare Systemarchitektur für iterative Optimierung
**Performance-spezifische Anforderungen:**
- **FA-07:** Boolean-Node-Triggering/Switch-Triggers und Python-basierte Eigenschaftsmanipulation
- **FA-08:** Personen-Eintrittserkennung mit automatischer Aktivierung
- **FA-09:** Selektives Single-Person-\Tracking (Kameramann-Ausblendung)
**Projections-Mapping-Funktionalität:**
- **FA-11:** Beamer-Kinect-Kalibrierung für präzise Performer-Ausblendung/Hervorhebung
- **FA-14:** Relative 2D-Positionierung der Visuals zum Performer
**Choreographie-spezifische Visualisierungslogik:**
- **FA-16:** Extremitäten-responsive Blitzeffekte mit radialer Positionierung
- **FA-17:** Hockbewegung-getriggerte Umrandungseffekte bei kreisförmigen Visuals

---

## Entwicklungsweg

Die Entwicklung des M.A.S.K.-Systems durchlief eine fundamentale Transformation – von einem komplexen Dual-Source-Ansatz hin zu einer eleganten Single-Pipeline-Lösung. Diese Evolution demonstriert, wie praktische Produktionsanforderungen zu effektiven technischen Lösungen führen können.

## Phase 1: Initiale Systemkomplexität (Januar - Februar 2025)

**Hybrid-Tracking-Architektur:**
Basierend auf Expertenberatung entwickelte ich zunächst ein komplexes Dual-Source-System:
}

![Mask](_documentation/images/docupictures/MASK.png)

*Anfängliches Systemdesin von M.A.S.K. mit Analyse- und Triggerprozess und dem später nach Sprint 2 deprecated Dual-Source-Ansatz*
- **MediaPipe-Integration:** ML-basierte Pose-Detection über RGB-Stream
- **Native Kinect-Tracking:** Hardware-Skeleton mit Tiefensensor-Daten
- **Kalman-Filter-Fusion:** Synchronisation und Glättung beider Datenquellen
- **Adaptive Fallback-Logik:** Automatische Umschaltung bei Tracking-Verlust
beginalgorithm[H] *Ursprüngliche Dual-Source-Verarbeitungsschleife* beginalgorithmic[1] State $textkinect\_data leftarrow textreceiveKinectSkeleton()$ State $textmediapipe\_data leftarrow textprocessRGBStream()$ If$textmediapipe\_data neq textnull land textkinect\_data neq textnull$ State $textskeleton leftarrow textfusionProcess(textkinect\_data, textmediapipe\_data)$ Else State $textskeleton leftarrow textfallbackToStrongerSource()$ EndIf State $textskeleton leftarrow textapplyKalmanFilter(textskeleton)$ State **evaluateTriggers**(textskeleton) endalgorithmic endalgorithm
**Erste Validierung:**
raggedright Komparative Tests zwischen MediaPipe und Kinect zeigten MediaPipes bessere Robustheit bei partieller Okklusion. Das ML-Modell generierte höhere Confidence-Werte für nicht-sichtbare Körperregionen, was für komplexe Choreographien entscheidend war.
}

![Kinect Nodes](_documentation/images/docupictures/kinect_nodes.png)

*Kinect V2 Skeleton-Visualisierung mit Node-Nummerierung | Vor Sprint 2 mit MediaPipe Nodes gemischt mit Mapping, später deprecated*
}

![Kinectmediapipe Testing](_documentation/images/docupictures/KinectMediaPipe_Testing.png)

*TouchDesigner Testing-Interface: Unterschied zwischen der Mediapipe Skeleton-Visualisierung (oben, pink) und der Kinect V2 Skeleton-Visualisierung (unten, grün)*

## Phase 2: Visual Requirements Engineering (März 2025)

**Stakeholder-Driven\Design:**
raggedright Die intensive Zusammenarbeit mit den Filmakademie-Designerinnen führte zu präzisen Visual-Anforderungen, die über einfache Bewegungstrigger hinausgingen:
- **Adaptive Größenmodulation:** Visuals skalieren basierend auf Performer-Zustand
- **Räumliche Choreographie:** Präzise Beamer-Projektion um Performer herum
- **Emotionale Responsivität:** Visual-Transformation entsprechend choreographischer Intentionen
**Konzeptuelle Visualisierungsansätze:**
}

![Sprint3 1](_documentation/images/docupictures/Sprint3_1.jpg)

*Erstes künsterlisches Konzept der Blobs: Blobs sind magnetisch anziehend/abstoßend zum Künstler*
}

![Sprint3 2](_documentation/images/docupictures/Sprint3_2.jpg)

*Künsterlisches Konzept, das übernommen wurde: Je nach Position des Performers werden die Blobs krisselig/blitzig oder ruhig dargestellt)*
}

![Sprint3 3](_documentation/images/docupictures/Sprint3_3.jpg)

*Künsterlisches Konzept, das deprecated wurde, nachdem meine Shader-Solution nicht geklappt hatte: Magnetische Interaktion: Dynamische Visual-Performer-Relation*
}

![Sprint3 4](_documentation/images/docupictures/Sprint3_4.jpg)

*Künsterlisches Konzept, das übernommen wurde: der Performer ist in einem hellen Kreis, und bewegt sich*
}

![Sprint3 5](_documentation/images/docupictures/Sprint3_5.jpg)

*Künsterlisches Konzept, das übernommen wurde: der Performer ist in einem hellen Kreis, und die Visuals brechen interaktiv mit seinen Extremitäten-Koordinaten passend aus*
**Technische Herausforderungen:**
raggedright Diese künstlerischen Anforderungen stellten das ursprüngliche System vor erhebliche Performance-Probleme. Die Dual-Source-Architektur erwies sich als zu ressourcenintensiv für komplexe Real-time-Visuals.

## Phase 3: Architektonische Vereinfachung (April 2025)

**Strategische Entscheidung:**
raggedright Angesichts der Performance-Limitationen entschied ich mich für eine radikale Vereinfachung: Vollständige Fokussierung auf MediaPipe als primäres Tracking-System.
**Systemvereinfachung:**
- **Kinect-Elimination:** Entfernung der nativen Kinect-SDK-Abhängigkeiten
- **MediaPipe-Optimierung:** Direkter RGB-zu-Pose-Pipeline ohne Datenfusion
- **Modulare Architektur:** Plug-and-Play TouchDesigner-Container
- **Performance-Boost:** CPU-Nutzung reduziert
**Unerwartete Erkenntnisse:**
raggedright Die Vereinfachung führte nicht nur zu besserer Performance, sondern auch zu erhöhter Systemstabilität und einfacherer Wartung – ein klassisches Beispiel für "weniger ist mehr" in der Systemarchitektur.

## Phase 4: Produktionsvalidierung und Lösungsfindung (Mai 2025)

**Beleuchtungsproblem:**
raggedright Bei den ersten Produktionstests stellte sich heraus, dass intensive Beamer-Projektionen die RGB-Kameras überlasten und MediaPipe funktionsunfähig machen. Ein fundamentales Problem für Live-Performance-Anwendungen.
**Praxisorientierte Lösung - Infrarot-Pipeline:**
raggedright Unter Produktionsdruck entwickelte ich eine spezifische Adaptation: Routing des Kinect-Infrarot-Streams (512×424 Pixel, 16-bit) über OBS Virtual Camera direkt zu MediaPipe.
**Technische Spezifikationen der finalen Lösung:**
- **Input:** Kinect V2 Infrarot-Stream (512×424@30fps)
- **Processing:** OBS Virtual Camera → MediaPipe Pose Detection
- **Output:** TouchDesigner-kompatible Koordinaten-CHOPs

## Phase 5: Spezialisierte Visual-Systeme

**Drei finale Implementierungen:**
raggedright *1. Hand-Feuer-Effekte:* ParticleGPU-basierte blaue Flammenpartikel, die Handbewegungen in Echtzeit folgen. Implementation extrahiert Hand-Landmarks (MediaPipe Nodes 15/16) und transformiert diese in normalisierte Bildschirmkoordinaten. Dafür werden per Script die Hand-Node-Positionen in TouchDesigner als Partikel-Emitter genutzt. Die Partikel haben eine Lebenszeit von 1,2 Sekunden und werden basierend auf der Handgeschwindigkeit emittiert.
*2. Adaptive Kopfpartikel:*
Zustandsbasiertes System mit Hand-zu-Schulter-Positionsvergleich. Eine Interpolationsfunktion sorgt für sanfte Übergänge zwischen zwei visuellen Modi.
Die Visuals folgen der Kopf-Node über Setzung des particleGPU offsets von der Mitte des Bildschirms per Script-Mapping.
*3. 64-Spike Radialsystem:*
Hochpräzise Winkelauflösung (5,625°) für Extremitätenerkennung. Polar-Koordinaten-Mapping ermöglicht exakte Richtungstrigger basierend auf Körperhaltung.
Per Skript werden die Hand- und Fußpositionen relativ zum Bildschirmzentrum in Polarkoordinaten umgerechnet. Der atan2-Algorithmus mappt Winkel auf diskrete Spike-Indizes (0-63),
und wird anschließend auf RAMP positionen gemappt, und per connect- disconnect logic anhand der Distanz der Nodes zur Mitte zum Comp verbunden.

## Technische Bilanz

**Entwicklungsevolution im Überblick:**
**Lessons Learned:**
- **Constraints fördern Lösungsansätze:** Die Beleuchtungsbeschränkung führte zur infrarot-basierten Adaptation
- **Systemvereinfachung verbessert Robustheit:** MediaPipe-only erwies sich als stabiler als Dual-Source-Ansatz
- **Produktionsvalidierung ist entscheidend:** Reale Umgebungsbedingungen deckten wichtige Designanpassungen auf
- **Interdisziplinarität steigert Qualität:** Zusammenarbeit mit Designerinnen optimierte sowohl technische als auch künstlerische Aspekte
Die Entwicklung von M.A.S.K. demonstriert, wie iterative Vereinfachung und praxisorientierte Problemlösung zu eleganten, produktionstauglichen Lösungen führen können. Das finale System ist nicht nur technisch ausgereift, sondern auch konzeptuell klarer und wartungsfreundlicher als die ursprüngliche komplexe Architektur.

---

## Systemarchitektur und Innovation

## Finale Systemarchitektur

M.A.S.K. implementiert die drei bereits benannten spezialisierte Visualisierungssysteme über eine gemeinsame (Optional Infrarot-)Tracking-Pipeline. Die modulare Architektur ermöglicht eigenständige Komponenten mit standardisierten Schnittstellen – ein entscheidender Faktor für die erfolgreiche Produktionsintegration.
}

![Finished Mediapipecontainer Miterklärungen](_documentation/images/docupictures/Finished_MediaPipeContainer_mitErklärungen.png)

*M.A.S.K. MediaPipe-Container: Alle modules des Containers mit Erklärungen (farblich markiert)*

### Praxisorientierte Lösung: Infrarot-MediaPipe-Pipeline

Die zentrale technische Lösung besteht in der Weiterleitung des Kinect V2 Infrarot-Streams über OBS Virtual Camera an MediaPipe. Diese spezifische Adaptation für Produktionsanforderungen reduziert deutlich die Beleuchtungsinterferenzen durch Beamer-Projektionen, die RGB-basierte Systeme beeinträchtigen können.
}

![Infraredobscameratomediapipefortopdowncirlcegrademapping](_documentation/images/docupictures/InfraRedOBSCameraToMediaPipeForTopDownCirlceGradeMapping.png)

*Infrarot-Pipeline im Test zuhause: Kinect V2 IR-Stream über OBS Virtual Camera zu MediaPipe für störungsfreies Top-Down-Tracking*
**Pipeline-Architektur im Detail:**
- **Kinect IR-Capture:** 16-bit Tiefendaten werden als Graustufenbild interpretiert
- **OBS-Konversion:** Bit-Shift von 16-bit auf 8-bit für Kompatibilität
- **Virtual Camera Bridge:** Simuliert Webcam-Input für MediaPipe
- **MediaPipe Processing:** Pose-Detection auf IR-Bildern statt RGB
- **TouchDesigner Integration:** Python-Scripts parsen MediaPipe-Output zu CHOP-Daten
**MediaPipe Debug-Visualisierung (PY\_MediaPipeDebugCirclesForCompTops.py):**
- **Pixel-Koordinaten-Berechnung:** 
- `x\_px = x\_norm * width - width/2`
- `y\_px = -(y\_norm * height - height/2)` (Y-Achse invertiert)
- **Transform-TOP-Kontrolle:** Dynamische Positionierung von Debug-Kreisen
- **Resolution-Mapping:** Automatische Anpassung an Ausgabe-Auflösung
- **Toggle-Control:** debugValue-CHOP für Ein/Ausblenden der Visualisierung
**Technische Spezifikationen:**
- **Input:** Kinect V2 IR-Stream mit hochauflösender Tiefenauflösung
- **Processing:** Real-time Grayscale-Konversion über OBS Virtual Camera
- **Detection:** MediaPipe Pose-Model optimiert für Infrarot-Input
- **Output:** TouchDesigner-kompatible CHOP-Koordinaten für drei Visual-Systeme
- **Latenz:** Niedrige End-to-End-Latenz unter Produktionsbedingungen

## MediaPipe-Container: Detaillierte technische Implementierung

**Interne Container-Architektur:**
raggedright Der MediaPipe-Container fungiert als zentrale Tracking-Konversionseinheit zwischen dem MediaPipe-Pose-Detection-System und TouchDesigners nativen CHOP-Datenstrukturen. Die interne Architektur folgt einem modularen Design mit klar definierten Verarbeitungsschichten.
**Container-Komponenten im Detail:**
- **MediaPipe Interface Layer:** Direkter Zugriff auf MediaPipe-Pose-Detection-API
- **Data Normalization Unit:** Konvertierung von MediaPipe-Landmarks zu normalisierten Koordinaten [0,1]
- **Coordinate System Adapter:** Transformation zwischen verschiedenen Koordinatensystemen (Camera, Screen, World)
- **CHOP Output Generator:** Erzeugung TouchDesigner-kompatibler Channel-Operator-Datenstrukturen
}

![Finished Mediapipecontainer](_documentation/images/docupictures/Finished_MediaPipeContainer.png)

*Vollständiger MediaPipe-Integration-Container ohne Erklärungen: Modulare Node-Netzwerk-Architektur für Skelett-Tracking-Datenverarbeitung*
**Container-Zustandsmanagement:**
- **Initialization State:** MediaPipe-Model-Loading und Camera-Input-Validation
- **Active Tracking State:** Kontinuierliche Pose-Detection mit Confidence-Monitoring
**Datenverarbeitungs-Pipeline im Detail:**
raggedright Die interne Datenverarbeitung erfolgt in einem mehrstufigen Pipeline-System mit präzise definierten Transformationsschritten:
**Stufe 1: MediaPipe Raw Data Extraction**
- `camera\_input ← OBS\_Virtual\_Camera.getFrame()`
- `pose\_results ← MediaPipe.process(camera\_input)`
- `landmarks ← pose\_results.pose\_landmarks`
**Stufe 2: Coordinate Normalization \& Validation**
- **Landmark-Extraktion:** raggedright 33 MediaPipe-Körperpunkte mit x,y,z,visibility-Werten, mit zusäzlicher SpineBase-Approximation
- **Confidence-Filtering:** raggedright Schwellenwert-basierte Validierung (Standard: visibility > 0.5 per MediaPipe Container Parameter)
- **Optionale Koordinaten-Normalisierung (wird auch per Python Skript außerhalb gemacht:** Umwandlung zu [0,1]-Bereich für TouchDesigner-Kompatibilität
**Stufe 3: TouchDesigner CHOP Integration**
- **Channel-Mapping:** Jeder Landmark wird zu spezifischen CHOP-Kanälen (x, y, z, confidence)
- **Real-time Update:** Frame-synchrone Aktualisierung aller CHOP-Outputs
- **Data Smoothing:** Optional: Kalman-Filter-Integration für Motion-Smoothing
**Schnittstellen-Dokumentation:**
**Input-Interfaces:**
- **Camera Input:** OBS Virtual Camera (Grayscale, Echtzeit)
- **Configuration Parameters:** 
- `model\_complexity`: MediaPipe-Model-Precision (0=Light, 1=Full, 2=Heavy)
- `min\_detection\_confidence`: Minimum-Confidence für Pose-Detection (Standard: 0.5)
- `min\_tracking\_confidence`: Minimum-Confidence für Pose-Tracking (Standard: 0.5)
**Output-Interfaces:**
- **Primary CHOP Outputs:** 33 Landmark-Channels × 4 Dimensionen (x,y,z,visibility)
- **Derived CHOP Outputs:** Spine Base
- **Debug Outputs:** raggedright Debug-Visualization-TOPs für Development und Troubleshooting, Head, Extremitäten werden als OUTs aus dem Modul geliefert
**Implementierungsdetails:**
**Python-Script-Integration:**
raggedright Innerhalb des Containers wird ein Skript genutzt, um auffällige grüne Kreise auf das TOP der Visuals genutzt, um die MediaPipe-Landmarks in Echtzeit zu visualisieren. Dieses Skript ist entscheidend für die Debugging-Phase und ermöglicht eine schnelle Validierung der Tracking-Daten.
**PY\_MediaPipeDebugCirclesForCompTops.py:**
- Funktion: Real-time Debug-Visualization der MediaPipe-Landmarks
- Implementation: Transform-TOP-Kontrolle mit dynamischer Circle-Positionierung
- Performance: CPU-optimiert für Echtzeit-Verarbeitung
**Fehlerbehebungs-Leitfaden:**
**Häufige Container-Probleme und Lösungsansätze:**
- **Problem: MediaPipe-Detection-Failure**
- **Symptom:** Alle CHOP-Outputs zeigen -1 oder 0-Werte
- **Diagnose:** Confidence-Werte überprüfen, Camera-Input validieren
- **Lösung:** Beleuchtung optimieren, Person vollständig im Frame positionieren
- **Problem: Coordinate-System-Mismatch**
- **Symptom:** Visual-Effects erscheinen an falschen Positionen
- **Diagnose:** Resolution-Mapping in Koordinaten-Transform-Scripts überprüfen
- **Lösung:** `constant1`-TOP Auflösungswerte mit Ausgabe-Display abgleichen
- **Problem: Performance-Degradation**
- **Symptom:** Frame-Rate < 30fps, erhöhte Latenz
- **Lösung:** MediaPipe-Model-Complexity reduzieren, CHOP-Update-Rate optimieren
**Debug-Workflow:**
- **MediaPipe-Output-Validation:** Debug-Circles aktivieren über `debugValue`-CHOP
- **CHOP-Data-Inspection:** Channel-Werte in TouchDesigner-Info-CHOP monitoren
- **Coordinate-Transform-Verification:** Transform-TOP-Outputs visuell validieren
}

![Headtrackingperspectivetouchdesignerwithvisualsoverlayedabovedebugcomptoseeaccuratetrackingofparticlegpuaboveheadwithreallifebeamerprojectioncorrectlyplaced](_documentation/images/onSetImages/HeadTrackingPerspectiveTouchDesignerWithVisualsOverlayedAboveDebugCompToSeeaccurateTrackingOfParticleGPUaboveHeadWithReallifeBeamerProjectionCorrectlyPlaced.png)

*Debug-Visualisierung: Präzises ParticleGPU-Tracking über Kopfposition mit korrekt ausgerichteter Beamer-Projektion*
}

![Headtrackedbubblesinactiontouchdesignerperspectiveslightmediapipeframedelayseeablebutalsovisualsdirectlyathead](_documentation/images/onSetImages/HeadTrackedBubblesInActionTouchDesignerPerspectiveslightMediaPipeFrameDelaySeeableButAlsoVisualsDirectlyAtHead.png)

*TouchDesigner Head-Tracking in Aktion: Kopfpartikel-Bubbles mit sichtbarer MediaPipe-Frame-Verzögerung aber direkter visueller Kopfanbindung*

## Drei produktionsvalidierte Visual-Systeme

**Gemeinsame Analyse-Pipeline für Trigger-Logik:**
raggedright Alle Visual-Systeme nutzen geometrische Beziehungsanalysen zwischen Skelett-Knoten für ihre Trigger-Logik:
**PY\_NodeDatsToDistanceAngles.py:**
- **Funktion:** Berechnung geometrischer Beziehungen zwischen Skelett-Knoten
- **Features:**
- Extrahiert alle 33 MediaPipe-Landmarks (nose bis right\_heel)
- Berechnet SpineBase als Mittelwert der Hüften
- Distanzberechnung zwischen definierten Gelenkpaaren
- Winkelberechnung über Dot-Product mit Clamping [-1,1]
- **Berechnete Metriken:**
- 13 Distanzen (Schulter-, Ellbogen-, Handgelenk-, Knie-, Knöchel-Abstände)
- 14 Winkel (Gelenk-Winkel für Arme, Beine, Hüfte-Hand-Beziehungen)
- **Output:** Direkte Zuweisung zu Constant-CHOPs über `assignToNode()`
- **Usage:** Trigger-Bedingungen für Visual-Aktivierung und Modus-Wechsel

### Visual-System 1: Hand-Feuer-Effekte

**Implementation:** raggedright TouchDesigners ParticleGPU für blaue Flammenpartikel, extrahiert Hand-Landmarks (MediaPipe Nodes 15/16) und transformiert diese in normalisierte Bildschirmkoordinaten.
**Koordinaten-Transformation im Detail (PY\_NodeToParticleGPUtranslate.py):**
- **Input:** MediaPipe normalisierte Koordinaten [0,1] vom HEAD-Operator
- **Remapping-Formel:** 
- X: `tdu.remap(x\_norm, 0.0, 1.0, -9.0, 9.0)`
- Y: `tdu.remap(y\_norm, 0.0, 1.0, 6.0, -6.0)` (invertiert für TouchDesigner)
- **Koordinatenraum:** [-9, 9] horizontal, [-6, 6] vertikal für ParticleGPU-Weltkoordinaten
}

![Nodexyzusopzentriertemtranslate](_documentation/images/docupictures/NodeXYzuSOPZentriertemTranslate.png)

*Koordinatentransformation der Hand-Feuer-Visualisierung: Node-XY zu zentralisiertem SOP-Translate*
}

![Noisyblob Head To Particlegpu Translate](_documentation/images/docupictures/NoisyBlob_HEAD_to_ParticleGPU_Translate.png)

*NoisyBlob ParticleGPU-Pipeline: Head-Node zu ParticleGPU Translation mit Transformation von Mediapipe zu Center-Offsets*
- **Resolution-Referenz:** constant1-TOP liefert Ausgabeauflösung (1920x1080)
- **Output:** CHOP-Kanäle 'x' und 'y' für direkte ParticleGPU-Force-Steuerung
**Produktionsergebnis:** raggedright Robuste Performance nach initialem Setup, fehlerfrei während gesamter Aufnahmezeit.

### Visual-System 2: Adaptive Kopfpartikel

**Zustandsmaschine:** raggedright Hand-zu-Schulter-Positionsvergleich triggert Partikel-Modus-Wechsel mit Interpolationsfunktion für sanfte Übergänge.
**Koordinaten-Transformation für Visualisierungs-Modi (PY\_NodeXYzuCentralisedSOPTranslate.py):**
- **Funktion:** Koordinaten-Transformation von normalized zu projection space für rechte Hand
- **Algorithm:** `x = x\_norm * width/height - 1; y = 0.5 - y\_norm`
- **Input:** `rechteHand` CHOP mit normalisierten Koordinaten
- **Usage:** raggedright SOP-Koordinaten-Mapping für 3D-Geometrie-Positionierung beim Wechsel zwischen Visualisierungs-Modi
- **Integration:** Ermöglicht präzise Partikel-Positionierung relativ zum Performer
**Technische Umsetzung der Zustandslogik (PY\_RelativeNodeValuesToBlended0and1Switch.py):**
- **Vergleichsalgorithmus:** `logic = 1 if (ly < sy or ry < sy) else 0`
- sy: SpineBase Y-Koordinate (Referenzpunkt)
- ly/ry: Linke/Rechte Hand Y-Koordinate
- **Animationssteuerung:** Zeitbasierte Interpolation mit absTime.seconds
- **Blend-Duration:** Dynamisch über blend\_param CHOP (Standard: 0.3s)
- **Interpolationsformel:** `anim\_value = start + (target - start) * t`
- **Switch-TOP Integration:** Direktes Schreiben auf switch1.par.index
}

![Noisyblob Animatedswitchzwischenblitzundnichtblitzbeitrackingtrigger](_documentation/images/docupictures/NoisyBlob_animatedSwitchzwischenBlitzUndNichtBlitzBeiTrackingTrigger.png)

*NoisyBlob Adaptive Visual-Switch: Animierte Zustandsmaschine mit Tracking-Triggern anhand der Spine-Base zu Händen-Position mit Smooth Transition zwischen Blitz und Nicht-Blitz*
**Produktionserfahrung:** raggedright Funktional, aber frontale Kamera-Beamer-Konstellation erfordert häufige Nachkalibrierung – arbeitsintensiv in Produktionsumgebung.

### Visual-System 3: 64-Spike Radialsystem

**Algorithmus:** raggedright atan2-basierte Polar-Koordinaten-Berechnung mappt Hand-/Fußpositionen auf diskrete Spike-Indizes (0-63) mit Intensitäts-Distanz-Korrelation.
**Detaillierte Polar-Koordinaten-Transformation (PY\_AngleToPhaseSkript):**
- **Aspect-Ratio-Korrektur:** `x\_wide = x\_raw * aspect` für kreisförmige Distanzen
- **Zentrierung:** `dx = x\_wide - cx\_wide`, `dy = y - cy` (cx\_wide = 0.5 * aspect)
- **Polar-Konversion:** 
- `dist = math.hypot(dx, dy)`
- `angle = math.atan2(dy, dx)`
- **Phase-Mapping (20-Spoke):** `angle\_to\_phase\_20(angle)`
- Basis: `((2*$pi$ - angle + $pi$/4) / (2*$pi$)) \
- Diskretisierung: `idx = int(p * 20 + 0.5) \
- 18°-Schritte mit 0/20 = 45° (SE)
- **Schwellenwert-Logik:** Dynamische Verbindung bei `dist >= threshold`
- **Ramp-TOP-Control:** Automatisches connect/disconnect zu comp15
}

![Topdown Kreiszurampsparametisierteberechnungen](_documentation/images/docupictures/TopDown_KreisZuRampsParametisierteBerechnungen.png)

*64-Spike Radialsystem im Testing: Polar-Koordinaten-Berechnung mit parametrisierter Ramp-Generation, hier mit erklärenden farblichen Texten zu den einzelnen Modulen*
**Produktionserfolg:** raggedright Optimale Performance bei Top-Down-Aufbau, vollständig fehlerfrei während gesamter Aufnahme – das zuverlässigste der drei Systeme.

## Produktionsvalidierung im Albrecht-Ade-Studio

**Zweitägige Intensivtests unter realen Bedingungen:**
**Tag 1 - System-Integration und Setup-Optimierung:**
- **Infrarot-Modi:** Problemlose Integration, keine Beleuchtungsinterferenzen
- **RGB-Modi:** Funktional unter kontrollierten Lichtbedingungen
- **Setup-Wechsel:** Unter 30 Minuten zwischen Visualisierungsmodi
- **Systemstabilität:** Null kritische Ausfälle während Produktionszeit
**Tag 2 - Vollständige Choreographie-Integration:**
- **1,5 TB Footage:** Vollständige 4K-Aufnahme mit M.A.S.K.-Integration
- **45 Takes:** Kontinuierliche Tracking-Performance ohne Unterbrechungen
- **Professional Workflow:** Nahtlose Integration in Filmproduktions-Pipeline

## Quantifizierte Performance-Metriken

## Technische Lösungsbilanz

**Erfolgreiche Lösungsansätze:**
**Infrarot-Adaptation:** raggedright Die spezifisch für Produktionsanforderungen angepasste Infrarot-MediaPipe-Pipeline adressiert effektiv das Problem der Beleuchtungsinterferenz – eine praxisorientierte Lösung mit direkter Produktionsrelevanz.
**Modulare TouchDesigner-Integration:** raggedright Container-basierte Architektur ermöglicht Plug-and-Play-Funktionalität und parallele Entwicklung verschiedener Visualisierungen.
**Performance-Optimierung:** Signifikante CPU-Nutzungsreduktion durch Systemvereinfachung und Architektur-Refactoring.
**Produktionserkenntnisse:**
**Top-Down-Überlegenheit:** Overhead-Tracking erwies sich als robuster und wartungsärmer als frontale Kamera-Setups.
**Infrarot-Immunität:** raggedright Vollständige Beleuchtungsunabhängigkeit ermöglicht kreative Freiheit bei Beamer-Intensität und -Effekten.
**Setup-Effizienz:** raggedright Kurze Setup-Zeiten erfüllen professionelle Produktionsanforderungen.

## Systemlimitationen und Scope

- **Single-Person-\Tracking:** Bewusste Beschränkung auf einzelne Performer für Choreographie-Fokus.
- **Manuelle Kalibrierung:** raggedright Setup-Änderungen erfordern manuellen Kalibrierungsaufwand – akzeptabel für geplante Produktionsabläufe.
- **Hardware-Abhängigkeit:** raggedright Kinect V2 als einzige Infrarot-Quelle – robust und kostengünstig ($approx$90€ gebraucht).
- **Positionierung vs. Konkurrenz:** raggedright M.A.S.K. konkurriert nicht mit professionellen Systemen wie OptiTrack, sondern schließt die Lücke zwischen Consumer-Hardware und Profi-Equipment für spezielle Anwendungen unter herausfordernden Beleuchtungsbedingungen.
Das M.A.S.K.-System demonstriert erfolgreich, wie constraints-driven engineering zu eleganten, produktionstauglichen Lösungen führt. Die Infrarot-Adaptation entstand aus praktischen Notwendigkeiten und beweist ihre Wirksamkeit durch fehlerfreie Performance unter realen Produktionsbedingungen.

---

## Produktionsnachweis

## Praxistest: Zwei Tage im Filmstudio

Am Montagmorgen stand ich vor dem Albrecht-Ade-Studio der Filmakademie Ludwigsburg. Die große Soundstage ist professionell ausgestattet. In wenigen Stunden würde hier im Produktionssetting getestet werden, ob M.A.S.K. dem Druck einer echten Filmproduktion standhalten konnte.
}

![Insidewideshotalbrechtadestudio](_documentation/images/onSetImages/InsideWideshotAlbrechtAdeStudio.jpg)

*Albrecht-Ade-Studio: Eindrücke der großen Soundstage nach den zwei Drehtagen. Das Studio wirkt wie leergefegt.*
Das technische Setup verlief gut – die Proben hatten sich ausgezahlt. Schnell waren Kinect, Beamer und TouchDesigner einsatzbereit. Die eigentliche Herausforderung begann mit den Abstimmungen zwischen Kamerateam, Lichtcrew, Producern und Directors. Jede Kameraposition bedeutete neue Offset-Kalibrierungen, da der Tänzer bewusst Abstand zu den projizierten Visuals hielt. Was in der Theorie einfach klang – Parameter anpassen, fertig – wurde zur geduldigen Arbeit zwischen den Takes.
}

![Martybehindthestudiocurtaindoingtouchdesigner](_documentation/images/onSetImages/MartyBehindTheStudioCurtainDoingTouchDesigner.jpg)

*Technische Umsetzung: TouchDesigner-Bedienung hinter dem Studievorhang während der Produktion*
clearpage ## Tag 1: Die drei Systeme im Einsatz
**Spike-System: Funktionstest**
raggedright Das 64-Spike-System machte den Anfang. Die Overhead-Kamera blickte von der Decke auf den Tänzer, während 64 radiale Segmente auf dem Boden projiziert wurden. Die wenige Tage alte Infrarot-Lösung bewährte sich: Trotz intensiver Beamer-Beleuchtung erkannte MediaPipe den Tänzer mit einer Genauigkeit, bei der man keine Fehler merkte.
}

![Widestudioshotpreparingtopdownspikeshot](_documentation/images/onSetImages/wideStudioShotPreparingTopDownSpikeShot.jpg)

*Studio-Vorbereitung: Setup für Top-Down-Spike-System mit Overhead-Kamera-Positionierung*
Die Geschichte hinter der Infrarot-Lösung war kurz: Maja und Rahel hatten mir während eines Wanderausflugs eine WhatsApp geschickt – das RGB-Tracking versagte unter Beamer-Licht. Beim Laufen kam die Eingebung: OBS Virtual Camera könnte den Kinect-Infrarot-Stream als Kameraeingang ausgeben. Nach der Wanderung folgte die Umsetzung: Plugin suchen, DLL installieren, Technical Rider schreiben. Die Lösung war unkonventionell, aber sie funktionierte.
Das Spike-System lief ohne einen einzigen Aussetzer. Die hohe Winkelauflösung reichte aus, um selbst subtile Handbewegungen in präzise Spike-Aktivierungen zu übersetzen. Nach wenigen Takes war die Sequenz im Kasten.
}

![Camerabtspicofacamerascreenoftopdown64Spikeofdanceronfloor](_documentation/images/onSetImages/cameraBTSPicofACameraScreenOfTopDown64SpikeOfDancerOnFloor.jpg)

*Kameramonitor: Top-Down-Aufnahme BTS des 64-Spike-Systems mit Tänzer auf dem Studioboden*
}

![Bts Producerscreen](_documentation/images/onSetImages/BTS_ProducerScreen.png)

*Spike-System in Aktion: Reagierte präzise auf Hand- und Fußbewegungen*
**Kopfpartikel: Die Geduldsprobe**
raggedright Das Kopfpartikel-System war die schwierigste Aufgabe. Frontale Kamera, RGB-Modus (Infrarot funktionierte aus diesem Winkel nicht), Beamer von hinten – eine Konstellation, die MediaPipe an seine Grenzen brachte.
}

![Pictureofdancerbtsinsetupforheadtrackingbubbles](_documentation/images/onSetImages/PictureOfDancerBTSinSetupForHeadTrackingBubbles.jpg)

*Kopfpartikel-Setup: Tänzer bei Vorbereitung für Head-Tracking mit kritischen Lichtbedingungen. Schön zu sehen ist die Beamer-Visuals hinter Ihm.*
Die Beleuchtung erwies sich als unzureichend für die RGB-basierte Skelett-Erkennung von MediaPipe. Nach mehreren fehlgeschlagenen Tracking-Versuchen wurde das Lichtteam gebeten, die Ausleuchtung zu verstärken. Diese Anpassung war essentiell für die Funktionsfähigkeit des Systems, da MediaPipe auf ausreichende Beleuchtung für die Bildanalyse angewiesen ist. Das Lichtteam setzte die Anforderung professionell um.
Ein weiteres Problem: Der Kameramann stand im Sichtfeld der Kinect. In den meisten Momenten war das in Ordnung, da ich MediaPipe auf ein einzigen Körper parametisiert hatte, aber falls der Tänzer nicht vor dem Kamermann begonnen wurde zu tracken, oder es zu einem kurzen Aussetzer kommt, kam es manchmal dazu, dass der Kameramann getrackt wurde.
Nach mehreren Takes und unzähligen Mikro-Anpassungen hatten wir die Sequenz. Die Partikel folgten dem Kopf, wechselten die Zustände wenn die Hände über die Schultern gingen, und die Projektion passte endlich zur Kameraposition.
**Hand-Feuer: Wenn Effekte zu gut funktionieren**
raggedright Nach der Mittagspause – es gab selbstgemachtes Curry – folgte nach einem kurzen finish der Head-Partikel das Hand-Feuer-Setup. Die modulare Architektur erwies sich als vorteilhaft: Das System war in wenigen Minuten einsatzbereit.
Der erste Take verlief problematisch. Die blauen Flammen folgten den Händen so präzise, dass der Kameramann mit seinem Zugwagen den Effekten folgte – und dabei den Tänzer aus dem Frame verlor. Die Visuals funktionierten zu gut für die geplante Kameraführung.
}

![Hqcinemacameraperspectiveofhandfiretothesidesofthehands](_documentation/images/onSetImages/HQCinemaCameraPerspectiveOfHandFireToTheSidesOfTheHands.png)

*Performer hat das Hand-Feuer bei sich beim beidseitigen Anheben seiner Arme. Hier aus der Sicht der HQ-Kamera.*
Dann kam die Stoff-Sequenz. Niemand hatte erwähnt, dass der Tänzer sich in durchsichtigen weißem Stoff hüllen würde. Der Stoff verschleierte die Körperform so effektiv, dass MediaPipe sofort das Skelett-Tracking verlor. Panik? Nicht wirklich. Die Debug-Visualisierung auf dem zweiten Monitor zeigte genau, wann MediaPipe den Tänzer wieder erkannte. Im richtigen Moment aktivierten wir die Effekte per Tastatur-Shortcut. Nicht elegant, aber funktional, und ein Einsetzen der Hand-Magie konnte in dem Moment getriggert werden, wenn der Tänzer sich aus dem Stoff befreit hat und die Arme ausstreckt.

## Tag 2: Dokumentation und Reflexion

Der zweite Tag fokussierte sich auf traditionelle Filmaufnahmen ohne interaktive Systeme. Neben der Dokumentation durch Behind-the-Scenes-Fotografie unterstützte ich das Team bei verschiedenen Produktionsaufgaben, einschließlich der Bedienung der studioeigenen Zugmaschine. Die Production Assistants vermittelten wertvolle Einblicke in die professionelle Studiotechnik. Trotz gelegentlicher organisatorischer Unterbrechungen zwischen den Aufnahmen verlief der Tag produktiv.
Maja und Rahel, die Directors, waren durchgehend gestresst aber sehr freundlich. Ihre Energie war ansteckend – sie glaubten an das Projekt, auch wenn die Technik manchmal zickte. Das Team war größer als erwartet, professioneller als befürchtet, und am Ende des Tages folgten wir uns alle auf Instagram.
}

![Martysmileyintocameraonset](_documentation/images/onSetImages/MartySmileyIntoCameraOnSet.jpg)

*Teamdynamik: Entspannte Atmosphäre zwischen den Takes trotz technischer Herausforderungen*
clearpage ## Ehrliche Bilanz
Nach zwei Tagen Produktion mit umfangreichem 4K-Material stand fest: M.A.S.K. hatte seinen Produktionstest bestanden. Die Infrarot-Lösung erwies sich als wirksam, das 64-Spike-System lief zuverlässig, und selbst die problematischen RGB-Modi lieferten am Ende brauchbare Ergebnisse.
**Was gut lief:**
- Die Infrarot-Lösung eliminierte die Beleuchtungsprobleme vollständig
- Das 64-Spike-System arbeitete über Stunden hinweg sehr zuverlässig
- Alle Setups waren schnell einsatzbereit
- Kein einziger System-Absturz während der gesamten Produktion
- Die modulare Architektur ermöglichte schnelle Anpassungen
**Was schwierig war:**
- Head-Particle-Modi erforderten konstante Rekalibrierung bei Positionswechseln
- Schwaches Licht degradierte die Tracking-Performance erheblich
- Live-Debugging unter Zeitdruck testete die Nerven
- Extreme Verdeckungen (durchsichtiger Stoff) überforderten MediaPipe
- Die eigene Stimme zu finden und technische Bedürfnisse zu kommunizieren
**Finale Metriken:**
- **Setup-Zeit:** Kurze Zeit pro System (inklusive Kalibrierung)
- **Tracking-Zuverlässigkeit:** Sehr hoch (Infrarot), gut (RGB bei ausreichend Licht)
- **Takes pro Sequenz:** Wenige (Spike-System), mehrere (Kopfpartikel), einige (Hand-Feuer)
- **Datenvolumen:** Umfangreiches 4K-Material
- **Crew-Integration:** Nach anfänglicher Skepsis volle Akzeptanz
- **Gesamtkosten:** Kostengünstige Hardware + kostenlose Software
}

![Wideshotofoutsideofstudioafter2Dayshoot](_documentation/images/onSetImages/WideShotOfOutsideOfStudioAfter2DayShoot.jpg)

*Produktionsabschluss: Außenansicht des Albrecht-Ade-Studios nach zweitägiger Drehzeit*

---

## Zentrale Erkenntnisse

## Technische Erkenntnisse

**Problemlösung durch Constraints:**
raggedright Die Infrarot-Pipeline entwickelte sich aus spezifischen Produktionsanforderungen und praktischen Constraints. MediaPipes Verarbeitungsfähigkeit für Infrarot-Daten wurde empirisch validiert und für die Projektanforderungen angepasst. Diese Erfahrung verdeutlichte, wie praxisorientierte Lösungsansätze zur Systemoptimierung beitragen können.
**Architektonische Evolution:**
raggedright Der Projektverlauf dokumentiert eine schrittweise Vereinfachung: Von der geplanten Dual-Sensor-Fusion mit Kalman-Filter zu einer reinen MediaPipe-Lösung. Jede Reduktion verbesserte Stabilität und Wartbarkeit. Die finale Architektur ist nicht die technisch komplexeste, aber die praktikabelste.
**Modularität als Designprinzip:**
raggedright Die Entscheidung, jeden Aspekt (Tracking, Analyse, Visualisierung) in separate TouchDesigner-Container zu kapseln, erwies sich als fundamental. Sie ermöglichte nicht nur parallele Entwicklung, sondern macht das System zukunftssicher: Neue Tracking-Technologien können ohne Änderung der Visualisierungslogik integriert werden.
**Projektmanagement im interdisziplinären Kontext:**
**Adaptive Planung:**
raggedright Die Sprint-Struktur musste mehrfach angepasst werden. Choreographische Anforderungen entstanden organisch während der Proben, nicht durch Requirements Engineering. Sprint 3 wurde komplett umgeplant, als die handgezeichneten Visual-Konzepte eintrafen. Diese Flexibilität war keine Schwäche, sondern Stärke des Prozesses.
**Dokumentation als Kommunikationswerkzeug:**
raggedright Die parallele Dokumentation diente nicht nur der Nachvollziehbarkeit, sondern wurde zum primären Kommunikationsmedium mit den Stakeholdern. Screenshots und Diagramme überbrückten die Sprachbarriere zwischen Technik und Kunst effektiver als verbale Erklärungen.
**Solo-Development-Strategien:**
raggedright Als Alleinentwickler musste ich spezifische Strategien für die Stakeholder-Kommunikation entwickeln:
**Erfolgreiche Ansätze:**
- **Regelmäßige Demo-Sessions:** Konkrete Fortschritte reduzierten Stakeholder-Unsicherheit
- **Transparente Dokumentation:** GitHub-Repository und .toe-Dateien als Kommunikationsbasis
- **Proaktive Problem-Kommunikation:** Frühe Information bei technischen Herausforderungen
- **Sprint-synchronisierte Updates:** Strukturierte 2-3 Wochen Kommunikationsrhythmus
**Herausforderungen der Solo-Entwicklung:**
- **Isolation bei technischen Problemen:** Eigenständige Problemlösung zeitaufwändig
- **Stakeholder-Erwartungsmanagement:** Balance zwischen Ambition und Realisierbarkeit
- **Dokumentations-Overhead:** Umfassende Dokumentation für interdisziplinäre Kommunikation
}

![Headtracking Hqcamera](_documentation/images/onSetImages/HeadTracking_HQCamera.png)

*Kopfpartikel-Setup: Komplexe Kamera-Beamer-Ausrichtung mit hardcoded Offsets in particleGPU je nach Kamera-Winkel, was zu einer Erhöhung der Zeit zwischen Takes führte*
**Kollaboration über Disziplingrenzen:**
**Visuelle Kommunikation:**
raggedright Die wichtigste Herausforderung war die Übersetzung zwischen künstlerischer Vision und technischer Implementation. "Es soll aussehen wie Gedanken, die explodieren" musste in Partikel-Emissionsraten und Geschwindigkeitsvektoren übersetzt werden. Die Lösung: Rapid Prototyping mit sofortigem visuellem Feedback.
**Gegenseitiges Lernen:**
raggedright Das Filmteam lernte technische Constraints zu respektieren (MediaPipe braucht Kontrast), ich lernte künstlerische Prioritäten zu verstehen (Effekt vor Präzision). Diese gegenseitige Bildung war wertvoll über das Projekt hinaus.
**Iterative Stakeholder-Integration:**
Schlüsselmomente der Zusammenarbeit prägten die Entwicklungsrichtung:
- **Frühe Expertenberatung:** Technical Review (17.01.2025) definierte Projektrichtung
- **Stakeholder-Integration:** Choreographie-Meeting (10.03.2025) prägte Entwicklung
- **Iterative Validation:** Kontinuierliche Demo-Sessions verhinderten Fehlentwicklung
- **Lösungen durch Notwendigkeit:** Produktionsanforderungen führten zu praktischen technischen Anpassungen
**Produktionsumgebung und Systemvalidierung:**
**Echtzeit-Anforderungen:**
raggedright Die Produktionsumgebung erforderte robuste Systemarchitektur mit minimalen Ausfallzeiten. Entwickelte Debug-Visualisierungen dienten gleichzeitig als Produktionsmonitoring-Tools. Die Echtzeit-Skelett-Overlays erwiesen sich als essentiell für die operative Systemüberwachung während der Aufnahmen.
}

![Dancernotmediapipefoundcorrectlywheninclothonfloor](_documentation/images/onSetImages/DancerNotMediaPipeFoundCorrectlyWhenInClothOnFloor.png)

*Tracking-Problem: MediaPipe verliert Tänzer-Skelett-Erkennung bei Stoffverschleierung zu Beginn des Visuals -> Visuals werden manuell von mir anhand der Debug-Visualisierung an und dann zum Ende ausgeschaltet, wenn Ich sah, dass der Tänzer gut erkennt wird.*
**Professionelle Koordination:**
raggedright Die Integration in professionelle Produktionsabläufe erforderte strukturierte Kommunikation technischer Anforderungen mit der Produktionsleitung. Diese Koordination zwischen technischen Systemanforderungen und kreativen Produktionszielen war ein wichtiger Aspekt des interdisziplinären Projektmanagements.
**Professionelle Entwicklung:**
**Vollständige Projektverantwortung:**
raggedright Als einziger Entwickler trug ich die komplette technische Verantwortung. Jede Architekturentscheidung, jede Optimierung, jeder Workaround – alles lag in meiner Hand. Diese Erfahrung der vollständigen Ownership war gleichzeitig belastend und ermächtigend.
**Realistische Selbsteinschätzung:**
raggedright Das Projekt lehrte mich, eigene Grenzen zu erkennen und zu kommunizieren. M.A.S.K. konkurriert nicht mit industriellen Motion-Capture-Systemen – und das ist in Ordnung. Diese Ehrlichkeit ermöglichte fokussierte Entwicklung statt feature creep.
**Nachhaltige Learnings:**
Drei Erkenntnisse prägen meine weitere Arbeit:
**1. Pragmatismus schlägt Perfektionismus:** Die funktionierende 80\
**2. Interdisziplinarität erfordert Demut:** Andere Fachbereiche haben eigene Exzellenzkriterien, die respektiert werden müssen.
**3. Constraints fördern Kreativität:** raggedright Die Limitierungen (Budget, Hardware, Zeit) zwangen zu alternativen Lösungen, die in einem ressourcenreichen Umfeld nie entstanden wären.
Die eigenständige Entwicklung von M.A.S.K. demonstriert, wie strukturierte Kommunikation und agile Methoden auch bei Solo-Projekten zu erfolgreicher interdisziplinärer Zusammenarbeit führen können.

---

## Fazit und Beiträge

## Projektergebnis

M.A.S.K. demonstriert, dass spezialisierte Motion-Capture-Lösungen mit Consumer-Hardware realisierbar sind. Das System adressiert erfolgreich die spezifische Herausforderung des Trackings unter intensiver Bühnenbeleuchtung und macht diese Technologie für Projekte mit begrenztem Budget zugänglich.

## Technischer Beitrag

Die Infrarot-MediaPipe-Pipeline stellt eine praxisorientierte Lösung für spezifische Produktionsanforderungen dar. Während professionelle Systeme auf spezialisierte Hardware setzen, nutzt M.A.S.K. die verfügbare Infrarot-Funktionalität der Kinect V2 in Kombination mit MediaPipes Machine-Learning-Modell. Diese Adaptation wurde spezifisch für die Projektanforderungen entwickelt und validiert.
Die modulare TouchDesigner-Architektur ermöglicht es anderen Entwicklern, einzelne Komponenten für eigene Projekte zu adaptieren. Das GitHub-Repository enthält nicht nur Code, sondern auch die komplette Entwicklungshistorie inklusive verworfener Ansätze – wertvoll für Lernende.

## Praktische Relevanz

Für Bildungseinrichtungen und unabhängige Künstler bietet M.A.S.K. eine realistische Alternative zu kommerziellen Systemen. Die Hardware-Kosten beschränken sich auf circa 100 Euro für gebrauchte Kinect V2 Hardware, wobei zusätzliche Software-Infrastruktur (TouchDesigner, OBS Studio) und Entwicklungszeit je nach Projektanforderungen zu kalkulieren sind.
Die erfolgreiche Produktion von "Echoes of the Mind" validiert die Praxistauglichkeit. Das System bewältigte 45 Takes über zwei Produktionstage ohne kritische Ausfälle – ein Beweis für die Stabilität der gewählten Architektur.

## Limitierungen und Kontext

M.A.S.K. ersetzt keine professionellen Motion-Capture-Systeme. Für Anwendungen, die Millimeterpräzision, Multi-Person-Tracking oder 360-Grad-Erfassung erfordern, bleiben kommerzielle Lösungen überlegen. Diese Einschränkung ist bewusst: Durch Fokussierung auf einen spezifischen Use-Case konnte eine robuste Lösung entstehen.
Technische Grenzen:
- Single-Person-\Tracking only
- Frontalerfassung (keine 360-Grad-Abdeckung)
- Manuelle Kalibrierung bei Setup-Änderungen
- Abhängigkeit von MediaPipes Modell-Limitierungen

## Weiterentwicklungspotenzial

Die Open-Source-Natur des Projekts lädt zu Erweiterungen ein:
**Kurzfristig:**
- Automatische Kalibrierungsroutinen
- Weitere Visual-Effekte für die bestehende Pipeline
- Verbessertes Handling von Okklusionen
**Mittelfristig:**
- Integration neuerer ML-Modelle (MediaPipe Holistic)
- Multi-Sensor-Fusion mit IMUs oder LiDAR
- Echtzeit-Performance-Metriken
**Langfristig:**
- Portierung auf andere Plattformen (Mac, Linux)
- Web-basierte Konfigurationsoberfläche
- Integration in Game-Engines

## Breitere Implikationen

Die zunehmende Verschmelzung von Performance-Kunst und digitaler Technologie erfordert zugängliche Werkzeuge. M.A.S.K. zeigt, dass akademische Projekte diese Lücke füllen können, wenn sie sich auf praktische Probleme fokussieren statt auf theoretische Vollständigkeit.
Die Infrarot-Lösung könnte Anwendungen über die Kunst hinaus finden: Physiotherapie-Überwachung, Sporttechnik-Analyse oder barrierefreie Interfaces könnten von der Beleuchtungsunabhängigkeit profitieren.

## Abschließende Bewertung

M.A.S.K. ist eine praxisorientierte Lösung, die bewährte Technologien für spezifische Anwendungsanforderungen kombiniert. Das System entstand aus konkreten Produktionsnotwendigkeiten und demonstriert, wie interdisziplinäre Zusammenarbeit zu funktionsfähigen technischen Lösungen führen kann. Der Wert liegt in der durchdachten Integration verfügbarer Komponenten und der bewiesenen Produktionstauglichkeit.
Das Projekt erfüllte seinen Zweck: Es ermöglichte "Echoes of the Mind" und bleibt als Open-Source-Werkzeug für andere verfügbar. In einer Welt, in der Technologie oft als Selbstzweck entwickelt wird, ist diese zielgerichtete Pragmatik vielleicht die wichtigste Stärke von M.A.S.K.

---

## Vollständiges Code-Repository

## Open-Source-Repository

Das vollständige M.A.S.K.-System ist als strukturiertes GitHub-Repository verfügbar für Reproduktion und Weiterentwicklung.
**Repository:** urlhttps://github.com/mklemmingen/MASK (GPL-2.0 License)
**Kern-Komponenten:**
**Technische Reproduzierbarkeit:**
**Installation:** Repository-Download und TouchDesigner 2023.11+ für vollständige Funktionalität.
**Hardware-Anforderungen:** Kinect V2, OBS Studio 28.0+, NVIDIA GPU empfohlen für ParticleGPU.
**Dokumentation:** raggedright README.md mit detaillierten Setup-Anweisungen und Konfigurationshinweisen.

## Python-Skript-Referenz

**Kern-Algorithmen:**
**PY\_MediaPipeDebugCirclesForCompTops.py**
- **Funktion:** Echtzeit-Debug-Visualisierung aller MediaPipe-Skeleton-Nodes
- **Features:** Confidence-basierte Farbkodierung, Größen-Mapping, Toggle-Control
- **Integration:** Text-DAT in Debug-Container
**PY\_NodeXYzuCentralisedSOPTranslate.py**
- **Funktion:** MediaPipe-Koordinaten zu TouchDesigner-SOP-Transformation
- **Features:** Normalisierung, Aspect-Ratio-Korrektur, Calibration-Offset
- **Input:** MediaPipe XYZ-Koordinaten
- **Output:** TouchDesigner-kompatible SOP-Koordinaten
**PY\_NodeDatsToDistanceAngles.py**
- **Funktion:** Geometrische Analyse zwischen Skeleton-Nodes
- **Features:** 
- 33 MediaPipe-Landmarks (nose bis right\_heel)
- Echtzeit-Distanzberechnung zwischen definierten Gelenkpaaren
- Winkelberechnung über Dot-Product mit Clamping [-1,1]
- SpineBase-Approximation als Mittelwert der Hüften
- **Berechnete Metriken:** 13 Distanzen, 14 Winkel zwischen Gelenken
- **Output:** CHOP-Channels für geometrische Parameter über assignToNode()
**Visual-Spezifische Skripte:**
**PY\_NodeToParticleGPUtranslate.py**
- **Funktion:** Hand-Node zu ParticleGPU-Koordinaten-Mapping
- **Features:** Real-normalized Coordinates, Multi-Hand-Support
- **Use-Case:** Hand-Feuer-Effekte (Visual 1)
**PY\_RelativeNodeValuesToBlended0and1Switch.py**
- **Funktion:** Hand-über-Schulter-Erkennung für Zustandsumschaltung
- **Features:** Sanfte Interpolation, Bilateral-Hand-Processing
- **Use-Case:** Adaptive Kopf-Partikel-System (Visual 2)
**PY\_AngleToPhaseSkript\_HandsToCenter\_direct.py**
- **Funktion:** 64-Spike-Winkel-zu-Phase-Transformation
- **Features:** Multi-Resolution (8,12,20,64), Atan2-Präzision
- **Input:** Hand/Fuß-Koordinaten relativ zu Screen-Center
- **Use-Case:** Radiales Spike-System (Visual 3)
**Legacy-Implementierungen:**
**PY\_OG\_TestingWithSynchAndKalman.py**
- **Funktion:** Historische MediaPipe-Kinect-Datenfusion
- **Features:** Kalman-Filter-Glättung, Sensor-Synchronisation
- **Status:** Archiviert, funktional für Referenz
- **Research-Value:** Multi-Sensor-Fusion-Algorithmus

## TouchDesigner-Projektdateien

**Visual-System-Implementierungen:**
**250421\_NoisyBlob\_withTrackingAndBlitzeSwitch.tox**
- **Fokus:** Experimentelle Bubble-Physik mit Tracking-Integration
- **Features:** Noise-basierte Blob-Bewegungen, Blitz-Effekte
- **Status:** Entwicklungs-Prototyp
**250421\_Topshot\_Visual\_withTracking20Spoke.tox**
- **Fokus:** Top-Down 20-Spike-System für Overhead-Kamera
- **Features:** Radiale Spike-Geometrie, Extremitäten-Tracking
- **Use-Case:** Produktions-Implementierung Visual 3
**250421\_Topshot\_Visual\_withTracking20Spoke\_v2.tox**
- **Fokus:** Erweiterte Version des 20-Spike-Systems
- **Improvements:** Optimierte Performance, erweiterte Parameter
- **Status:** Finale Produktionsversion
**250421\_prettyBubbles\_blaueFade\_withTracking.tox**
- **Fokus:** Blaue Bubble-Effekte mit Fade-Transition
- **Features:** Tracking-responsive Bubble-Generierung
- **Use-Case:** Alternative zu Hand-Feuer-Effekten
**Kern-Komponenten:**
**Focus.tox**
- **Funktion:** Fokus-Steuerung für Visual-Effekte
- **Integration:** Modulare TouchDesigner-Komponente
**Grain.tox**
- **Funktion:** Grain-Effekt für visuelle Textur
- **Integration:** Post-Processing-Komponente
**TrackingAsATox\_needsRelativeMediaPipeTox.tox**
- **Funktion:** Tracking-System als modulare Komponente
- **Dependencies:** Relative MediaPipe-Komponente erforderlich
- **Use-Case:** Wiederverwendbare Tracking-Pipeline

## Testing und Validierung

**Komparative Evaluation:**
**Testing\_KinectVsMediapipe.toe**
- **Funktion:** Direkte Vergleichstests zwischen Kinect V2 und MediaPipe
- **Features:** Simultanes Tracking, Performance-Vergleich
- **Outcome:** Validierung der MediaPipe-Überlegenheit bei partieller Okklusion
- **Documentation:** Testing\_README.md

## Dokumentation und Assets

**Visuelle Dokumentation:**
**DocuPictures/**
- Enthält alle Screenshots und Diagramme für die Projektdokumentation
- Visual-Pipeline-Übersichten und Systemarchitektur-Diagramme
- Debug-Interface-Screenshots und Production-Dokumentation
**comment\_assets/**
- Zusätzliche Assets für Kommentierung und Erklärung
- Unterstützende Materialien für Code-Dokumentation
**Backup und Versionierung:**
**Backup/**
- Backup-Versionen kritischer TouchDesigner-Dateien
- Entwicklungs-Snapshots für Rollback-Fähigkeiten
- Archivierte Versionen verschiedener Entwicklungsphasen
Das Repository unter urlhttps://github.com/mklemmingen/MASK bietet eine kompakte, aber vollständige Implementation des M.A.S.K.-Systems. Die direkte Struktur ermöglicht einfachen Zugang zu allen Kern-Komponenten ohne komplexe Hierarchien, während die Dateinamen die chronologische Entwicklung und spezifische Funktionen klar kennzeichnen.

---

## Team und Kommunikation

## Professionelle Kollaboration zwischen Hochschulen

**Interdisziplinäres Entwicklungsteam:**
**Technische Führung - Hochschule Reutlingen:**
- **Entwickler:** Marty Lauterbach (Sole Developer, Technische Projektleitung)
- **Rolle:** System-\Architektur, MediaPipe-Integration, TouchDesigner-Pipeline-\Entwicklung
- **Verantwortung:** Vollständige technische Implementation als einziger Entwickler der Hochschule
- **Entwicklung:** Eigenständige Umsetzung der Infrarot-MediaPipe-Pipeline
**Kreative Partner - Filmakademie Baden-Württemberg:**
- **Designerinnen:** Maja Litzke und Rahel Fundinger (Creative Direction, Künstlerische Leitung)
- **Projektkontext:** "Echoes of the Mind" - Cinematographische Tanzproduktion über mentale Zustände
- **Kollaborationsqualität:** Intensive interdisziplinäre Partnerschaft zwischen Technik und Kunst
- **Kommunikation:** Regelmäßige Sprint-Meetings und kontinuierlicher fachlicher Austausch
**Interdisziplinäre Konstellation:**
raggedright Diese Kooperation zwischen einem Hochschulentwickler und erfahrenen Filmakademie-Designerinnen ermöglichte eine produktive Synthese aus technischer Entwicklung und künstlerischer Vision.
**Betreuung und Beratung:**
**Hochschule Reutlingen:**
- **Projektbetreuung:** Anja Hartmann (Akademische Betreuung, Bewertung)
- **Fachberatung:** Niklas Zidarov Digital Art (Technische Beratung, 17.01.2025)
- **Rolle:** Akademische Unterstützung
**Produktionsumgebung:**
- **Albrecht-Ade-Studio:** Produktionsstudio der Filmakademie
- **Technische Crew:** Kamerateam, Beleuchtung, Tontechnik
- **Equipment-Management:** Hardware-Bereitstellung und -Support

## Kommunikationsprotokoll

**Meeting-Struktur:**
**Regelmäßige Termine:**
- **Sprint-Meetings:** Alle 2-3 Wochen, 90 Minuten, Online mit Filmakademie
- **Demo-Sessions:** Nach jedem Sprint, 60 Minuten, Live-Demonstration der Fortschritte
- **Technical-Reviews:** Bei Bedarf, Problem-focused
- **Production-Meetings:** Pre-Production, intensivere Koordination für Studioeinsatz
**Laufende Kommunikation:**
- **WhatsApp-Gruppe:** Schnelle Updates, Terminkoordination, Dateiaustausch
- **Video-Calls:** Spontane Problem-Lösung, Screen-Sharing für technische Diskussionen
- **GitHub-Repository:** Code-Sharing, Versions-Dokumentation

## Professionelle Kollaborationsmeilensteine

**Technische Grundlegung (17.01.2025):**
**Ausgangssituation:** raggedright Als einziger Entwickler der Hochschule Reutlingen suchte ich Expertenberatung für eine geeignete Motion-Capture-Strategie.
- **Fachberatung:** Lehrbeauftragter Digital Art empfahl MediaPipe-Integration
- **Strategische Entscheidung:** MediaPipe als Subprozess für Kinect RGB-Stream
- **Technische Vision:** Hybrid-System für verbesserte Tracking-Robustheit
- **Eigenständige Umsetzung:** Vollständige Implementation-Verantwortung übernommen
**Interdisziplinärer Projekt-Kick-off (Ende Januar 2025):**
**Erste Zusammenarbeit:** raggedright Intensive Kollaboration mit Maja Litzke und Rahel Fundinger zur Definition der technischen Architektur basierend auf künstlerischen Anforderungen.
**Gemeinsam entwickelte Systemarchitektur:**
- **Dual-Source-Konzept:** MediaPipe-Kinect-Fusion basierend auf technischer Analyse und kreativen Anforderungen
- **Interdisziplinäre Integration:** Choreographie-spezifische Trigger-Pipeline durch kollaborative Spezifikation
- **Bewegungsanalyse:** raggedright Geschwindigkeit, Rotation und Winkelbeziehungen entsprechend künstlerischer und technischer Kriterien
- **Kollaborative Arbeitsweise:** Sprint-basierte Entwicklung mit regelmäßigen interdisziplinären Abstimmungen
**Kreative Anforderungsdefinition (10.03.2025):**
**Wendepunkt der Zusammenarbeit:** raggedright Die Designerinnen präsentierten konkrete choreographische Konzepte, die meine technischen Lösungsansätze fundamental beeinflussten.
**Interdisziplinäre Systemdefinition:**
- **Hand-Tracking-Priorisierung:** Fokus auf Arm- und Handbewegungen nach kreativer Spezifikation
- **Räumliche Kalibrierung:** Präzise Beamer-Projektion für Bodenchoreographie
- **Visual-Responsivität:** Echtzeit-Bewegungserkennung für emotionale Tanznarrative  
- **Multi-Perspektiven-System:** Top-Down und frontale Tracking-Modi
**Interdisziplinäre Translation:** raggedright Künstlerische Anforderungen und technische Möglichkeiten wurden gemeinsam in umsetzbare Implementation-Spezifikationen entwickelt.

## Entscheidungslogprotokoll

**Eigenständige Architekturentscheidungen:**
**Hybrid-Tracking-System Definition (Ende Januar 2025)**
- **Kontext:** Projekt-Kick-off mit Filmakademie zur Systemarchitektur
- **Entwickler-Entscheidung:** Dual-Source-Ansatz basierend auf Technical Review
- **Begründung:** Kombination aus MediaPipe-Robustheit und Kinect-Tiefendaten
- **Implementation-Plan:** Kalman-Filter-basierte Datenfusion
**MediaPipe-Priorisierung (Sprint 2, bis 24.03.2025)**
- **Eigenständige Evaluation:** Komparative Tests zeigen MediaPipe-Überlegenheit bei partieller Okklusion
- **Stakeholder-Konsultation:** Filmakademie bevorzugt Robustheit über absolute Präzision
- **Technische Analyse:** MediaPipe höhere Confidence-Werte bei nicht-sichtbaren Körperregionen
- **Entwicklungsentscheidung:** MediaPipe als primäres System, Kinect als Backup
- **Dokumentation:** Testing\_KinectVsMediapipe.toe als Vergleichsreferenz
**Kinect-Deprecation (Sprint 4, bis 20.04.2025)**
- **Problem-Identifikation:** Hybrid-System erhöht Komplexität ohne klaren Mehrwert
- **Stakeholder-Feedback:** Vereinfachung für bessere Wartbarkeit gewünscht
- **Performance-Analyse:** MediaPipe-Only zeigt gute Performance bei unvollständigen Skeleton-Daten
- **Architektur-Refactoring:** Vollständige Modularisierung von MediaPipe, Elimination der Kinect-Dependencies
- **Begründung:** Limitierte Partial-Body-Detection der Kinect vs. MediaPipe-Robustheit
**Iterative Scope-Entwicklung:**
**Bubble-Physics zu Visual-System-Trias (Sprint 4-5)**
- **Ursprünglicher Plan:** Komplexe Bubble-Displacement-Algorithmen
- **Technische Herausforderung:** Unzureichende Feedback-Loops für persistente Bubble-Lifecycles
- **Evaluierte Implementierungen:** C\# Shader, ParticleGPU Manipulation, Hybrid CPU-GPU Approach
- **Stakeholder-Realignment:** Alternative Visual-Ansätze für praktische Choreographie-Integration
- **Finale Implementierung:** Hand-Fire-Effects, Adaptive Head-Particles, Radial Spike-System
- **Outcome:** Drei konkrete, choreographie-spezifische und produktionstaugliche Visualisierungen
**Infrarot-Lösung (Sprint 6, bis 12.05.2025)**
- **Kritisches Problem:** Beamer-Projektionen verursachen RGB-Kamera-Überbelichtung
- **Stakeholder-Impact:** Fundamental für Produktionsumgebung der Filmakademie
- **Eigenständige Lösung:** Kinect V2 Infrarot-Stream als Primary Input über OBS Virtual Camera
- **Technische Implementation:** IR-optimierte MediaPipe Skeleton-Detection
- **Zeitmanagement:** Zusätzliche Entwicklungszeit für fundamentale Problemlösung
- **Validation:** Vollständige Beleuchtungs-Immunität in Produktionsumgebung erreicht

## Eigenständige Entwicklungsprozesse

**Solo-Development-Workflow:**
**Tägliche Entwicklungsroutine:**
- **Morgendliche Prioritätssetzung:** Sprint-Ziele vs. technische Herausforderungen
- **Iterative Implementation:** Kurze Entwicklungszyklen mit kontinuierlicher Validierung
- **Dokumentation parallel:** Code-Kommentierung und Architektur-Notizen während Entwicklung
- **Abendliche Reflektion:** Fortschritts-Assessment und nächste Schritte
**Problem-Solving-Ansatz:**
- **Eigenständige Recherche:** MediaPipe-Dokumentation, TouchDesigner-Community
- **Prototyping:** Schnelle Proof-of-Concept-Implementierungen
- **Stakeholder-Konsultation:** Bei konzeptionellen oder künstlerischen Entscheidungen
- **Iterative Verfeinerung:** Kontinuierliche Optimierung basierend auf Testing
**Sprint-Retrospektiven (Solo-Reflektion):**
**Sprint 1-2: Grundlagen-Phase**
- **Lernkurve:** MediaPipe-TouchDesigner-\Integration steiler als erwartet
- **Stakeholder-Alignment:** Regelmäßige Kommunikation essentiell für Richtung
- **Technische Validation:** Komparative Tests bestätigen Hybrid-Ansatz-Wert
**Sprint 3-4: Architektur-Phase**
- **Komplexitäts-Management:** Vereinfachung führt zu besserer Performance
- **Modularität:** Containerization erleichtert Debugging deutlich
- **Scope-Flexibilität:** Bereitschaft zu Architektur-Änderungen erweist sich als nützlich
**Sprint 5-6: Produktions-Phase**
- **Lösungsfindung unter Druck:** Infrarot-Adaptation entsteht aus Produktionsnotwendigkeit
- **Stakeholder-Coordination:** Enge Abstimmung für Studio-Integration kritisch
- **Performance-Validation:** Real-world Testing unerlässlich für Produktionsreife

---

## Danksagung

Mein herzlicher Dank gilt allen Beteiligten, die dieses Projekt ermöglicht und unterstützt haben.
Besonderer Dank geht an die **Filmakademie Baden-Württemberg in Ludwigsburg**, insbesondere an **Maka Litzke** und **Rahel Fundinger**raggedright , für ihre wertvolle fachliche Expertise und die konstruktive Zusammenarbeit während des gesamten Projektverlaufs.
Ebenso möchte ich mich bei der **Hochschule Reutlingen** bedanken, namentlich bei **Prof. Anja Hartmann** für das Angebot und die Möglichkeit, das Projekt als Teil meines Studiums zu machen, und **Niklas Zidarov**raggedright , für seine kompetente Hilfestellung und Anregung bei der Umsetzung dieses Vorhabens.
Die interdisziplinäre Zusammenarbeit zwischen beiden Institutionen hat maßgeblich zum Erfolg dieses Projekts beigetragen und wertvolle Einblicke in verschiedene Fachbereiche ermöglicht.
*Vielen Dank für Ihre Unterstützung*

---

## Project Structure

```
MASK-main/
├── *.toe                    # TouchDesigner project files
├── *.py                     # Python DAT operators
├── *.tox                    # TouchDesigner components
├── Backup/                  # Project file versions
├── _documentation/          # Complete LaTeX documentation
│   ├── src/                # Individual section files
│   ├── images/             # Figures and diagrams
│   └── document.pdf        # Compiled documentation
└── README.md               # This file
```

---

*This README.md was automatically generated from the LaTeX documentation.
For the complete formatted document, see `_documentation/document.pdf`.*

*Generated on: 27.06.2025*