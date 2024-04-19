class Circle:
    def __init__(self , radius ):      #دایره
        self.r=radius
    def introducing(self):             #اطلاعات دایره
        return """<<<<<name of thid shape is(circle) \n there are two radius and one diameter>>>>"""

    def area_circle(self , radius):     #مساحت دایره
        return f">>>>Area of the figure is {radius* radius * 3.14}"
    def environment_circle(self , radius):   #محیط دایره
        return f">>>environment of the figure is {2*radius*3/14}"
        
class Square:              #مربع
    def __init__(self ,width ):
        self.width=width
    def square(self):     #اطلاعات مربع
        return """<<<<  name of this shape is (square) \n it have four side >>>>>"""
    def area_square(self , width):     #مساحت مربع
        return f"<<<<< area of this shape is {width*width} >>>>"
    def environment(self , width):      #محیط مربع
        return f"<<<<<  environment of the shape is {width*4} >>>>"
        

class Ractangle:         #مستطیل
    def __init__(self , width,length):     
        self.width=width
        self.length=length
    def rectangle(self):      #اطلاعات مستطیل
        return "name of this shape is (ractangle) \n it has one width and one length"
    def area_rectangle(self):   #مساحت مستطیل
        return f"<<<<<area of this shape is {width*length} >>>>>>>"
    def environment(self):   #محیط مستطیل
        return f"<<<<environment of the shape is {(width+length)*2} >>>>>"


while True:
    operator=int(input("""please select one of the options :
                        1-circle
                        2-squer
                        3-rectangle
                        4-leave """))
    if operator==1:
        radius=float(input("enter number for radius pleas!!! "))
        object1=Circle(radius)

        print(object1.introducing())
        print(object1.Area_circle(radius))
        print(object1.environment_circle(radius))
        print("&"*50)
    if operator==2:
        width=float(input("enter number for width please !!!! "))
        object2=Square(width)

        print(object2.square())
        print(object2.area_square(width))
        print(object2.environment(width))
        print("&"*50)
    if operator==3:
        width=float(input("enter number for width please !!!! "))
        length=float(input("enter number for length please !!!"))
        object3=Ractangle(width,length)

        print(object3.rectangle())
        print(object3.area_rectangle())
        print(object3.environment())
        print("&"*50)
    if operator==4:
        break
