# Imports, sorted alphabetically.

# Python packages
import os

# Third-party packages
import pyglet

# Modules from this project
import globals as G


def load_image(*args):
    path = os.path.join(*args)
    return pyglet.image.load(os.path.join(*args)) if os.path.isfile(
        path) else None


def image_sprite(image, batch, group, x=0, y=0, width=None, height=None):
    if image == None or batch == None or group == None:
        return None
    width = width or image.width
    height = height or image.height
    if isinstance(group, int):
        group = pyglet.graphics.OrderedGroup(group)
    return pyglet.sprite.Sprite(image.get_region(x, y, width, height),
                                batch=batch, group=group)


def hidden_image_sprite(*args, **kwargs):
    sprite = image_sprite(*args, **kwargs)
    if sprite:
        sprite.visible = False
    return sprite


# fast math algorithms
class FastRandom(object):
    def __init__(self, seed):
        self.seed = seed

    def randint(self):
        self.seed = (214013 * self.seed + 2531011)
        return (self.seed >> 16) & 0x7FFF


def init_resources():
    init_font('resources/fonts/Chunkfive.ttf', 'ChunkFive Roman')


def init_font(filename, fontname):
    pyglet.font.add_file(filename)
    pyglet.font.load(fontname)


def get_block_icon(block, icon_size, world):
    block_icon = load_image(G.ICONS_PATH,
                            block.id.filename() + ".png") \
        or (block.group or world.group).texture.get_region(
            int(block.texture_data[2 * 8] * G.TILESET_SIZE) * icon_size,
            int(block.texture_data[2 * 8 + 1] * G.TILESET_SIZE) * icon_size,
            icon_size,
            icon_size)
    return block_icon

