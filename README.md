# Python Mastery

Complete roadmap from Python Basics to AI Engineering.

> 📘 **How to use this repo:** every topic folder contains three notebooks —
> `notes.ipynb` (the lesson), `exercises.ipynb` (your practice) and `solutions.ipynb`
> (check yourself *after* attempting). Run each notebook top-to-bottom in Jupyter /
> VS Code; all code cells are executable and outputs are embedded.

## Roadmap

| Module | Topic | What you'll learn | Status |
|--------|-------|-------------------|--------|
| 01 | [Python Basics](01_Python_Basics/README.md) | Variables, data types, numbers, casting, strings, booleans, operators, user input | ✅ |
| 02 | [Control Flow](02_Control_Flow/README.md) | If/else, match statements, while & for loops, break/continue | ✅ |
| 03 | [Functions](03_Functions/README.md) | Defining functions, arguments, return values, scope, lambda | ✅ |
| 04 | [Data Structures](04_Data_Structures/README.md) | Lists, tuples, sets, dictionaries, comprehensions + cheat sheet | ✅ |
| 05 | [Intermediate Python](05_Intermediate_Python/README.md) | Modules, math, datetime, JSON, regex, pip, virtual environments | ✅ |
| 06 | [File Handling](06_File_Handling/README.md) | Reading, writing, appending files and CSV processing | ✅ |
| 07 | [Error Handling](07_Error_Handling/README.md) | try/except, finally, robust programs that never crash silently | ✅ |
| 08 | [OOP](08_OOP/README.md) | Classes, objects, inheritance, polymorphism, encapsulation | ✅ |
| 09 | *(reserved)* | Projects & practice — e.g. [`tic_tac_toe_game`](tic_tac_toe_game/tic_tac_toe.py) | 🔨 |
| 10 | [NumPy](10_NumPy/README.md) | Arrays, indexing, broadcasting, aggregation, random numbers | ✅ |
| 11 | [Pandas](11_Pandas/README.md) | Series, DataFrames, cleaning, groupby, merging real datasets | ✅ |
| 12 | [Matplotlib](12_Matplotlib/README.md) | Pyplot, styling, chart types, subplots, publication-quality plots | ✅ |
| 13 | [Machine Learning](13_Machine_Learning/README.md) | Preprocessing, regression, classification, clustering, pipelines | ✅ |
| 14 | [Deep Learning](14_Deep_Learning/README.md) | Neural nets from scratch, tensors, training, CNNs, transfer learning | ✅ |
| 15 | [Computer Vision](15_Computer_Vision/README.md) | Images as arrays, OpenCV processing, edges, CNN classifiers | ✅ |
| 16 | [NLP](16_NLP/README.md) | Text preprocessing, TF-IDF, embeddings, transformers | ✅ |
| 17 | [LLMs](17_LLMs/README.md) | Prompting, LLM APIs, vector DBs, RAG, fine-tuning, agents | ✅ |
| 18 | [MLOps](18_MLOps/README.md) | Reproducibility, experiment tracking, serving, CI/CD, monitoring | ✅ |

## Suggested pace

- **Weeks 1–4:** Modules 01–04 (core language + data structures)
- **Weeks 5–6:** Modules 05–08 (intermediate Python → OOP)
- **Weeks 7–9:** Modules 10–12 (data stack: NumPy / Pandas / Matplotlib)
- **Weeks 10–13:** Modules 13–15 (ML → DL → CV)
- **Weeks 14–16:** Modules 16–18 (NLP → LLMs → MLOps)

## Environment setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

Then open any notebook with `jupyter lab` or VS Code and select the `.venv` kernel.
