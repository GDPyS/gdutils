# Shared code between scripts.
import time
import os

def ensure_out_folder() -> None:
    """Ensures the presence of the out folder, creating it if it does not
    exist."""

    if not os.path.exists():
        os.mkdir("out")

def get_timestamp() -> int:
    """Returns the current UNIX timestamp as an integer."""

    return int(time.time())

def simple_xor(string: str, key: int) -> str:
    """Simple xor xipher that XORs every char in the `string` by `key`."""

    return "".join(
        chr(ord(char) ^ key) for char in string
    )
