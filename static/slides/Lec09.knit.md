---
title: "more pandas"
subtitle: "Lecture 09"
author: "Dr. Colin Rundel"
footer: "Sta 663 - Spring 2023"
format:
  revealjs:
    theme: slides.scss
    transition: fade
    slide-number: true
    self-contained: true
execute:
  echo: true
---






# Index objects

## Columns and Indexes

When constructing a DataFrame we can specify the indexes for both the rows (`index`) and columns (`columns`),

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df = pd.DataFrame(
  np.random.randn(5, 3), 
  columns=['A', 'B', 'C']
)
df
```

::: {.cell-output .cell-output-stdout}
```
          A         B         C
0 -1.024725 -0.528534  1.374409
1 -0.278814  0.684864 -1.263935
2 -2.074225 -0.367352  0.797532
3  0.963922  0.880177 -1.181410
4  0.673957  0.709230  0.454526
```
:::

```{.python .cell-code}
df.columns
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', 'C'], dtype='object')
```
:::

```{.python .cell-code}
df.index
```

::: {.cell-output .cell-output-stdout}
```
RangeIndex(start=0, stop=5, step=1)
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df = pd.DataFrame(
  np.random.randn(3, 3), 
  index=['x','y','z'], 
  columns=['A', 'B', 'C']
)
df
```

::: {.cell-output .cell-output-stdout}
```
          A         B         C
x -0.228518 -1.604281  0.635195
y  1.954459 -0.320655 -0.103808
z -1.044734  0.844904  0.056481
```
:::

```{.python .cell-code}
df.columns
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', 'C'], dtype='object')
```
:::

```{.python .cell-code}
df.index
```

::: {.cell-output .cell-output-stdout}
```
Index(['x', 'y', 'z'], dtype='object')
```
:::
:::

:::
::::


## Index objects

pandas' `Index` class and its subclasses provide the infrastructure necessary for lookups, data alignment, and other related tasks. You can think of them as being an immutable *multiset* (duplicate values are allowed).


::: {.cell}

```{.python .cell-code}
pd.Index(['A','B','C'])
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', 'C'], dtype='object')
```
:::

```{.python .cell-code}
pd.Index(['A','B','C','A'])
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', 'C', 'A'], dtype='object')
```
:::

```{.python .cell-code}
pd.Index(range(5))
```

::: {.cell-output .cell-output-stdout}
```
RangeIndex(start=0, stop=5, step=1)
```
:::

```{.python .cell-code}
pd.Index(list(range(5)))
```

::: {.cell-output .cell-output-stdout}
```
Int64Index([0, 1, 2, 3, 4], dtype='int64')
```
:::
:::



## Indexes as sets

While it is not something you will need to do very often, since Indexes are "sets" the various set operations and methods are available.


::: {.cell}

```{.python .cell-code}
a = pd.Index(['c', 'b', 'a'])
b = pd.Index(['c', 'e', 'd'])
```
:::



:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
a.union(b)
```

::: {.cell-output .cell-output-stdout}
```
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
```
:::

```{.python .cell-code}
a.intersection(b)
```

::: {.cell-output .cell-output-stdout}
```
Index(['c'], dtype='object')
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
a.difference(b)
```

::: {.cell-output .cell-output-stdout}
```
Index(['a', 'b'], dtype='object')
```
:::

```{.python .cell-code}
a.symmetric_difference(b)
```

::: {.cell-output .cell-output-stdout}
```
Index(['a', 'b', 'd', 'e'], dtype='object')
```
:::
:::

:::
::::

. . .

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
c = pd.Index([1.0, 1.5, 2.0])
d = pd.Index(range(5))

c.union(d)
```

::: {.cell-output .cell-output-stdout}
```
Float64Index([0.0, 1.0, 1.5, 2.0, 3.0, 4.0], dtype='float64')
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
e = pd.Index(["A","B","C"])
f = pd.Index(range(5))

e.union(f)
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', 'C', 0, 1, 2, 3, 4], dtype='object')
```
:::
:::

:::
::::


## Index metadata

You can attach names to an index, which will then show when displaying the DataFrame or Index,

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df = pd.DataFrame(
  np.random.randn(3, 3), 
  index=pd.Index(['x','y','z'], name="rows"),
  columns=pd.Index(['A', 'B', 'C'], name="cols")
)
df
```

::: {.cell-output .cell-output-stdout}
```
cols         A         B         C
rows                              
x    -0.203274 -0.077825 -0.357602
y    -1.042075  0.377500  0.125953
z    -0.678463  0.608896  0.366187
```
:::

```{.python .cell-code}
df.columns
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', 'C'], dtype='object', name='cols')
```
:::

```{.python .cell-code}
df.index
```

::: {.cell-output .cell-output-stdout}
```
Index(['x', 'y', 'z'], dtype='object', name='rows')
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
df.columns.rename("m")
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', 'C'], dtype='object', name='m')
```
:::

```{.python .cell-code}
df.index.set_names("n")
```

::: {.cell-output .cell-output-stdout}
```
Index(['x', 'y', 'z'], dtype='object', name='n')
```
:::

```{.python .cell-code}
df
```

::: {.cell-output .cell-output-stdout}
```
cols         A         B         C
rows                              
x    -0.203274 -0.077825 -0.357602
y    -1.042075  0.377500  0.125953
z    -0.678463  0.608896  0.366187
```
:::
:::

:::
::::

## Renaming indexes inplace

If you want to change the index names inplace either assign directly to the `name` attribute or use the `inplace=TRUE` argument with `rename()`.

::: {.small}

::: {.cell}

```{.python .cell-code}
df
```

::: {.cell-output .cell-output-stdout}
```
cols         A         B         C
rows                              
x    -0.203274 -0.077825 -0.357602
y    -1.042075  0.377500  0.125953
z    -0.678463  0.608896  0.366187
```
:::
:::

