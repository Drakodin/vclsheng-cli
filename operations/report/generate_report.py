import numpy as np
import uuid

from operator import itemgetter
from typing import Any, Dict


def get_report(prediction: Dict[str, np.float32], verbose: bool, audio_results = None) -> Dict[str, Any]:
    report = Report(verbose).analyze_prediction(prediction)

    if (audio_results):
        report.analyze_audio_spec(audio_results)

    return report.generate()

class Report:
    def __init__(self, verbose: bool):
        self.id = uuid.uuid4()
        self.report_dict = {}
        self.verbose = verbose
    
    def analyze_prediction(self, prediction: Dict[str, np.float32]):
        if (self.verbose):
            self.report_dict["probabilities"] = {
                "masculine": f"{prediction['masculine'] * 100.00}%",
                "feminine": f"{prediction['feminine'] * 100.00}%"
            }
            self.report_dict["notice"] = "Using 40 Mel Frequency Cepstrum Coefficients parsed by Librosa."
        
        base_prediction = max(list(prediction.items()), key=itemgetter(1))
        self.report_dict["result"] = base_prediction[0]
        return self
    
    def analyze_audio_spec(self, audio_spec_data: dict):
        return self
    
    def generate(self):
        return self.report_dict