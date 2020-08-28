import pyglet
from pyglet.window import key, mouse
from game import resources


window = pyglet.window.Window()
bg = resources.bg_img

label = pyglet.text.Label('Welcome to University',
        font_name = 'Arial',
        font_size = 30,
        x = window.width//2, y = window.height//2,
        anchor_x='center', anchor_y = 'center')

label_2 = pyglet.text.Label('I hope you have a good time',
        font_name = 'Arial',
        font_size = 10,
        x = window.width//2, y = window.height//2,
        anchor_x='center', anchor_y = 'center')

score_label = pyglet.text.Label(text="Score: 0", x=10, y=460)

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)


@window.event
def on_draw():
    window.clear()
    bg.blit(0, 0)
    label.draw()
    score_label.draw()
    player_ship.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        label_2.draw()
    elif symbol == key.M:
        print('M key was pressed!')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.RIGHT:
        print('The right mouse button pressed and the app will close')
        pyglet.app.exit()


if __name__ == '__main__':
    pyglet.app.run()
