from pathlib import Path
import base64
import io
import shutil
import zipfile

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "appsrc"
PAYLOAD_PARTS = 9


def ensure_project():
    parts = [ROOT / f"privaty_payload_{i}.b64" for i in range(PAYLOAD_PARTS)]
    missing = [str(p.name) for p in parts if not p.exists()]
    if missing:
        raise FileNotFoundError(f"Missing Privaty Car payload parts: {', '.join(missing)}")

    encoded = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
    raw = base64.b64decode(encoded)

    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        archive.extractall(TARGET)

    return TARGET


if __name__ == "__main__":
    project = ensure_project()
    print(f"Privaty Car extracted to {project}")
