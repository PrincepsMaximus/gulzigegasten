# De gulzige gasten
Opdracht 2 van het Wiskunnend Wiske, jaargang 2020-2021.

## Manier van werken
Het programma toetst elk **geheel getal**, beginnend bij een, aan een voorwaarde(n). Het eerste getal dat hieraan voldoet wordt weergegeven en het programma stopt. Dit wordt verwezenlijkt met een herhalend patroon: een loop.

## De voorwaarde(n)
* Elk getal wordt eerst getest of **de rest**, wanneer het **gedeeld wordt door 5** (het aantal gelijke stapels), gelijk **is aan 1**. Deze rest moet namelijk aan Tobias gegeven worden.
In het programmatje beginnen we dus met een getal. Wanneer het voor de eerste test slaagt, delen we dit getal (-1, want dit hebben we aan Tobias gegeven) door 5. Dit is het *aantal gelijke stapels*. Zo één stapel geven we dan een nieuwe naam (a, b, c...). Vervolgens worden vier van deze stapels (het aantal muffins dat de stiekemerd overlaat), weer herverdeeld door de volgende. We checken dus weer de voorwaarde en **herhalen dit proces zes keer**.

- Maxime Deryck
