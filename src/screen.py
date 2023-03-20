import pygame

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

        pygame.display.set_caption('Life')

    def _draw(self):
        self.display.fill(BLACK)

        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                if self.cells[x][y] == 1:
                    pygame.draw.rect(self.display, WHITE, pygame.Rect(x * self.block_size, y * self.block_size, 
                                                                    self.block_size,  self.block_size))
        

    def play(self):
        self._draw()
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                print("QUIT")
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    position = pygame.mouse.get_pos()
                    self.cells[position[0]//self.block_size][position[1]//self.block_size] = 1               

                elif mouse_presses[2]:
                    position = pygame.mouse.get_pos()
                    self.cells[position[0]//self.block_size][position[1]//self.block_size] = 0
                    
        pygame.display.update()
        self.clock.tick(30)
                   
