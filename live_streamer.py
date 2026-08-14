import subprocess
import time
import json

def start_live_stream():
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    rtmp = "rtmp://" + config['live_stream']['rtmp_url'] + "/" + config['live_stream']['stream_key']
    video = config['live_stream']['loop_video']

    # FFmpeg के जरिए वीडियो को लगातार लूप करके YouTube Live पर भेजना
    cmd = [
        'ffmpeg', '-re', '-stream_loop', '-1', '-i', video,
        '-c:v', 'libx264', '-preset', 'veryfast', '-maxrate', '3000k',
        '-bufsize', '6000k', '-pix_fmt', 'yuv420p', '-g', '50',
        '-c:a', 'aac', '-b:a', '128k', '-ar', '44100',
        '-f', 'flv', rtmp
    ]
    
    print("Starting 20 Hours Non-Stop Live Stream Engine...")
    process = subprocess.Popen(cmd)
    
    # 20 घंटे बाद अपने आप बंद होने का टाइमर (20 * 3600 seconds)
    time.sleep(72000) 
    process.terminate()

if __name__ == "__main__":
    start_live_stream()
  
