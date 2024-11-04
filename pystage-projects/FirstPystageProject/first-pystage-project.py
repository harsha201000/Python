from pystage.en import Sprite,Stage

stage = Stage()
character = stage.add_a_sprite()

def doit(character: Sprite):
    for i in range(5):
        character.move(10)
        character.turn_right(90)
        character.wait(1)
        
character.when_program_starts(doit)
stage.play()