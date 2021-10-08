# typoer
Types text with typos and correction

# Installation

1. Download `typoer.py` and `requirements.txt`
2. ```pip install -r requirements```
3. In your file add `from typoer import typoer`

# Usage

## Example

```
text = r'''Lorem Ipsum is simply dummy text of the printing and typesetting industry.'''
typoer(text, wpm = 100, accuracy = 0.95, wait_key = 'up', break_key = 'down')
```

This will type `text` at an average rate of 100WPM with an accuracy of 95%. Press <kdb>Up<kbd> to begin typing, and <kdb>Down<kbd> to stop.
