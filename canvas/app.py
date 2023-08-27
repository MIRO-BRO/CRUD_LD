import pygame
import graphics

class Canvas:
    def __init__(self) -> None:
        self.active = True
        self.display = graphics.Display(
            dimensions  = (800,800), 
            caption     = "Canvas", 
            bgColor     = (0,0,0)
            )
        self.clock = graphics.Clock(fps=25)

    def run(self) -> None:
        pygame.init()
        while self.active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.active = False

            self.display.clear_display()
            self.display.update_display()
            self.clock.set_framerate()
        pygame.quit()