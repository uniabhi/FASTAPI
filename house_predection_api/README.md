# California house prediction API

Run these PowerShell commands from the repository root (`Python_test_2026`):

```powershell
.\FASTAPI\venv\Scripts\python.exe -m pip install -r .\FASTAPI\house_predection_api\requirements.txt
.\FASTAPI\venv\Scripts\python.exe -m uvicorn FASTAPI.house_predection_api.main:app --reload
```

Open http://127.0.0.1:8000/docs and use **POST /predict** with:

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.9841,
  "AveBedrms": 1.0238,
  "Population": 322,
  "AveOccup": 2.5556,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

The `confidence_range` response uses a fixed $39,000 margin; it is an approximate error range, not a statistically calibrated confidence interval.

The model and feature files are loaded relative to `main.py`. Retrain with:

```powershell
.\FASTAPI\venv\Scripts\python.exe .\FASTAPI\house_predection_api\train.py
```

Training and exploration download the California housing dataset on their first run. The API uses the existing model files without downloading data. The scikit-learn version matches the supplied model's training version.
