from pygame_functions import *
import pygame

def asianGame():
    screenSize(1280,720)

    setBackgroundImage("C:/Users/vansh/Desktop/gameforHistory/assets/Asian/bg.png")

    character = makeSprite("C:/Users/vansh/Desktop/gameforHistory/AsianSprite/1.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/AsianSprite/2.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/AsianSprite/3.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/AsianSprite/4.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/AsianSprite/5.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/AsianSprite/6.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/AsianSprite/7.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/AsianSprite/8.png")
    addSpriteImage(character, "C:/Users/vansh/Desktop/gameforHistory/AsianSprite/9.png")

    textBox = makeSprite("C:/Users/vansh/Desktop/gameforHistory/assets/Asian/text1.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Asian/text2.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Asian/text3.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Asian/text4.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Asian/text5.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Asian/text6.png")
    addSpriteImage(textBox, "C:/Users/vansh/Desktop/gameforHistory/assets/Asian/text7.png")

    characterX = 400
    characterImage = 0
    characterY = 250

    showSprite(character)
    nextFrame = clock()

    transformSprite(character, 0, 3)
    moveSprite(character, characterX, 250)

    while True:
        if keyPressed("right"):
            if clock() > nextFrame:
                characterImage += 1
                if characterImage > 3:
                    characterImage = 0
                changeSpriteImage(character,characterImage)
                nextFrame = clock() + 80

            characterX += 0.115
            moveSprite(character, characterX, characterY)
            scrollBackground(-2,0)

        

        if keyPressed("left"):
            if clock() > nextFrame:
                characterImage += 1
                if characterImage < 4:
                    characterImage = 5
                if characterImage > 8:
                    characterImage = 5
                changeSpriteImage(character,characterImage)
                nextFrame = clock() + 80

            characterX -= 0.115
            moveSprite(character, characterX, characterY)
            scrollBackground(2,0)

    # Event Listener
        if (int(characterX) == 424):
            moveSprite(textBox,400,500)
            showSprite(textBox)

        if (int(characterX)  == 444):
            hideSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 455):
            characterX = 456
            characterY = 490
            moveSprite(character,characterX,characterY)
            showSprite(character)

        if (int(characterX) == 491):
            moveSprite(textBox,400,100)
            changeSpriteImage(textBox,1)
            showSprite(textBox)

    #    
        if (int(characterX) == 519):
            hideSprite(textBox)
        
        if (int(characterX) == 520):
            hideSprite(character)
        
        if (int(characterX) == 529):
            characterX = 530
            characterY = 550
            moveSprite(character, characterX, characterY)
            showSprite(character)

    # 
        if (int(characterX) == 563):
            changeSpriteImage(textBox,2)
            showSprite(textBox)

        if (int(characterX) == 596):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 605):
            characterX = 606
            characterY = 500
            moveSprite(character, characterX, characterY)
            showSprite(character)

    #
        if (int(characterX) == 643):
            changeSpriteImage(textBox,3)
            showSprite(textBox)

        if (int(characterX) == 672):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 681):
            characterX = 682
            characterY = 500
            moveSprite(character, characterX, characterY)
            showSprite(character)

    #
        if (int(characterX) == 725):
            changeSpriteImage(textBox,4)
            showSprite(textBox)

        if (int(characterX) == 793):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 801):
            characterX = 802
            characterY = 530
            moveSprite(character, characterX, characterY)
            showSprite(character)

    #
        if (int(characterX) == 854):
            changeSpriteImage(textBox,5)
            showSprite(textBox)

        if (int(characterX) == 900):
            hideSprite(character)
            hideSprite(textBox)
        
        if (int(characterX) == 908):
            characterX = 909
            characterY = 530
            moveSprite(character, characterX, characterY)
            showSprite(character)

        if(int(characterX) == 955):
            changeSpriteImage(textBox,6)
            showSprite(textBox)
            hideSprite(character)

        if (int(characterX) == 961):
            pygame.time.wait(10)
            hideSprite(textBox)
            return 1
				

                

        
        

        

    endWait()