# Python Mastery

Complete roadmap from Python Basics to AI Engineering.

## About

**Python Mastery** is a comprehensive, structured learning path designed to take you from absolute beginner to AI engineer. Every module contains hands-on Jupyter notebooks with lessons, exercises, and solutions so you learn by doing.

### What makes this different

- **18 progressive modules** - each building on the previous
- **Learn by doing** - every topic has notes, practice exercises, and solutions
- **Zero to Hero** - starts from variables and ends at LLMs and MLOps
- **Real projects** - not just theory, actual code you can run
- **Industry aligned** - covers the exact skills employers look for

### Who is this for?

- Beginners who want a clear, structured path to learn Python
- Students transitioning into data science or AI
- Developers adding Python to their skill set
- Anyone who wants to go from zero to building real AI systems

### How to use this repo

Every topic folder contains three notebooks:
- `notes.ipynb` - the lesson (read this first)
- `exercises.ipynb` - your practice (do this yourself)
- `solutions.ipynb` - check yourself (only after attempting)

Run each notebook top-to-bottom in Jupyter or VS Code; all code cells are executable and outputs are embedded.

## Roadmap

| Module | Topic | What you'll learn |
|--------|-------|-------------------|
| 01 | Python Basics | Variables, data types, numbers, casting, strings, booleans, operators, user input |
| 02 | Control Flow | If/else, match statements, while & for loops, break/continue |
| 03 | Functions | Defining functions, arguments, return values, scope, lambda |
| 04 | Data Structures | Lists, tuples, sets, dictionaries, comprehensions + cheat sheet |
| 05 | Intermediate Python | Modules, math, datetime, JSON, regex, pip, virtual environments |
| 06 | File Handling | Reading, writing, appending files and CSV processing |
| 07 | Error Handling | try/except, finally, robust programs that never crash silently |
| 08 | OOP | Classes, objects, inheritance, polymorphism, encapsulation |
| 09 | Projects | Real-world practice projects |
| 10 | NumPy | Arrays, indexing, broadcasting, aggregation, random numbers |
| 11 | Pandas | Series, DataFrames, cleaning, groupby, merging real datasets |
| 12 | Matplotlib | Pyplot, styling, chart types, subplots, publication-quality plots |
| 13 | Machine Learning | Preprocessing, regression, classification, clustering, pipelines |
| 14 | Deep Learning | Neural nets from scratch, tensors, training, CNNs, transfer learning |
| 15 | Computer Vision | Images as arrays, OpenCV processing, edges, CNN classifiers |
| 16 | NLP | Text preprocessing, TF-IDF, embeddings, transformers |
| 17 | LLMs | Prompting, LLM APIs, vector DBs, RAG, fine-tuning, agents |
| 18 | MLOps | Reproducibility, experiment tracking, serving, CI/CD, monitoring |

## Suggested pace

| Weeks | Focus | Modules |
|-------|-------|---------|
| 1-4 | Core language + data structures | 01-04 |
| 5-6 | Intermediate Python + OOP | 05-08 |
| 7-9 | Data stack: NumPy / Pandas / Matplotlib | 10-12 |
| 10-13 | ML + DL + Computer Vision | 13-15 |
| 14-16 | NLP + LLMs + MLOps | 16-18 |

## Environment setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

Then open any notebook with `jupyter lab` or VS Code and select the `.venv` kernel.

## License

MIT
