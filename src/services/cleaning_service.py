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

    
    # Remove Duplicate Rows
    

    @staticmethod
    def remove_duplicates_from_file(dataset_path):

        df = CleaningService.load_dataset(dataset_path)

        df = df.drop_duplicates()

        CleaningService.save_dataset(df, dataset_path)

    
    # Drop Missing Rows
    

    @staticmethod
    def drop_missing_from_file(dataset_path):

        df = CleaningService.load_dataset(dataset_path)

        df = df.dropna()

        CleaningService.save_dataset(df, dataset_path)

    
    # Fill Missing Values
    

    @staticmethod
    def fill_missing_from_file(dataset_path, strategy):

        df = CleaningService.load_dataset(dataset_path)

        try:

            if strategy == "Fill with Mean":

                numeric_cols = df.select_dtypes(include="number").columns

                df[numeric_cols] = df[numeric_cols].fillna(
                    df[numeric_cols].mean()
                )

            elif strategy == "Fill with Median":

                numeric_cols = df.select_dtypes(include="number").columns

                df[numeric_cols] = df[numeric_cols].fillna(
                    df[numeric_cols].median()
                )

            elif strategy == "Fill with Mode":

                df = df.fillna(df.mode().iloc[0])

            elif strategy == "Fill with 0":

                df = df.fillna(0)

            elif strategy == "Drop Missing Rows":

                df = df.dropna()

            CleaningService.save_dataset(df, dataset_path)

        except Exception as e:

            raise Exception(
                f"Error while filling missing values: {e}"
            )

    
    # Drop Columns
    

    @staticmethod
    def drop_columns_from_file(dataset_path, columns):

        df = CleaningService.load_dataset(dataset_path)

        valid_columns = [

            column

            for column in columns

            if column in df.columns

        ]

        if valid_columns:

            df = df.drop(columns=valid_columns)

            CleaningService.save_dataset(df, dataset_path)

    
    # Rename Column
    

    @staticmethod
    def rename_column_in_file(
        dataset_path,
        old_name,
        new_name
    ):

        df = CleaningService.load_dataset(dataset_path)

        if old_name not in df.columns:

            raise Exception("Column not found.")

        if new_name in df.columns:

            raise Exception(
                "Column name already exists."
            )

        df = df.rename(

            columns={
                old_name: new_name
            }

        )

        CleaningService.save_dataset(df, dataset_path)

    
    # Change Data Type
    

    @staticmethod
    def change_dtype_in_file(
        dataset_path,
        column,
        dtype
    ):

        df = CleaningService.load_dataset(dataset_path)

        if column not in df.columns:

            raise Exception("Column not found.")

        try:

            if dtype == "datetime":

                df[column] = pd.to_datetime(

                    df[column],

                    errors="coerce"

                )

            elif dtype == "category":

                df[column] = df[column].astype(
                    "category"
                )

            elif dtype == "string":

                df[column] = df[column].astype(
                    "string"
                )

            elif dtype == "bool":

                df[column] = df[column].astype(
                    bool
                )

            elif dtype == "int":

                df[column] = df[column].astype(
                    "Int64"
                )

            elif dtype == "float":

                df[column] = df[column].astype(
                    float
                )

            else:

                raise Exception(
                    "Unsupported data type."
                )

            CleaningService.save_dataset(
                df,
                dataset_path
            )

        except Exception as e:

            raise Exception(
                f"Unable to convert datatype: {e}"
            )