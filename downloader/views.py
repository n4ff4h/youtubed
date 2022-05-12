from django.shortcuts import render
from django.views import View
from pytube import YouTube
from django.http import FileResponse
from django.conf import settings

import os

# Create your views here.
class IndexView(View):
    template_name = 'downloader/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            # Get link from the html form using the name of the input element
            url = request.POST.get('url')
            file_path = os.path.join(settings.BASE_DIR, 'videos')

            # Create videos directory if not present
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            try:
                # Download and serve file to the client side
                return FileResponse(open(YouTube(url).streams.first().download(skip_existing=True, output_path=file_path),'rb'))
            finally:
                for file in os.scandir(file_path):
                    os.remove(file.path)
        except:
            return render(request, self.template_name)
