import datetime
from pydub import AudioSegment
from pydub.playback import play
import time

def cuckoo(n_times):
    combined = AudioSegment.empty() 
    sound = AudioSegment.from_mp3('assets/open.mp3')
    combined += sound
    while n_times != 1:
        sound = AudioSegment.from_mp3('assets/one.mp3')
        combined += sound
        n_times -= 1
    else:
        sound = AudioSegment.from_mp3('assets/one+end.mp3')
        combined += sound
    play(combined)


while True:
    current_time = datetime.datetime.now()
    minutes = current_time.minute
    hour = current_time.hour - 12 if current_time.hour > 12 else current_time.hour 

    if minutes == 30:
        cuckoo(1)
    elif minutes == 0:
        cuckoo(hour)
    time.sleep(60)       
    


