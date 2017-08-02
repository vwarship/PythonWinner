import pytesseract
from PIL import Image


# We then applied the Tesseract program to test and evaluate the performance of the OCR engine
# on a very small set of example images.
text = pytesseract.image_to_string(Image.open('images/english_text.png'))
print(text)

# srnon-u/oao-r (J) °A
text = pytesseract.image_to_string(Image.open('images/char_number.png'))
print(text)
