import pandas as pd
class DataProfiler:
    @staticmethod
    def generate_profile(df):
        return {'missing': df.isnull().sum().to_dict(), 'duplicates': int(df.duplicated().sum()), 'stats': df.describe().to_dict(), 'head': df.head(5).to_dict()}
