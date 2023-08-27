import pygame

class Display:
    def __init__(self, dimensions: tuple, caption: str, bgColor: tuple) -> None:
        self.dimensions = dimensions
        self.caption = caption
        self.bgColor = bgColor
        self.display = self.create_display()

    def create_display(self) -> object:
        pygame.display.set_caption(self.caption)
        return pygame.display.set_mode(self.dimensions)
    
    def clear_display(self) -> None:
        self.display.fill(self.bgColor)

    def update_display(self):
        pygame.display.update()

class Clock:
    def __init__(self, fps=int) -> None:
        self.clock = pygame.time.Clock()
        self.fps = fps
    
    def set_framerate(self) -> object:
        self.clock.tick(self.fps)