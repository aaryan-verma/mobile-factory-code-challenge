from enum import Enum

class ComponentCategory(str, Enum):
    SCREEN = "Screen"
    CAMERA = "Camera" 
    PORT = "Port"
    OS = "OS"
    BODY = "Body" 