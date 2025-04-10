"""Coordinate class to represent a point in 2D space.
This class provides methods to get and set the x and y coordinates of the point.
"""
class Coordinate:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def get_x_coordinate(self) -> int:
        """
        Returns the x-coordinate.
        :return: int
        """
        return self.x
    def get_y_coordinate(self) -> int:
        """
        Returns the y-coordinate.
        :return: int
        """
        return self.y
    
    def set_x_coordinate(self, x: int) -> None:
        """
        Sets the x-coordinate.
        :param x: int
        """
        self.x = x
        
    def set_y_coordinate(self, y: int) -> None:
        """
        Sets the y-coordinate.
        :param y: int
        """
        self.y = y