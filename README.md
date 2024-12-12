# typoer
Types text with typos and correction

![demo](demo.gif)

# Installation

1. Download `typoer.py` and `requirements.txt`
2. ```pip install -r requirements.txt```
3. In your file add `from typoer import typoer`

# Usage

## Example

```
from typoer import typoer
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
typoer(text, wpm = 120, accuracy = 0.8, wait_key = 'right')
```

This will type `text` at an average rate of 120WPM with an accuracy of 80%. Press the right arrow key to begin typing.

# Documentation

See `typoer.py`
