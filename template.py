import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

PROJECT_NAME = "Customer-Churn-Guard"
SRC = f"src/{PROJECT_NAME.lower().replace(' ', '_')}"   

FILES = [

    # Root Files
    ".dockerignore",
    ".gitignore",
    "dockerfile",
    "README.md",

    # Notebooks
    "notebooks/EDA.ipynb",

    # Source
    f"{SRC}/__init__.py",
    f"{SRC}/app/__init__.py",
    f"{SRC}/data/__init__.py",
    f"{SRC}/features/__init__.py",
    f"{SRC}/models/__init__.py",
    f"{SRC}/serving/__init__.py",
    f"{SRC}/utils/__init__.py",

]

DIRECTORIES = [

    ".github/workflows",


    "data/raw_data",
    "data/processed_data",
    "data/external",
    
    "notebooks",

    # MLflow artifacts 
    "mlruns",

    "great_expectations",
    
    "artifacts",
]


def create_directories() -> None:
    """Create project directories."""
    for directory in DIRECTORIES:
        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory  : {path}")


def create_files() -> None:
    """Create project files."""
    for file in FILES:
        file_path = Path(file)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if not file_path.exists():
            file_path.touch()
            logging.info(f"Created file       : {file_path}")
        else:
            logging.info(f"File already exists: {file_path}")


if __name__ == "__main__":
    logging.info("=" * 60)
    logging.info(PROJECT_NAME)
    logging.info("Creating project structure...")
    logging.info("=" * 60)

    create_directories()
    create_files()

    logging.info("=" * 60)
    logging.info("Project structure created successfully.")
    logging.info(f"Total files       : {len(FILES)}")
    logging.info(f"Total directories : {len(DIRECTORIES)}")
    logging.info("=" * 60)