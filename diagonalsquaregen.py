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

        while (protdrawn + neutdrawn) < (proton_count + neutron_count):

            choice = random.randint(0, 1)

            if loop_count == 0:
                if choice == 0 and (protdrawn < proton_count):
                    # proton(prx, pry, prr, color=blue):
                    proton(x, y, nucleon_radius)
                    protdrawn += 1
                    loop_count += 1
                    continue

                elif choice == 1 and (neutdrawn < neutron_count):
                    # def neutron(nex, ney, ner, color=white):
                    neutron(x, y, nucleon_radius)
                    neutdrawn += 1
                    loop_count += 1
                    continue

            else:
                if choice == 0 and protdrawn < proton_count:

                    if loop_count in (1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265, 313, 365):
                        layer_count += 1
                        x += r
                        check = 1

                    # proton(prx, pry, prr, color=blue):
                    proton(x, y, nucleon_radius)
                    protdrawn += 1
                    loop_count += 1

                    if check == 1:
                        x -= r
                        y -= r
                        count += 1

                    if check == 2:
                        x -= r
                        y += r
                        count += 1

                    if check == 3:
                        x += r
                        y += r
                        count += 1

                    if check == 4:
                        x += r
                        y -= r
                        count += 1

                    if count == layer_count:
                        check += 1
                        count = 0

                elif choice == 1 and neutdrawn < neutron_count:

                    if loop_count in (1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265, 313, 365):
                        layer_count += 1
                        x += r
                        check = 1

                    # def neutron(nex, ney, ner, color=white):
                    neutron(x, y, nucleon_radius)
                    neutdrawn += 1
                    loop_count += 1

                    if check == 1:
                        x -= r
                        y -= r
                        count += 1

                    if check == 2:
                        x -= r
                        y += r
                        count += 1

                    if check == 3:
                        x += r
                        y += r
                        count += 1

                    if check == 4:
                        x += r
                        y -= r
                        count += 1

                    if count == layer_count:
                        check += 1
                        count = 0

        x = x_temp
        y = y_temp
        pygame.display.update()

        clock.tick(60)


sim_loop()
pygame.quit()
quit()
