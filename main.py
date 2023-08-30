from pygame import *

init()

window = display.set_mode((800,600))
display.set_caption('MK11')

run = True

bg_pic = image.load('fields.jpeg')#background picture/Ð·Ð°Ð´Ð½Ð¸Ð¹ Ñ„Ð¾Ð½
bg_pic = transform.scale(bg_pic, (800,600))

GREEN = (0, 255, 0)#Ð—ÐµÐ»ÐµÐ½Ñ‹Ð¹ Ñ†Ð²ÐµÑ‚
win_width = 800
win_height = 600

class Card(sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)

player1 = Card(80, 80, 100, 150, GREEN)

while run:
    time.delay(50)
    window.blit(bg_pic, (0,0))
    player1.draw()
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()