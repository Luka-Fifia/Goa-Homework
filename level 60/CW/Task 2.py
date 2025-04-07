def is_planet_mnemonic_correct(solar_system, mnemonic):
    planets = []
    for i in solar_system:
        if i != "Asteroid":
            planets.append(i)
    
    upper_case_letters = []
    words = mnemonic.split()
    for char in words:
        upper_case_letters.append(char[0])
    
    planet_ucl = []
    for planet in planets:
        planet_ucl.append(planet[0])
    
    return upper_case_letters == planet_ucl