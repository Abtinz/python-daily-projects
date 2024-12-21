from ursina import *


class Rubik():
    def __init__(self):

        # plane setup
        Entity(model='quad', scale=60, texture='white_cube', texture_scale=(60, 60),
            rotation_x=90, y=-5, color=color.light_gray)

        # camera setup
        EditorCamera()
        camera.world_position = (0, 0, -10)

        # text setup
        self.text = None
        self.text_position = (0, -8)

        # cubie model and texture
        model, texture = 'models/custom_cube', 'textures/rubik_texture'

        # defining cube sides
        LEFT = {Vec3(-0.5, y, z) for y in [-0.5, 0.5] for z in [-0.5, 0.5]}
        RIGHT = {Vec3(0.5, y, z) for y in [-0.5, 0.5] for z in [-0.5, 0.5]}
        DOWN = {Vec3(x, -0.5, z) for x in [-0.5, 0.5] for z in [-0.5, 0.5]}
        UP = {Vec3(x, 0.5, z) for x in [-0.5, 0.5] for z in [-0.5, 0.5]}
        BACK = {Vec3(x, y, 0.5) for x in [-0.5, 0.5] for y in [-0.5, 0.5]}
        FRONT = {Vec3(x, y, -0.5) for x in [-0.5, 0.5] for y in [-0.5, 0.5]}
        C = LEFT | RIGHT | DOWN | UP | BACK | FRONT 

        # defining transition dictionaries
        self.rotation_axes = {'LEFT': 'x', 'RIGHT': 'x', 'DOWN': 'y', 'UP': 'y', 'BACK': 'z', 'FRONT': 'z'}
        self.cubes_side_positons = {'LEFT': LEFT, 'RIGHT': RIGHT, 'DOWN': DOWN, 'UP': UP, 'BACK': BACK, 'FRONT': FRONT}

        # parameters
        self.action_trigger = True

        # creating the cubes
        self.PARENT = Entity()
        self.CUBES = [Entity(model=model, texture=texture, position=pos) for pos in C]

        # action dictionaries
        self.keys = dict(zip('123456', 'LEFT RIGHT DOWN UP BACK FRONT'.split()))
        self.reverse_keys = dict(zip('qwerty', 'LEFT RIGHT DOWN UP BACK FRONT'.split()))

    def toggle_trigger(self):
        self.action_trigger = not self.action_trigger

    def reparent_to_scene(self):
        for cube in self.CUBES:
            if cube.parent == self.PARENT:
                world_pos, world_rot = round(cube.world_position, 1), cube.world_rotation
                cube.parent = scene
                cube.position, cube.rotation = world_pos, world_rot
        self.PARENT.rotation = 0

    def rotate_side(self, side_name, animation_time, reverse=False):
        self.toggle_trigger()
        cube_positions = self.cubes_side_positons[side_name]
        rotation_axis = self.rotation_axes[side_name]
        self.reparent_to_scene()
        for cube in self.CUBES:
            if cube.position in cube_positions:
                cube.parent = self.PARENT
                angle = -90 if reverse else 90
                eval(f'self.PARENT.animate_rotation_{rotation_axis}({angle}, duration=animation_time)')
        invoke(self.toggle_trigger, delay=animation_time+0.05)

    def action(self, key, animation_time):
        if self.action_trigger:
            if key in self.keys:
                self.rotate_side(self.keys[key], animation_time)
            elif key in self.reverse_keys:
                self.rotate_side(self.reverse_keys[key], animation_time, reverse=True)

    def action_sequence(self, scramble_seq, solve_seq):
        if len(scramble_seq) == 0 and len(solve_seq) == 0:
            return
        
        if len(scramble_seq) != 0:
            if self.text is None or self.text.is_empty():
                self.text = Text('Scramble', scale=2, origin=self.text_position)
            action = scramble_seq[0]
            self.action(action, animation_time=0.1)
            if len(scramble_seq) == 1:
                destroy(self.text, delay=0.2)
                invoke(self.action_sequence, scramble_seq[1:], solve_seq, delay=2+0.1)
            else:
                invoke(self.action_sequence, scramble_seq[1:], solve_seq, delay=0.2+0.1)
        else:
            if self.text.is_empty():
                self.text = Text('Solve', scale=2, origin=self.text_position)
            action = solve_seq[0]
            self.action(action, animation_time=0.5)
            if len(solve_seq) == 1:
                destroy(self.text, delay=1)
            invoke(self.action_sequence, scramble_seq, solve_seq[1:], delay=0.5+0.1)
    