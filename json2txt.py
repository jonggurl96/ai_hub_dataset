import os
import glob
import json

"""
directory structure
Training
  [라벨]1.AI챗봇
  [라벨]2.음성수집도구
  [라벨]3.스튜디오
  [원천]1.AI챗봇_1
  [원천]1.AI챗봇_2
  [원천]2.음성수집도구_1
  [원천]3.스튜디오_1
    영역구분[일반남여, 노인남여, 소아남여, 외래어]_스크립트셋 번호_성별[M, F]_녹음자정보recorderId__나이_지역_녹음위치[실내, 실외, 녹음실]
      영역구분[일반남여, 노인남여, 소아남여, 외래어]_스크립트셋 번호_성별[M, F]_녹음자정보recorderId__나이_지역_녹음위치[실내, 실외, 녹음실]_스크립트번호

Validation
  [라벨]1.AI챗봇
  [라벨]2.음성수집도구
  [라벨]3.스튜디오
  [원천]1.AI챗봇
  [원천]2.음성수집도구
  [원천]3.스튜디오
    영역구분[일반남여, 노인남여, 소아남여, 외래어]_스크립트셋 번호_성별[M, F]_녹음자정보recorderId__나이_지역_녹음위치[실내, 실외, 녹음실]
      영역구분[일반남여, 노인남여, 소아남여, 외래어]_스크립트셋 번호_성별[M, F]_녹음자정보recorderId__나이_지역_녹음위치[실내, 실외, 녹음실]_스크립트번호

LibriSpeech와 같은 형태로 변경
  Training
    recorderId
      chapter
        script_id
        recorderId-chapter.trans.txt
"""

drive = "F:\\"
main_dir = drive + "AI-Hub data\\자유대화 음성(일반남녀)"
sub_dir = ["Training", "Validation"]

for sd in sub_dir:
  print("Current Directory: ", sd)
  jsondirs = sorted(os.listdir(os.path.join(main_dir, sd)))
  jsondirs = [jd for jd in jsondirs if jd.startswith("[라벨]")]
  for jd in jsondirs:
    print(sd, "-", jd)
    jsondir = os.path.join(main_dir, sd, jd) # drive:\AI-Hub data\자유대화 음성(일반남녀)\Training\[라벨]1.AI챗봇
    recorderIds = sorted(os.listdir(jsondir)) # 일반남여_일반통합05_M_1455308554-6_37_수도권_실내, etc..
    for recorderId in recorderIds:
      recorderIdDir = os.path.join(jsondir, recorderId)
      jsonfilenames = sorted(glob.glob(os.path.join(recorderIdDir, "*.json")))
      jsonfilenames = os.listdir(recorderIdDir)
      for filename in jsonfilenames:
        filename = os.path.join(recorderIdDir, filename)
        with open(filename, "rt", encoding="UTF-8") as jf:
          jf = json.load(jf)
          recorderID = jf["녹음자정보"]["recorderId"]
          stt = jf["발화정보"]["stt"]
          print(recorderID, stt)
          exit()


