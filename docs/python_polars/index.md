# Polars in Python

Lange Zeit war Pandas die erste Wahl für die Datenverarbeitung in Python. Zwar ist Pandas deutlich schneller als beispielsweise Excel, doch für große Datensätze reicht die Performance teilweise nicht mehr aus. Hier kommt Polars ins Spiel. Polars ist eine moderne Datenverarbeitungsbibliothek, die speziell für die Verarbeitung großer Datensätze entwickelt wurde. In diesem Kapitel werden wir uns ansehen, wie Polars in Python verwendet werden kann.


## Warum ist Polars schneller als Pandas?

Polars ist deutlich schneller als pandas, was auf eine Reihe technischer und architektonischer Unterschiede zurückzuführen ist:

### 1. **Speicherlayout und Hardware-Nutzung**
   - **Spaltenorientiertes Speicherlayout**: Polars speichert Daten in einem spaltenorientierten Format, ähnlich wie Apache Arrow. Das bedeutet, dass alle Daten einer Spalte im Speicher direkt hintereinander liegen. Das ermöglicht es modernen CPUs, diese Daten schneller zu verarbeiten, da sie optimierte Speicherzugriffe und Caching besser nutzen können.
   - **Vektorisiertes Rechnen**: Polars nutzt sogenannte SIMD-Instruktionen (Single Instruction, Multiple Data). Das bedeutet, es kann mehrere Werte mit einem einzigen CPU-Befehl verarbeiten, was die Geschwindigkeit der Berechnungen erheblich erhöht.
   - **Multithreading und Parallelisierung**: Polars verteilt Rechenoperationen automatisch auf mehrere CPU-Kerne. Da pandas im Wesentlichen Single-threaded ist, profitiert Polars stark von Multi-Core-Prozessoren.

### 2. **Programmiersprache Rust**
   - Polars wurde in **Rust** entwickelt, einer Hochleistungssprache, die sowohl sehr schnell als auch speichereffizient ist. Rust bietet zudem strenge Speichersicherheitsmechanismen, die verhindern, dass typische Fehler wie Speicherlecks oder Pufferüberläufe entstehen, ohne dass dabei die Performance leidet.
   - Pandas hingegen ist in Python geschrieben, einer interpretieren Sprache, die im Vergleich langsamer ist. Zwar sind viele Funktionen von pandas in C oder Cython implementiert, aber Python selbst bleibt oft der Flaschenhals.

### 3. **Lazy Evaluation**
   - Polars nutzt **Lazy Evaluation**, d. h. Berechnungen werden nicht sofort ausgeführt. Stattdessen erstellt Polars einen optimierten Ausführungsplan, bevor es die Daten verarbeitet. Das ermöglicht eine deutliche Effizienzsteigerung, da unnötige Berechnungen vermieden werden.
   - Im Gegensatz dazu führt pandas Operationen direkt aus, was häufig zu einer weniger optimalen Nutzung von Rechenressourcen führt.

### 4. **Effiziente Speicherverwaltung**
   - Polars bietet eine sehr optimierte **Speicherverwaltung**. Rust kommt ohne Garbage Collection aus, was bedeutet, dass Polars den Speicher effizient und kontrolliert nutzen kann. Dies minimiert unnötige Speicherbewegungen und maximiert die Rechenleistung.
   - Pandas hingegen verwendet Python's Garbage Collector, was zu unnötigem Overhead führen kann und sich negativ auf die Performance auswirkt.

### 5. **Optimiertes Handling von Null-Werten**
   - Polars verwendet optimierte Datenstrukturen, um fehlende Werte effizient zu handhaben. Pandas hingegen nutzt häufig NaN-Werte, was in numerischen Berechnungen zusätzlichen Overhead verursachen kann.

### 6. **Schnellere Ein-/Ausgabe (I/O)**
   - Polars ist für effiziente I/O-Operationen optimiert. Es kann Daten aus Formaten wie Parquet oder Arrow direkt von der Festplatte lesen, ohne sie vollständig in den Arbeitsspeicher zu laden. Dies reduziert sowohl die Verarbeitungszeit als auch den Speicherverbrauch erheblich.


Einen ausführlichen Vergleich zum Einlese von Daten in pandas und polars können wir hier finden: [Polars vs Pandas](https://www.linkedin.com/pulse/polars-vs-pandas-benchmarking-performances-beyond-l6svf/)

Neben Polars bietet auch Spark eine performante Alternative zu Pandas. Wir werden uns in diesem Fall auf Polars beschränken, da es in lokalen Umgebungen in der Regel performanter ist. Spark hingegen ist für verteilte Systeme und Big Data-Anwendungen optimiert.

Einen weiteren Vergleich für die Frage, wann pandas, polars oder spark verwendet werden sollte, finden wir hier: [Polars vs Pandas vs Spark](https://betterprogramming.pub/pandas-spark-and-polars-when-to-use-which-f4e85d909c6f). Zusammenfassend wird aus der Quelle folgendes empfohlen:


| Anwendungsfall                                                            | Empfehlung | Begründung                                                                                                            |
| ------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------- |
| Kleinere Datensätze                                                       | Polars     | Gute Standardwahl für kleinere Datenmengen                                                                            |
| Kleinere Datensätze mit begrenzter CPU-Auslastung                         | Pandas     | Optimiert für niedrige CPU-Auslastung                                                                                 |
| Große DataFrames mit verteiltem Rechnen                                   | Spark      | Schnellste Ausführungszeit, jedoch hohe Spitzen bei Speicher- und CPU-Auslastung                                      |
| Vorhersehbare Speicher- und CPU-Nutzung bei kleinen und großen DataFrames | Polars     | Stabile, vorhersehbare Nutzung von Speicher und CPU, auch bei größeren Datensätzen, längere Ausführungszeit als Spark |

Aktuell wird für lokale Entwicklungsumgebungen die Verwendung von Polars empfohlen.