import numpy as np
import uuid

from operator import itemgetter
from typing import Any, Dict


def get_report(prediction: Dict[str, np.float32], verbose: bool) -> Dict[str, Any]:
    report = Report(verbose).analyze(prediction).generate()
    return report

class Report:
    def __init__(self, verbose: bool):
        self.id = uuid.uuid4()
        self.report_dict = {}
        self.verbose = verbose
    
    def analyze(self, prediction: Dict[str, np.float32]):
        if (self.verbose):
            self.report_dict.update({"probabilities", {
                "masculine": f"{prediction['masculine']}%",
                "feminine": f"{prediction['feminine']}%"
            }})
            self.report_dict.update({"notice", "Using 40 Mel Frequency Cepstrum Coefficients parsed by Librosa."})
        
        base_prediction = max(list(prediction.items()), key=itemgetter(1))
        self.report_dict.update({"result", base_prediction[0]})
        return self
    
    def generate(self):
        return self.report_dict