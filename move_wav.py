import os
import glob
import json
import shutil
from tqdm import tqdm

"""
BEFORE
E:\\AI-Hub data\\자유대화 음성(일반남녀)\\Training\\[원천]1.AI챗봇_1\\일반남여_일반통합05_M_1455308554-6_37_수도권_실내
일반남여_일반통합05_M_1455308554-6_37_수도권_실내_06313.wav

AFTER
E:\\AI-Hub data\\자유대화 음성(일반남녀)\\Training\\1455308554-6\\일반통합
1455308554-6-일반통합-06313.wav
"""
drive = "E:\\"
main_dir = drive + "AI-Hub data\\자유대화 음성(일반남녀)"
sub_dir = ["Training", "Validation"]

successed_list=[]
try:
  for sd in sub_dir:
    subpath = os.path.join(main_dir, sd)
    wavdirs = sorted(os.listdir(subpath))
    wavdirs = [wd for wd in wavdirs if wd.startswith("[원천]")]

    for wd in wavdirs:
      # [원천]1.AI챗봇_1
      wavpath = os.path.join(subpath, wd)
      print(wavpath)
      print("=====================")
      speakers = sorted(os.listdir(wavpath))

      # 일반남여_일반통합05_M_1455308554-6_37_수도권_실내
      for speaker in tqdm(speakers):
        wavs = glob.glob(os.path.join(wavpath, speaker, "*.wav"))
        splitted = speaker.split("_")
        speaker = splitted[3]
        chapter = splitted[1][:-2] # 일반통합05 -> 일반통합

        # 일반남여_일반통합05_M_1455308554-6_37_수도권_실내_06313.wav
        for wav in wavs:
          scriptId = wav.split("_")[-1]
          new_file_name = speaker + "-" + chapter + "-" + scriptId
          new_file_path = os.path.join(subpath, speaker, chapter)
          shutil.move(wav, os.path.join(new_file_path, new_file_name))


except:
  print("Error!! successed these:")
  for sl in successed_list:
    print(sl)