:::

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df.columns.name = "o"
df.index.name = "p"
df
```

::: {.cell-output .cell-output-stdout}
```
o         A         B         C
p                              
x -0.203274 -0.077825 -0.357602
y -1.042075  0.377500  0.125953
z -0.678463  0.608896  0.366187
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df.columns.rename("q", inplace=True)
df.index.rename("r", inplace=True)
df
```

::: {.cell-output .cell-output-stdout}
```
q         A         B         C
r                              
x -0.203274 -0.077825 -0.357602
y -1.042075  0.377500  0.125953
z -0.678463  0.608896  0.366187
```
:::
:::

:::
::::



## Indexes and missing values

It is possible for an index to contain missing values (e.g. `np.nan`) but this is generally a bad idea and should be avoided.


::: {.cell}

```{.python .cell-code}
pd.Index([1,2,3,np.nan,5])
```

::: {.cell-output .cell-output-stdout}
```
Float64Index([1.0, 2.0, 3.0, nan, 5.0], dtype='float64')
```
:::

```{.python .cell-code}
pd.Index(["A","B",np.nan,"D", None])
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', nan, 'D', None], dtype='object')
```
:::
:::


. . .

Missing values can be replaced via the `fillna()` method,


::: {.cell}

```{.python .cell-code}
pd.Index([1,2,3,np.nan,5]).fillna(0)
```

::: {.cell-output .cell-output-stdout}
```
Float64Index([1.0, 2.0, 3.0, 0.0, 5.0], dtype='float64')
```
:::

```{.python .cell-code}
pd.Index(["A","B",np.nan,"D", None]).fillna("Z")
```

::: {.cell-output .cell-output-stdout}
```
Index(['A', 'B', 'Z', 'D', 'Z'], dtype='object')
```
:::
:::



## Changing a DataFrame's index

::: {.small}
Existing columns can be made an index via `set_index()` and removed via `reset_index()`,
::: 





::: {.small}

::: {.cell}

```{.python .cell-code}
data
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
0  bar  one  z  1
1  bar  two  y  2
2  foo  one  x  3
3  foo  two  w  4
```
:::
:::

:::

. . .

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.set_index('a')
```

::: {.cell-output .cell-output-stdout}
```
       b  c  d
a             
bar  one  z  1
bar  two  y  2
foo  one  x  3
foo  two  w  4
```
:::

```{.python .cell-code}
data.set_index('c', drop=False)
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
c                
z  bar  one  z  1
y  bar  two  y  2
x  foo  one  x  3
w  foo  two  w  4
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
data.set_index('a').reset_index()
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
0  bar  one  z  1
1  bar  two  y  2
2  foo  one  x  3
3  foo  two  w  4
```
:::

```{.python .cell-code}
data.set_index('c').reset_index(drop=True)
```

::: {.cell-output .cell-output-stdout}
```
     a    b  d
0  bar  one  1
1  bar  two  2
2  foo  one  3
3  foo  two  4
```
:::
:::

:::
::::


## Creating a new index

New index values can be attached to a DataFrame via `reindex()`,

::: {.small}

::: {.cell}

```{.python .cell-code}
data
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
0  bar  one  z  1
1  bar  two  y  2
2  foo  one  x  3
3  foo  two  w  4
```
:::
:::

:::

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.reindex(["w","x","y","z"])
```

::: {.cell-output .cell-output-stdout}
```
     a    b    c   d
w  NaN  NaN  NaN NaN
x  NaN  NaN  NaN NaN
y  NaN  NaN  NaN NaN
z  NaN  NaN  NaN NaN
```
:::

```{.python .cell-code}
data.reindex(range(5,-1,-1))
```

::: {.cell-output .cell-output-stdout}
```
     a    b    c    d
5  NaN  NaN  NaN  NaN
4  NaN  NaN  NaN  NaN
3  foo  two    w  4.0
2  foo  one    x  3.0
1  bar  two    y  2.0
0  bar  one    z  1.0
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
data.reindex(columns = ["a","b","c","d","e"])
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d   e
0  bar  one  z  1 NaN
1  bar  two  y  2 NaN
2  foo  one  x  3 NaN
3  foo  two  w  4 NaN
```
:::

```{.python .cell-code}
data.index = ["w","x","y","z"]
data
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
w  bar  one  z  1
x  bar  two  y  2
y  foo  one  x  3
z  foo  two  w  4
```
:::
:::


:::
::::


## Renaming levels

Alternatively, row or column index levels can be renamed via `rename()`,

::: {.small}

::: {.cell}

```{.python .cell-code}
data
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
0  bar  one  z  1
1  bar  two  y  2
2  foo  one  x  3
3  foo  two  w  4
```
:::
:::

:::


:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.rename(index = pd.Series(["m","n","o","p"]))
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
m  bar  one  z  1
n  bar  two  y  2
o  foo  one  x  3
p  foo  two  w  4
```
:::

```{.python .cell-code}
data.rename_axis(index="rows")
```

::: {.cell-output .cell-output-stdout}
```
        a    b  c  d
rows                
0     bar  one  z  1
1     bar  two  y  2
2     foo  one  x  3
3     foo  two  w  4
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.rename(columns = {"a":"w", "b":"x", 
                       "c":"y", "d":"z"})
```

::: {.cell-output .cell-output-stdout}
```
     w    x  y  z
0  bar  one  z  1
1  bar  two  y  2
2  foo  one  x  3
3  foo  two  w  4
```
:::

```{.python .cell-code}
data.rename_axis(columns="cols")
```

::: {.cell-output .cell-output-stdout}
```
cols    a    b  c  d
0     bar  one  z  1
1     bar  two  y  2
2     foo  one  x  3
3     foo  two  w  4
```
:::
:::

:::
::::


# MultiIndexes

## MultiIndex objects

These are a hierarchical analog of standard Index objects, there are a number of methods for constructing them based on the initial object

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
tuples = [('A','x'), ('A','y'),
          ('B','x'), ('B','y'),
          ('C','x'), ('C','y')]
