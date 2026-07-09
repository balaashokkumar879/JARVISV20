"""
=========================================
PLUGIN MANAGER
=========================================
"""

class PluginManager:

    def __init__(self):

        self.plugins = {}

    # ----------------------------

    def register(self, name, func):

        self.plugins[name] = func

    # ----------------------------

    def execute(self, name, *args, **kwargs):

        if name in self.plugins:

            return self.plugins[name](*args, **kwargs)

        return None

    # ----------------------------

    def list(self):

        return list(self.plugins.keys())


plugins = PluginManager()