# ChronoBias: A Benchmark for Evaluating Time-conditional Group Bias in LLMs

[![Paper](https://img.shields.io/badge/Paper-EMNLP%202025-blue)](https://aclanthology.org/2025.findings-emnlp.405/)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-yellow)](https://huggingface.co/datasets/YOUR_HF_USERNAME/ChronoBias)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This repository contains the **ChronoBias** benchmark dataset and usage examples, corresponding to the following paper:

> **ChronoBias: A Benchmark for Evaluating Time-conditional Group Bias in the Time-sensitive Knowledge of Large Language Models**
> Kyungmin Kim, Youngbin Choi, Hyounghun Kim, Dongwoo Kim, Sangdon Park
> *Findings of the Association for Computational Linguistics: EMNLP 2025*, pp. 7658–7693
> Suzhou, China, November 2025
> DOI: [10.18653/v1/2025.findings-emnlp.405](https://doi.org/10.18653/v1/2025.findings-emnlp.405)

---

## Overview

**ChronoBias** is a benchmark designed to evaluate how **group bias** varies across time intervals in the time-sensitive knowledge of Large Language Models (LLMs). The benchmark focuses on two types of bias:

- **Parametric Knowledge Bias**: Bias in group-specific knowledge encoded in model parameters
- **Time-sensitivity Bias**: Bias in the degree of time-sensitivity across groups

The dataset covers football league standings from multiple international leagues, enabling controlled evaluation of LLM performance across groups (leagues) and time periods.

---

## Dataset

The dataset is hosted on HuggingFace: [trustml-users/ChronoBias](https://huggingface.co/datasets/trustml-users/ChronoBias)

### Dataset Statistics

| Field | Value |
|---|---|
| Total examples | 13,502 |
| Group | 6 (EPL, K-League1, Saudi Pro League, Ligue 1 Algeria, Serie A Brazil, Primera Liga Spain) |
| Time-sensitivity | 3 (never_changing, slow_changing, moderate_to_fast_changing) |

### Data Fields

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for the example |
| `question_id` | string | Identifier for the question |
| `league_name` | string | Name of the football league |
| `season_name` | string | Season year |
| `round` | string | Match round number |
| `question` | string | The question asked to the LLM |
| `answer` | list | Ground-truth answer (list of [team, points] pairs) |
| `context` | string | HTML table with league standings as context (for RAG) |
| `current_date` | string | The date at which the question is posed (YYYY-MM-DD) |
| `start_date` | string | Start date of the round (YYYY/MM/DD) |
| `end_date` | string | End date of the round (YYYY/MM/DD) |
| `end_month` | string | End month of the round (YYYY/MM) |
| `qtype` | string | Question subtype (e.g., top_1, bottom_3) |
| `qtype_agg` | string | Aggregated question type (top or bottom) |
| `question_type` | string | Question category |
| `time_type` | string | How fast this type of information changes over time |

### Example Entry

```json
{
    "league_name": "EPL",
    "current_date": "2025-04-26",
    "time_type": "moderate_to_fast_changing",
    "season_name": "2015",
    "round": "1",
    "qtype": "top_1",
    "start_date": "2014/08/16",
    "end_date": "2014/08/18",
    "question": "Name the top 1 teams in EPL at round 1 during the 2015 season.",
    "answer": [["Chelsea FC", "3"]],
    "context": "<table>...</table>",
    "end_month": "2014/08",
    "qtype_agg": "top",
    "question_type": "league_table_by_round",
    "id": "2014/08/18_EPL_2015_round1_top_league_table_by_round_gold",
    "question_id": "2014/08/18_EPL_2015_round1_top_1_league_table_by_round"
}
```

---

## Quick Start

### Installation

```bash
pip install datasets
```

### Loading the Dataset

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("YOUR_HF_USERNAME/ChronoBias")

print(dataset)
# DatasetDict({
#     train: Dataset({
#         features: ['id', 'question_id', 'league_name', 'season_name', 'round',
#                    'question', 'answer', 'context', 'current_date', 'start_date',
#                    'end_date', 'end_month', 'qtype', 'qtype_agg', 'question_type', 'time_type'],
#         num_rows: 13502
#     })
# })
```

See [examples/load_dataset.py](examples/load_dataset.py) for more detailed usage.

---

## Citation

If you use this dataset or benchmark in your research, please cite our paper:

```bibtex
@inproceedings{kim-etal-2025-chronobias,
    title = "{C}hrono{B}ias: A Benchmark for Evaluating Time-conditional Group Bias in the Time-sensitive Knowledge of Large Language Models",
    author = "Kim, Kyungmin  and
      Choi, Youngbin  and
      Kim, Hyounghun  and
      Kim, Dongwoo  and
      Park, Sangdon",
    editor = "Rambow, Owen  and
      Wanner, Leo  and
      Apidianaki, Marianna  and
      Al-Khalifa, Hend  and
      Eugenio, Barbara Di  and
      Schockaert, Steven",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2025",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-emnlp.405/",
    doi = "10.18653/v1/2025.findings-emnlp.405",
    pages = "7658--7693",
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
