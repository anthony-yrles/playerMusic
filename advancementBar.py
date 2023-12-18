from mutagen.mp3 import MP3
from globals import *
import time

def songDataSecond():
    selectedSong = get_selected_song()
    if selectedSong is not None:
        songMetadata = MP3(f'./assets/songs/{selectedSong}')
        songSecond = songMetadata.info.length
        return(songSecond)
    
def render_circle():
    global start_time
    songSecond = songDataSecond()
    song_running = get_song_running()
    if songSecond is not None and song_running == True:
        pos_x_min = 250
        pos_x_max = 700
        width_bar = pos_x_max - pos_x_min
        speed_movement = width_bar / songSecond
        elapsed_time = time.time() - start_time
        actual_x_pos = pos_x_min + speed_movement * elapsed_time
        return actual_x_pos
