---
library: pandas
language: python
---

# pandas

## Save dataframe

Save a pandas dataframe to a csv file without an index column

<!-- pd-save -->

```python
pd.to_csv("${1:path}", index_col=False)
```

## Read dataframe

Read a pandas dataframe to a csv file without an index column

<!-- pd-read -->

```python
pd_read_csv("${1:path}", index_col=False)
```

## Convert column to numeric

Convert a pandas series datatype to numeric, changing non-numeric values to NaN

<!-- pd-col-numeric -->

```python
pd.to_numeric(${1:df}["${2:Column Name}"], errors="coerce")
```

## Get matching rows

Grab dataframe rows where column = specific value

<!-- pd-match-rows|pd-get -->

```python
${4:df_s} = ${1:df}.loc[${1:df}["${2:column}"] == "${3:value}"]
```

## Describe dataframe

Get the description of listed columns in the dataframe

<!-- pd-describe|pd-stats -->

```python
${1:df}[["${2:column1}", "${3:column2}"]]
```

## Replace values

Replace specific values in a dataframe with new ones

<!-- pd-val-replace|pd-sub -->

```python
${1:df}.replace(${2:0},${3:np.NaN})
```

## N Largest Values

Select the N largest values from a column in a dataframe.

<!-- pd-val-nlargest -->

```python
${1:df}.nlargest(${2:NumOfValues},'${3:ColumnName}')
```

## N Smallest Values

Select the N smallest values from a column in a dataframe.

<!-- pd-val-nsmallest -->

```python
${1:df}.nsmallest(${2:NumOfValues},'${3:ColumnName}')
```

## Create pivot table

Create a pivot table, which aggregates values of one column along different columns

<!-- pd-pivot -->

```python
${4:new_df} = pd.pivot_table(${1:df}, values="${2:valueColumn}", columns=[${3:columnsToGroupBy}])
```

## Group by with count

Group by a set of columns, and then count the number of occurrences of a value in another column within those groups

<!-- pd-groupby-count -->

```python
${4:newDf} = ${1:df}.groupby("${2:displayColumn}")["${3:aggregatedColumn}"].count()
```

## Group By with Mean

Group By with Mean Aggregate.

<!-- pd-groupby-mean -->

```python
${4:newDf} = ${1:df}.groupby("${2:displayColumn}")["${3:aggregatedColumn}"].mean()
```

## Apply Function Single Column

Apply function to single column.

<!-- pd-apply-col -->

```python
def ${3}(x):
	return ${4:x*x}

${1:df}["${2:ColumnName}"] = ${1:df}["${2}"].apply(${3:yourFunction})
```

## Apply Function Multiple Columns

Apply function to multiple columns.

<!-- pd-apply-cols -->

```python
def ${3}(x):
	return x*x

${1:df}[[${2:Columns}] = ${1:df}[[${2}]].apply(${3:yourFunction})
```

## Apply Column Lambda

Apply inline function/lambda to a column.

<!-- pd-apply-lambda -->

```python
${1:df}["${2:ColumnOne}"] = ${1:df}["${2}"].apply(lambda x: ${3:x*x})$0
```
