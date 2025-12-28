from src.data_loader import load_dataset

def test_load_dataset_exists():
    assert callable(load_dataset)
