# Python-DataScience-Masterclass

A structured, hands-on curriculum that takes you from Python fundamentals to statistical inference — built entirely with Jupyter Notebooks.

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python 3.13+](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/downloads/)

---

## Why This Exists

Most Python tutorials teach syntax. Most data science courses jump straight to libraries. This masterclass bridges the gap — every concept is implemented **from first principles** before introducing the library shortcut. You understand the *why* before the *how*.

The curriculum follows a **university-style progression** (PY100 → PY500), where each level builds on the previous one.

---

## Curriculum Overview

### PY100 — Foundations of Python (9 notebooks)

Core language fundamentals — syntax, data types, control flow, and development environment setup.

| # | Notebook | Topics |
|---|---|---|
| 01 | [Basics](PY100/01_Basics.ipynb) | Compiler vs interpreter, static vs dynamic binding, error types |
| 02 | [Print Function](PY100/02_Print%20Function.ipynb) | `print()`, formatting, `sep`, `end`, f-strings |
| 03 | [String Functions](PY100/03_String%20functions.ipynb) | String methods, slicing, immutability |
| 04 | [Int and Float](PY100/04_Int%20and%20Float.ipynb) | Numeric types, type casting, arithmetic, precision |
| 05 | [Date Functions](PY100/05_Date%20Functions.ipynb) | `datetime`, `timedelta`, formatting, parsing |
| 06 | [List, Tuple, Dict](PY100/06_List%20Tuple%20Dict.ipynb) | Data structures, CRUD operations, comprehensions |
| 07 | [Conditional Logic](PY100/07_Conditional%20Logic.ipynb) | `if/elif/else`, ternary, truthiness, `match-case` |
| 08 | [Loops](PY100/08_Loops.ipynb) | `for`, `while`, `enumerate`, `zip`, `break/continue` |
| 09 | [Environment & Tools Setup](PY100/09_Environment%20and%20Tools%20Setup.ipynb) | venv/uv/conda, VS Code shortcuts, Jupyter, Git CLI |

### PY200 — Problem-Solving & Mathematical Computation (5 notebooks)

Apply Python fundamentals to solve real problems — implement algorithms manually, then compare with library solutions.

| # | Notebook | Topics |
|---|---|---|
| 01 | [Greatest & Least Number](PY200/01_Greatest_Least_Number.ipynb) | Loops vs `max()`/`min()` vs `heapq` |
| 02 | [GST Calculation](PY200/02_GST_Calculation.ipynb) | Tax computation, nested logic, formatting |
| 03 | [Mean](PY200/03_Mean.ipynb) | Arithmetic, weighted, and trimmed mean |
| 04 | [Mode](PY200/04_Mode.ipynb) | Frequency counting, `Counter`, edge cases |
| 05 | [Median](PY200/05_Median.ipynb) | Sorting-based, partitioning, odd vs even length |

### PY300 — Exploratory Data Analysis (5 notebooks)

Statistics, visualization, and data quality — the skills that turn raw data into insight.

| # | Notebook | Topics |
|---|---|---|
| 01 | [Summary Statistics](PY300/01_Summary_Stats.ipynb) | Mean, median, std, skewness, kurtosis — pure Python → NumPy → Pandas |
| 02 | [Box Plots & Outliers](PY300/02_Box_Plot_Outliers.ipynb) | IQR method, box plots, visual outlier detection |
| 03 | [Visualizations](PY300/03_Visualizations.ipynb) | Matplotlib — bar, line, scatter, histogram, subplots |
| 04 | [Plotly Interactive](PY300/04_Plotly_Interactive.ipynb) | Interactive charts with Plotly Express |
| 05 | [Outlier Treatment & Normalization](PY300/05_Outlier_Treatment_Missing_Normalization.ipynb) | Capping, missing values, min-max, z-score scaling |

### PY400 — Data Wrangling & Operations (3 notebooks)

Real-world data handling — loading, transforming, and extracting data from diverse sources.

