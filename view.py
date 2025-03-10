import os

import pandas as pd

from helpers_logging import log_message


def display_results(df: pd.DataFrame) -> None:
    file_path = "temp.html"

    log_message(f"display data frame shape={df.shape}")

    html_table = df.to_html()
    with open(file_path, 'w') as file:
        file.write(html_table)

    log_message(f"html results ={file_path}")

    os.startfile(file_path)
