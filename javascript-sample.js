((state, timeLeftFn) => {
    const directions = ['right', 'left', 'about-face'];
    const direction = directions[Math.floor(Math.random() * 3)];
    
    const index = Math.floor(Math.random() * 17);
    const command = index < 10 ?
        { action: 'move', metadata: {} } : 
        index < 12 ?
            { action: 'turn', metadata: { direction } } :
            index < 16 ?
                { action: 'shoot', metadata: {} } :
                { action: 'smoke', metadata: {} };
                
    return {
        command, 
        state: {
            hello: 'world'
        }
    };
});
