# Lazy vs. Eager API

Polars bietet zwei APIs, die wir in unseren Analysen verwenden können: die Lazy API und die Eager API. Die Lazy API ist ein wesentlicher Bestandteil von Polars und ermöglicht es uns, Berechnungen zu verzögern, bis wir die Daten tatsächlich benötigen. Dies kann insbesondere bei der Verarbeitung großer Datensätze von Vorteil sein, da unnötige Berechnungen vermieden werden. Die Eager API hingegen führt Berechnungen sofort aus und gibt das Ergebnis zurück.


![Lazy vs. Eager API](/pictures/Eager_vs_Lazy.webp)
## Lazy API

In der Lazy API werden Berechnungen nicht sofort ausgeführt, sondern erst, wenn wir die Daten wirklich benötigen. Die Lazy API erstellt zunächst einen optimierten Ausführungsplan, bevor sie die Daten verarbeitet. Dies ermöglicht eine deutliche Effizienzsteigerung, da unnötige Berechnungen vermieden werden. 

Ein Beispiel für die Verwendung der Lazy API ist das Einlesen einer CSV-Datei mit `pl.scan_csv()`:

```python
q = pl.scan_csv('data.csv')
df = q.collect()
print(df)
```

In diesem Beispiel wird die CSV-Datei nicht sofort eingelesen, sondern erst, wenn wir die Daten tatsächlich benötigen. Dies kann insbesondere dann nützlich sein, wenn wir die Daten filtern oder manipulieren möchten.

Wir können in `q` auch eine komplexere Query speichern, die wir später ausführen möchten:

```python
# Variante 1
q = pl.scan_csv('data.csv')
q = q.filter(pl.col('amount') > 10)
q = q.select(pl.col('amount'), pl.col('unit'))
df = q.collect()
print(df)

# Variante 2
q = (
    pl.scan_csv('data.csv')
    .filter(pl.col('amount') > 10)
    .select(pl.col('amount'), pl.col('unit'))
)
df = q.collect()
```

Polars wird bei Lazy Operationen die Query optimieren und nur die benötigten Daten verarbeiten. Dies kann die Performance erheblich verbessern, insbesondere bei großen Datensätzen. Wir können uns dies am beisoiel des Query-Plans anzeigen lassen:

```python
...
q.show_plan()
```

![Query Plan optimized](/pictures/query_plan_opt.png)

Wenn wir die Optimierung ausschalten möchten, können wir das über das Keyword Argument `optimized=False`
    
```python
...
q.show_plan(optimized=False)
```

![Query Plan not optimized](/pictures/query_plan_not_opt.png)

Der Query Plan ist von Unten nach Oben zu lesen. Das $\sigma$ zeigt an, dass es sich um eine Filter Operation handelt Konkret weist es in diesem Fall darauf hin, dass wir nur Zeilen wählen. bei denen `nutrient_id == 2047` gilt. Mit dem $\pi$ wird eine Projektion durchgeführt (also in diesem Fall das Wählen eines Subsets). Die Zahhl hinter dem $\pi$ gibt an, wie viele Spalten wir auswählen.


Wir können uns den Query Plan auch in einer SQL ähnlichen Syntax anzeigen lassen:

```python
...
print(q.explain(optimized=False))
```

Dies führt zu der nachfolgenden Ausgabe:

```
FILTER [(col("nutrient_id")) == (2047)] FROM
  Csv SCAN [../datasets/FoodData_Central_csv_2024-04-18/food_nutrient.csv]
  PROJECT */13 COLUMNS
```

## Eager API

Im Gegensatz zur Lazy API führt die Eager API Berechnungen sofort aus und gibt das Ergebnis zurück. Die Eager API eignet sich gut für kleinere Datensätze, bei denen die Verzögerung durch die Lazy API nicht erforderlich ist.

Ein Beispiel für die Verwendung der Eager API ist die direkte Filterung von Daten mit `pl.col()`:

```python
df = pl.scan_csv('data.csv')
filtered = df.filter(pl.col('amount') > 10)
print(filtered)
```

In diesem Beispiel wird die Filterung der Daten sofort ausgeführt, ohne dass ein Ausführungsplan erstellt wird. Die Eager API eignet sich gut für kleinere Datensätze, bei denen die Verzögerung durch die Lazy API nicht erforderlich ist. 

Im Hintergrund greift die Eager API aus Performance Gründen teilweise auf die Lazy API zurück, um die Berechnungen durchzuführen. Die Eager API ist daher eine bequeme Möglichkeit, um schnell und einfach Daten zu filtern und zu manipulieren.
