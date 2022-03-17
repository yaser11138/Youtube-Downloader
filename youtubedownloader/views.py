from django.shortcuts import render

import youtube_dl
import datetime


def download_video(request):
    if request.method == 'POST':
        video_url = request.POST['url']
        try:
            with youtube_dl.YoutubeDL({}) as yd:
                video_info = yd.extract_info(video_url, download=False)
                context = {"title": video_info["title"],
                           "audio": video_info["formats"][0]["url"],
                           "video": video_info["formats"][-1]["url"],
                           "upload": change_date_format(video_info["upload_date"]),
                           "duration": convert(video_info["duration"]),
                           "thumbnail": video_info["thumbnail"],
                           }
            return render(request, "download.html", context=context)
        except :
            return render(request, "index.html", {"error": True})

    else:
        return render(request, "index.html", context={})


# convert seconds to 00:00:00 time format
def convert(seconds):
    return str(datetime.timedelta(seconds=seconds))


# convert date form this format 20170110 to this format Tue 10 January 2017
def change_date_format(raw_date):
    date = datetime.date(int(raw_date[:4]), int(raw_date[4:6]),int(raw_date[6:]))
    return date.strftime("%a %d %B %Y")