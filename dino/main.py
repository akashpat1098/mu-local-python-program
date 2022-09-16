from PIL import Image,ImageGrab

def take_screenshot():
    image=ImageGrab.grab()
    image.show()

if __name__=="__main__":
    take_screenshot()