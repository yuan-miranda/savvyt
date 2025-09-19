
# Savvy YouTube (savvyt)

A Python script that saves YouTube videos as MP3 or MP4 using [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [ffmpeg](https://ffmpeg.org/).


https://github.com/user-attachments/assets/7b0e6931-8cb3-495b-b7b5-9560267ec966


[sauce](https://youtu.be/dQw4w9WgXcQ?si=_N2JCn6x8-l7MRFC)

## Install

Clone the repository and install the dependencies

```
git clone https://github.com/yuan-miranda/savvyt.git
```

```
cd savvyt
```

```
pip install -r requirements.txt
```

* Install a cookie parser for [Chrome/Edge](https://chromewebstore.google.com/detail/cclelndahbckbenkjhflpdbgdldlbecc?utm_source=item-share-cb), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)
> [!NOTE]
> After installing, save the cookies.txt file containing cookies from youtube.com only inside `savvyt/` directory.


## Usage

### Run the script:

```
python .\main.py
```
> [!NOTE]
> It will prompt you to enter a YouTube URL and choose whether to download it as MP4 or MP3. The output will be saved in the current directory.

## Contributing

PRs accepted.
