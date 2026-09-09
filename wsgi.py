import sys

from bootstrap import ensure_project

project = ensure_project()
sys.path.insert(0, str(project))

from app import app
