from django.shortcuts import render
from django.views import View
from pytube import YouTube

# Create your views here.
class IndexView(View):
    template_name = 'downloader/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Get link from the html form using the name of the input element
        link = request.POST.get('link')
        video = YouTube(link)

        # Set video resolution
        stream = video.streams.get_lowest_resolution()

        # Download the video
        stream.download()

        return render(request, self.template_name)
