import pygame, sys, time
from pygame.locals import *
pygame.init()
FPS = 150
fpsClock = pygame.time.Clock()
pygame.display.set_caption('OVERBEAT v1.1')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (192, 192, 192)
PURPLE = (204, 0, 204)
ORANGE = (255, 128, 0)
OVERWATCH_BLUE = (17, 151, 214)
OVERWATCH_MUSTARD = (217, 152, 34)
DISPLAYSURF = pygame.display.set_mode((960, 540))

def main_surf1():
    soundObj1 = pygame.mixer.Sound('OVERWATCH_MAIN.wav')
    soundObj1.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
        DISPLAYSURF.fill(WHITE)
        background_img1 = pygame.image.load('background_surf1.png')
        DISPLAYSURF.blit(background_img1, (100, 0))
        fontObj1 = pygame.font.Font('koverwatch.ttf', 32)
        textSurfaceObj1 = fontObj1.render('새로운 비트는 언제나 환영이야!', True, BLACK)
        textRectObj1 = textSurfaceObj1.get_rect()
        textRectObj1.center = (480, 350)
        DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
        fontObj2= pygame.font.Font('koverwatch.ttf', 24)
        textSurfaceObj2 = fontObj2.render('계속하려면 아무 곳이나 클릭하십시오', True, GRAY)
        textRectObj2 = textSurfaceObj2.get_rect()
        textRectObj2.center = (480, 430)
        DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
        fontObj3 = pygame.font.Font('gulim.ttc', 12)
        textSurfaceObj3 = fontObj3.render('Copyright ⓒ 2016 ILC05 Koo Bonseung, Lee Seungwon, Nam Hoje, Park Mokyun, Park Donghyeon All Rights Reserved. v1.1', True, BLACK)
        textRectObj3 = textSurfaceObj3.get_rect()
        textRectObj3.center = (480, 500)
        DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)
        pygame.mouse.set_visible(False)
        cursor_position = pygame.mouse.get_pos()
        cursor_img = pygame.image.load('overwatch_cursor.cur')
        DISPLAYSURF.blit(cursor_img, (cursor_position[0], cursor_position[1]))
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            soundObj1.stop()
            break

