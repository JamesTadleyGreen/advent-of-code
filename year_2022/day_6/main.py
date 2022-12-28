from typing import List, Tuple
from year_2022.day_6.data import (
    test_data_1,
    test_data_2,
    test_data_3,
    test_data_4,
    test_data_5,
    actual_data,
)


def start_of_packet_index(data: str, num_unique_chars: int) -> int:
    message_length = len(data)
    for i in range(0, message_length - num_unique_chars + 1):
        packet = data[i : i + num_unique_chars]
        if len(packet) == len(set(packet)):
            return i + num_unique_chars


def jamie():
    # return start_of_packet_index(actual_data, 4)
    return start_of_packet_index(actual_data, 14)
