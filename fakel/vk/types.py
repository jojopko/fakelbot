from enum import Enum

class UpdateTypes:
    CONFIRMATION = "confirmation"
    WALL_NEW_POST = "wall_post_new"

# https://dev.vk.com/reference/objects/photo-sizes
# От меньшего до большего
PHOTO_SIZES = {
    "s" : 0,
    "m" : 1,
    "x" : 2,
    "o" : -1,
    "p" : -1,
    "q" : -1,
    "r" : -1,
    "y" : 3,
    "z" : 4,
    "w" : 5
}