def main_surf2():
    soundObj2 = pygame.mixer.Sound('Lucky_Strike.wav')
    time.sleep(3)
    soundObj2.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
        DISPLAYSURF.fill(BLACK)
        background_img2 = pygame.image.load('background_surf2.png')
        DISPLAYSURF.blit(background_img2, (0, 0))
        pygame.draw.rect(DISPLAYSURF, BLACK, (75, 0, 200, 540))
        pygame.draw.line(DISPLAYSURF, WHITE, (125, 0), (125, 540), 2)
        pygame.draw.line(DISPLAYSURF, WHITE, (175, 0), (175, 540), 2)
        pygame.draw.line(DISPLAYSURF, WHITE, (225, 0), (225, 540), 2)
        pygame.draw.line(DISPLAYSURF, RED, (75, 450), (275, 450), 10)
        note1.note_function()
        '''note2.note_function()'''
        note3.note_function()
        '''note4.note_function()'''
        note5.note_function()
        '''note6.note_function()'''
        note7.note_function()
        '''note8.note_function()'''
        '''note9.note_function()'''
        note10.note_function()
        '''note11.note_function()'''
        note12.note_function()
        '''note13.note_function()'''
        note14.note_function()
        '''note15.note_function()'''
        note16.note_function()
        note17.note_function()
        '''note18.note_function()'''
        note19.note_function()
        '''note20.note_function()'''
        note21.note_function()
        '''note22.note_function()'''
        note23.note_function()
        '''note24.note_function()'''
        '''note25.note_function()'''
        note26.note_function()
        '''note27.note_function()'''
        note28.note_function()
        '''note29.note_function()'''
        note30.note_function()
        '''note31.note_function()'''
        note32.note_function()
        '''note33.note_function()'''
        note34.note_function()
        '''note35.note_function()'''
        note36.note_function()
        note37.note_function()
        '''note38.note_function()'''
        note39.note_function()
        note40.note_function()
        note41.note_function()
        note42.note_function()
        note43.note_function()
        note44.note_function()
        note45.note_function()
        note46.note_function()
        note47.note_function()
        note48.note_function()
        note49.note_function()
        note50.note_function()
        note51.note_function()
        note52.note_function()
        note53.note_function()
        note54.note_function()
        note55.note_function()
        note56.note_function()
        note57.note_function()
        note58.note_function()
        note59.note_function()
        note60.note_function()
        note61.note_function()
        note62.note_function()
        note63.note_function()
        note64.note_function()
        note65.note_function()
        note66.note_function()
        note67.note_function()
        note68.note_function()
        note69.note_function()
        note70.note_function()
        note71.note_function()
        note72.note_function()
        note73.note_function()
        note74.note_function()
        note75.note_function()
        note76.note_function()
        note77.note_function()
        note78.note_function()
        note79.note_function()
        note80.note_function()
        note81.note_function()
        note82.note_function()
        note83.note_function()
        note84.note_function()
        note85.note_function()
        note86.note_function()
        note87.note_function()
        note88.note_function()
        note89.note_function()
        note90.note_function()
        note91.note_function()
        note92.note_function()
        note93.note_function()
        note94.note_function()
        note95.note_function()
        note96.note_function()
        note97.note_function()
        note98.note_function()
        note99.note_function()
        note100.note_function()
        note101.note_function()
        note102.note_function()
        note103.note_function()
        note104.note_function()
        note105.note_function()
        note106.note_function()
        note107.note_function()
        note108.note_function()
        note109.note_function()
        note110.note_function()
        note111.note_function()
        note112.note_function()
        note113.note_function()
        note114.note_function()
        note115.note_function()
        note116.note_function()
        note117.note_function()
        note118.note_function()
        note119.note_function()
        note120.note_function()
        note121.note_function()
        note122.note_function()
        note123.note_function()
        note124.note_function()
        note125.note_function()
        note126.note_function()
        note127.note_function()
        note128.note_function()
        note129.note_function()
        note130.note_function()
        note131.note_function()
        note132.note_function()
        note133.note_function()
        note134.note_function()
        note135.note_function()
        note136.note_function()
        note137.note_function()
        note138.note_function()
        note139.note_function()
        note140.note_function()
        note141.note_function()
        note142.note_function()
        note143.note_function()
        note144.note_function()
        note145.note_function()
        note146.note_function()
        note147.note_function()
        note148.note_function()
        note149.note_function()
        note150.note_function()
        note151.note_function()
        fontObj4 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj4 = fontObj4.render(str(round(main_status.score)), True, WHITE)
        textRectObj4 = textSurfaceObj4.get_rect()
        textRectObj4.center = (880, 35)
        DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)
        fontObj5 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj5 = fontObj5.render(str(main_status.accuracy) + '%', True, WHITE)
        textRectObj5 = textSurfaceObj5.get_rect()
        textRectObj5.center = (880, 105)
        DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)
        fontObj6 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj6 = fontObj6.render(str(main_status.combo), True, YELLOW)
        textRectObj6 = textSurfaceObj6.get_rect()
        textRectObj6.center = (175, 105)
        DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)
        fontObj24 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj24 = fontObj24.render('SCORE', True, WHITE)
        textRectObj24 = textSurfaceObj24.get_rect()
        textRectObj24.center= (400, 35)
        DISPLAYSURF.blit(textSurfaceObj24, textRectObj24)
        fontObj25 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj25 = fontObj25.render('ACCURACY', True, WHITE)
        textRectObj25 = textSurfaceObj25.get_rect()
        textRectObj25.center = (400, 105)
        DISPLAYSURF.blit(textSurfaceObj25, textRectObj25)
        fontObj26 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj26 = fontObj26.render('COMBO', True, YELLOW)
        textRectObj26 = textSurfaceObj26.get_rect()
        textRectObj26.center = (175, 35)
        DISPLAYSURF.blit(textSurfaceObj26, textRectObj26)
        pygame.draw.rect(DISPLAYSURF, OVERWATCH_BLUE, (75, 455, 50, 85))
        pygame.draw.rect(DISPLAYSURF, OVERWATCH_MUSTARD, (125, 455, 50, 85))
        pygame.draw.rect(DISPLAYSURF, OVERWATCH_BLUE, (175, 455, 50, 85))
        pygame.draw.rect(DISPLAYSURF, OVERWATCH_MUSTARD, (225, 455, 50, 85))
        fontObj27 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj27 = fontObj27.render('A', True, WHITE)
        textRectObj27 = textSurfaceObj27.get_rect()
        textRectObj27.center = (100, 505)
        DISPLAYSURF.blit(textSurfaceObj27, textRectObj27)
        fontObj28 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj28 = fontObj28.render('S', True, WHITE)
        textRectObj28 = textSurfaceObj28.get_rect()
        textRectObj28.center = (150, 505)
        DISPLAYSURF.blit(textSurfaceObj28, textRectObj28)
        fontObj29 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj29 = fontObj29.render('D', True, WHITE)
        textRectObj29 = textSurfaceObj29.get_rect()
        textRectObj29.center = (200, 505)
        DISPLAYSURF.blit(textSurfaceObj29, textRectObj29)
        fontObj30 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj30 = fontObj30.render('F', True, WHITE)
        textRectObj30 = textSurfaceObj30.get_rect()
        textRectObj30.center = (250, 505)
        DISPLAYSURF.blit(textSurfaceObj30, textRectObj30)
        pygame.mouse.set_visible(False)
        cursor_position = pygame.mouse.get_pos()
        cursor_img = pygame.image.load('overwatch_cursor.cur')
        DISPLAYSURF.blit(cursor_img, (cursor_position[0], cursor_position[1]))
        if note151.judgment == True:
            break

