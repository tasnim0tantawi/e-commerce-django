from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'))

]

# Now we have a unique url path for our images.
# When we upload an image, it will be saved in the 'media' folder after creating a folder with the name 'images'.
# static/media/images/imagename.jpg
# static() function is used to serve static files like images, css, js, etc.

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
