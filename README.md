# my_custom_watch

`my_custom_watch` is a simple custom smartwatch-style utility for terminal use. It is designed for an environment where internet-enabled smartwatches are not allowed, but students still need a reliable way to see the time and stay motivated during the day.

## What it does

The project currently includes the following functions:

- `time()` - displays the current time and date in color, plus a motivational message.
- `motd()` - shows a short daily message based on the current weekday.
- `earth()` - fetches an ASCII art Earth in the terminal using `curl`.

## Why this exists

School clocks are often unreliable, and personal smartwatches may be banned. This project is a lightweight Python solution that runs in a terminal and gives you a friendly watchface experience without internet smartwatch functionality.

## Requirements

- Python 3
- `curl` (required only for `earth()`)

## Usage

Run the file directly:

```bash
python3 watchface.py
```

Or import it into another Python script or interactive shell:

```python
from watchface import time, motd, earth

time()
motd()
earth()
```

## Available functions

- `time()`
  - prints the current time in `HH:MM:SS` format and the current date
  - uses ANSI colors for a nicer terminal presentation
  - pauses for one second and clears the screen afterward

- `motd()`
  - prints a different message for each weekday
  - encourages productivity, rest, or preparation depending on the day

- `earth()`
  - uses `curl` to retrieve ASCII art from `http://ascii.live/earth`
  - displays a simple ASCII Earth animation or picture in the terminal

## Notes

- The project does not yet include a full graphical interface.
- It is intended to be a starting point for a custom terminal-based watchface.
- Feel free to extend it with additional features like alarms, timers, or a real terminal UI.