pd.MultiIndex.from_tuples(
  tuples, names=["1st","2nd"]
)
```

::: {.cell-output .cell-output-stdout}
```
MultiIndex([('A', 'x'),
            ('A', 'y'),
            ('B', 'x'),
            ('B', 'y'),
            ('C', 'x'),
            ('C', 'y')],
           names=['1st', '2nd'])
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
pd.MultiIndex.from_product(
  [["A","B","C"],["x","y"]], names=["1st","2nd"]
)
```

::: {.cell-output .cell-output-stdout}
```
MultiIndex([('A', 'x'),
            ('A', 'y'),
            ('B', 'x'),
            ('B', 'y'),
            ('C', 'x'),
            ('C', 'y')],
           names=['1st', '2nd'])
```
:::
:::

:::
::::

## DataFrame with MultiIndex



::: {.cell}

```{.python .cell-code}
idx = pd.MultiIndex.from_tuples(
  tuples, names=["1st","2nd"]
)

pd.DataFrame(
  np.random.rand(6,2), 
  index = idx, 
  columns=["m","n"]
)
```

::: {.cell-output .cell-output-stdout}
```
                m         n
1st 2nd                    
A   x    0.813745  0.252105
    y    0.208630  0.173328
B   x    0.278051  0.618472
    y    0.465477  0.493497
C   x    0.679689  0.459811
    y    0.627524  0.076458
```
:::
:::



## Column MultiIndex

MultiIndexes can also be used for columns (or both rows and columns),

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
cidx = pd.MultiIndex.from_product(
  [["A","B"],["x","y"]], names=["c1","c2"]
)

pd.DataFrame(
  np.random.rand(4,4), columns = cidx
)
```

::: {.cell-output .cell-output-stdout}
```
c1         A                   B          
c2         x         y         x         y
0   0.509536  0.604471  0.778093  0.048791
1   0.565980  0.632290  0.639640  0.030117
2   0.091139  0.794274  0.387421  0.478644
3   0.892136  0.698861  0.364970  0.573778
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
ridx = pd.MultiIndex.from_product(
  [["m","n"],["l","p"]], names=["r1","r2"]
)

pd.DataFrame(
  np.random.rand(4,4), 
  index= ridx, columns = cidx
)
```

::: {.cell-output .cell-output-stdout}
```
c1            A                   B          
c2            x         y         x         y
r1 r2                                        
m  l   0.037452  0.390261  0.463647  0.919985
   p   0.603874  0.959840  0.902961  0.908091
n  l   0.729398  0.120052  0.396046  0.479204
   p   0.925252  0.344313  0.734838  0.279018
```
:::
:::

:::
::::



## MultiIndex indexing





:::: {.columns .small}
::: {.column width='50%'}


::: {.cell}

```{.python .cell-code}
data
```

::: {.cell-output .cell-output-stdout}
```
c1            A                   B          
c2            x         y         x         y
r1 r2                                        
m  l   0.668319  0.633033  0.115614  0.661077
   p   0.565510  0.733761  0.501812  0.540387
n  l   0.284368  0.796559  0.116583  0.051118
   p   0.225906  0.194516  0.108035  0.997241
```
:::
:::

::: {.cell}

```{.python .cell-code}
data["A"]
```

::: {.cell-output .cell-output-stdout}
```
c2            x         y
r1 r2                    
m  l   0.668319  0.633033
   p   0.565510  0.733761
n  l   0.284368  0.796559
   p   0.225906  0.194516
```
:::

```{.python .cell-code}
data["x"]
```

::: {.cell-output .cell-output-error}
```
Error: KeyError: 'x'
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
data["m"]
```

::: {.cell-output .cell-output-error}
```
Error: KeyError: 'm'
```
:::

```{.python .cell-code}
data["m","A"]
```

::: {.cell-output .cell-output-error}
```
Error: KeyError: ('m', 'A')
```
:::

```{.python .cell-code}
data["A","x"]
```

::: {.cell-output .cell-output-stdout}
```
r1  r2
m   l     0.668319
    p     0.565510
n   l     0.284368
    p     0.225906
Name: (A, x), dtype: float64
```
:::

```{.python .cell-code}
data["A"]["x"]
```

::: {.cell-output .cell-output-stdout}
```
r1  r2
m   l     0.668319
    p     0.565510
n   l     0.284368
    p     0.225906
Name: x, dtype: float64
```
:::
:::

:::
::::


## MultiIndex indexing via `iloc`

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.iloc[0]
```

::: {.cell-output .cell-output-stdout}
```
c1  c2
A   x     0.668319
    y     0.633033
B   x     0.115614
    y     0.661077
Name: (m, l), dtype: float64
```
:::

```{.python .cell-code}
data.iloc[(0,1)]
```

::: {.cell-output .cell-output-stdout}
```
0.6330325939237109
```
:::

```{.python .cell-code}
data.iloc[[0,1]]
```

::: {.cell-output .cell-output-stdout}
```
c1            A                   B          
c2            x         y         x         y
r1 r2                                        
m  l   0.668319  0.633033  0.115614  0.661077
   p   0.565510  0.733761  0.501812  0.540387
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.iloc[:,0]
```

::: {.cell-output .cell-output-stdout}
```
r1  r2
m   l     0.668319
    p     0.565510
n   l     0.284368
    p     0.225906
Name: (A, x), dtype: float64
```
:::

```{.python .cell-code}
data.iloc[0,1]
```

::: {.cell-output .cell-output-stdout}
```
0.6330325939237109
```
:::

```{.python .cell-code}
data.iloc[0,[0,1]]
```

::: {.cell-output .cell-output-stdout}
```
c1  c2
A   x     0.668319
    y     0.633033
Name: (m, l), dtype: float64
```
:::
:::

:::
::::

::: {.aside}
Note that tuples and lists are not treated the same by pandas when it comes to indexing
:::


## MultiIndex indexing via `loc`

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.loc["m"]
```

::: {.cell-output .cell-output-stdout}
```
c1         A                   B          
c2         x         y         x         y
r2                                        
l   0.668319  0.633033  0.115614  0.661077
p   0.565510  0.733761  0.501812  0.540387
```
:::

