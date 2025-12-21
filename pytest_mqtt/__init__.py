from importlib.metadata import PackageNotFoundError, version

from .model import MqttMessage

try:
    __version__ = version("pytest-mqtt")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__ = ["MqttMessage"]
