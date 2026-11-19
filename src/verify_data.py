
from pathlib import Path
from astropy.io import fits

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"

for file_path in sorted(DATA_DIR.glob("*.fits.gz")):

    print("\n" + "=" * 75)
    print("FILE:", file_path.name)
    print("SIZE:", round(file_path.stat().st_size / 1024**2, 2), "MB")

    with fits.open(
        file_path,
        memmap=False,
        checksum=True
    ) as hdul:

        hdul.verify("exception")

        print("\nFITS HDU STRUCTURE")
        print("-" * 75)

        for index, hdu in enumerate(hdul):

            shape = (
                hdu.data.shape
                if hdu.data is not None
                else "No data"
            )

            print(
                f"{index:02d} | "
                f"{hdu.name:25s} | "
                f"{shape}"
            )

        print("\nFITS file opened successfully!")

print("\nAll datasets inspected.")
