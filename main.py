print("Azimuth to Quadrant Converter")
number=input("Enter azimuth: ")
new_number=float(number)
if new_number >0 and new_number<90:
    print("Quadrant: "+"N"+str(new_number)+"E""\nQuadrant 1: Northeast quadrant\nAzimuth=Quadrant")
elif new_number >90 and new_number<180:
    print("Quadrant: "+"S"+str(180-new_number)+"E""\nQuadrant 2: Southeast quadrant\nQuadrant=180-Azimuth")
elif new_number >180 and new_number<270:
    b=new_number-180
    bb=round(b,2)
    print("Quadrant: "+"S"+str(bb)+"W""\nQuadrant 3: Southwest quadrant\nQuadrant=Azimuth-180")
elif new_number >270 and new_number<360:
    a=360-new_number
    aa=round(a,2)
    print("Quadrant: "+"N"+str(aa)+"W""\nQuadrant 4: Northwest quadrant\nQuadrant=360-Azimuth")
elif new_number ==360 or new_number ==0:
    print("due north")
elif new_number ==180:
    print("due south")
elif new_number ==90:
    print("due east")
elif new_number ==270:
    print("due west")