| # | Notebook | Topics |
|---|---|---|
| 01 | [DataFrames](PY400/01_DataFrames.ipynb) | Pandas CRUD, filtering, grouping, SQL comparison |
| 02 | [File Operations](PY400/02_File_Operations.ipynb) | CSV, Excel, JSON — read, write, transform |
| 03 | [Web Crawling](PY400/03_Web_Crawling.ipynb) | BeautifulSoup, requests, scraping HTML tables |

### PY500 — Statistical Inference & Hypothesis Testing (4 notebooks)

Make data-driven decisions — from distributions to A/B testing.

| # | Notebook | Topics |
|---|---|---|
| 01 | [Variations & Distributions](PY500/01_Variations_Distributions.ipynb) | Variance, std, IQR, normal/binomial/Poisson, CLT |
| 02 | [Sampling & Estimation](PY500/02_Sampling_Estimation.ipynb) | Random/stratified sampling, confidence intervals |
| 03 | [Hypothesis Testing](PY500/03_Hypothesis_Testing.ipynb) | Z-test, t-test, p-values, Type I/II errors |
| 04 | [A/B Testing & ANOVA](PY500/04_AB_Testing_ANOVA.ipynb) | Two-sample tests, one-way ANOVA, post-hoc analysis |

---

## Learning Path

```
PY100  Foundations        →  Learn the language
  ↓
PY200  Problem-Solving    →  Apply it to real problems
  ↓
PY300  EDA                →  Explore and visualize data
  ↓
PY400  Data Wrangling     →  Handle real-world data sources
  ↓
PY500  Statistical Tests  →  Make data-driven decisions
```

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.13+ |
| Package Manager | [uv](https://docs.astral.sh/uv/) |
| Notebooks | Jupyter (via VS Code) |
| Core Libraries | NumPy, Pandas, Matplotlib, Seaborn |
| Interactive Viz | Plotly |
| Statistics | SciPy, statsmodels, scikit-learn |
| Web Scraping | BeautifulSoup, requests, lxml |
| File I/O | openpyxl (Excel), built-in csv/json |

---

## Getting Started

### Prerequisites

- Python 3.13 or higher
- [VS Code](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- Git

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/shri-singh/Python-DataScience-Masterclass.git
cd Python-DataScience-Masterclass

# 2. Install uv (if not already installed)
pip install uv

# 3. Create virtual environment and install all dependencies
uv sync

# 4. Activate the environment
source .venv/Scripts/activate      # Git Bash on Windows
source .venv/bin/activate           # macOS / Linux

# 5. Register the Jupyter kernel
python -m ipykernel install --user --name=python-demo --display-name "Python Demo"

# 6. Open in VS Code
code .
```

Then open any `.ipynb` file and select the **"Python Demo"** kernel from the top-right kernel picker.

---

## Project Structure

```
Python-DataScience-Masterclass/
├── PY100/                  # Foundations of Python
├── PY200/                  # Problem-Solving & Math
├── PY300/                  # Exploratory Data Analysis
├── PY400/                  # Data Wrangling & Operations
├── PY500/                  # Statistical Inference
├── pyproject.toml          # Project config & dependencies (uv)
├── uv.lock                 # Deterministic lock file
├── requirements.txt        # Pip-compatible dependency list
├── LICENSE                 # CC BY-NC 4.0
└── README.md
```

---

## Who Is This For

- **Beginners** starting their Python journey from scratch
- **Analysts** transitioning from Excel/SQL to Python
- **Students** who want a structured, progressive curriculum
- **Self-learners** who prefer understanding fundamentals over memorizing library calls

---

## License

This work is licensed under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

**You are free to:**
- Share, copy, and redistribute the material
- Adapt, remix, and build upon the material

**Under these terms:**
- **Attribution** — Credit the original work and link to this repository
- **NonCommercial** — You may not use the material for commercial purposes

See the full [LICENSE](LICENSE) file for details.

---

**Author:** [Shri Singh](https://github.com/shri-singh)
