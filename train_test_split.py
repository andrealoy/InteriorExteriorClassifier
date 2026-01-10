import random 
from pathlib import Path
import shutil

DATA = Path("data/")
TRAIN = DATA / "train/"
TEST = DATA / "test/"
TEST_SIZE = 0.8

random.seed(42)

for category in ["Interior", "Exterior"]:
    files = list((DATA / category).rglob("*.*"))
    files = [f for f in files if f.is_file()]

    random.shuffle(files)
    split = int(TEST_SIZE * len(files))

    train_files = files[:split]
    test_files = files[split:]

    # Créer les dossiers 
    (TRAIN / category).mkdir(parents=True, exist_ok=True)
    (TEST / category).mkdir(parents=True, exist_ok=True)

    for f in train_files:
        shutil.copy(f, TRAIN / category / f.name)
    for f in test_files:
        shutil.copy(f, TEST / category / f.name)

print(f"Copied {len(train_files)} files to {TRAIN} and {len(test_files)} files to {TEST}")