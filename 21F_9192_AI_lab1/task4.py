


Task:4

def calculate_area(length,width):
    value=length*width
    return value
def calculate_volume(length,width,height):
    value=length*width*height
    return value
def main():
    length=input("Enter the length of the room :")
    width=input("Enter the width of the room :")
    height=input("Enter the height of the room :")
    length=float(length)
    width = float(width)
    height=float(height)
    print("Area of the room is: ",calculate_area(length,width))
    print("Volume of the room is: ",calculate_volume(length, width, height))
    print("\t\t\t\t!!Cleaning Start!!")

if __name__=="__main__":
    main()