def main_surf3():
    soundObj3 = pygame.mixer.Sound('OVERWATCH_VICTORY.wav')
    soundObj3.play()
    if 90 <= main_status.accuracy:
        main_status.rank = 'S'
        main_status.rank_color = PURPLE
    elif 80 <= main_status.accuracy:
        main_status.rank = 'A'
        main_status.rank_color = BLUE
    elif 70 <= main_status.accuracy:
        main_status.rank = 'B'
        main_status.rank_color = GREEN
    elif 60 <= main_status.accuracy:
        main_status.rank = 'C'
        main_status.rank_color = YELLOW
    elif 50 <= main_status.accuracy:
        main_status.rank = 'D'
        main_status.rank_color = ORANGE
    else:
        main_status.rank = 'F'
        main_status.rank_color = RED
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
        DISPLAYSURF.fill(BLACK)
        background_img3 = pygame.image.load('background_surf2.png')
        DISPLAYSURF.blit(background_img3, (0, 0))
        fontObj7 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj7 = fontObj7.render('SCORE', True, WHITE)
        textRectObj7 = textSurfaceObj7.get_rect()
        textRectObj7.center = (160, 45)
        DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)
        fontObj8 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj8 = fontObj8.render(str(round(main_status.score)), True, WHITE)
        textRectObj8 = textSurfaceObj8.get_rect()
        textRectObj8.center = (640, 45)
        DISPLAYSURF.blit(textSurfaceObj8, textRectObj8)
        fontObj9 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj9 = fontObj9.render('JUSTICE', True, BLUE)
        textRectObj9 = textSurfaceObj9.get_rect()
        textRectObj9.center = (160, 135)
        DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)
        fontObj10 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj10 = fontObj10.render(str(main_status.justice), True, BLUE)
        textRectObj10 = textSurfaceObj10.get_rect()
        textRectObj10.center = (480, 135)
        DISPLAYSURF.blit(textSurfaceObj10, textRectObj10)
        fontObj11 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj11 = fontObj11.render('ATTACK', True, GREEN)
        textRectObj11 = textSurfaceObj11.get_rect()
        textRectObj11.center = (160, 225)
        DISPLAYSURF.blit(textSurfaceObj11, textRectObj11)
        fontObj12 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj12 = fontObj12.render(str(main_status.attack), True, GREEN)
        textRectObj12 = textSurfaceObj12.get_rect()
        textRectObj12.center = (480, 225)
        DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)
        fontObj13 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj13 = fontObj13.render('MISS', True, RED)
        textRectObj13 = textSurfaceObj13.get_rect()
        textRectObj13.center = (160, 315)
        DISPLAYSURF.blit(textSurfaceObj13, textRectObj13)
        fontObj14 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj14 = fontObj14.render(str(main_status.miss), True, RED)
        textRectObj14 = textSurfaceObj14.get_rect()
        textRectObj14.center = (480, 315)
        DISPLAYSURF.blit(textSurfaceObj14, textRectObj14)
        fontObj15 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj15 = fontObj15.render('MAX COMBO', True, YELLOW)
        textRectObj15 = textSurfaceObj15.get_rect()
        textRectObj15.center = (240, 405)
        DISPLAYSURF.blit(textSurfaceObj15, textRectObj15)
        fontObj16 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj16 = fontObj16.render(str(max(main_status.combo_list)), True, YELLOW)
        textRectObj16 = textSurfaceObj16.get_rect()
        textRectObj16.center = (240, 495)
        DISPLAYSURF.blit(textSurfaceObj16, textRectObj16)
        fontObj17 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj17 = fontObj17.render('ACCURACY', True, WHITE)
        textRectObj17 = textSurfaceObj17.get_rect()
        textRectObj17.center = (550, 405)
        DISPLAYSURF.blit(textSurfaceObj17, textRectObj17)
        fontObj18= pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj18 = fontObj18.render(str(main_status.accuracy) + '%', True, WHITE)
        textRectObj18 = textSurfaceObj18.get_rect()
        textRectObj18.center = (550, 495)
        DISPLAYSURF.blit(textSurfaceObj18, textRectObj18)
        fontObj19 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
        textSurfaceObj19 = fontObj19.render('RANK', True, WHITE)
        textRectObj19 = textSurfaceObj19.get_rect()
        textRectObj19.center = (800, 135)
        DISPLAYSURF.blit(textSurfaceObj19, textRectObj19)
        fontObj20 = pygame.font.Font('big_noodle_titling_oblique.ttf', 128)
        textSurfaceObj20 = fontObj20.render(str(main_status.rank), True, main_status.rank_color)
        textRectObj20 = textSurfaceObj20.get_rect()
        textRectObj20.center = (800, 270)
        DISPLAYSURF.blit(textSurfaceObj20, textRectObj20)
        pygame.mouse.set_visible(False)
        cursor_position = pygame.mouse.get_pos()
        cursor_img = pygame.image.load('OVERWATCH_CURSOR.cur')
        DISPLAYSURF.blit(cursor_img, (cursor_position[0], cursor_position[1]))

