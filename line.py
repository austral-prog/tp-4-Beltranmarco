def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))

    print("El coeficiente A de su ecuación de la recta es:", A)
    print("El coeficiente B de su ecuación de la recta es:", B)
    print("El coeficiente X1 de su ecuación de la recta es:", X1)
    print("El coeficiente X2 de su ecuación de la recta es:", X2)

    print()
    print("Para la siguiente ecuación:")
    print("Y = ({})x + ({})".format(A, B))

    Y1 = A * X1 + B
    Y2 = A * X2 + B

    print()
    print("Dados los siguientes puntos:")
    print("\tP1 ({}, {})".format(X1, Y1))
    print("\tP2 ({}, {})".format(X2, Y2))

    D = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5

    print()
    print("La distancia entre ellos es:", D)
