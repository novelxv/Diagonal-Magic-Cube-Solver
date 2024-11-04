import json
import os
import numpy as np
from datetime import datetime

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "../../assets/results")
os.makedirs(RESULTS_DIR, exist_ok=True)

def convert_to_serializable(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()  
    elif isinstance(obj, datetime):
        return obj.isoformat()  
    elif isinstance(obj, (list, dict)):
        return [convert_to_serializable(item) if isinstance(item, (np.ndarray, datetime)) else item for item in obj]
    else:
        return obj

def save_experiment_results(results, filename=None):
    if not filename:
        filename = f"experiment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    else:
        base, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{base}_{timestamp}{ext}"

    file_path = os.path.join(RESULTS_DIR, filename)
    
    serializable_results = {key: convert_to_serializable(value) for key, value in results.items()}
    
    with open(file_path, "w") as f:
        json.dump(serializable_results, f, indent=4)
    
    print(f"Experiment result saved at: {file_path}")
    return file_path

def load_experiment_results(filename):
    file_path = os.path.join(RESULTS_DIR, filename)
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return None
    
    with open(file_path, "r") as f:
        results = json.load(f)
    
    print(f"Experiment result load from: {file_path}")
    return results