class status:
    def __init__(self):
        self.score = 0
        self.justice = 0
        self.attack = 0
        self.miss = 0
        self.combo = 0
        self.accuracy = 100
        self.note_number = 0
        self.combo_list = list()

class note:
    def __init__(self, note_x, note_y):
        self.note_x = note_x
        self.note_y = note_y
        self.judgment = False
        if self.note_x == 75:
            self.img = pygame.image.load('note_blue.png')
            self.note_key = K_a
        elif self.note_x == 125:
            self.img = pygame.image.load('note_mustard.png')
            self.note_key = K_s
        elif self.note_x == 175:
            self.img = pygame.image.load('note_blue.png')
            self.note_key = K_d
        else:
            self.img = pygame.image.load('note_mustard.png')
            self.note_key = K_f
    def note_function(self):
        self.note_y += 35
        DISPLAYSURF.blit(self.img, (self.note_x, self.note_y))
        if self.judgment == False:
            if self.note_y > 500:
                main_status.miss += 1
                main_status.combo = 0
                main_status.note_number += 1
                main_status.combo_list.append(main_status.combo)
                main_status.accuracy = round(main_status.score / (1000000 * main_status.note_number / 132) * 100, 2)
                fontObj21 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
                textSurfaceObj21 = fontObj21.render('MISS', True, RED)
                textRectObj21 = textSurfaceObj21.get_rect()
                textRectObj21.center = (175, 350)
                DISPLAYSURF.blit(textSurfaceObj21, textRectObj21)
                self.judgment = True
            for event in pygame.event.get():
                if 400< self.note_y <= 500 and event.type == KEYDOWN and event.key == self.note_key:
                    main_status.justice += 1
                    main_status.score += 1000000 / 132
                    main_status.combo += 1
                    main_status.note_number += 1
                    main_status.combo_list.append(main_status.combo)
                    main_status.accuracy = round(main_status.score / (1000000 * main_status.note_number / 132) * 100, 2)
                    fontObj22 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
                    textSurfaceObj22 = fontObj22.render('JUSTICE', True, BLUE)
                    textRectObj22 = textSurfaceObj22.get_rect()
                    textRectObj22.center = (175, 350)
                    DISPLAYSURF.blit(textSurfaceObj22, textRectObj22)
                    self.judgment = True
                if 300< self.note_y <= 400 and event.type == KEYDOWN and event.key == self.note_key:
                    main_status.attack += 1
                    main_status.score += 1000000 * 0.5 / 132
                    main_status.combo += 1
                    main_status.note_number += 1
                    main_status.combo_list.append(main_status.combo)
                    main_status.accuracy = round(main_status.score / (1000000 * main_status.note_number / 132) * 100, 2)
                    fontObj23 = pygame.font.Font('big_noodle_titling_oblique.ttf', 64)
                    textSurfaceObj23 = fontObj23.render('ATTACK', True, GREEN)
                    textRectObj23 = textSurfaceObj23.get_rect()
                    textRectObj23.center = (175, 350)
                    DISPLAYSURF.blit(textSurfaceObj23, textRectObj23)
                    self.judgment = True