```{.python .cell-code}
data.loc["l"]
```

::: {.cell-output .cell-output-error}
```
Error: KeyError: 'l'
```
:::

```{.python .cell-code}
data.loc[:,"A"]
```

::: {.cell-output .cell-output-stdout}
```
c2            x         y
r1 r2                    
m  l   0.668319  0.633033
   p   0.565510  0.733761
n  l   0.284368  0.796559
   p   0.225906  0.194516
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.loc[("m","l")]
```

::: {.cell-output .cell-output-stdout}
```
c1  c2
A   x     0.668319
    y     0.633033
B   x     0.115614
    y     0.661077
Name: (m, l), dtype: float64
```
:::

```{.python .cell-code}
data.loc[:,("A","y")]
```

::: {.cell-output .cell-output-stdout}
```
r1  r2
m   l     0.633033
    p     0.733761
n   l     0.796559
    p     0.194516
Name: (A, y), dtype: float64
```
:::
:::

:::
::::


## Fancier indexing with `loc`

Index slices can also be used with combinations of indexes and index tuples,

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.loc["m":"n"]
```

::: {.cell-output .cell-output-stdout}
```
c1            A                   B          
c2            x         y         x         y
r1 r2                                        
m  l   0.668319  0.633033  0.115614  0.661077
   p   0.565510  0.733761  0.501812  0.540387
n  l   0.284368  0.796559  0.116583  0.051118
   p   0.225906  0.194516  0.108035  0.997241
```
:::

```{.python .cell-code}
data.loc[("m","l"):("n","l")]
```

::: {.cell-output .cell-output-stdout}
```
c1            A                   B          
c2            x         y         x         y
r1 r2                                        
m  l   0.668319  0.633033  0.115614  0.661077
   p   0.565510  0.733761  0.501812  0.540387
n  l   0.284368  0.796559  0.116583  0.051118
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.loc[("m","p"):"n"]
```

::: {.cell-output .cell-output-stdout}
```
c1            A                   B          
c2            x         y         x         y
r1 r2                                        
m  p   0.565510  0.733761  0.501812  0.540387
n  l   0.284368  0.796559  0.116583  0.051118
   p   0.225906  0.194516  0.108035  0.997241
```
:::

```{.python .cell-code}
data.loc[[("m","p"),("n","l")]]
```

::: {.cell-output .cell-output-stdout}
```
c1            A                   B          
c2            x         y         x         y
r1 r2                                        
m  p   0.565510  0.733761  0.501812  0.540387
n  l   0.284368  0.796559  0.116583  0.051118
```
:::
:::

:::
:::: 


## Selecting nested levels

The previous methods don't give easy access to indexing on nested index levels, this is possible via the cross-section method `xs()`,

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.xs("p", level="r2")
```

::: {.cell-output .cell-output-stdout}
```
c1         A                   B          
c2         x         y         x         y
r1                                        
m   0.565510  0.733761  0.501812  0.540387
n   0.225906  0.194516  0.108035  0.997241
```
:::

```{.python .cell-code}
data.xs("m", level="r1")
```

::: {.cell-output .cell-output-stdout}
```
c1         A                   B          
c2         x         y         x         y
r2                                        
l   0.668319  0.633033  0.115614  0.661077
p   0.565510  0.733761  0.501812  0.540387
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.xs("y", level="c2", axis=1)
```

::: {.cell-output .cell-output-stdout}
```
c1            A         B
r1 r2                    
m  l   0.633033  0.661077
   p   0.733761  0.540387
n  l   0.796559  0.051118
   p   0.194516  0.997241
```
:::

```{.python .cell-code}
data.xs("B", level="c1", axis=1)
```

::: {.cell-output .cell-output-stdout}
```
c2            x         y
r1 r2                    
m  l   0.115614  0.661077
   p   0.501812  0.540387
n  l   0.116583  0.051118
   p   0.108035  0.997241
```
:::
:::

:::
:::: 



## Setting MultiIndexes

It is also possible to construct a MultiIndex or modify an existing one using `set_index()` and `reset_index()`,





::: {.small}

::: {.cell}

```{.python .cell-code}
data
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
0  bar  one  z  1
1  bar  two  y  2
2  foo  one  x  3
```
:::
:::

:::

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.set_index(['a','b'])
```

::: {.cell-output .cell-output-stdout}
```
         c  d
a   b        
bar one  z  1
    two  y  2
foo one  x  3
```
:::

```{.python .cell-code}
data.set_index('c', append=True)
```

::: {.cell-output .cell-output-stdout}
```
       a    b  d
  c             
0 z  bar  one  1
1 y  bar  two  2
2 x  foo  one  3
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
data.set_index(['a','b']).reset_index()
```

::: {.cell-output .cell-output-stdout}
```
     a    b  c  d
0  bar  one  z  1
1  bar  two  y  2
2  foo  one  x  3
```
:::

```{.python .cell-code}
data.set_index(['a','b']).reset_index(level=1)
```

::: {.cell-output .cell-output-stdout}
```
       b  c  d
a             
bar  one  z  1
bar  two  y  2
foo  one  x  3
```
:::
:::

:::
::::

# Reshaping data

## Long to wide (pivot)





:::: {.columns .medium}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df
```

::: {.cell-output .cell-output-stdout}
```
   country  year   type count
0        A  1999  cases  0.7K
1        A  1999    pop   19M
2        A  2000  cases    2K
3        A  2000    pop   20M
4        B  1999  cases   37K
5        B  1999    pop  172M
6        B  2000  cases   80K
7        B  2000    pop  174M
8        C  1999  cases  212K
9        C  1999    pop    1T
10       C  2000  cases  213K
11       C  2000    pop    1T
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
df_wide = df.pivot(
  index=["country","year"], 
  columns="type", 
  values="count"
)
df_wide
```

::: {.cell-output .cell-output-stdout}
```
type         cases   pop
country year            
A       1999  0.7K   19M
        2000    2K   20M
B       1999   37K  172M
        2000   80K  174M
C       1999  212K    1T
        2000  213K    1T
```
:::
:::

