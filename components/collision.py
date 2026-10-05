import transform
collisions = {}

class Collision:
    def __init__(self, id):
        self.id = id
        collisions[id] = self

    def apply(self, transform):
        pass

def handle_collisions():
    for collision in collisions.values():
        collision.apply(transform.krijg_transform_op_id(collision.id))