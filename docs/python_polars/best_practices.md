# Best Practices für die Arbeit mit Polars

#### 1. **Nutze Lazy Execution**

- **Do**: Verwende `LazyFrames`, um deine Abfragen zu optimieren. Lass Polars die gesamte Abfrage analysieren und optimieren, bevor du die Ausführung anforderst.

  ```python
  lazy_df = df.lazy().filter(pl.col("age") > 30).groupby("city").agg(pl.col("salary").mean())
  result = lazy_df.collect()
  ```

- **Don't**: Vermeide es, `EagerFrames` ohne Grund zu verwenden, da dies zu ineffizienten Berechnungen führen kann, die Ressourcen verschwenden.

  ```python
  result = df.filter(pl.col("age") > 30).groupby("city").agg(pl.col("salary").mean())  # ineffizient
  ```

---

#### 2. **Optimierung durch Expression API**

- **Do**: Nutze die Expression API, um klare und lesbare Abfragen zu erstellen, die Polars helfen, deine Absichten zu verstehen.

  ```python
  result = df.select([
      pl.col("salary").mean().alias("avg_salary"),
      pl.col("age").min().alias("min_age")
  ])
  ```

- **Don't**: Vermeide es, mehrere Schritte in einer einzelnen Pipeline ohne Verwendung der Expression API zu kombinieren, da dies die Lesbarkeit und Wartbarkeit deines Codes beeinträchtigen kann.

  ```python
  result = df.with_column(pl.col("salary") * 1.1).select("salary", "age")  # nicht optimal
  ```

---

#### 3. **Datenformate und I/O-Optimierung**

- **Do**: Wähle effiziente Datenformate wie Parquet oder Arrow für den Import und Export, um die Leistung zu steigern.

  ```python
  df.write_parquet("data.parquet")
  ```

- **Don't**: Verwende keine textbasierten Formate wie CSV für große Datenmengen, da dies die Ladezeiten und die Effizienz negativ beeinflussen kann.

  ```python
  df.to_csv("data.csv")  # ineffizient für große Datenmengen
  ```

---

#### 4. **Nutze die Vorteile von Multithreading**

- **Do**: Lass Polars die Vorteile der Multithreading-Verarbeitung nutzen, indem du Operationen auf großen DataFrames durchführst, die parallelisiert werden können.

  ```python
  result = df.filter(pl.col("age") > 30).groupby("city").agg(pl.col("salary").mean())
  ```

- **Don't**: Vermeide es, manuell Threads zu erstellen oder Daten selbst zu partitionieren. Polars kümmert sich automatisch um die Parallelisierung.

  ```python
  # Manuelles Multithreading ist nicht notwendig
  ```

---

#### 5. **Speicher- und Typmanagement**

- **Do**: Verwende die richtigen Datentypen für deine Spalten (z.B. `Int32` statt `Int64`), um den Speicherverbrauch zu optimieren.

  ```python
  df = df.with_columns(pl.col("id").cast(pl.Int32))  # Speichereffizient
  ```

- **Don't**: Vermeide es, unnötige Datentypen zu verwenden, die mehr Speicherplatz als nötig beanspruchen.

  ```python
  df = df.with_columns(pl.col("id").cast(pl.Int64))  # nicht optimal, wenn Int32 ausreichend ist
  ```

---

#### 6. **Effiziente Filterung und Aggregation**

- **Do**: Wende Filteroperationen so früh wie möglich an, um die Anzahl der verarbeiteten Zeilen zu reduzieren.

  ```python
  df.filter(pl.col("age") > 30).groupby("city").agg(pl.col("salary").mean())
  ```

- **Don't**: Vermeide es, zuerst Aggregationen durchzuführen, bevor du die Daten filterst, da dies die Verarbeitung unnötig aufblähen kann.

  ```python
  df.groupby("city").agg(pl.col("salary").mean()).filter(pl.col("age") > 30)  # ineffizient
  ```

---

#### 7. **Profiling und Debugging**

- **Do**: Nutze die Funktionen `describe_plan()` und `describe_optimized_plan()`, um den Query Plan zu analysieren und Leistungsengpässe zu identifizieren.

  ```python
  lazy_df.describe_plan()
  ```

- **Don't**: Ignoriere die Möglichkeit zur Profilierung und führe nicht optimierte Abfragen aus, ohne deren Leistung zu prüfen.

  ```python
  # Keine Profilierung macht die Performance schwer zu bewerten
  ```

---

#### 8. **Fallstricke vermeiden**

- **Do**: Speichere Zwischenergebnisse in Variablen, um redundante Berechnungen zu vermeiden.

  ```python
  filtered_df = df.filter(pl.col("age") > 30)
  result = filtered_df.groupby("city").agg(pl.col("salary").mean())
  ```

- **Don't**: Führe gleiche Berechnungen mehrfach durch, da dies unnötige Ressourcen verbraucht.

  ```python
  result = df.filter(pl.col("age") > 30).groupby("city").agg(pl.col("salary").mean())
  result2 = df.filter(pl.col("age") > 30).groupby("city").agg(pl.col("salary").sum())  # redundant
  ```

---

#### 9. **Datenvalidierung und -bereinigung**

- **Do**: Behandle fehlende Werte und andere Datenprobleme, um die Integrität deiner Analysen sicherzustellen.

  ```python
  df.fill_null(0)  # Fehlende Werte mit 0 ersetzen
  ```

- **Don't**: Ignoriere fehlende oder ungültige Daten, da dies zu fehlerhaften Ergebnissen führen kann.

  ```python
  # Fehlende Werte werden nicht behandelt, was die Analyse beeinträchtigen kann
  ```

---

#### 10. **Dokumentation und Community**

- **Do**: Nutze die offizielle Polars-Dokumentation, um dich über Funktionen und Best Practices zu informieren.

  ```python
  # Lese die Dokumentation auf der offiziellen Polars-Website
  ```

- **Don't**: Verlasse dich nicht ausschließlich auf Tutorials oder externe Quellen ohne Verweis auf die offizielle Dokumentation, da diese veraltet oder ungenau sein können.

  ```python
  # Vermeide das Vertrauen auf potenziell ungenaue Informationen
  ```

---

Mit diesen **Do's and Don'ts** erhältst du klare Anleitungen, wie du Polars effektiv nutzen kannst, um die Effizienz und Leistung deiner Datenanalysen zu maximieren.