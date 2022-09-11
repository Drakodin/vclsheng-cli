from operations.inference.predict import get_model_response
from operations.report.generate_report import get_report

def run(
    url: str = None,
    input_path: str = None,
    verbose: bool = False,
    audio_spec: bool = False
):
    inf = None
    if (input_path):
        inf = get_model_response(input_path)
    elif(url):
        inf = get_model_response(url, fetch=True)
    
    get_report(inf, verbose)