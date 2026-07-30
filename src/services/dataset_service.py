import pandas as pd


class DatasetService:

    @staticmethod
    def read_dataset(file_path):

        return pd.read_csv(file_path)


    @staticmethod
    def preview(df):

        return df.head(10).to_html(
            classes="preview-table",
            index=False
        )


    @staticmethod
    def summary(df):

        return {

            "rows": df.shape[0],

            "columns": df.shape[1],

            "missing_values": df.isnull().sum().sum(),

            "duplicate_rows": df.duplicated().sum()

        }
        
    @staticmethod
    def dashboard_summary(dataset_path):

        df = DatasetService.read_dataset(dataset_path)

        return {

            "rows": df.shape[0],

            "columns": df.shape[1],

            "missing": df.isnull().sum().sum(),

            "duplicates": df.duplicated().sum(),

            "memory": round(
                df.memory_usage(deep=True).sum() / 1024,
                2
            )
        }    