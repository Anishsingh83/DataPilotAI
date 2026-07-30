import pandas as pd


class ExplorerService:

    @staticmethod
    def load_dataset(dataset_path):
        return pd.read_csv(dataset_path)

    @staticmethod
    def get_dataset_info(df):

        return {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "memory": round(
                df.memory_usage(deep=True).sum() / 1024,
                2
            ),
            "column_names": list(df.columns)
        }

    @staticmethod
    def get_page(df):

        return df.to_html(
            classes="preview-table display",
            table_id="datasetTable",
            index=False,
            border=0
        )