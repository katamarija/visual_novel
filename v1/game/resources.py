import pyglet

pyglet.resource.path= ['../resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image("player.gif")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")

bg_img = pyglet.resource.image("bg_uni.jpg")
