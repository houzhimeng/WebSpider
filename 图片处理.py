import tinify
import os

tinify.key = 'GemEMqfVHmJhrSDySVqdUvIDxnvCoXgN'
path = "/Users/houzhimeng/Downloads/push" # 图片存放的路径

for dirpath, dirs, files in os.walk(path):
    for file in files:
        try:
            imgpath = os.path.join(dirpath, file)
            print("compressing ..." + imgpath)
            tinify.from_file(imgpath).to_file(imgpath)
        except :
            pass
        continue



