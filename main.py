from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess
import shutil


def has_ffmpeg():
    return shutil.which("ffmpeg") is not None


def download(url, file_type="mp4"):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        minutes, seconds = divmod(yt.length, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"\n{yt.title} [{hours:02d}:{minutes:02d}:{seconds:02d}]")

        # mp4
        if file_type == "mp4":
            ys = yt.streams.get_highest_resolution()
            ys.download()

        # mp3
        elif file_type == "mp3":
            if not has_ffmpeg():
                print("ffmpeg not found. Please download and add it to your PATH.")
                print("https://ffmpeg.org/")
                return

            ys = yt.streams.get_lowest_resolution()
            out_file = ys.download()

            base, _ = os.path.splitext(out_file)
            new_file = base + ".mp3"

            subprocess.run(
                ["ffmpeg", "-i", out_file, "-q:a", "0", "-map", "a", "-y", new_file],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT,
            )
            os.remove(out_file)

        # unsupported
        else:
            print("Unsupported file type. Please choose 'mp4' or 'mp3'.")
            return

        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    file_type = input("Enter file type [mp4 | mp3]: ").strip().lower()

    download(url, file_type=file_type)
