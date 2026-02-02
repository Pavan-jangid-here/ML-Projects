import numpy as np
import pandas as pd
from scipy.stats import ks_2samp

def detect_drift(reference_df, new_df, threshold=0.05):
    drift_report = {}

    for col in reference_df.columns:
        stat, p_value = ks_2samp(reference_df[col], new_df[col])
        drift_report[col] = {
            "p_value": p_value,
            "drift": p_value < threshold
        }

    return drift_report
