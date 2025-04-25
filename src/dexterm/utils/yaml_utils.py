from enum import Enum
from typing import Any


class YAMLSerializableEnum(Enum):
    """Base class for enums that can be serialized to/from YAML."""

    @classmethod
    def to_yaml(cls, representer: Any, node: Any) -> Any:
        """
        Convert enum instance to YAML representation.

        Args:
            representer: YAML representer object
            node: The enum instance to convert

        Returns:
            YAML scalar node
        """
        return representer.represent_scalar(
            f"!{cls.__name__}",
            "{.name}".format(node),
        )

    @classmethod
    def from_yaml(cls, constructor: Any, node: Any) -> Any:
        """
        Convert YAML representation back to enum instance.
        """
        return cls[node.value]
