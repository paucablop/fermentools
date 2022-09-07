from mbpls.mbpls import MBPLS

import joblib
import os

MODEL_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def load_pls_glucose_model() -> MBPLS:
    with open(
            os.path.join(MODEL_DIRECTORY, "./pls_glucose.joblib"), "rb"
        ) as f:
            return joblib.load(f)
