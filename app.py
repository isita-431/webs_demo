import io
import cloudpickle
import requests

response = requests.get("https://github.com/isita-431/BADM-576/blob/main/App/artifacts/model/model.pkl")

try:
    model = cloudpickle.loads(response.content)
except cloudpickle.pickle.UnpicklingError:
    # Try decoding the response content to a string using UTF-8 encoding
    content_str = response.content.decode('utf-8')
    model = cloudpickle.loads(content_str.encode('utf-8'))

# Use the model as needed
