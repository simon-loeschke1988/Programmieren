from module import abc


if __name__ == "__main__":
    
    circle1 = abc.Circle(30)
    circle2 = abc.Circle(49)
    rectangle = abc.Rectangle(3,4)
    rectangle2= abc.Rectangle(90,49)
    triangle1= abc.Triangle(2,5)
    triangle2 = abc.Triangle(78,324)
    
    forms = [circle1,circle2,rectangle,rectangle2,triangle1,triangle2]
    
    for _ in forms:
        print(f"{_.describe()}: area = {_.describe()}")
     