:::
::::

## pivot indexes

:::: {.columns .medium}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df_wide.index
```

::: {.cell-output .cell-output-stdout}
```
MultiIndex([('A', 1999),
            ('A', 2000),
            ('B', 1999),
            ('B', 2000),
            ('C', 1999),
            ('C', 2000)],
           names=['country', 'year'])
```
:::

```{.python .cell-code}
df_wide.columns
```

::: {.cell-output .cell-output-stdout}
```
Index(['cases', 'pop'], dtype='object', name='type')
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
( df_wide
  .reset_index()
  .rename_axis(
    columns=None
  )
)
```

::: {.cell-output .cell-output-stdout}
```
  country  year cases   pop
0       A  1999  0.7K   19M
1       A  2000    2K   20M
2       B  1999   37K  172M
3       B  2000   80K  174M
4       C  1999  212K    1T
5       C  2000  213K    1T
```
:::
:::

:::
::::


## Wide to long (melt)





:::: {.columns}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df
```

::: {.cell-output .cell-output-stdout}
```
  country  1999  2000
0       A  0.7K    2K
1       B   37K   80K
2       C  212K  213K
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
df_long = df.melt(
  id_vars="country", 
  var_name="year"
)
df_long
```

::: {.cell-output .cell-output-stdout}
```
  country  year value
0       A  1999  0.7K
1       B  1999   37K
2       C  1999  212K
3       A  2000    2K
4       B  2000   80K
5       C  2000  213K
```
:::
:::

:::
::::


## Separate Example - splits and explosions





:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df
```

::: {.cell-output .cell-output-stdout}
```
  country  year      rate
0       A  1999  0.7K/19M
1       A  2000    2K/20M
2       B  1999  37K/172M
3       B  2000  80K/174M
4       C  1999   212K/1T
5       C  2000   213K/1T
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
df.assign(
  rate = lambda d: d.rate.str.split("/")
)
```

::: {.cell-output .cell-output-stdout}
```
  country  year         rate
0       A  1999  [0.7K, 19M]
1       A  2000    [2K, 20M]
2       B  1999  [37K, 172M]
3       B  2000  [80K, 174M]
4       C  1999   [212K, 1T]
5       C  2000   [213K, 1T]
```
:::
:::

:::
::::

. . .

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
( df.assign(
    rate = lambda d: d.rate.str.split("/")
  )
  .explode("rate")
  .assign(
    type = lambda d: ["cases", "pop"] * int(d.shape[0]/2)
  )
)
```

::: {.cell-output .cell-output-stdout}
```
  country  year  rate   type
0       A  1999  0.7K  cases
0       A  1999   19M    pop
1       A  2000    2K  cases
1       A  2000   20M    pop
2       B  1999   37K  cases
2       B  1999  172M    pop
3       B  2000   80K  cases
3       B  2000  174M    pop
4       C  1999  212K  cases
4       C  1999    1T    pop
5       C  2000  213K  cases
5       C  2000    1T    pop
```
:::
:::

:::
::::

## Putting it together

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
( df
  .assign(
    rate = lambda d: d.rate.str.split("/")
  )
  .explode("rate")
  .assign(
    type = lambda d: ["cases", "pop"] * 
                     int(d.shape[0]/2)
  )
)
```

::: {.cell-output .cell-output-stdout}
```
  country  year  rate   type
0       A  1999  0.7K  cases
0       A  1999   19M    pop
1       A  2000    2K  cases
1       A  2000   20M    pop
2       B  1999   37K  cases
2       B  1999  172M    pop
3       B  2000   80K  cases
3       B  2000  174M    pop
4       C  1999  212K  cases
4       C  1999    1T    pop
5       C  2000  213K  cases
5       C  2000    1T    pop
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
( df.assign(
    rate = lambda d: d.rate.str.split("/")
  )
  .explode("rate")
  .assign(
    type = lambda d: ["cases", "pop"] * 
                     int(d.shape[0]/2)
  )
  .pivot(
    index=["country","year"], 
    columns="type", 
    values="rate"
  )
  .reset_index()
)
```

::: {.cell-output .cell-output-stdout}
```
type country  year cases   pop
0          A  1999  0.7K   19M
1          A  2000    2K   20M
2          B  1999   37K  172M
3          B  2000   80K  174M
4          C  1999  212K    1T
5          C  2000  213K    1T
```
:::
:::

:::
::::


## Separate Example - A better way

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df
```

::: {.cell-output .cell-output-stdout}
```
  country  year      rate
0       A  1999  0.7K/19M
1       A  2000    2K/20M
2       B  1999  37K/172M
3       B  2000  80K/174M
4       C  1999   212K/1T
5       C  2000   213K/1T
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
df.assign(
  counts = lambda d: d.rate.str.split("/").str[0],
  pop    = lambda d: d.rate.str.split("/").str[1]
)
```

::: {.cell-output .cell-output-stdout}
```
  country  year      rate counts   pop
0       A  1999  0.7K/19M   0.7K   19M
1       A  2000    2K/20M     2K   20M
2       B  1999  37K/172M    37K  172M
3       B  2000  80K/174M    80K  174M
4       C  1999   212K/1T   212K    1T
5       C  2000   213K/1T   213K    1T
```
:::
:::

:::
::::

. . .

If you dont want to repeat the split,

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
df.assign(
  rate = lambda d: d.rate.str.split("/"),
  counts = lambda d: d.rate.str[0],
  pop    = lambda d: d.rate.str[1]
).drop("rate", axis=1)
```

::: {.cell-output .cell-output-stdout}
```
  country  year counts   pop
