import logging
import os
from datetime import datetime
from typing import Optional

def setup_logger(debug_mode: bool = False) -> logging.Logger:
    logger = logging.getLogger("AlgorithmStudy")
    logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG if debug_mode else logging.INFO)
        console_formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        log_file = f"{log_dir}/{datetime.now().strftime('%y%m%d')}.log"
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

def log_problem_data(problem_id: str, data: dict) -> None:
    logger = setup_logger()
    logger.info(f"Problem {problem_id} - Title: {data.get('title', 'N/A')}")
    logger.debug(f"Problem {problem_id} - Description: {data.get('description', 'N/A')[:200]}...")
    logger.debug(f"Problem {problem_id} - Input Format: {data.get('input_format', 'N/A')}")
    logger.debug(f"Problem {problem_id} - Output Format: {data.get('output_format', 'N/A')}")