main_status = status()
note1 = note(125, 35)
'''note2 = note(175, 35)'''
note3 = note(75, -955)
'''note4 = note(225, -955)'''
note5 = note(125, -1805)
'''note6 = note(175, -1805)'''
note7 = note(75, -2705)
'''note8 = note(225, -2705)'''
'''beat1'''
'''note9 = note(75, -3705)'''
note10 = note(125, -3705)
'''note11 = note(75, -4005)'''
note12 = note(125, -4005)
'''note13 = note(75, -4305)'''
note14 = note(125, -4305)
'''note15 = note(75, -4605)'''
note16 = note(125, -4605)
'''beat2'''
note17 = note(75, -4820)
'''note18 = note(225, -4820)'''
note19 = note(75, -5120)
'''note20 = note(225, -5120)'''
note21 = note(75,-5420)
'''note22 = note(225,-5420)'''
note23 = note(75,-5720)
'''note24 = note(225,-5720)'''
'''beat3'''
'''note25 = note(75,-5820)'''
note26 = note(125,-5820)
'''note27 = note(75,-6120)'''
note28 = note(125,-6120)
'''note29 = note(75,-6420)'''
note30 = note(125,-6420)
'''note31 = note(75,-6620)'''
note32 = note(125,-6620)
'''note33 = note(75,-6920)'''
note34 = note(125,-6920)
'''note35 = note(75,-7220)'''
note36 = note(125,-7220)
'''beat4'''
note37 = note(75,-7420)
'''note38 = note(225,-7420)'''
note39 = note(225,-7570)
note40 = note(175,-7720)
note41 = note(125,-7870)
note42 = note(75,-8020)
note43 = note(225,-8270)
note44 = note(75,-8520)
note45 = note(225,-8770)
note46 = note(75,-9020)
note47 = note(225,-9270)
note48 = note(75,-9520)
note49 = note(225,-9770)
note50 = note(125,-10020)
note51 = note(175,-10270)
note52 = note(125,-10520)
note53 = note(175,-10770)
note54 = note(225,-11020)
note55 = note(75,-11270)
note56 = note(225,-11520)
note57 = note(175,-11790)
note58 = note(125,-12040)
note59 = note(75,-12290)
note60 = note(75,-12540)
note61 = note(225,-12790)
note62 = note(75,-13040)
note63 = note(225,-13290)
note64 = note(75,-13540)
note65 = note(225,-13790)
note66 = note(75,-14040)
note67 = note(225,-14290)
note68 = note(75,-14540)
note69 = note(225,-14790)
note70 = note(75,-15040)
note71 = note(225,-15290)
note72 = note(75,-15540)
note73 = note(225,-15790)
note74 = note(75,-16090)
note75 = note(225,-16390)
note76 = note(125,-16690)
note77 = note(175,-16990)
note78 = note(125,-17290)
note79 = note(175,-17590)
note80 = note(75,-17890)
note81 = note(75,-18190)
note82 = note(75,-18490)
note83 = note(75,-18790)
note84 = note(125,-19090)
note85 = note(125,-19390)
note86 = note(175,-19690)
note87 = note(175,-19990)
note88 = note(75,-20290)
note89 = note(225,-20590)
note90 = note(125,-20860)
note91 = note(175,-21130)
note92 = note(125,-21390)
note93 = note(175,-21650)
note94 = note(125,-21920)
note95 = note(175,-22190)
note96 = note(125,-22460)
note97 = note(175,-22730)
note98 = note(125,-23000)
note99 = note(175,-23270)
note100 = note(75,-23540)
note101 = note(225,-23810)
note102 = note(75,-24080)
note103 = note(225,-24350)
note104 = note(125,-24620)
note105 = note(175,-24890)
note106 = note(125,-25160)
note107 = note(175,-25430)
note108 = note(125,-25680)
note109 = note(175,-25930)
note110 = note(125,-26180)
note111 = note(175,-26430)
note112 = note(125,-26680)
note113 = note(175,-26930)
note114 = note(75,-27180)
note115 = note(225,-27430)
note116 = note(75,-27680)
note117 = note(225,-27930)
note118 = note(75,-28180)
note119 = note(225,-28430)
note120 = note(125,-28680)
note121 = note(175,-28930)
note122 = note(125,-29180)
note123 = note(175,-29430)
note124 = note(75,-29680)
note125 = note(225,-29930)
note126 = note(75,-30180)
note127 = note(225,-30430)
note128 = note(125,-30680)
note129 = note(175,-30930)
note130 = note(125,-31180)
note131 = note(175,-31430)
note132 = note(75,-31680)
note133 = note(225,-31930)
note134 = note(75,-32180)
note135 = note(225,-32430)
note136 = note(125,-32680)
note137 = note(175,-32930)
note138 = note(125,-33180)
note139 = note(175,-33430)
note140 = note(125,-33680)
note141 = note(175,-33930)
note142 = note(125,-34180)
note143 = note(175,-34430)
note144 = note(75,-34680)
note145 = note(225,-34930)
note146 = note(75,-35180)
note147 = note(225,-35430)
note148 = note(75,-35680)
note149 = note(225,-35930)
note150 = note(75,-36180)
note151 = note(225,-36430)
main_surf1()
main_surf2()
main_surf3()
