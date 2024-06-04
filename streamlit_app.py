import sys

import streamlit as st
import uuid


def bytes_to_human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0 or unit == 'PB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def human_readable_to_bytes(size_str):
    size_str = size_str.strip().upper()  # Remove whitespace and convert to upper case
    units = {"K": 1024, "KB": 1024, "M": 1024**2, "MB": 1024**2,
             "G": 1024**3, "GB": 1024**3, "T": 1024**4, "TB": 1024**4}

    for unit, value in units.items():
        if size_str.endswith(unit):
            try:
                size = float(size_str[:-(len(unit) + 1)])
                return int(size * value)
            except ValueError:
                raise ValueError(f"Invalid number in size string: {size_str}")

    raise ValueError(f"Invalid size string: {size_str}")


array = []


def generate(size):
    for i in range(size):
        array.append("test")


value = st.text_input("use memory", value="300MB")

add = st.button('Add')
if add:
    generate(human_readable_to_bytes(value))
    st.text(f'Currently used memory: {bytes_to_human_readable_size(sys.getsizeof(array))}')
    st.text(len(array))

