import win32com.client

camera = win32com.client.Dispatch("MaxIm.CCDCamera")

camera.LinkEnabled = True

print(camera.CameraStatus)

camera.GuiderExpose(2)

#while 1:

#    xError = camera.GuiderXError   
#    print(xError)
#    yError = camera.GuiderYError
#    print(yError)

