import os

import pandas as pd


def display_results(df: pd.DataFrame) -> None:
    file_path = "temp.html"

    print(f"display data frame shape={df.shape}")

    html_table = df.to_html()
    with open(file_path, 'w') as file:
        file.write(html_table)
    print(f"html results ={file_path}")

    os.startfile(file_path)


def export_data(df: pd.DataFrame) -> None:
    file_path = "results.csv"
    df.to_csv(file_path, index=False)
    print(f"export results file={file_path}")