0       A  1999   0.7K   19M
1       A  2000     2K   20M
2       B  1999    37K  172M
3       B  2000    80K  174M
4       C  1999   212K    1T
5       C  2000   213K    1T
```
:::
:::

:::
::::


## Exercise 1





Create a DataFrame from the data available at [https://sta663-sp23.github.io/slides/data/us_rent.csv](https://sta663-sp23.github.io/slides/data/us_rent.csv) using `pd.read_csv()`. 

These data come from the 2017 American Community Survey and reflect the following values:

* `name` - name of state

* `variable` - Variable name: income = median yearly income, rent = median monthly rent

* `estimate` - Estimated value

* `moe` - 90% margin of error

Using these data find the state(s) with the lowest income to rent ratio.

# Split-Apply-Combine





## groupby

Groups can be created within a DataFrame via `groupby()` - these groups are then used by the standard summary methods (e.g. `sum()`, `mean()`, `std()`, etc.).

::: {.small}

::: {.cell}

```{.python .cell-code}
cereal = pd.read_csv("https://sta663-sp23.github.io/slides/data/cereal.csv")
cereal
```

::: {.cell-output .cell-output-stdout}
```
                         name             mfr  ... sugars     rating
0                   100% Bran         Nabisco  ...      6  68.402973
1           100% Natural Bran     Quaker Oats  ...      8  33.983679
2                    All-Bran       Kellogg's  ...      5  59.425505
3   All-Bran with Extra Fiber       Kellogg's  ...      0  93.704912
4              Almond Delight  Ralston Purina  ...      8  34.384843
..                        ...             ...  ...    ...        ...
72                    Triples   General Mills  ...      3  39.106174
73                       Trix   General Mills  ...     12  27.753301
74                 Wheat Chex  Ralston Purina  ...      3  49.787445
75                   Wheaties   General Mills  ...      3  51.592193
76        Wheaties Honey Gold   General Mills  ...      8  36.187559

[77 rows x 6 columns]
```
:::

```{.python .cell-code}
cereal.groupby("type")
```

::: {.cell-output .cell-output-stdout}
```
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x29b9b4e50>
```
:::
:::

:::

## GroupBy attributes and methods

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
cereal.groupby("type").groups
```

::: {.cell-output .cell-output-stdout}
```
{'Cold': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], 'Hot': [20, 43, 57]}
```
:::

```{.python .cell-code}
cereal.groupby("type").mean(numeric_only=True)
```

::: {.cell-output .cell-output-stdout}
```
        calories    sugars     rating
type                                 
Cold  107.162162  7.175676  42.095218
Hot   100.000000  1.333333  56.737708
```
:::
:::

:::

::: {.column width='50%' .fragment}

::: {.cell}

```{.python .cell-code}
cereal.groupby("mfr").groups
```

::: {.cell-output .cell-output-stdout}
```
{'General Mills': [5, 7, 11, 12, 13, 14, 18, 22, 31, 36, 40, 42, 47, 51, 59, 69, 70, 71, 72, 73, 75, 76], 'Kellogg's': [2, 3, 6, 16, 17, 19, 21, 24, 25, 26, 28, 38, 39, 46, 48, 49, 50, 53, 58, 60, 62, 66, 67], 'Maltex': [43], 'Nabisco': [0, 20, 63, 64, 65, 68], 'Post': [9, 27, 29, 30, 32, 33, 34, 37, 52], 'Quaker Oats': [1, 10, 35, 41, 54, 55, 56, 57], 'Ralston Purina': [4, 8, 15, 23, 44, 45, 61, 74]}
```
:::

```{.python .cell-code}
cereal.groupby("mfr").size()
```

::: {.cell-output .cell-output-stdout}
```
mfr
General Mills     22
Kellogg's         23
Maltex             1
Nabisco            6
Post               9
Quaker Oats        8
Ralston Purina     8
dtype: int64
```
:::
:::

:::
::::

## Selecting groups

Groups can be accessed via `get_group()` or the DataFrameGroupBy can be iterated over,

::: {.small}

::: {.cell}

```{.python .cell-code}
cereal.groupby("type").get_group("Hot")
```

::: {.cell-output .cell-output-stdout}
```
                      name          mfr type  calories  sugars     rating
20  Cream of Wheat (Quick)      Nabisco  Hot       100       0  64.533816
43                   Maypo       Maltex  Hot       100       3  54.850917
57          Quaker Oatmeal  Quaker Oats  Hot       100       1  50.828392
```
:::

```{.python .cell-code}
cereal.groupby("mfr").get_group("Post")
```

::: {.cell-output .cell-output-stdout}
```
                                      name   mfr  ... sugars     rating
9                              Bran Flakes  Post  ...      5  53.313813
27  Fruit & Fibre Dates; Walnuts; and Oats  Post  ...     10  40.917047
29                          Fruity Pebbles  Post  ...     12  28.025765
30                            Golden Crisp  Post  ...     15  35.252444
32                       Grape Nuts Flakes  Post  ...      5  52.076897
33                              Grape-Nuts  Post  ...      3  53.371007
34                      Great Grains Pecan  Post  ...      4  45.811716
37                              Honey-comb  Post  ...     11  28.742414
52                   Post Nat. Raisin Bran  Post  ...     14  37.840594

[9 rows x 6 columns]
```
:::
:::

:::

## Iterating groups

::: {.small}

::: {.cell}

```{.python .cell-code}
for name, group in cereal.groupby("type"):
  print(f"# {name}\n{group}\n\n")
```

::: {.cell-output .cell-output-stdout}
```
# Cold
                         name             mfr  ... sugars     rating
0                   100% Bran         Nabisco  ...      6  68.402973
1           100% Natural Bran     Quaker Oats  ...      8  33.983679
2                    All-Bran       Kellogg's  ...      5  59.425505
3   All-Bran with Extra Fiber       Kellogg's  ...      0  93.704912
4              Almond Delight  Ralston Purina  ...      8  34.384843
..                        ...             ...  ...    ...        ...
72                    Triples   General Mills  ...      3  39.106174
73                       Trix   General Mills  ...     12  27.753301
74                 Wheat Chex  Ralston Purina  ...      3  49.787445
75                   Wheaties   General Mills  ...      3  51.592193
76        Wheaties Honey Gold   General Mills  ...      8  36.187559

[74 rows x 6 columns]


# Hot
                      name          mfr type  calories  sugars     rating
20  Cream of Wheat (Quick)      Nabisco  Hot       100       0  64.533816
43                   Maypo       Maltex  Hot       100       3  54.850917
57          Quaker Oatmeal  Quaker Oats  Hot       100       1  50.828392
```
:::
:::

