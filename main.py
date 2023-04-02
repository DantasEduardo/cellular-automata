import argparse
from src.screen import Screen

def main(param):
    param.size = int(param.size)

    if param.free and param.observation:
        raise Exception ("set only one argument")

    if param.size <= 0:
        raise Exception ("Invalid size for the cells")

    if param.free:
        screen = Screen(param.width, param.height)
        screen.set_block_size(param.size)
        while True: 
            screen.play_freemode()

    if param.observation:
        screen = Screen(param.width, param.height)
        screen.set_block_size(param.size)
        screen.play_observation_mode()

    else:
        print("No arguments specified\n start in observation mode")
        screen = Screen(param.width, param.height)
        screen.play_observation_mode()

  

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--free', default=False, action='store_true', help='set the game in a free mode, you can place a cell anywhere')
    parser.add_argument('-o','--observation', default=False, action='store_true', 
                        help='set the game in a observation mode, the cells are automatically generated')
    parser.add_argument('-s','--size', default=2,
                        help='set the size of the cells in the screen')

    parser.add_argument('-w','--width', default=400,
                            help='set the width of the screen')

    parser.add_argument('-a','--height', default=400,
                            help='set the height of the screen')


    args = parser.parse_args()

    main(args)