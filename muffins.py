import sys                  # Import libraries

getal = 1                   # We beginnen bij het getal 1.

while True:
    getal = getal + 1       # Elke keer wanneer de loop ergens vastloopt, proberen we het opnieuw met het volgende (gehele) getal.
    if getal % 5 == 1:      # Is de rest van het getal, gedeeld door 5, gelijk aan 1 (de muffin voor Tobias)? Indien neen: keer terug en verhoog getal.
        a = (getal - 1)/5   # Indien ja, elke stapel muffins die wordt gemaakt is a groot
        if (a*4) % 5 != 1:  # Is de overgebleven stapel muffins (nadat Suske er één heeft weggelegd) deelbaar door 5 met rest 1?
            continue        # Zo neen, ga terug naar begin.
        b = (a*4-1)/5       # Zo ja, bereken hiervoor de grootte van 1 stapel...
        if (b*4) % 5 != 1:  # ...
            continue
        c = (b*4-1)/5
        if (c*4) % 5 != 1:
            continue
        d = (c*4-1)/5
        if (d*4) % 5 != 1:
            continue
        e = (d*4-1)/5
        if (e*4) % 5 != 1:
            continue
        print(getal)
        sys.exit()