"""
ChronoBias Dataset - Usage Examples
Paper: https://aclanthology.org/2025.findings-emnlp.405/
Dataset: https://huggingface.co/datasets/YOUR_HF_USERNAME/ChronoBias
"""

from datasets import load_dataset

# ── 1. Load the full dataset ──────────────────────────────────────────────────
dataset = load_dataset("tml-lab/ChronoBias")
print(dataset)
# DatasetDict({
#     train: Dataset({
#         features: [...],
#         num_rows: 13502
#     })
# })

data = dataset["train"]

# ── 2. Inspect a single example ───────────────────────────────────────────────
example = data[0]
print("\n--- Example Entry ---")
print(f"Question : {example['question']}")
print(f"Answer   : {example['answer']}")
print(f"League   : {example['league_name']}")
print(f"Season   : {example['season_name']}, Round: {example['round']}")
print(f"Time Type: {example['time_type']}")

# ── 3. Filter by league ───────────────────────────────────────────────────────
epl_data = data.filter(lambda x: x["league_name"] == "EPL")
print(f"\nEPL examples: {len(epl_data)}")

kl_data = data.filter(lambda x: x["league_name"] == "K-League1")
print(f"K-League1 examples: {len(kl_data)}")

# ── 4. Filter by question type ────────────────────────────────────────────────
top1_data = data.filter(lambda x: x["qtype"] == "top_1")
print(f"\ntop_1 question examples: {len(top1_data)}")

# ── 5. Filter by time_type ────────────────────────────────────────────────────
fast_changing = data.filter(lambda x: x["time_type"] == "moderate_to_fast_changing")
print(f"moderate_to_fast_changing examples: {len(fast_changing)}")

# ── 6. Use context for RAG evaluation ────────────────────────────────────────
print("\n--- RAG Context Example ---")
rag_example = data[0]
print(f"Question : {rag_example['question']}")
print(f"Context  : {rag_example['context'][:200]}...")   # HTML table with standings
print(f"Answer   : {rag_example['answer']}")

# ── 7. Convert to pandas DataFrame ────────────────────────────────────────────
df = data.to_pandas()
print(f"\nDataFrame shape: {df.shape}")
print(df[["league_name", "qtype", "time_type", "season_name"]].value_counts().head(10))
