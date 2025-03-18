import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime

def extract_video_id(youtube_url):
    """Extract the video ID from a YouTube URL."""
    # Regex pattern to match YouTube URL formats
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',  # Standard YouTube URLs
        r'(?:embed\/)([0-9A-Za-z_-]{11})',  # Embedded URLs
        r'(?:youtu\.be\/)([0-9A-Za-z_-]{11})'  # Shortened youtu.be URLs
    ]
    
    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)
    
    return None

def download_transcript(video_id):
    """Download transcript for a YouTube video."""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript_list
    except Exception as e:
        print(f"Error downloading transcript: {e}")
        return None

def format_transcript(transcript_list):
    """Format transcript for output."""
    if not transcript_list:
        return ""
    
    formatted_transcript = ""
    for entry in transcript_list:
        text = entry['text']
        start_time = entry['start']
        
        # Format timestamp as MM:SS
        minutes = int(start_time // 60)
        seconds = int(start_time % 60)
        timestamp = f"[{minutes:02d}:{seconds:02d}]"
        
        formatted_transcript += f"{timestamp} {text}\n"
    
    return formatted_transcript

def save_transcript_to_file(transcript, video_id):
    """Save transcript to a text file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcript_{video_id}_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(transcript)
    
    return filename

def main():
    # Check if URL was provided
    if len(sys.argv) != 2:
        print("Usage: python youtube_transcript.py <youtube_url>")
        return
    
    youtube_url = sys.argv[1]
    video_id = extract_video_id(youtube_url)
    
    if not video_id:
        print("Error: Could not extract video ID from URL")
        return
    
    print(f"Downloading transcript for video ID: {video_id}")
    transcript_list = download_transcript(video_id)
    
    if transcript_list:
        formatted_transcript = format_transcript(transcript_list)
        filename = save_transcript_to_file(formatted_transcript, video_id)
        print(f"Transcript saved to: {filename}")
    else:
        print("Failed to download transcript")

if __name__ == "__main__":
    main()