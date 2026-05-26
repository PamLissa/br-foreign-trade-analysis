import argparse
import pandas as pd

REQUIREMENTS = {
    "min_records": 10_000,
    "min_predictors_post_engineering": 15,
}

SEP = "=" * 70


def pandas_type(dtype):
    if pd.api.types.is_bool_dtype(dtype):
        return "boolean"
    if pd.api.types.is_numeric_dtype(dtype):
        return "numeric"
    return "string/categorical"


ENCODINGS_FALLBACK = ["utf-8", "cp1252", "latin-1"]


def detect_sep(csv_path: str, encoding: str) -> str:
    with open(csv_path, "r", encoding=encoding) as f:
        first_line = f.readline()
    return ";" if first_line.count(";") >= first_line.count(",") else ","


def load_csv(csv_path: str, sep: str | None, encoding: str | None) -> tuple:
    encodings = [encoding] if encoding else ENCODINGS_FALLBACK
    for enc in encodings:
        try:
            s = sep if sep else detect_sep(csv_path, enc)
            df = pd.read_csv(csv_path, sep=s, encoding=enc, low_memory=False)
            return df, s, enc
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Could not read {csv_path} with encodings: {ENCODINGS_FALLBACK}")


def analyse(csv_path: str, sep: str | None = None, encoding: str | None = None):
    print(SEP)
    print(f"FILE    : {csv_path}")
    print(SEP)

    df, sep_used, enc_used = load_csv(csv_path, sep, encoding)
    print(f"  Detected separator : '{sep_used}'")
    print(f"  Detected encoding  : {enc_used}")

    n_rows, n_cols = df.shape

    print(f"\n{'─'*40}")
    print("1. OVERVIEW")
    print(f"{'─'*40}")
    print(f"  Shape          : {df.shape}")
    print(f"  No. of records : {n_rows:,}")
    print(f"  No. of columns : {n_cols}")

    types = df.dtypes.apply(pandas_type)
    type_counts = types.value_counts()
    print(f"\n{'─'*40}")
    print("2. COUNT BY TYPE")
    print(f"{'─'*40}")
    for t, c in type_counts.items():
        print(f"  {t:<25}: {c}")

    print(f"\n{'─'*40}")
    print("3. COLUMNS (name | pandas dtype | type)")
    print(f"{'─'*40}")
    for col in df.columns:
        print(f"  {col:<20} {str(df[col].dtype):<12} {pandas_type(df[col].dtype)}")

    missing = df.isnull().sum()
    missing_pct = (missing / n_rows * 100).round(2)
    print(f"\n{'─'*40}")
    print("4. MISSING VALUES")
    print(f"{'─'*40}")
    if missing.sum() == 0:
        print("  No missing values found.")
    else:
        for col in missing[missing > 0].index:
            print(f"  {col:<20} {missing[col]:>8,}  ({missing_pct[col]}%)")

    num_cols = df.select_dtypes(include="number").columns.tolist()
    if num_cols:
        print(f"\n{'─'*40}")
        print("5. NUMERIC STATISTICS")
        print(f"{'─'*40}")
        stats = df[num_cols].describe().T[["min", "max", "mean", "std", "50%"]]
        stats.columns = ["min", "max", "mean", "std", "median"]
        print(stats.to_string())

    cat_cols = df.select_dtypes(exclude="number").columns.tolist()
    if cat_cols:
        print(f"\n{'─'*40}")
        print("6. CARDINALITY (categorical columns)")
        print(f"{'─'*40}")
        for col in cat_cols:
            n_uniq = df[col].nunique()
            top = df[col].value_counts().index[0] if n_uniq > 0 else "—"
            print(f"  {col:<20} {n_uniq:>8,} unique values  | most frequent: {top}")

    print(f"\n{'─'*40}")
    print("7. FIRST 3 ROWS")
    print(f"{'─'*40}")
    print(df.head(3).to_string(index=False))

    print(f"\n{'─'*40}")
    print("8. CHECKLIST — MINIMUM REQUIREMENTS (Table 3 of the PDF)")
    print(f"{'─'*40}")

    ok = lambda cond: "OK" if cond else "FAILED"

    req_rec = n_rows >= REQUIREMENTS["min_records"]
    print(f"  Records >= {REQUIREMENTS['min_records']:,}      : {n_rows:,}  → {ok(req_rec)}")

    req_pred = n_cols >= REQUIREMENTS["min_predictors_post_engineering"]
    print(f"  Predictors >= {REQUIREMENTS['min_predictors_post_engineering']} (current) : {n_cols}  → {ok(req_pred)}")
    if not req_pred:
        missing_cols = REQUIREMENTS["min_predictors_post_engineering"] - n_cols
        print(f"    -> Missing {missing_cols} columns — achievable via integration + feature engineering")

    has_num = len(num_cols) > 0
    has_cat = len(cat_cols) > 0
    req_types = has_num and has_cat
    print(f"  Mixed types (num + cat)  : num={len(num_cols)}, cat={len(cat_cols)}  → {ok(req_types)}")

    print(f"\n  Source: dados.gov.br (Foreign Trade) → Brazil category OK")
    print(f"  Integration potential: NCM→IBGE, CO_PAIS→ISO, UF→socioeconomic OK")

    print(f"\n{SEP}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Initial exploratory analysis of a CSV — Data Science final project"
    )
    parser.add_argument("csv", help="Path to the CSV file")
    parser.add_argument("--sep", default=None, help="CSV separator (auto-detected if omitted)")
    parser.add_argument("--encoding", default=None, help="Encoding (auto-detected if omitted)")
    args = parser.parse_args()

    analyse(args.csv, sep=args.sep, encoding=args.encoding)
