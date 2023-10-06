import numpy as np

def gamma_correction_one_channel(img, gamma):
    img = np.double(img)  # Conversión tipo de dato
    img = img / 255  # Cambio de rango de 0 a 1
    img = np.power(img, gamma)  # Transformación gamma
    img = img * 255  # Regresamos a rango 0 a 255
    img = np.uint8(img)  # Regresamos a tipo de dato uint8
    return img


def filtrado_local(matriz):
    rows, cols = matriz.shape
    matriz_gradiente = matriz.copy()
    #matriz de unos multiplicados por 1/9
    kernel = np.ones((3,3)) * (1/9)
    local = np.zeros((3,3))
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            local = matriz[range(row-1,row+2), range(col-1,col+2)]

            matriz_gradiente[row, col] = np.sum(kernel * local)

    matriz_gradiente = np.uint8((matriz_gradiente + 255)/2)
    return matriz_gradiente
