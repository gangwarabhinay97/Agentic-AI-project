import pandas as pd
class DataIngestion:
    @staticmethod
    def load_data(file_source, filename):
        if filename.endswith('.csv'): return pd.read_csv(file_source)
        return pd.read_excel(file_source)
    @staticmethod
    def inspect_schema(df):
        return {'rows': len(df), 'cols': df.shape[1], 'columns': df.columns.tolist(), 'dtypes': df.dtypes.astype(str).to_dict()}
