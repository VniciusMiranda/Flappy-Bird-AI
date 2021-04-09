import os


class GameObject:

    def __init__(self):
        """
        Defines the variables that the game objects needs to access their
        resources.
        """
        self.PROJECT_PATH = os.path.abspath(__file__).replace(os.path.basename(__file__), "").replace("src/game/", "")
        self.RESOURCES_PATH = self.PROJECT_PATH + "resources"


        self.IMGS_PATH = self.RESOURCES_PATH + "/imgs/"

        self.RESOURCE_IMAGES = os.listdir(self.IMGS_PATH)


    def update(self):
        """
        Every game object will have an update method where the coordinates
        and other values are updated.
        :return: nothing
        """
        pass


    def render(self, win):
        """
        Every game object will have a render method where it will be render to
        the screen accordingly.
        :param win: Window object
        :return: nothing
        """

        pass