## Pandas
Data manipulation library built on the top of Numpy and Matplotlib. 

### Used Functions in different coding part
* **pd.read_csv()**- Use to read csv files.

|parameters | used cases                  |Example  |
|-----------|-----------------------------|---------|
|usecols=[ ]|read particular column only  |[1](https://www.youtube.com/)|
|nrows=500  |skip first 500 rows          |         |
|hello      |                             |         |

* **df.shape** - Pandas attribute(not a method) use to find the shape of a dataframe df
* **df.columns** - Pandas attribute use to find the columns of a dataframe df
* **df.drop()** - ` df.drop([list of columns to drop], axis=1, inplace=True)` | [example](https://www.youtube.com/)
* **df.head()** - `df.head(5)` print first 5 rows of a dataframe
* **df.tail()** - `df.tail(5)` print last 5 rows of a dataframe
* **df.info()** - Get info whether a dataframe has any null object
* **df[col].min()**
* **df[col].max()**
* **df[col].mean()**
* **df[col].std()**
* **df[col].medain()**
* **df[col].mode()**
* **df[col].var()**
* **df[col].quantile()**
* **df[col].sum()**
* **df[col].describe()** - Computes summary statistics about numerical columns
* **df['height'].agg(pct60)** - aggregate | `def pct60(col): return col.quantile(0.6)` | `df[[colA,colB]].agg(pct60)` | `df[colA].agg([pct60,pct70])` | `def IQR(col): col.quantile(0.75) - col.quantile(0.25)`
* **df[colA].cumsum()** - cumulative sum
* **df[colA].cummax()** - cumulative maximum
* **df[colA].cummin()** - cumulative minimum
* **df[colA].cumprod()** - cumulative product
* **df.values()** - Get data as a 2-D Numpy array
* **df.columns** - Pandas attribute to get column names
* **df.index** - Pandas attribute to get index values
* **df.sort_values()** - `df.sort_values([colA,colB,colC],ascending=[True,False,True],inplace=True,)`
* **df[col].isin([0,1])** - use `.isin()` instead of `or |` operator if comparison is with many | `df[df['survival'].isin([0,1])]`
* **df.drop_duplicates(subset=[colA,colB])** - Removing duplicate items from columns
* **df[col].value_counts(sort=True)** - count categorical data in a column [col] 

|parameters | used cases                  |Example  |
|-----------|-----------------------------|---------|
|sort=True  |use to sort categorical data in a col. based upon count| |
|normalize=True|normalizing categorical data count| |

* **df.groupby()** - 

|method     |used program                 |Example  |
|-----------|-----------------------------|---------|
|`.mean()`  | `df.groupby('categorical_col')["numerical_col(s)"].mean()` |  |
|`.max() .min() .sum()`|`df.groupby("cat. col")["num_col(s)"].agg([max,min,sum])`|  |
|  | `df.groupby(['cat.ColA','cat.ColB'])["num_col(s)"].mean()`|  |
