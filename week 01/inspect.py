# week01/inspect.py
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Read a CSV file and return a pandas DataFrame."""
    return pd.read_csv(path)
def shape_and_columns(df: pd.DataFrame) -> dict:
    """Return {rows, cols, column names} as a dict."""
    return {"rows": len(df), "cols": df.shape[1], "column names": list(df.columns)}
def first_n(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return the first n rows."""
    return df.head(n)

df = load_csv("/databricks-datasets/COVID/coronavirusdataset/PatientInfo.csv")
print(shape_and_columns(df))
print(first_n(df))
