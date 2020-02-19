from pygame_functions import *
import pygame

def bmanGame():
    screenSize(1280,720)

    setBackgroundImage("C:/Users/vansh/Desktop/gameforHistory/assets/Bman/bg.png")

    character = makeSprite("C:/Users/vansh/Desktop/gameforHistory/Bmansprite/1.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/2.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/3.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/4.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/5.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/6.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/7.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/8.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/9.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Bmansprite/10.png")

    textBox = makeSprite("C:/Users/vansh/Desktop/gameforHistory/assets/Bman/text1.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Bman/text2.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Bman/text3.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Bman/text4.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Bman/text5.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Bman/text6.png")

    characterX = 400
    characterImage = 0
    characterY = 390

    showSprite(character)
    nextFrame = clock()

    transformSprite(character, 0, 3)
    moveSprite(character, characterX, characterY)

    while True:
        if keyPressed("right"):
            if clock() > nextFrame:
                characterImage += 1
                if characterImage > 4:
                    characterImage = 0
                changeSpriteImage(character,characterImage)
                nextFrame = clock() + 80

            characterX += 0.115
            moveSprite(character, characterX, characterY)
            scrollBackground(-2,0)

        

        if keyPressed("left"):
            if clock() > nextFrame:
                characterImage += 1
                if characterImage < 5:
                    characterImage = 5
                if characterImage > 9:
                    characterImage = 5
                changeSpriteImage(character,characterImage)
                nextFrame = clock() + 80

            characterX -= 0.115
            moveSprite(character, characterX, characterY)
            scrollBackground(2,0)

    # Event Listener
        if (int(characterX) == 424):
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX)  == 461):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 468):
            characterX = 469
            characterY = 390
            moveSprite(character,characterX,characterY)
            showSprite(character)
    # 
        if (int(characterX) == 505):
            moveSprite(textBox,400,100)
            changeSpriteImage(textBox,1)
            showSprite(textBox)

        if (int(characterX)  == 552):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 561):
            characterX = 562
            characterY = 490
            moveSprite(character,characterX,characterY)
            showSprite(character)
    # 
        if (int(characterX) == 592):
            moveSprite(textBox,400,100)
            changeSpriteImage(textBox,2)
            showSprite(textBox)

        if (int(characterX)  == 626):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 633):
            characterX = 634
            characterY = 490
            moveSprite(character,characterX,characterY)
            showSprite(character)

    # 
        if (int(characterX) == 655):
            moveSprite(textBox,400,100)
            changeSpriteImage(textBox,3)
            showSprite(textBox)

        if (int(characterX)  == 690):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 698):
            characterX = 699
            characterY = 490
            moveSprite(character,characterX,characterY)
            showSprite(character)

        if(int(characterX) == 722):
            moveSprite(textBox,400,100)
            changeSpriteImage(textBox,4)
            showSprite(textBox)

        if(int(characterX) == 739):
            hideSprite(character)
            changeSpriteImage(textBox,5)
            showSprite(textBox)

        if (int(characterX) == 745):
            pygame.time.wait(10)
            hideSprite(textBox)
            return 1


        

    endWait()