import instaloader
import requests, time
from PIL import Image
from io import BytesIO as bt

lo = instaloader.Instaloader(); ses = requests.Session()
pros = lambda url: instaloader.Post.from_shortcode(lo.context,str(url[1].strip("/")))
url = input("url ignya? ").split("p/")
pic = pros(url).url; vid = pros(url).video_url
print("\nHere image url>>",pic)
print("\nHere video url>>",vid)
wan = input("\nWant to download? y/n: ").lower()
if wan:
    if vid is None:
        r = ses.get(pic,stream=True); im = Image.open(bt(r.content))
        im.save(f"picture{url[1].strip('/')}.jpg"); print("completes download pic")
    else:
        r = ses.get(pic,stream=True); im = Image.open(bt(r.content))
        im.save(f"picture{url[1].strip('/')}.jpg"); print("completes download pic")
        time.sleep(2)
        rr = ses.get(vid, stream=True)
        with open(f"videos{url[1].strip('/')}.mp4","wb") as f:
            for cc in rr.iter_content(chunk_size=1024):
                if cc:
                    f.write(cc)
            f.close();print("completes download vid")
