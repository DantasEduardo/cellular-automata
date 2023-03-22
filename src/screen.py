import pygame
from src.rules import check_cells

#COLORS#
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

class Screen:
    def __init__(self, width, height):
        pygame.init()

        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.display.fill(BLACK)

        self.block_size = 8
        self.cells = [[0 for _ in range(self.width)] for _ in range(height)]

        self.bool = False

        pygame.display.set_caption('Life')

    def _draw(self):
        self.display.fill(BLACK)

        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                if self.cells[x][y] == 1:
                    pygame.draw.rect(self.display, WHITE, pygame.Rect(x * self.block_size, y * self.block_size, 
                                                                    self.block_size,  self.block_size))
        
        pygame.display.flip()
        

    def play_freemode(self):
        self._draw()
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                print("QUIT")
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and self.bool is False:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    position = pygame.mouse.get_pos()
                    self.cells[position[0]//self.block_size][position[1]//self.block_size] = 1               

                elif mouse_presses[2]:
                    position = pygame.mouse.get_pos()
                    self.cells[position[0]//self.block_size][position[1]//self.block_size] = 0

            elif event.type == pygame.KEYUP and self.bool is False:
                if event.key == pygame.K_RETURN:
                    print("STARTED!")    
                    self.bool = True

        if self.bool:
            print("Update cells")
            self.cells = check_cells(self.cells)

        self.clock.tick(30)
                   
