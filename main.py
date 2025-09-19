import shutil
from yt_dlp import YoutubeDL


def has_ffmpeg():
    return shutil.which("ffmpeg") is not None


def download(url, file_type="mp4"):
    try:
        if file_type == "mp3" and not has_ffmpeg():
            print("ffmpeg not found. Please download and add it to your PATH.")
            print("https://ffmpeg.org/")
            return

        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s",
            "cookiefile": "cookies.txt",
        }

        # mp4
        if file_type == "mp4":
            ydl_opts.update(
                {
                    "format": "bestvideo+bestaudio/best",
                    "merge_output_format": "mp4",
                    "postprocessors": [
                        {
                            "key": "FFmpegVideoConvertor",
                            "preferedformat": "mp4",
                        },
                        {
                            "key": "FFmpegMetadata",
                        },
                    ],
                    "postprocessor_args": [
                        "-c:v", "copy",
                        "-c:a", "aac",
                        "-b:a", "192k"
                    ],
                }
            )


        # mp3
        elif file_type == "mp3":
            ydl_opts.update(
                {
                    "format": "bestaudio/best",
                    "postprocessors": [
                        {
                            "key": "FFmpegExtractAudio",
                            "preferredcodec": "mp3",
                            "preferredquality": "192",
                        }
                    ],
                }
            )

        else:
            print("Unsupported file type. Please choose 'mp4' or 'mp3'.")
            return

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    file_type = input("Enter file type [mp4 | mp3]: ").strip().lower()
    download(url, file_type=file_type)