:::



## Aggregation


The `aggregate()` function or `agg()` method can be used to compute summary statistics for each group,

::: {.small}

::: {.cell}

```{.python .cell-code}
cereal.groupby("mfr").agg("mean")
```

::: {.cell-output .cell-output-stdout}
```
                  calories    sugars     rating
mfr                                            
General Mills   111.363636  7.954545  34.485852
Kellogg's       108.695652  7.565217  44.038462
Maltex          100.000000  3.000000  54.850917
Nabisco          86.666667  1.833333  67.968567
Post            108.888889  8.777778  41.705744
Quaker Oats      95.000000  5.500000  42.915990
Ralston Purina  115.000000  6.125000  41.542997

<string>:1: FutureWarning: The default value of numeric_only in DataFrameGroupBy.mean is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.
```
:::
:::

:::

::: {.aside}
Think `summarize()` from dplyr.
:::


## Aggregation with multiple functions

::: {.small}

::: {.cell}

```{.python .cell-code}
cereal.groupby("mfr").agg([np.mean, np.std])
```

::: {.cell-output .cell-output-stdout}
```
                  calories               sugars               rating           
                      mean        std      mean       std       mean        std
mfr                                                                            
General Mills   111.363636  10.371873  7.954545  3.872704  34.485852   8.946704
Kellogg's       108.695652  22.218818  7.565217  4.500768  44.038462  14.457434
Maltex          100.000000        NaN  3.000000       NaN  54.850917        NaN
Nabisco          86.666667  10.327956  1.833333  2.857738  67.968567   5.509326
Post            108.888889  10.540926  8.777778  4.576510  41.705744  10.047647
Quaker Oats      95.000000  29.277002  5.500000  4.780914  42.915990  16.797673
Ralston Purina  115.000000  22.677868  6.125000  3.563205  41.542997   6.080841

<string>:1: FutureWarning: ['name', 'type'] did not aggregate successfully. If any error is raised this will raise in a future version of pandas. Drop these columns/ops to avoid this warning.
```
:::
:::

:::

## Aggregation by column

::: {.small}

::: {.cell}

```{.python .cell-code}
cereal.groupby("mfr").agg({
  "calories": ['min', 'max'],
  "sugars":   ['mean', 'median'],
  "rating":   ['sum', 'count']
})
```

::: {.cell-output .cell-output-stdout}
```
               calories         sugars              rating      
                    min  max      mean median          sum count
mfr                                                             
General Mills       100  140  7.954545    8.5   758.688737    22
Kellogg's            50  160  7.565217    7.0  1012.884634    23
Maltex              100  100  3.000000    3.0    54.850917     1
Nabisco              70  100  1.833333    0.0   407.811403     6
Post                 90  120  8.777778   10.0   375.351697     9
Quaker Oats          50  120  5.500000    6.0   343.327919     8
Ralston Purina       90  150  6.125000    5.5   332.343977     8
```
:::
:::

:::


## Named aggregation

It is also possible to use special syntax to aggregate specific columns into a named output column,

::: {.medium}

::: {.cell}

```{.python .cell-code}
cereal.groupby("mfr", as_index=False).agg(
  min_cal = ("calories", "min"),
  max_cal = ("calories", "max"),
  med_sugar = ("sugars", "median"),
  avg_rating = ("rating", "mean")
)
```

::: {.cell-output .cell-output-stdout}
```
              mfr  min_cal  max_cal  med_sugar  avg_rating
0   General Mills      100      140        8.5   34.485852
1       Kellogg's       50      160        7.0   44.038462
2          Maltex      100      100        3.0   54.850917
3         Nabisco       70      100        0.0   67.968567
4            Post       90      120       10.0   41.705744
5     Quaker Oats       50      120        6.0   42.915990
6  Ralston Purina       90      150        5.5   41.542997
```
:::
:::

:::

::: {.aside}
Tuples can also be passed using `pd.NamedAgg()` but this offers no additional functionality.
:::


## Transformation

The `transform()` method returns a DataFrame with the aggregated result matching the size (or length 1) of the input group(s),

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
cereal.groupby("mfr").transform(np.mean)
```

::: {.cell-output .cell-output-stdout}
```
      calories    sugars     rating
0    86.666667  1.833333  67.968567
1    95.000000  5.500000  42.915990
2   108.695652  7.565217  44.038462
3   108.695652  7.565217  44.038462
4   115.000000  6.125000  41.542997
..         ...       ...        ...
72  111.363636  7.954545  34.485852
73  111.363636  7.954545  34.485852
74  115.000000  6.125000  41.542997
75  111.363636  7.954545  34.485852
76  111.363636  7.954545  34.485852

[77 rows x 3 columns]

<string>:1: FutureWarning: The default value of numeric_only in DataFrameGroupBy.mean is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
cereal.groupby("type").transform("mean")
```

::: {.cell-output .cell-output-stdout}
```
      calories    sugars     rating
0   107.162162  7.175676  42.095218
1   107.162162  7.175676  42.095218
2   107.162162  7.175676  42.095218
3   107.162162  7.175676  42.095218
4   107.162162  7.175676  42.095218
..         ...       ...        ...
72  107.162162  7.175676  42.095218
73  107.162162  7.175676  42.095218
74  107.162162  7.175676  42.095218
75  107.162162  7.175676  42.095218
76  107.162162  7.175676  42.095218

[77 rows x 3 columns]

<string>:1: FutureWarning: The default value of numeric_only in DataFrameGroupBy.mean is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.
```
:::
:::

:::
::::

::: {.aside}
Note that we have lost the non-numeric columns
:::


## Practical transformation

`transform()` will generally be most useful via a user defined function, the lambda argument is each column of each group.

::: {.small}

::: {.cell}

```{.python .cell-code}
( cereal
  .groupby("mfr")
  .transform( lambda x: (x - np.mean(x))/np.std(x) ) 
)
```

::: {.cell-output .cell-output-stdout}
```
    calories    sugars    rating
