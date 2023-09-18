import os
import librosa
import soundfile as sf
import wave
from pydub import AudioSegment

source_dir = 'F:\\Drive D\\DATASET Speech\\Single static speech 4mic\\S14\\Respeaker'
dest_dir = 'F:\\Drive D\\DATASET Speech\\Single static speech 4mic\\S14\\Respeaker\\RS_raw'
entries = os.listdir(source_dir)
print(entries)

for file in entries:
  if file.endswith(".wav"):
    stereo_audio = AudioSegment.from_file(f"{file}", format="wav")
    mono_audios = stereo_audio.split_to_mono()
    mono_audios[0].export(f"{dest_dir}\\{file[0:-4]}_BF.wav", format="wav")
    mono_audios[1].export(f"{dest_dir}\\{file[0:-4]}_1.wav", format="wav")
    mono_audios[2].export(f"{dest_dir}\\{file[0:-4]}_2.wav", format="wav")
    mono_audios[3].export(f"{dest_dir}\\{file[0:-4]}_3.wav", format="wav")
    mono_audios[4].export(f"{dest_dir}\\{file[0:-4]}_4.wav", format="wav")
    mono_audios[5].export(f"{dest_dir}\\{file[0:-4]}_5.wav", format="wav")

