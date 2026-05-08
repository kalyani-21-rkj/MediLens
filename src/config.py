import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUDIO_PROCESSED_DIR = os.path.join(BASE_DIR, "processed_audio")

SEGMENTS_DIR = os.path.join(
    BASE_DIR,
    "audio_segment_keySearch_summary"
)