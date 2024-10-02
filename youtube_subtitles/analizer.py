from pytubefix import YouTube

url_no_sub = 'https://www.youtube.com/watch?v=YDAZ6hNe9pg&list=RDQO0IWTDp96c&index=2'
url_auto = 'https://www.youtube.com/watch?v=6rjaNgA8Okc&list=RDQO0IWTDp96c&index=3'
url_manual = 'https://www.youtube.com/watch?v=uXleufh2mY0'

yt = YouTube(url_auto)
captions = yt.captions

def main():
    if len(captions) == 0:
        print('No subs')
        return

    caption = captions.get('en', False)
    print(caption)

    try:
        caption = captions['en']
        print('Suc')
    except KeyError:
        print('Key not founded')


main()
