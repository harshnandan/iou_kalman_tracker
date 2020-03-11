import imageio
import os, sys
import ffmpy
import ffmpeg

class TargetFormat(object):
    GIF = ".gif"
    MP4 = ".mp4"
    AVI = ".avi"

def convertFile(inputpath, targetFormat):
    """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
    outputpath = os.path.splitext(inputpath)[0] + targetFormat
    print("converting\r\n\t{0}\r\nto\r\n\t{1}".format(inputpath, outputpath))

    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputpath, fps=25)
    
    for i,im in enumerate(reader):
        sys.stdout.write("\rframe {0}".format(i))
        sys.stdout.flush()
        writer.append_data(im)
    print("\r\nFinalizing...")
    writer.close()
    print("Done.")
    
def convert_to_gif(inputpath):
    outputpath = os.path.splitext(inputpath)[0] + ".gif"
    print("converting\r\n\t{0}\r\nto\r\n\t{1}".format(inputpath, outputpath))
    
    ff = ffmpy.FFmpeg( inputs = {"constant_acc_allframes.mp4" : None}, outputs = {"constant_acc_allframes.gif" : None})
    ff.run()
    
#def cvt(inputpath):
#    from moviepy.editor import *#

#    clip = (VideoFileClip(inputpath))
#    clip.write_gif("output.gif")

#convert_to_gif("../output/constant_acc_allframes.mp4")
convertFile("../output/constant_acc_allframes_noise.mp4", TargetFormat.GIF)