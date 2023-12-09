from mutagen.mp3 import MP3

def songDataSecond():
    songMetadata = MP3("./songs/son1.mp3")
    songSecond = songMetadata.info.length
    return(songSecond)


def affichage(songSecond):
    songMinute = songSecond // 60
    songHour = songMinute // 60
    songHourstr = ""
    songMinutestr = ""
    songSecondstr = ""
    songHourInt = int(songHour)
    if songHourInt < 10:
        songHourstr = "0" + str(songHourInt)
    else:
        songMinutestr = str(songHourInt)
    songMinute = songMinute - (songHour * 60)
    songMinuteInt = int(songMinute)
    if songMinuteInt < 10:
        songMinutestr = "0" + str(songMinuteInt)
    else:
        songMinutestr = str(songMinuteInt)
    songSecond = int(songSecond) - (songMinute * 60)
    songSecondInt = int(songSecond)
    if songSecondInt < 10:
        songSecondstr = "0" + str(songSecondInt)
    else:
        songSecondstr = str(songSecondInt)
    return(f"{songHourstr}H {songMinutestr}M {songSecondstr}S")




