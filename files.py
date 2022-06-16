import os
from pathlib import Path
from typing import Union
from datetime import datetime

record_folder_name = 'Записи голоса'
record_name = 'Запись'
desktop_path = os.path.expanduser("~/Desktop")
record_folder_path = Path(desktop_path, record_folder_name)

def get_current_time() -> str:
    return datetime.now().strftime("%d.%m.%Y_%H-%M-%S")

def get_record_filepath() -> Path:
    return Path(record_folder_path, f'{record_name} {get_current_time()}.mp3')

def create_folder_if_not_exists(folder_path: Union[Path, str]) -> None:
    if not Path.exists(folder_path):
        Path.mkdir(folder_path)