from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global ax, ay
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDLK_ESCAPE and event.type == SDL_KEYDOWN:
            running = False

        elif event.type == SDL_KEYDOWN:
            x, y = ax, ay


def move():
    global x, y
    global ax, ay

    if(ax, ay) != (x, y):
         if x > ax:
            while ax == x:
                x -= 1
         elif x < ax:
            while ax == x:
                x += 1

         elif y < ay:
            while ay == y:
                y += 1

         elif y > ay:
             while ay == y:
                y -= 1

    else:
        ax, ay = random.randint(1, KPU_WIDTH), random.randint(1, KPU_HEIGHT)
        update_canvas()




open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mousecursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH//2, KPU_HEIGHT//2
ax, ay = random.randint(1, KPU_WIDTH),  random.randint(1, KPU_HEIGHT)
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    mousecursor.draw(ax, ay)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




