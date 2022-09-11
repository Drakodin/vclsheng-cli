import torch
import aiohttp
import asyncio
import librosa
import numpy as np
import io

from arch import ANN

model = ANN()
device = torch.device("cpu")
model.load_state_dict(torch.load("model.pth", map_location="cpu"))
model.eval()

def get_model_response(path: str, fetch: bool = False):
    tensor = None

    if fetch:
        tensor = asyncio.run(audio_to_tensor_async(path))
    else:
        tensor = audio_to_tensor(path)

    prediction = model(tensor).detach().numpy()
    return {
        "masculine": prediction[0],
        "feminine": prediction[1]
    }

def audio_to_tensor(audio) -> torch.Tensor:
    X, sr = librosa.core.load(audio)
    features = np.mean(librosa.feature.mfcc(y=X, sr=sr, n_mfcc=40).T, axis=0)

    tensor = torch.from_numpy(features)
    return tensor

async def audio_to_tensor_async(url) -> torch.Tensor:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            buffer = io.BytesIO(await response.read())

            return audio_to_tensor(buffer)