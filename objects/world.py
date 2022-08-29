import gen.worlds, gen.world
from src.cache import cached_property


class World:
    def __init__(self, world_name, world_data):
        self.world_name = world_name
        self.world_data = world_data

    def __html__(self):
        return f'<a href="{url_for("get_world", **self.url_package)}">{self.name}</a>'

    @cached_property
    def name(self):     # House name in case the house is also a shop
        return self.world.name

    @cached_property
    def url_package(self):
        return {
            'world_name': self.world_name
        }
