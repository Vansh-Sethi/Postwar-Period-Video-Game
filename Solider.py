from pygame_functions import *
import pygame

def SoliderGame():
    screenSize(1280,720)

    setBackgroundImage("C:/Users/vansh/Desktop/gameforHistory/assets/Solider/bg.png")

    character = makeSprite("C:/Users/vansh/Desktop/gameforHistory/Mansprite/Right/1.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Right/1.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Right/2.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Right/3.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Right/4.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Right/5.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Right/6.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Right/7.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Left/8.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Left/9.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Left/10.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Left/11.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Left/12.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Left/13.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/Mansprite/Left/14.png")

    textBox = makeSprite("C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox1.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox2.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox3.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox4.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox5.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox6.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox7.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox8.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Solider/textBox9.png")



    characterX = 200
    characterY = 480
    characterImage = 0


    transformSprite(character,0,1)
    moveSprite(character,characterX,characterY)
    showSprite(character)
    nextFrame = clock()

    while True:
        if keyPressed("right"):
            if clock() > nextFrame:
                characterImage += 1
                if characterImage > 6:
                    characterImage = 1
                changeSpriteImage(character,characterImage)
                nextFrame = clock() + 80

            characterX += 0.06
            moveSprite(character, characterX, characterY)
            scrollBackground(-2,0)
        

        if keyPressed("left"):
            if clock() > nextFrame:
                characterImage += 1
                if characterImage < 7:
                    characterImage = 7
                if characterImage > 14:
                    characterImage = 8
                changeSpriteImage(character,characterImage)
                nextFrame = clock() + 80

            characterX -= 0.06
            moveSprite(character, characterX, characterY)
            scrollBackground(2,0)

    # 1
        if (int(characterX) == 211):
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX) == 228):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 232):
            characterX = 233
            characterY = 480
            transformSprite(character,0,1.4)
            moveSprite(character, characterX, characterY)
            showSprite(character)

    # 2
        if (int(characterX) == 245):
            changeSpriteImage(textBox,1)
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX) == 273):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 277):
            characterX = 278
            characterY = 510
            transformSprite(character,0,0.7)
            moveSprite(character, characterX, characterY)
            showSprite(character)

    # 3
        if (int(characterX) == 288):
            changeSpriteImage(textBox,2)
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX) == 313):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 317):
            characterX = 318
            characterY = 475
            transformSprite(character,0,1.9)
            moveSprite(character, characterX, characterY)
            showSprite(character)

    # 4
        if (int(characterX) == 328):
            changeSpriteImage(textBox,3)
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX) == 348):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 353):
            characterX = 357
            characterY = 570
            transformSprite(character,0,0.8)
            moveSprite(character, characterX, characterY)
            showSprite(character)
        
    # 5
        if (int(characterX) == 372):
            changeSpriteImage(textBox,4)
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX) == 388):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 392):
            characterX = 394
            characterY = 470
            transformSprite(character,0,1.9)
            moveSprite(character, characterX, characterY)
            showSprite(character)
        print(characterX)

    # 6
        if (int(characterX) == 409):
            changeSpriteImage(textBox,5)
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX) == 426):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 431):
            characterX = 432
            characterY = 570
            transformSprite(character,0,0.8)
            moveSprite(character, characterX, characterY)
            showSprite(character)

    # 7
        if (int(characterX) == 445):
            changeSpriteImage(textBox,6)
            moveSprite(textBox,400,100)
            showSprite(textBox)

        if (int(characterX) == 463):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 467):
            characterX = 468
            characterY = 450
            transformSprite(character,0,1.5)
            moveSprite(character, characterX, characterY)
            showSprite(character)

    #8
        if (int(characterX) == 475):
            changeSpriteImage(textBox,7)
            moveSprite(textBox,400,100)
            showSprite(textBox)
        
        if (int(characterX) == 487):
            changeSpriteImage(textBox,8)
            moveSprite(textBox,400,100)
            showSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 495):
            pygame.time.wait(10)
            hideSprite(textBox)
            return 1
        
            

    endWait()