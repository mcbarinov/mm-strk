"""CLI utility functions."""

import importlib.metadata


def get_version() -> str:
    """Return the installed version of mm-strk."""
    return importlib.metadata.version("mm-strk")
