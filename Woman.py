from pygame_functions import *
import pygame

def womanGame():
    screenSize(1280,720)

    setBackgroundImage("C:/Users/vansh/Desktop/gameforHistory/assets/Femal/bg.png")

    character = makeSprite("C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/1.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/2.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/3.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/4.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/5.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/6.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/7.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/8.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/9.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/10.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/11.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/FemaleSprite/12.png")

    textBox = makeSprite("C:/Users/vansh/Desktop/gameforHistory/assets/Femal/text1.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Femal/text2.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Femal/text3.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Femal/text4.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Femal/text5.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Femal/text6.png")

    characterX = 400
    characterImage = 0
    characterY = 500

    showSprite(character)
    nextFrame = clock()

    transformSprite(character, 0, 8)
    moveSprite(character, characterX, characterY)

    while True:
        if keyPressed("right"):
            if clock() > nextFrame:
                characterImage += 1
                if characterImage > 5:
                    characterImage = 0
                changeSpriteImage(character,characterImage)
                nextFrame = clock() + 80

            characterX += 0.115
            moveSprite(character, characterX, characterY)
            scrollBackground(-2,0)

        

        if keyPressed("left"):
            if clock() > nextFrame:
                characterImage += 1
                if characterImage < 6:
                    characterImage = 6
                if characterImage > 11:
                    characterImage = 6
                changeSpriteImage(character,characterImage)
                nextFrame = clock() + 80

            characterX -= 0.115
            moveSprite(character, characterX, characterY)
            scrollBackground(2,0)

    # 1
        if (int(characterX) == 412):
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX)  == 440):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 449):
            characterX = 450
            characterY = 250
            moveSprite(character,characterX,characterY)
            showSprite(character)

    # 2
        if (int(characterX) == 469):
            moveSprite(textBox,400,50)
            changeSpriteImage(textBox,1)
            showSprite(textBox)

        if (int(characterX)  == 503):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 511):
            characterX = 512
            characterY = 475
            transformSprite(character, 0, 14)
            moveSprite(character,characterX,characterY)
            showSprite(character)

    # 3
        if (int(characterX) == 536):
            moveSprite(textBox,400,100)
            changeSpriteImage(textBox,2)
            showSprite(textBox)

        if (int(characterX)  == 595):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 609):
            characterX = 610
            characterY = 600
            transformSprite(character, 0, 4)
            moveSprite(character,characterX,characterY)
            showSprite(character)
        
    # 4
        if (int(characterX) == 660):
            moveSprite(textBox,400,100)
            changeSpriteImage(textBox,3)
            showSprite(textBox)

        if (int(characterX)  == 712):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 719):
            characterX = 720
            characterY = 500
            transformSprite(character, 0, 7)
            moveSprite(character,characterX,characterY)
            showSprite(character)
        
        if (int(characterX) == 746):
            moveSprite(textBox,400,100)
            changeSpriteImage(textBox,4)
            showSprite(textBox)
        
        if(int(characterX) == 790):
            changeSpriteImage(textBox,5)
            hideSprite(character)

        if (int(characterX) == 795):
            pygame.time.wait(10)
            hideSprite(textBox)
            return 1
        

        

    endWait()