# Erste Schritte mit Polars

Polars ähnelt sich in der Syntax zu Pandas. So können wir auch hier mit `DataFrame`-Objekten arbeiten. 

```python
import polars as pl

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [24, 25, 26, 27],
    'city': ['Berlin', 'Hamburg', 'Munich', 'Cologne']
}

df = pl.DataFrame(data)
print(df)
```

```
shape: (4, 3)
┌─────────┬─────┬─────────┐
│ name    ┆ age ┆ city    │
│ str     ┆ i64 ┆ str     │
├─────────┼─────┼─────────┤
│ Alice   ┆ 24  ┆ Berlin  │
│ Bob     ┆ 25  ┆ Hamburg │
│ Charlie ┆ 26  ┆ Munich  │
│ David   ┆ 27  ┆ Cologne │
└─────────┴─────┴─────────┘
```

Wir können auch die Daten filtern, sortieren und gruppieren. 

```python
filtered = df.filter(pl.col('age') > 25)
print(filtered)
```

```
shape: (2, 3)
┌─────────┬─────┬─────────┐
│ name    ┆ age ┆ city    │
│ str     ┆ i64 ┆ str     │
├─────────┼─────┼─────────┤
│ Charlie ┆ 26  ┆ Munich  │
│ David   ┆ 27  ┆ Cologne │
└─────────┴─────┴─────────┘
```

Anders als bei Pandas müssen wir hier die Spaltennamen als `pl.col('name')` angeben.

```python
sorted_df = df.sort('age', reverse=True)
print(sorted_df)
```

```
shape: (4, 3)
┌─────────┬─────┬─────────┐
│ name    ┆ age ┆ city    │
│ str     ┆ i64 ┆ str     │
├─────────┼─────┼─────────┤
│ David   ┆ 27  ┆ Cologne │
│ Charlie ┆ 26  ┆ Munich  │
│ Bob     ┆ 25  ┆ Hamburg │
│ Alice   ┆ 24  ┆ Berlin  │
└─────────┴─────┴─────────┘
```

## Daten lesen und filtern

Einen überblick zu den Einlesefunktion von Polars finden wir in der [Dokumentation](https://docs.pola.rs/user-guide/io/). Hier finden wir Funktionen für die gängigen Datenformate, wie CSV, Parquet, JSON, aber auch für Datenbanken. Im Folgenden werden wir das Einlesen und Filtern auf Basis von CSV-Dateien zeigen. Dafür verwenden wir nachfolgend den Datensatz [FoodData_Central_csv_2024-04-18](https://fdc.nal.usda.gov/download-datasets.html) (Full Download of All Data Types).

```python
df = pl.read_csv('../datasets/FoodData_Central_csv_2024-04-18/food_nutrient.csv')
print(df)
```

!!! note
    Das Einlesen der Datei food_nutrient.csv (Größe 1,83 GB) benötigt auf einem MacBook Pro mit 16 GB RAM unter Verwendung von Polars ca. 2 Sekunden. Pandas benötigt für die gleiche Datei ca. 15 Sekunden.

Wir können die Performance unseres Einlesens noch weiter verbessern, indem wir auf die Lazy API von Polars zurückgreifen. Hierbei wird die Datei nicht sofort eingelesen, sondern erst, wenn wir die Daten wirklich benötigen. 

```python
q = pl.pl.scan_csv('../datasets/FoodData_Central_csv_2024-04-18/food_nutrient.csv')
df = q.collect()
print(df)
```
Dies kann insbesondere dann nützlich sein, wenn wir die Daten früher oder später filtern oder manupulieren möchten. Mehr dazu später.

Haben wir die Datei, können wir das DataFrame filtern und manupulieren. Zu unterschieden ist hierbei zwischen den Funktionen `filter` und `select`. `filter` wird verwendet, um Zeilen zu filtern, während `select` verwendet wird, um Spalten zu filtern.


Mit select können wir aus unserem DataFrame beispielweise die Spalten `nutrient_id`, `amount` und `percent_daily_value` auswählen.
```python
selected = df.select(
    pl.col('nutrient_id'),
    pl.col('amount'),
    pl.col('percent_daily_value')
)
print(selected)
```

Mit filter können wir die Zeilen filtern, die beispielsweise einen `percent_daily_value` von mehr als 10 haben.
```python
filtered = df.filter(pl.col('amount') > 10)
print(filtered)
```

Wir können auch Spalten ein Alias vergeben, um die Spaltennamen zu verdeutlichen. 
```python

renamed = df.select(
    pl.col('nutrient_id').alias('ID'),
    pl.col('amount').alias('Amount'),
    pl.col('percent_daily_value').alias('Percent Daily Value')
)
print(renamed)
```

## Manupulation von Spalten

Polars bietet auch die Möglichkeit, Spalten zu manupulieren. So können wir beispielsweise eine neue Spalte hinzufügen, die die Spalten `amount`und `unit` zusammenfügt und als `amount_unit` speichert. 

```python
df.with_columns(
    (pl.col('amount').cast(str) + ' ' + pl.col('unit_name')).alias('amount_with_unit')
)
print(df)
```

Ein ähnliches Resultat können wir über ein `select` erreichen. In diesem Fall erhalten wir jedoch nur die gewählten Spalten, während wir bei `with_columns` das gesamte DataFrame erhalten.

```python
df.select(
    (pl.col('amount').cast(str) + ' ' + pl.col('unit_name')).alias('amount')
)
print(df)
```


## Join und Merge

Polars bietet auch die Möglichkeit, DataFrames zu joinen und zu mergen. Um beispielsweise die Namen der Nutrients zu den Nutrient IDs hinzuzufügen, können wir die DataFrames `food_nutrient.csv` und `nutrient.csv` joinen.

```python
df1 = pl.read_csv('../datasets/FoodData_Central_csv_2024-04-18/food_nutrient.csv')
df2 = pl.read_csv('../datasets/FoodData_Central_csv_2024-04-18/nutrient.csv')

joined = df1.join(df2, 'nutrient_id', left_on='nutrient_id', right_on='id')
print(joined)
```

!!! note
    Spätestens beim Joinen weiterer Tabellen wird Pandas langsam aber sicher zu einem Bottleneck bei der Analyse der Daten.





