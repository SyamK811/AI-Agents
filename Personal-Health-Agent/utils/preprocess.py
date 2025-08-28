import pandas as pd

def load_data(path=r'C:\Users\HP-NBT\Desktop\project\AI Agents\Personal Health Agent\data\health_data.csv'):
    df = pd.read_csv(path)
    df.fillna("None", inplace=True)
    return df
