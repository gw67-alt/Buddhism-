import time

buddhist_states = [
    "Our precious human life",
    "Death and impermanence",
    "The danger of lower rebirth",
    "Refuge practice",
    "Actions and their effects",
    "Developing renunciation for samsara",
    "Developing equanimity",
    "Recognizing that all living beings are our mothers",
    "Remembering the kindness of living beings",
    "Equalizing self and others",
    "The disadvantages of self-cherishing",
    "The advantages of cherishing others",
    "Exchanging self with others",
    "Great compassion",
    "Taking",
    "Wishing love",
    "Giving",
    "Bodhichitta",
    "Tranquil abiding",
    "Superior seeing",
    "Relying upon a Spiritual Guide"
]

try:
    while True:
        for state in buddhist_states:
            print(f"\r{state}", end="", flush=True)
            time.sleep(60)  # Display each state for 3 seconds
except KeyboardInterrupt:
    print("\nClock stopped.")
