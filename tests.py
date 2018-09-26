import atom
import pygame
import numpy
import random

pygame.init()

display_width = 900
display_height = 700

nucleon_radius = 5
electron_radius = 1

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

prots = input("Protons: ")
neuts = input("Neutrons: ")
elecs = input("Electrons: ")

userAtom = atom.Atom(prots, elecs, neuts)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Atomic Model')
clock = pygame.time.Clock()


def proton(prx, pry, prr, color=blue):
    pygame.draw.circle(gameDisplay, black, (int(prx), int(pry)), prr + 2, 2)
    pygame.draw.circle(gameDisplay, color, (int(prx), int(pry)), prr)


def electron(elecx, elecy, elecr, color=red):
    pygame.draw.circle(gameDisplay, black, (int(elecx), int(elecy)), elecr + 1, 1)
    pygame.draw.circle(gameDisplay, color, (int(elecx), int(elecy)), elecr)


def neutron(nex, ney, ner, color=white):
    pygame.draw.circle(gameDisplay, black, (int(nex), int(ney)), ner + 2, 2)
    pygame.draw.circle(gameDisplay, color, (int(nex), int(ney)), ner)


def nucleus(radius, offset):
    x, y = 0, radius
    plot_nucleon(x, y, radius, offset)


def symmetry_points(x, y, offset, prr=nucleon_radius):
    proton(x + offset, y + offset, prr)
    proton(-x + offset, y + offset, prr)
    proton(x + offset, -y + offset, prr)
    proton(-x + offset, -y + offset, prr)
    proton(y + offset, x + offset, prr)
    proton(-y + offset, x + offset, prr)
    proton(y + offset, -x + offset, prr)
    proton(-y + offset, -x + offset, prr)


def plot_nucleon(x, y, radius, offset):
    d = 5 / 4.0 - radius
    symmetry_points(x, y, radius + offset)
    while x < y:
        if d < 0:
            x += 14
            d += 2 * x + 14
        else:
            x += 14
            y -= 14
            d += 2 * (x - y) + 14
        symmetry_points(x, y, radius + offset)


def sim_loop():

    # atomic toString
    print(userAtom.str())

    # for nucleons and filling alg
    x = (display_width * 0.5)
    y = (display_height * 0.5)
    proton_count = userAtom.atom_num
    neutron_count = userAtom.neut_num
    r = 2 * (nucleon_radius + 2)

    # for moving atom
    x_change = 0
    y_change = 0

    # for electrons
    angle = 0
    angle_change = .2
    startx = 15 * numpy.cos(angle)
    starty = 15 * numpy.sin(angle)
    electron_count = userAtom.elec_num

    sim_exit = False

    while not sim_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5

            if event.type == pygame.KEYUP:  # Key has been released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        x_temp = x + x_change
        y_temp = y + y_change
        gameDisplay.fill(white)

        # variables that need to be reset for filling
        protdrawn = 0
        neutdrawn = 0
        layer_count = 0
        loop_count = 0
        count = 0
        check = 0

        random.seed(42)

        # filling algoritm for the nucleus

        nucleus(50, 50)
        nucleus(14, 50)

        x = x_temp
        y = y_temp
        pygame.display.update()

        clock.tick(60)


sim_loop()
pygame.quit()
quit()
