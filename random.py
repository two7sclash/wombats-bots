import random

def wombat(state, time_left):
    turnDirections = ['right', 'left', 'about-face']
    turnDirection = turnDirections[random.randrange(0,3)]

    smokeDirections = ['forward', 'backward', 'left', 'right', 'drop']
    csmokeDirection = smokeDirections[random.randrange(0,5)]

    index = random.randrange(0,17)
    command = (((({ action: 'smoke', metadata: { direction: smokeDirection } }, { action: 'shoot', metadata: {} })[bool(index)], index < 16)[index],index < 12)[index], index < 10)[index]
                
    return {
        command,
        state
    }

echo wombat()