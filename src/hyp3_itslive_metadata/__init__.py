"""ITS_LIVE metadata generator"""

from importlib.metadata import version


__version__ = version(__name__)

__all__ = [
    '__version__',
]
