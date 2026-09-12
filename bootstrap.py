from pathlib import Path
import base64
import io
import tarfile

ROOT = Path(__file__).resolve().parent

def ensure_project():
    encoded = "".join((ROOT / f"privaty_payload_{i}.b64").read_text().strip() for i in range(3))
    with tarfile.open(fileobj=io.BytesIO(base64.b64decode(encoded)), mode="r:xz") as archive:
        archive.extractall(ROOT, filter="data")
    return ROOT / "Privaty_Car_V1"

if __name__ == "__main__":
    print(ensure_project())
