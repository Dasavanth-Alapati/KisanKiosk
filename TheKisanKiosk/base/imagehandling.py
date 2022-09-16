from PIL import Image
from django.conf import settings


def imageformatter(image):
    img = Image.open(settings.MEDIA_ROOT/'ProfilePics'/image)
    img = img.convert('RGB')
    img.resize((500, 500))
    img.save(settings.MEDIA_ROOT/'ProfilePics'/(image.split('.')[0]+'.jpeg'),format='JPEG')



