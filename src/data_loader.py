import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    """
    Load dataset from a given path.
    """
    return pd.read_csv(path)

