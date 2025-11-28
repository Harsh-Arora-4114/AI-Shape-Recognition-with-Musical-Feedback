#!/usr/bin/env python

# Giving class label from probabilities
# FIX: Removed the unnecessary and deprecated 'from keras.utils import np_utils'
import numpy as np


def probas_to_classes(y_pred):
    """
    Converts model prediction probabilities to class labels.
    Handles both binary and categorical (one-hot) outputs.
    """
    if len(y_pred.shape) > 1 and y_pred.shape[1] > 1:
        # Categorical output: return the index of the max probability
        return categorical_probas_to_classes(y_pred)
    # Binary output: return 1 if probability > 0.5, else 0
    return np.array([1 if p > 0.5 else 0 for p in y_pred])


def categorical_probas_to_classes(p):
    """
    For categorical output, returns the index of the maximum probability.
    """
    return np.argmax(p, axis=1)