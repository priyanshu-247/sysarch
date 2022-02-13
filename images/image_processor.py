# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow
# usage change image_resize & post value

image_resize='chart-preview.png'
post= 'post_img/'+'post2.png'
from PIL import Image
image = Image.open(image_resize)
new_image = image.resize((200, 200))
new_image.save(post)