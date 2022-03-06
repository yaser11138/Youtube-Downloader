from django.shortcuts import render, redirect

import youtube_dl
import datetime


def download_video(request):
    if request.method == 'POST':
        video_url = request.POST['url']
        with youtube_dl.YoutubeDL({}) as yd:
            video_info = yd.extract_info(video_url, download=False)
            context = {"title": video_info["title"],
                       "audio": video_info["formats"][0]["url"],
                       "video": video_info["formats"][-1]["url"],
                       "upload": video_info["upload_date"],
                       "duration": convert(video_info["duration"]),
                       "thumbnail": video_info["thumbnail"],
                       }
        return render(request, "h.html", context=context)
    else:
        return render(request,"index.html",context={})

# convert seconds to 00:00:00 time format
def convert(seconds):
    return str(datetime.timedelta(seconds=seconds))


