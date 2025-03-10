import os

import pandas as pd

from helpers_logging import logging_status


def display_results(df: pd.DataFrame) -> None:
    file_path = "temp.html"

    if logging_status:
        print(f"display data frame shape={df.shape}")

    html_table = df.to_html()
    with open(file_path, 'w') as file:
        file.write(html_table)
    print(f"html results ={file_path}")

    os.startfile(file_path)
