"""Privaty Car boot hook.

Render currently unpacks the historical V1 archive during the build. Loading this
module reapplies the validated visual package, then transparently delegates to the
real Stripe SDK so payment behaviour stays unchanged.
"""
from pathlib import Path
import importlib.machinery
import importlib.util
import sys

_here = Path(__file__).resolve().parent
_patch_file = _here / "sitecustomize.py"
if _patch_file.exists():
    _patch_spec = importlib.util.spec_from_file_location("_privaty_brand_patch", _patch_file)
    if _patch_spec and _patch_spec.loader:
        _patch = importlib.util.module_from_spec(_patch_spec)
        _patch_spec.loader.exec_module(_patch)
        if hasattr(_patch, "_apply"):
            _patch._apply()

# Apply the small live theme override after the archived brand bundle.
_theme_file = _here / "theme_override.py"
if _theme_file.exists():
    _theme_spec = importlib.util.spec_from_file_location("_privaty_theme_override", _theme_file)
    if _theme_spec and _theme_spec.loader:
        _theme = importlib.util.module_from_spec(_theme_spec)
        _theme_spec.loader.exec_module(_theme)
        if hasattr(_theme, "apply"):
            _theme.apply()

# Delegate to the installed third-party Stripe package instead of shadowing it.
_search = []
for _entry in sys.path:
    try:
        _resolved = Path(_entry or ".").resolve()
    except Exception:
        _resolved = None
    if _resolved != _here:
        _search.append(_entry)

_spec = importlib.machinery.PathFinder.find_spec("stripe", _search)
if _spec is None or (_spec.origin and Path(_spec.origin).resolve() == Path(__file__).resolve()):
    raise ImportError("The real Stripe SDK could not be located")
_real = importlib.util.module_from_spec(_spec)
sys.modules[__name__] = _real
_spec.loader.exec_module(_real)
globals().update(_real.__dict__)
