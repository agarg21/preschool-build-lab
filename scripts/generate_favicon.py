"""Generate the neutral fallback for browsers' implicit /favicon.ico request."""

from pathlib import Path
import struct


SITE = Path(__file__).resolve().parents[1] / "site"


def favicon_bytes():
    # One transparent BGRA pixel plus a DWORD-aligned transparent AND mask.
    pixels = bytes(4)
    mask = bytes((0x80, 0, 0, 0))
    bitmap = struct.pack("<IiiHHIIiiII", 40, 1, 2, 1, 32, 0, len(pixels), 0, 0, 0, 0)
    image = bitmap + pixels + mask
    directory = struct.pack("<HHH", 0, 1, 1)
    entry = struct.pack("<BBBBHHII", 1, 1, 0, 0, 1, 32, len(image), 22)
    return directory + entry + image


def main():
    (SITE / "favicon.ico").write_bytes(favicon_bytes())
    print("generated neutral favicon fallback")


if __name__ == "__main__":
    main()
