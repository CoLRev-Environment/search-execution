"""Execution framework for open and automated systematic literature searches."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version

try:
    __version__ = version("search-execution")
except PackageNotFoundError:
    __version__ = "0.0.0"
