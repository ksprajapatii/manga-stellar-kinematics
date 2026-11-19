
from pathlib import Path
import requests
import gzip
import os

# Project directories
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"

DATA_DIR.mkdir(parents=True, exist_ok=True)

# MaNGA DR17 dataset URLs
FILES = {
    "manga-8138-12704-MAPS-HYB10-MILESHC-MASTARSSP.fits.gz":
        "https://data.sdss.org/sas/dr17/manga/spectro/analysis/v3_1_1/3.1.0/HYB10-MILESHC-MASTARSSP/8138/12704/manga-8138-12704-MAPS-HYB10-MILESHC-MASTARSSP.fits.gz",

    "manga-8138-12704-LOGCUBE.fits.gz":
        "https://data.sdss.org/sas/dr17/manga/spectro/redux/v3_1_1/8138/stack/manga-8138-12704-LOGCUBE.fits.gz"
}


def download_file(url, filename):

    destination = DATA_DIR / filename
    temporary = DATA_DIR / (filename + ".part")

    if destination.exists():
        print(f"Already exists: {filename}")
        return

    print(f"\nDownloading: {filename}")

    try:
        with requests.get(
            url,
            stream=True,
            timeout=(30, 180)
        ) as response:

            response.raise_for_status()

            if "text/html" in response.headers.get(
                "Content-Type", ""
            ).lower():
                raise ValueError("Server returned HTML, not FITS data.")

            total = int(response.headers.get(
                "Content-Length", 0
            ))

            downloaded = 0

            with open(temporary, "wb") as file:

                for chunk in response.iter_content(
                    chunk_size=1024 * 1024
                ):

                    if chunk:
                        file.write(chunk)
                        downloaded += len(chunk)

                        if total:
                            percent = downloaded / total * 100
                            print(
                                f"\rProgress: {percent:.1f}%",
                                end=""
                            )

        # Verify gzip structure and CRC by reading to EOF.
        with gzip.open(temporary, "rb") as gz:
            while gz.read(8 * 1024 * 1024):
                pass

        os.replace(temporary, destination)

        print(f"\nDownload verified: {filename}")

    except Exception as error:

        if temporary.exists():
            temporary.unlink()

        print(f"\nDownload failed: {error}")
        raise


if __name__ == "__main__":

    for filename, url in FILES.items():
        download_file(url, filename)

    print("\nAll datasets downloaded successfully.")
