import sys
from bootstrap import ensure_project
sys.path.insert(0, str(ensure_project()))
from app import app
