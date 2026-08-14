import os
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# टोकन लोड करना (जो सीधा जीमेल/यूट्यूब से कनेक्ट करेगा)
def get_youtube_service():
    # GitHub Secrets या लोकल एनवायरनमेंट से टोकन उठाएगा
    token_data = os.getenv("TOKEN_JSON")
    if token_data:
        creds_info = json.loads(token_data)
        creds = Credentials.from_authorized_user_info(creds_info)
    else:
        creds = Credentials.from_authorized_user_file('token.json')
    return build('youtube', 'v3', credentials=creds)

def upload_content():
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    youtube = get_youtube_service()

    for channel in config['channels']:
        print(f"Processing Channel: {channel['channel_id']}")
        
        # 1. 50-मिनट की लंबी वीडियो अपलोड
        body_long = {
            'snippet': {
                'title': channel['title_prefix'] + " - 50 Min Special",
                'description': channel['description'],
                'tags': ['MrBeast', 'Challenge', 'Viral', '24/7'],
                'categoryId': '24'
            },
            'status': {'privacyStatus': 'public'}
        }
        if os.path.exists(channel['video_path']):
            media = MediaFileUpload(channel['video_path'], chunksize=-1, resumable=True)
            request = youtube.videos().insert(part='snippet,status', body=body_long, media_body=media)
            response = request.execute()
            print(f"Long Video Uploaded: {response.get('id')}")

        # 2. 5 इमेज पोस्ट / कम्युनिटी पोस्ट / शॉर्ट्स अपलोड
        if os.path.exists(channel['image_posts_dir']):
            images = os.listdir(channel['image_posts_dir'])[:5] # एक साथ 5 इमेज
            for img in images:
                img_path = os.path.join(channel['image_posts_dir'], img)
                print(f"Posting Image to Community/Shorts: {img_path}")
                # यहाँ इमेज पोस्टिंग का एपीआई कॉल या शॉर्ट्स शिड्यूलर ट्रिगर होगा

if __name__ == "__main__":
    upload_content()
