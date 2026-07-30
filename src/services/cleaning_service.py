import pandas as pd


class CleaningService:

    @staticmethod
    def load_dataset(dataset_path):
        return pd.read_csv(dataset_path)

    @staticmethod
    def save_dataset(df, dataset_path):
        df.to_csv(dataset_path, index=False)

    @staticmethod
    def dataset_summary(dataset_path):

        df = CleaningService.load_dataset(dataset_path)

        return {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": int(df.isna().sum().sum()),
            "duplicate_rows": int(df.duplicated().sum()),
            "memory": round(
                df.memory_usage(deep=True).sum() / 1024,
                2
            ),
            "column_names": list(df.columns)
        }

    @staticmethod
    def remove_duplicates_from_file(dataset_path):

        df = CleaningService.load_dataset(dataset_path)

        df = df.drop_duplicates()

        CleaningService.save_dataset(df, dataset_path)

    @staticmethod
    def drop_missing_from_file(dataset_path):

        df = CleaningService.load_dataset(dataset_path)

        df = df.dropna()

        CleaningService.save_dataset(df, dataset_path)

    @staticmethod
    def fill_missing_from_file(dataset_path, value):

        df = CleaningService.load_dataset(dataset_path)

        df = df.fillna(value)

        CleaningService.save_dataset(df, dataset_path)

    @staticmethod
    def drop_columns_from_file(dataset_path, columns):

        df = CleaningService.load_dataset(dataset_path)

        columns = [
            column
            for column in columns
            if column in df.columns
        ]

        if columns:
            df = df.drop(columns=columns)

        CleaningService.save_dataset(df, dataset_path)

    @staticmethod
    def rename_column_in_file(dataset_path, old_name, new_name):

        df = CleaningService.load_dataset(dataset_path)

        if old_name in df.columns:
            df = df.rename(
                columns={
                    old_name: new_name
                }
            )

        CleaningService.save_dataset(df, dataset_path)

    @staticmethod
    def change_dtype_in_file(dataset_path, column, dtype):

        df = CleaningService.load_dataset(dataset_path)

        if column in df.columns:

            try:

                if dtype == "datetime":
                    df[column] = pd.to_datetime(df[column])

                elif dtype == "category":
                    df[column] = df[column].astype("category")

                elif dtype == "string":
                    df[column] = df[column].astype(str)

                else:
                    df[column] = df[column].astype(dtype)

            except Exception:
                pass

        CleaningService.save_dataset(df, dataset_path)