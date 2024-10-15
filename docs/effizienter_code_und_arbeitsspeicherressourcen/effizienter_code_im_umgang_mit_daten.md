## Richtlinien zur Erstellung von effizientem Code

Effizienter Code ist entscheidend für die Performance und Wartbarkeit unserer Datenanalysen. Hier sind einige Richtlinien, die wir befolgen sollten, um sowohl mit **Pandas** als auch mit **Polars** effektiv zu arbeiten.

### Pandas

#### Vektorisierung nutzen

Mit Pandas können wir vektorisierte Operationen durchführen, um ganze Spalten auf einmal zu bearbeiten und so die Leistung erheblich zu steigern.

**Beispiel**:

```python
import pandas as pd

df = pd.DataFrame({'Original_Spalte': [1, 2, 3, 4, 5]})
df['Neue_Spalte'] = df['Original_Spalte'] * 2  # Vektorisierte Operation
print(df)
```

#### Effizientes Einlesen von Daten

- **CSV-Dateien**: Nutzen wir die `dtype`-Option, um den Speicherbedarf zu optimieren.
- **Excel-Dateien**: Mit `usecols` können wir gezielt nur die benötigten Spalten laden.
- **SQL-Datenbanken**: Abfragen sollten so gestaltet sein, dass nur relevante Daten geladen werden.

**CSV-Beispiel**:

```python
df = pd.read_csv('daten.csv', dtype={'Spalte1': 'int32', 'Spalte2': 'float32'})
```

#### Speicherverbrauch optimieren

Datentypen wie `category` helfen, Speicher zu sparen und die Performance zu verbessern.

**Beispiel**:

```python
df['Kategorische_Spalte'] = df['Kategorische_Spalte'].astype('category')
```

#### Speicherplatz freigeben

Wir können den Speicher durch Löschen nicht mehr benötigter DataFrames freigeben.

```python
del df
```

### Polars

#### Vektorisierung nutzen

Auch Polars bietet leistungsstarke vektorisierte Operationen, die wir nutzen können.

**Beispiel**:

```python
import polars as pl

df = pl.DataFrame({'Original_Spalte': [1, 2, 3, 4, 5]})
df = df.with_columns((pl.col('Original_Spalte') * 2).alias('Neue_Spalte'))
print(df)
```

#### Effizientes Einlesen von Daten

- **CSV-Dateien**: Der `dtypes`-Parameter hilft, den Speicherbedarf zu kontrollieren.
- **Excel-Dateien**: Excel-Dateien müssen erst mit Pandas eingelesen und dann in Polars umgewandelt werden.
- **SQL-Datenbanken**: SQL-Abfragen in Polars sollten ebenfalls zielgerichtet sein.

**CSV-Beispiel**:

```python
df = pl.read_csv('daten.csv', dtypes={'Spalte1': pl.Int32, 'Spalte2': pl.Float32})
```

#### Speicherverbrauch optimieren

Wir sollten die `Categorical`-Klasse verwenden, um den Speicherverbrauch effizient zu gestalten.

**Beispiel**:

```python
df = df.with_columns(pl.col('Kategorische_Spalte').cast(pl.Categorical))
```

#### Speicherplatz freigeben

Sicherstellen, dass wir den Speicher freigeben, indem wir große DataFrames löschen, wenn sie nicht mehr benötigt werden.

```python
del df
```

### Wichtige Erkenntnisse

- **Vektorisierung** ist unerlässlich, um die Verarbeitungsgeschwindigkeit zu maximieren.
- **Gezieltes Einlesen von Daten** vermeidet unnötige Speicherbelastung.
- **Optimierte Datentypen** sparen Speicherplatz und verbessern die Leistung.
- **Speicherfreigabe** verhindert Speicherlecks und gewährleistet die Effizienz von Anwendungen. 