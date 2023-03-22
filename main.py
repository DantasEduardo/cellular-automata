from src.screen import Screen

def main():
    screen = Screen(400, 400)

    while True: 
        screen.play_freemode()

if __name__ == '__main__':
    main()