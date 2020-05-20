import cv2

# Exports one frame of a video as a jpg image
def extractFrame(sec, vidap, outDir, prefix):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*100)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(outDir+prefix+"_"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

# Exports all frames of a video as a jpg images
def getAllFrames(vidcap, frameRate, outDir, prefix):
    sec = 0
    count = 1
    success = extractFrame(sec, vidcap, outDir, prefix)
    while success:
        count = count + 1
        sec = round(sec + frameRate, 2)
        success = extractFrame(sec, vidcap, outDir, prefix)
    
""" Example usage : 

vidcap = cv2.VideoCapture('cuteCats.mp4')
getAllFrames(vidcap, 1, "output/", "frame");

"""
