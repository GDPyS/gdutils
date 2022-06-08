from shared import (
    ensure_out_folder,
    get_timestamp,
    prettify_xml,
    simple_xor,
)
import logging
import base64
import zlib
import sys
import os

def load_file(path: str) -> str:
    """Loads the file specified in `path` as a string."""

    with open(path, "r") as f:
        return f.read()

def write_file(path: str, contents: str) -> None:
    """Writes a string into a file specified in `path`."""

    with open(path, "w") as f:
        f.write(contents)

def main(args: list[str]) -> int:
    logging.basicConfig(level= logging.INFO)
    if len(args) <= 1:
        logging.error("No level path provided!")
        return 1
    
    path = args[1]

    if not os.path.exists(path):
        logging.error(f"File at the location '{path}' does not exist!")
        return 1

    logging.info("Loading the data file...")
    file = load_file(path)

    # Base64 decode.
    logging.info("Decoding the data")
    de_xored = simple_xor(file, 0xb)
    decoded = base64.b64decode(de_xored, altchars='-_')
    del file

    # ZLIB decompression.
    logging.info("Decompressing the save data...")
    dezlibed = zlib.decompress(decoded[10:], -zlib.MAX_WBITS).decode()
    del decoded

    # Pretty-print it.
    logging.info("Prettifying the output...")
    prettified = prettify_xml(dezlibed)
    del dezlibed


    # Write to file.
    cur_ts = get_timestamp()
    filename = f"out/{cur_ts}-level_data.plist"
    logging.info(f"Writing result to {filename}")
    ensure_out_folder()
    write_file(filename, prettified)
    logging.info("Done!")
    
    return 0


if __name__ == "__main__":
    raise SystemExit(
        main(sys.argv)
    )
