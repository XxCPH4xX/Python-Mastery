# 10_NumPy

NumPy is the foundation of numerical computing in Python: fast N-dimensional arrays, vectorized math, broadcasting, and the random tooling every data science and AI project is built on.

| # | Topic | What you'll learn |
|---|---|---|
| 1 | [Why NumPy And Arrays](01_Why_NumPy_And_Arrays/notes.ipynb) | Why arrays beat lists (speed benchmark), vectorization, `np.array` from nested lists, core attributes (`ndim`, `shape`, `size`, `dtype`, `itemsize`), creation helpers (`zeros`, `ones`, `full`, `empty`, `arange`, `linspace`, `eye`) |
| 2 | [Indexing Slicing](02_Indexing_Slicing/notes.ipynb) | 1-D/2-D indexing, slices, the views-not-copies trap, whole rows and columns, boolean mask filtering, fancy indexing, masked assignment |
| 3 | [DataTypes Copy View](03_DataTypes_Copy_View/notes.ipynb) | The dtype system, silent integer overflow, `astype`, and the full story of `b = a` vs `.view()` vs `.copy()` proved with `.base` |
| 4 | [Shape Reshape Broadcasting](04_Shape_Reshape_Broadcasting/notes.ipynb) | `reshape` and `-1`, `ravel` vs `flatten`, transpose, `newaxis`/`squeeze`, stacking, broadcasting rules with worked examples, column normalization |
| 5 | [Array Math Aggregation](05_Array_Math_Aggregation/notes.ipynb) | Element-wise ops, universal functions, comparisons as masks, aggregations, `axis=0` vs `axis=1` demystified, `argmax`, `cumsum`, `any`/`all`, NaN-aware functions |
| 6 | [Sorting Searching Filtering](06_Sorting_Searching_Filtering/notes.ipynb) | `np.sort` vs `.sort()`, axis sorting, `argsort` top-k pattern, three forms of `np.where`, `nonzero`, `unique(return_counts=True)`, `clip`, `searchsorted` |
| 7 | [Random Numbers](07_Random_Numbers/notes.ipynb) | Modern `default_rng` Generator API, integers/uniform/normal/choice/shuffle/permutation, legacy `np.random.*` decoder table, seeding for reproducibility, dice simulation |

**Next module:** [11_Pandas](../11_Pandas/README.md)
