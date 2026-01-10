import random
from pathlib import Path
import shutil

DATA = Path("data/")
TRAIN = DATA / "train/"
VAL = DATA / "val/"
TEST = DATA / "test/"

TRAIN_RATIO = 0.8
VAL_RATIO = 0.1
TEST_RATIO = 0.1

assert TRAIN_RATIO + VAL_RATIO + TEST_RATIO == 1.0

random.seed(42)

for category in ["Interior", "Exterior"]:
    files = [f for f in (DATA / category).rglob("*.*") if f.is_file()]
    random.shuffle(files)

    n = len(files)
    train_end = int(TRAIN_RATIO * n)
    val_end = train_end + int(VAL_RATIO * n)

    train_files = files[:train_end]
    val_files = files[train_end:val_end]
    test_files = files[val_end:]

    for split, split_files in zip(
        [TRAIN, VAL, TEST],
        [train_files, val_files, test_files]
    ):
        (split / category).mkdir(parents=True, exist_ok=True)
        for f in split_files:
            shutil.copy(f, split / category / f.name)

    print(
        f"{category}: "
        f"{len(train_files)} train | "
        f"{len(val_files)} val | "
        f"{len(test_files)} test"
    )
