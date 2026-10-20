import os
import pandas as pd
from datetime import datetime

df = pd.DataFrame({
    'timestamp': [datetime.now()],
    'value': [1]
})

# create data folder and save csv
os.makedirs('data', exist_ok=True)
file_path = 'data/data.csv'
df.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)