0  -1.767767  1.597191  0.086375
1   0.912871  0.559017 -0.568474
2  -1.780712 -0.582760  1.088220
3  -2.701081 -1.718649  3.512566
4  -0.235702  0.562544 -1.258442
..       ...       ...       ...
72 -0.134568 -1.309457  0.528580
73 -0.134568  1.069190 -0.770226
74 -0.707107 -0.937573  1.449419
75 -1.121403 -1.309457  1.957022
76 -0.134568  0.012013  0.194681

[77 rows x 3 columns]

<string>:3: FutureWarning: Dropping invalid columns in DataFrameGroupBy.transform is deprecated. In a future version, a TypeError will be raised. Before calling .transform, select only columns which should be valid for the function.
```
:::
:::

:::


## Filtering groups

`filter()` also respects groups and allows for the inclusion / exclusion of groups based on user specified criteria,

::: {.small}

::: {.cell}

```{.python .cell-code}
( cereal
  .groupby("mfr")
  .filter(lambda x: len(x) > 8)
)
```

::: {.cell-output .cell-output-stdout}
```
                                      name            mfr  ... sugars     rating
2                                 All-Bran      Kellogg's  ...      5  59.425505
3                All-Bran with Extra Fiber      Kellogg's  ...      0  93.704912
5                  Apple Cinnamon Cheerios  General Mills  ...     10  29.509541
6                              Apple Jacks      Kellogg's  ...     14  33.174094
7                                  Basic 4  General Mills  ...      8  37.038562
9                              Bran Flakes           Post  ...      5  53.313813
11                                Cheerios  General Mills  ...      1  50.764999
12                   Cinnamon Toast Crunch  General Mills  ...      9  19.823573
13                                Clusters  General Mills  ...      7  40.400208
14                             Cocoa Puffs  General Mills  ...     13  22.736446
16                             Corn Flakes      Kellogg's  ...      2  45.863324
17                               Corn Pops      Kellogg's  ...     12  35.782791
18                           Count Chocula  General Mills  ...     13  22.396513
19                      Cracklin' Oat Bran      Kellogg's  ...      7  40.448772
21                                 Crispix      Kellogg's  ...      3  46.895644
22                  Crispy Wheat & Raisins  General Mills  ...     10  36.176196
24                             Froot Loops      Kellogg's  ...     13  32.207582
25                          Frosted Flakes      Kellogg's  ...     11  31.435973
26                     Frosted Mini-Wheats      Kellogg's  ...      7  58.345141
27  Fruit & Fibre Dates; Walnuts; and Oats           Post  ...     10  40.917047
28                           Fruitful Bran      Kellogg's  ...     12  41.015492
29                          Fruity Pebbles           Post  ...     12  28.025765
30                            Golden Crisp           Post  ...     15  35.252444
31                          Golden Grahams  General Mills  ...      9  23.804043
32                       Grape Nuts Flakes           Post  ...      5  52.076897
33                              Grape-Nuts           Post  ...      3  53.371007
34                      Great Grains Pecan           Post  ...      4  45.811716
36                      Honey Nut Cheerios  General Mills  ...     10  31.072217
37                              Honey-comb           Post  ...     11  28.742414
38             Just Right Crunchy  Nuggets      Kellogg's  ...      6  36.523683
39                  Just Right Fruit & Nut      Kellogg's  ...      9  36.471512
40                                     Kix  General Mills  ...      3  39.241114
42                            Lucky Charms  General Mills  ...     12  26.734515
46                    Mueslix Crispy Blend      Kellogg's  ...     13  30.313351
47                    Multi-Grain Cheerios  General Mills  ...      6  40.105965
48                        Nut&Honey Crunch      Kellogg's  ...      9  29.924285
49               Nutri-Grain Almond-Raisin      Kellogg's  ...      7  40.692320
50                       Nutri-grain Wheat      Kellogg's  ...      2  59.642837
51                    Oatmeal Raisin Crisp  General Mills  ...     10  30.450843
52                   Post Nat. Raisin Bran           Post  ...     14  37.840594
53                              Product 19      Kellogg's  ...      3  41.503540
58                             Raisin Bran      Kellogg's  ...     12  39.259197
59                         Raisin Nut Bran  General Mills  ...      8  39.703400
60                          Raisin Squares      Kellogg's  ...      6  55.333142
62                           Rice Krispies      Kellogg's  ...      3  40.560159
66                                  Smacks      Kellogg's  ...     15  31.230054
67                               Special K      Kellogg's  ...      3  53.131324
69                       Total Corn Flakes  General Mills  ...      3  38.839746
70                       Total Raisin Bran  General Mills  ...     14  28.592785
71                       Total Whole Grain  General Mills  ...      3  46.658844
72                                 Triples  General Mills  ...      3  39.106174
73                                    Trix  General Mills  ...     12  27.753301
75                                Wheaties  General Mills  ...      3  51.592193
76                     Wheaties Honey Gold  General Mills  ...      8  36.187559

[54 rows x 6 columns]
```
:::
:::

:::

##

:::: {.columns .small}
::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
( cereal
  .groupby("mfr")
  .size()
)
```

::: {.cell-output .cell-output-stdout}
```
mfr
General Mills     22
Kellogg's         23
Maltex             1
Nabisco            6
Post               9
Quaker Oats        8
Ralston Purina     8
dtype: int64
```
:::
:::

:::

::: {.column width='50%'}

::: {.cell}

```{.python .cell-code}
( cereal
  .groupby("mfr")
  .filter(lambda x: len(x) > 8)
  .groupby("mfr")
  .size()  
)
```

::: {.cell-output .cell-output-stdout}
```
mfr
General Mills    22
Kellogg's        23
Post              9
dtype: int64
```
:::
:::

:::
::::

