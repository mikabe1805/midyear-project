# import winsound

# filename = 'voice_lines/Angry_Mikan.wav'
# winsound.PlaySound(filename, winsound.SND_FILENAME)

import simpleaudio as sa

filename = 'voice_lines/Angry_Mikan.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing