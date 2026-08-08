import os

import pandas as pd

import matplotlib.pyplot as plt

import plotly.express as px

import plotly.io as pio

class EDAService:

    # Load Dataset

    @staticmethod
    def load_dataset(dataset_path):

        return pd.read_csv(dataset_path)

    # Save Dataset

    @staticmethod
    def save_dataset(df, dataset_path):

        df.to_csv(dataset_path, index=False)

    # Dataset Summary

    @staticmethod
    def dataset_summary(dataset_path):

        df = EDAService.load_dataset(dataset_path)

        return {

            "rows": df.shape[0],

            "columns": df.shape[1],

            "missing": int(
                df.isna().sum().sum()
            ),

            "duplicates": int(
                df.duplicated().sum()
            ),

            "memory": round(

                df.memory_usage(
                    deep=True
                ).sum() / 1024,

                2

            ),

            "column_names": list(df.columns),

            "numeric_columns": list(

                df.select_dtypes(
                    include="number"
                ).columns

            )

        }

    # Numerical Summary

    @staticmethod
    def numerical_summary(dataset_path):

        df = EDAService.load_dataset(dataset_path)

        numeric_df = df.select_dtypes(
            include="number"
        )

        result = []

        for column in numeric_df.columns:

            result.append({

                "column": column,

                "mean": round(
                    numeric_df[column].mean(),
                    2
                ),

                "median": round(
                    numeric_df[column].median(),
                    2
                ),

                "std": round(
                    numeric_df[column].std(),
                    2
                )

            })

        return result

    # Dataset Preview

    @staticmethod
    def dataset_preview(dataset_path):

        df = EDAService.load_dataset(
            dataset_path
        )

        return df.head(10)

    @staticmethod
    def generate_histogram(dataset_path, column):

        import plotly.express as px

        df = EDAService.load_dataset(dataset_path)
        print("Column Type :", df[column].dtype)
        print(df[column].head(10))

        if column not in df.columns:

            raise Exception("Invalid column selected.")

        fig = px.histogram(

            df,

            x=column,

            nbins=20,

            title=f"{column} Distribution"

        )

        fig.update_layout(

            template="plotly_white",

            margin=dict(

                l=20,

                r=20,

                t=50,

                b=20

            )

        )

        return fig.to_json()
    
    # Correlation Heatmap

    @staticmethod
    def generate_heatmap(dataset_path):

        df = EDAService.load_dataset(dataset_path)

        numeric_df = df.select_dtypes(include="number")

        if numeric_df.empty:

            raise Exception("No numerical columns found.")

        correlation = numeric_df.corr()

        fig = px.imshow(

            correlation,

            text_auto=True,

            color_continuous_scale="RdBu_r",

            title="Correlation Heatmap"

        )

        fig.update_layout(

            template="plotly_white",

            margin=dict(

                l=20,

                r=20,

                t=50,

                b=20

            )

        )

        return fig.to_json()