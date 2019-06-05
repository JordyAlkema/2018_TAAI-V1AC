import numpy as np

# Dit is de 'Magic Square' die wij gaan oplossen, 'None' staat voor een waarde die wij moeten berekenen.
magicSquare = np.array([
    8,     None,    None,
    None,  None,    2,
    None,  None,    9,
])

# Dit zijn de vergelijkingen omgeschreven naar een Matrix
defaultComparisonArray = np.array([
    [1, 1, 1, 0, 0, 0, 0, 0, 0, -1],    # Horizontal 1
    [0, 0, 0, 1, 1, 1, 0, 0, 0, -1],    # Horizontal 2
    [0, 0, 0, 0, 0, 0, 1, 1, 1, -1],    # Horizontal 3
    [1, 0, 0, 1, 0, 0, 1, 0, 0, -1],    # Vertical 1
    [1, 0, 0, 0, 1, 0, 0, 0, 1, -1],    # Diagonally L -> R
    [0, 1, 0, 0, 1, 0, 0, 1, 0, -1],    # Vertical 2
    [0, 0, 1, 0, 1, 0, 1, 0, 0, -1],    # Diagonally R -> L
    [0, 0, 1, 0, 0, 1, 0, 0, 1, -1],    # Vertical 3
    [0, 0, 0, 0, 3, 0, 0, 0, 0, -1],    # Total of each row
])

# Maak een nieuwe vector
comparisonMagicSquare = np.zeros(shape=(9, 1))

# Voor iedere plek die wij al kennen zetten wij de waarde in de comparisonArray op 0
# En halen wij de bekende waarde van de comparisonMagicSquare af
for rowKey in range(len(defaultComparisonArray) - 1):
    for numberKey in range(len(defaultComparisonArray[rowKey]) - 1):

        # Als wij de waarde niet kennen gaan wij door
        if magicSquare[numberKey] is None:
            continue

        comparisonMagicSquare[rowKey] -= defaultComparisonArray[rowKey][numberKey] * magicSquare[numberKey]
        defaultComparisonArray[rowKey][numberKey] = 0


# Omdat de dimensies niet kloppen gebruiken wij de pseudo inverse
inverseComparisonArray = np.linalg.pinv(defaultComparisonArray)
solutionVector = inverseComparisonArray.dot(comparisonMagicSquare)

# Vul de onbekende waardes in bij de magic square
for item in range(len(magicSquare) - 1):
    if magicSquare[item] is None:
        magicSquare[item] = solutionVector[item][0]

finalSolution = np.around(magicSquare.astype(np.double), 3)

# Voor formatting resizen wij hem naar een Matrix
finalSolution.resize(3, 3)

# Print het uitendelijke antwoord
print("De gevonden oplossing:")
print(finalSolution)
