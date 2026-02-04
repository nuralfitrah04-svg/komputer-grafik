import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# =========================
# DATA KUBUS 3D
# =========================
cube_vertices = [
    (-1, -1, -1), (1, -1, -1),
    (1,  1, -1), (-1,  1, -1),
    (-1, -1,  1), (1, -1,  1),
    (1,  1,  1), (-1,  1,  1)
]

cube_edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

# =========================
# DATA PERSEGI 2D
# =========================
rect_vertices = [
    (-0.5, -0.5),
    ( 0.5, -0.5),
    ( 0.5,  0.5),
    (-0.5,  0.5)
]

# =========================
# VAR TRANSFORMASI
# =========================
# Kubus 3D
cube_tx, cube_ty, cube_tz = -3, 0, -7
cube_rx, cube_ry = 0, 0
cube_scale = 1.0

# Persegi 2D
rect_tx, rect_ty = 3, 0
rect_rot = 0
rect_scale = 1.0
shear_x, shear_y = 0, 0
reflect_x, reflect_y = 1, 1

# =========================
# FUNGSI GAMBAR KUBUS
# =========================
def draw_cube():
    glPushMatrix()
    glTranslatef(cube_tx, cube_ty, cube_tz)
    glRotatef(cube_rx, 1, 0, 0)
    glRotatef(cube_ry, 0, 1, 0)
    glScalef(cube_scale, cube_scale, cube_scale)

    glBegin(GL_LINES)
    glColor3f(0.8, 0.8, 0.8)
    for edge in cube_edges:
        for v in edge:
            glVertex3fv(cube_vertices[v])
    glEnd()
    glPopMatrix()

# =========================
# FUNGSI GAMBAR PERSEGI 2D
# =========================
def draw_rectangle():
    glPushMatrix()
    glTranslatef(rect_tx, rect_ty, 0)
    glRotatef(rect_rot, 0, 0, 1)
    glScalef(rect_scale * reflect_x, rect_scale * reflect_y, 1)

    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    for x, y in rect_vertices:
        glVertex2f(x + shear_x * y, y + shear_y * x)
    glEnd()
    glPopMatrix()

# =========================
# MAIN PROGRAM
# =========================
def main():
    global cube_tx, cube_ty, cube_rx, cube_ry, cube_scale
    global rect_tx, rect_ty, rect_rot, rect_scale
    global shear_x, shear_y, reflect_x, reflect_y

    pygame.init()
    pygame.display.set_mode((800,600), DOUBLEBUF | OPENGL)
    gluPerspective(45, 800/600, 0.1, 50)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                # ===== KONTROL KUBUS 3D =====
                if event.key == K_a: cube_tx -= 0.2
                if event.key == K_d: cube_tx += 0.2
                if event.key == K_w: cube_ty += 0.2
                if event.key == K_s: cube_ty -= 0.2
                if event.key == K_q: cube_rx += 5
                if event.key == K_e: cube_ry += 5
                if event.key == K_z: cube_scale += 0.1
                if event.key == K_x: cube_scale -= 0.1

                # ===== KONTROL PERSEGI 2D =====
                if event.key == K_LEFT: rect_tx -= 0.2
                if event.key == K_RIGHT: rect_tx += 0.2
                if event.key == K_UP: rect_ty += 0.2
                if event.key == K_DOWN: rect_ty -= 0.2
                if event.key == K_r: rect_rot += 10
                if event.key == K_t: rect_scale += 0.1
                if event.key == K_y: rect_scale -= 0.1
                if event.key == K_1: shear_x = 1
                if event.key == K_2: shear_y = 1
                if event.key == K_3: reflect_x *= -1
                if event.key == K_4: reflect_y *= -1
                if event.key == K_0:
                    shear_x = shear_y = 0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        draw_rectangle()
        pygame.display.flip()
        pygame.time.wait(10)

main()