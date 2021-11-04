import requests
import shutil

image_url = "https://firebasestorage.googleapis.com/v0/b/fashion-detection-1f3f2.appspot.com/o/a.jpg?alt=media&token=05930b00-12ad-43da-9fd4-2577dd84289f"
name = image_url.split('?')[-2]
filename = name.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream=True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image sucessfully Downloaded: ', filename)
else:
    print('Image Couldn\'t be retreived')
