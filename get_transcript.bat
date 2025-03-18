@echo off
echo YouTube Transcript Downloader
echo.
set /p youtube_url=Enter YouTube URL: 
py youtube_transcript.py %youtube_url%
pause