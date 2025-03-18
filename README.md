# YouTube Transcript Downloader

A simple Python script to download transcripts from YouTube videos.

## Installation

1. Clone this repository
2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

### Command Line

```
python youtube_transcript.py <youtube_url>
```

### Batch File (Windows)

Run `get_transcript.bat` and enter the YouTube URL when prompted.

## Features

- Extracts video ID from different YouTube URL formats
- Downloads transcript using youtube-transcript-api
- Formats transcript with timestamps
- Saves transcript to a text file with date and time

## Output

The transcript is saved to a file named `transcript_[video_id]_[timestamp].txt` in the current directory.