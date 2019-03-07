from typing import AnyStr


class Indent:
    """Indentation class."""

    def __init__(self, depth: int = 4,
                 spaceholder: str = ' '):
        self._indent = 0
        self._depth = int(depth)
        self._spaceholder = spaceholder

    def __enter__(self):
        self._indent += self._depth
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._indent -= self._depth

    def __call__(self, *args, **kwargs):
        return self.spaces()

    def spaces(self) -> str:
        """Return spaces for indentation."""

        return self._spaceholder * self._indent

    def spaceholder(self) -> AnyStr:
        """Returns indent spaceholder."""

        return self._spaceholder
