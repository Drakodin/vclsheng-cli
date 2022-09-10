from inference.predict import get_model_response

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