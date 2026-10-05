transforms = {}

class Transform:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        transforms[id] = self

    def apply(self):
        pass

def handle_transforms():
    for transform in transforms.values():
        transform.apply()

def krijg_transform_op_id(id):
    return transforms.get(id, None)