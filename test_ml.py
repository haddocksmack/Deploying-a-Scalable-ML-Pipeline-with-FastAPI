import pytest

from sklearn.ensemble import AdaBoostClassifier

from train_model import data, y_test, preds, model
from ml.model import compute_model_metrics


def test_precision():
    """
    Test if precision is at or above acceptable threshold: 0.5
    """
    precision, _, _ = compute_model_metrics(y_test, preds)
    assert precision >= 0.5


def test_data_shape():
    """
    Test to ensure data has no null values
    """
    assert data.shape == data.dropna().shape


def test_model_algorithm():
    """
    Test to ensure model is expected algorithm
    """
    assert isinstance(model, AdaBoostClassifier)
