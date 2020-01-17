# Imports necessários
import cv2

# Importando a imagem
image1 = cv2.imread('sudoku.jpg')

# cv2.cvtColor é aplicado na imagem (1º parametro)
# Convertendo a escala de cores de BlueGreenRed para RGB (2º parametro)
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Aplicando varios tipos de thresholds
# Todos os pixels abaixo de 120 serão setados para 255
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# Uma janela mostrará o nome com o threshold correspondente
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)
	
# Fechando tudo o que foi aberto
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
