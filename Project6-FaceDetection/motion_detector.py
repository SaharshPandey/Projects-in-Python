import cv2 as cv
from datetime import datetime
import pandas,imutils
first_frame=None    #stores the first frame...
status_list=[None,None]    #stroing the status if objects
times=[]    #storing the datetime for objects
df=pandas.DataFrame(columns=["Start","End"])
video=cv.VideoCapture(0)
while True:
    #two attributes check->:boolean that tells video is recording..while frame :-> ndarray
        check,frame=video.read()
        frame = imutils.resize(frame, width=500)
    #this status=0 means there is no motion right now..
        status=0
        #print(check)
        #print(frame)
    #converting RGB video into GrayScale
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #blurring the video so that motion is easily measured.
        gray=cv.GaussianBlur(gray,(21,21),0)
    #checking and storing the backgound,so the background finds out the difference with other frames of video.
        if first_frame is None:
            first_frame=gray
            continue    #now if we continue then there will be no first frame,because it is pre generated.

        delta_frame=cv.absdiff(first_frame,gray) #this finding the diff between the first frame(background) and other frames of video.
        #thresh_frame=cv.threshold(delta_frame,50,255,cv.THRESH_BINARY)[1] #create threshold frame

        #thresh_frame=cv.adaptiveThreshold(delta_frame,255,cv.ADAPTIVE_THRESH_MEAN_C ,cv.THRESH_BINARY,11,2)
        thresh_frame=cv.threshold(delta_frame,160,255,cv.THRESH_BINARY)[1]
        thresh_frame=cv.dilate(thresh_frame,None,iterations=2 ) #dilate means making tthe edges smoother
    #finding the contours which helps to find out objects in a frame.
        (_,cnts,_)=cv.findContours(thresh_frame.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        for contour in cnts:
            #if area of object is less then 1000 then we will continue otherwise there is an object.
            if cv.contourArea(contour)<15000:
                continue
            status=1 #this implies there is an object in a frame
            (x,y,w,h)=cv.boundingRect(contour) # finding the corners of object in a frame.
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) # making out rectangle for every objects
    #appending all the incoming and outgoing of the object in an frame
        status_list.append(status)
        status_list=status_list[-2:]

    #checking the datetime of apearing object
        if status_list[-1]==1 and status_list[-2]==0:
            times.append(datetime.now())
    #checking the datetime of disapearing object
        if status_list[-1]==0 and status_list[-2]==1:
            times.append(datetime.now())

    #showing the frames/windows
        cv.imshow("Gray Frame",gray)
        cv.imshow("Delta Frame",delta_frame)
        cv.imshow("THRESH_BINARY",thresh_frame)
        cv.imshow("RectFrame",frame)
    #1 is refreshing the frame in every 1 milisec:
        key=cv.waitKey(1)
    #displaying window until you press q
        if key ==ord('q'):
            #if thier is appearing object but that time is window is quited,then it will add the datetime for disappearing object as time of window exited.
            if status==1:
                times.append(datetime.now())
            break
print(status_list)
print(times)
#putting all the datetime of objects in csv file with the help of pandas.
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"END":times[i+1]},ignore_index=True)
df.to_csv("Times.csv") #saving file as "Times.csv"

#releasing window..
video.release()
#destroying all windows..
cv.destroyAllWindows()
