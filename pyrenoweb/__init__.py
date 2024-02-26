# ruff: noqa: F401
"""A Python Wrapper to communicate with RenoWeb API."""

from __future__ import annotations

from pyrenoweb.api import (
    GarbageCollection,
    RenowWebNotSupportedError,
    RenowWebNotValidAddressError,
    RenowWebNoConnection,
)
from pyrenoweb.data import RenoWebAddressInfo, RenoWebCollectionData

from pyrenoweb.const import MUNICIPALITIES_ARRAY

__title__ = "pymrenoweb"
__version__ = "2.0.0"
__author__ = "briis"
__license__ = "MIT"