## Pandas
Data manipulation and transformation library built on the top of *Numpy* and *Matplotlib*. 

### Used Functions in different programs
* **pd.DataFrame()** - Preparaing a pandas dataframe
* **pd.read_csv()**- Use to read csv files.

|parameters | used cases                  |Example  |
|-----------|-----------------------------|---------|
|usecols=[ ]|read particular column only  |[1](https://www.youtube.com/)|
|nrows=500  |skip first 500 rows          |         |
|           |                             |         |

* **df.shape** - Pandas attribute(not a method) use to find the shape of a dataframe df
* **df.columns** - Pandas attribute use to find the columns of a dataframe df
* **df.dtypes** - check datatype of each column
* **df.drop()** - ` df.drop([list of columns to drop], axis=1, inplace=True)` | [example](https://www.youtube.com/)
* **df.head()** - `df.head(5)` print first 5 rows of a dataframe
* **df.tail()** - `df.tail(5)` print last 5 rows of a dataframe
* **df.info()** - Get info whether a dataframe has any null object
* **df['textField'].str.contains('anyWord',case=False)** - Calculate how many times a particular word appered in each row of a dataframe df['textField'] and make case insensitive.
* **df.isna()** - checking for the number of missing values | `df.isna().sum()` | `df.isna().any()`
* **df.dropna()** - remove rows containing missing values
* **df.fillna(0)** - fill 0 for all missing values in a df
* **df.loc[]** - `df.loc[1:6]` | `df.loc['A':"D"]`| multilevel indexed slicing-`df.loc[("Country1",'city1'):('country2','city2'),colA:colD]` | `df.loc['1998':'2008']`(dates in ISO 8601 format i.e., yyyy-mm-dd)
* **df.iloc[]** - `df.iloc[1:6,3:9]`
* **df[col].min()**
* **df[col].max()**
* **df[col].mean()** - default is columnwise(axis='index') | use df.mean(axis='columns') to get mean of each row
* **df[col].std()**
* **df[col].medain()**
* **df[col].mode()**
* **df[col].var()**
* **df[col].quantile()**
* **df[col].sum()**
* **df[timeSeriesCol].resample("1 min").mean()** - Resampling df for every minute timeframe. 
* **df[col].describe()** - Computes summary statistics about numerical columns
* **df['height'].agg(pct60)** - aggregate | `def pct60(col): return col.quantile(0.6)` | `df[[colA,colB]].agg(pct60)` | `df[colA].agg([pct60,pct70])` | `def IQR(col): col.quantile(0.75) - col.quantile(0.25)`| `df.groupby('CategoricalCol').agg({'NumCol':'count'})`
* **df[colA].cumsum()** - cumulative sum
* **df[colA].cummax()** - cumulative maximum
* **df[colA].cummin()** - cumulative minimum
* **df[colA].cumprod()** - cumulative product
* **df.values()** - Get data as a 2-D Numpy array
* **df.columns** - Pandas attribute to get column names
* **df.index** - Pandas attribute to get index values
* **df[col].isin([0,1])** - `df[df['survival'].isin([0,1])]` | `df.loc[[0,1]]` if index is set as target column to filter
* **df.drop_duplicates(subset=[colA,colB])** - Removing duplicate items from columns
* **df[col].value_counts(sort=True)** - count categorical data in a column [col] 

|parameters    | used cases                  |Example  |
|--------------|-----------------------------|---------|
|sort=True     |use to sort categorical data in a col. based upon count| |
|normalize=True|normalizing categorical data count| |

* **df.groupby()** - 

|method                |used program                 |Example  |comment |
|----------------------|-----------------------------|---------|--------|
|`.mean()`             |type1`df.groupby('categoricalCol')["numericalCol"].mean()` ||type1 of `.groupby` ~ type1 of `.pivot_table`|
|`.max() .min() .sum()`|2`df.groupby("catCol")["numCol"].agg([max,min,sum])`       |||
|                      |3`df.groupby(['catColA','catColB'])["numCol"].mean()`      |||
|using numpy func      |`df.groupby('catCol')[['numColA','numColB']].agg([min,max,np.mean,np.median])`|||

* **df.pivot_table()** - 

|parameters    |used program                 |Example  |Comment|
|--------------|-----------------------------|---------|-------|
|default-mean()|type1 `df.pivot_table(values="numCol",index="catCol")`            |||
|`aggfunc`     |1`df.pivot_table(values="numCol",index="CatCol",aggfunc=np.mean)` |||
|              |2`df.pivot_table(values="numCol",index="CatCol",aggfunc=[np.mean,np.median])`  |||
| `columns`    |3`df.pivot_table(values="numCol",index="catColA",columns=catColB)`|||
| `fill_value` |3`df.pivot_table(values="numCol",index="catColA",columns=catColB,fill_value=0)`||replace missing value with real(imputation), not a problem in .`groupby`|
| `margins`    |3`df.pivot_table(values="numCol",index="catColA",columns=catColB,fill_value=0,margins=True)`||getting mean in last column excluding missing value(or imputed by fill_value)|

* **[df.melt][melt](id_vars=[categoricalCol(s)],value_vars=[numCol(s)],var_name=[xyz],value_name=abc)** - *unpivoting table*
* **df.set_index('colName')** - df.set_index([colA,colB]) - multi-level index(or hierarchical index) | access - df.loc[[list of tuples of multilevel indexes]]
* **df.reset_index()** - reset your index of the dataframe | **df.reset_index(drop=True)** - for dropping the previous index
* **df.sort_index()** - df.sort_index(level=[colA,colB],ascending=[False,False])
* **df.sort_values()** - `df.sort_values([colA,colB,colC],ascending=[True,False,True],inplace=True,)`
* **df.transpose() or df.T**
* **df[col].unique()** - find unique elements in a column
* **df.plot.line(rot=30)**
* **df.plot(kind=[bar,hist,scatter,etc],title=,rot=)** 
* **df.hist(alpha=0.15)** - 15% transparency[0-transparent & 1-opaque]
* **df.isna().sum().plot(kind='bar')**
* **Joins**

|Join          | Function                                           | Example |comment|
|--------------|----------------------------------------------------|---------|-------|
|Inner(default)|df1.merge(df2,on="commonCol",suffixes=["_s1","_s2"])|`df1.merge(df2, on='commonCol', suffixes=('_s1','_s2')).aggregate({"ColName":"count"})`| |
|Left          |df1.merge(df2,on='commonCOl',how='left')            |         |       |
|Right         |df1.merge(df2,how='right',left_on="A",right_on="B")|         |if common col have *different* name if two dfs|
|Outer         |df1.merge(df2,on='commonCOl',how='Outer')          |         |       |
|Self          |df.merge(df,left_on='A',right_on='B',suffixes=["_s1","_s2"])||       |
|on index      |`df1.merge(df2,left_on='A',left_index=True,right_on='B',right_index=True)` `df1.merge(df2,left_index=True,right_index=True)`|||

* **df.concat([df1,df2,df3],ignore_index=True)** - df.concat([df1,df2,df3],ignore_index=True,join='inner',keys=["df1K1",'k2','k3'])(show columns that are in all tables)
* **df.append([df1,df2,df3],ignore_index=True)**
* **pd.merge_ordered(df1,df2,on='commonCol',suffixes=["_s1","_s2"],fill_method='ffill')** - ffill(forward fill) is a method to fill all missing value with previous one(defalut-'outer join' check it)
* **[pd.merge_asof][merge_asof](df1,df2,on='col',suffixes=["_s1","_s2"],direction='forward')** 


[merge_asof]: https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.merge_asof.html
[melt]: https://pandas.pydata.org/docs/reference/api/pandas.melt.html
