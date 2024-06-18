import glfw
from OpenGL.GL import *
import numpy as np
import time
from assets import *
from Backdrop import *
# Window dimensions
cps = 4500

# Square properties
square_size = 400  # Adjusted for new coordinate system
square_pos = [375, 1500]  # Initial position (bottom left)
square_color = [0.0, 0.0, 0.0,0.0]  # Default color
square_health = 3  # Health blocks for square

# Circle properties
circle_radius = 300  # Adjusted for new coordinate system
circle_pos = [cps-575, 1500]  # Initial position (bottom right)
circle_color = [0.0, 0.0, 0.0,0.0]  # Default color
circle_health = 3  # Health blocks for circle

# Movement step
step = 100

# Projectiles
projectiles = []  # Initialize an empty list for projectiles
projectile_speed = 10
projectile_width = 100
projectile_height = 40

# Colors
hit_color_duration = 1.0
last_square_hit_time = 0
last_circle_hit_time = 0

# Game state
game_over = False
winner = ""

class Projectile:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.width = projectile_width
        self.height = projectile_height
        self.active = True  # Flag to check if projectile is active

    def move(self):
        self.x += self.dx * projectile_speed
        self.y += self.dy * projectile_speed

    def draw(self):
        if self.active:
            glColor3f(*self.color)
            glBegin(GL_QUADS)
            glVertex2f(self.x - self.width / 2, self.y - self.height / 2)
            glVertex2f(self.x + self.width / 2, self.y - self.height / 2)
            glVertex2f(self.x + self.width / 2, self.y + self.height / 2)
            glVertex2f(self.x - self.width / 2, self.y + self.height / 2)
            glEnd()

    def check_collision(self, shape_pos, shape_half_size):
        if (shape_pos[0] - shape_half_size <= self.x + self.width / 2 <= shape_pos[0] + shape_half_size and
            shape_pos[1] - shape_half_size <= self.y + self.height / 2 <= shape_pos[1] + shape_half_size):
            self.actives = False  # Deactivate projectile upon collision
            return True
        return False

def draw_square(x, y, color):
    global square_size
    half_square_size = square_size / 2
    glColor4f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x - half_square_size, y - half_square_size)
    glVertex2f(x + half_square_size, y - half_square_size)
    glVertex2f(x + half_square_size, y + half_square_size)
    glVertex2f(x - half_square_size, y + half_square_size)
    glEnd()

def draw_circle(x, y, segments=100, color=(1.0, 1.0, 1.0)):
    global circle_radius
    glColor4f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(segments + 1):
        angle = 2.0 * np.pi * i / segments
        dx = np.cos(angle) * circle_radius
        dy = np.sin(angle) * circle_radius
        glVertex2f(x + dx, y + dy)
    glEnd()

def draw_health_bars(x, y, health, color):
    bar_width = 600
    bar_height = 60
    glColor3f(*color)
    for i in range(health):
        glBegin(GL_QUADS)
        glVertex2f(x - bar_width / 2 + i * (bar_width / 3), y - bar_height / 2)
        glVertex2f(x - bar_width / 2 + (i + 1) * (bar_width / 3), y - bar_height / 2)
        glVertex2f(x - bar_width / 2 + (i + 1) * (bar_width / 3), y + bar_height / 2)
        glVertex2f(x - bar_width / 2 + i * (bar_width / 3), y + bar_height / 2)
        glEnd()

def key_callback(window, key, scancode, action, mods):
    global square_pos, circle_pos, projectiles, game_over, square_size, circle_radius
    half_square_size = square_size / 2

    if game_over:
        return

    if action == glfw.PRESS or action == glfw.REPEAT:
        # Move square
        if key == glfw.KEY_W and square_pos[1] > half_square_size+cps/8:
            square_pos[1] -= step
        elif key == glfw.KEY_S and square_pos[1] < cps - half_square_size:
            square_pos[1] += step
        elif key == glfw.KEY_A and square_pos[0] > half_square_size:
            square_pos[0] -= step
        elif key == glfw.KEY_D and square_pos[0] < cps/3- half_square_size:
            square_pos[0] += step

        # Move circle
        if key == glfw.KEY_UP and circle_pos[1] > circle_radius+cps/8:
            circle_pos[1] -= step
        elif key == glfw.KEY_DOWN and circle_pos[1] < cps - circle_radius:
            circle_pos[1] += step
        elif key == glfw.KEY_LEFT and circle_pos[0] > cps*2/3 + circle_radius:
            circle_pos[0] -= step
        elif key == glfw.KEY_RIGHT and circle_pos[0] < cps - circle_radius:
            circle_pos[0] += step

        # Shoot projectiles
        if key == glfw.KEY_SPACE:
            projectiles.append(Projectile(square_pos[0] + half_square_size, square_pos[1], 1, 0, [1, 0, 0]))
        if key == glfw.KEY_ENTER:
            projectiles.append(Projectile(circle_pos[0] - circle_radius, circle_pos[1], -1, 0, [255, 255, 0]))

def main():
    global square_color, circle_color, last_square_hit_time, last_circle_hit_time, square_health, circle_health, game_over, winner, projectiles, square_size, circle_radius
    half_square_size = square_size / 2

    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(1500, 800, "Space Combat Shooter", None, None)
    
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the key callback
    glfw.set_key_callback(window, key_callback)

    # Set the orthographic projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, cps, cps, 0, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    flag=True
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClear(GL_COLOR_BUFFER_BIT)
        flag= not flag
        # starts(flag)
        earth()
        
        # Draw the square on the left side
        # draw_square(square_pos[0], square_pos[1], square_color)
        newdog(square_pos[0],square_pos[1])

        # Draw the circle on the right side

        # draw_circle(circle_pos[0], circle_pos[1], color=circle_color)
        gooddogg(circle_pos[0],circle_pos[1])

        # Draw health bars
        draw_health_bars(375, 300, square_health, [1, 0, 0])
        draw_health_bars(cps-375, 300, circle_health, [0, 0, 1])

        # Move and draw projectiles
        for proj in projectiles:
            proj.move()
            proj.draw()

            # Check for collisions
            if proj.active:
                if proj.color == [1, 0, 0] and proj.check_collision(circle_pos, circle_radius):
                    # circle_radius = circle_radius * (2 / 3)
                    circle_health -= 1
                    proj.active = False  # Deactivate projectile after collision

                    if circle_health <= 0:
                        winner = "Catt"
                        game_over = True

                elif proj.color == [255, 255, 0] and proj.check_collision(square_pos, half_square_size):
                    # square_size = square_size * (2 / 3)
                    square_health -= 1
                    proj.active = False  # Deactivate projectile after collision

                    if square_health <= 0:
                        winner = "Dogg"
                        game_over = True

        # Remove inactive projectiles
        projectiles = [proj for proj in projectiles if proj.active]

        # Display winner message if game over
        if game_over:
            print(f"{winner} won!")
            break

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
