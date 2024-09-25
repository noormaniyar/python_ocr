import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Update with the correct path

image_path = 'media/1.jpg'
image = Image.open(image_path)
text = pytesseract.image_to_string(image)

print(text)




























# import pytesseract
# from PIL import Image

# # pytesseract.pytesseract.tesseract_cmd = '/home/ewayprint/projects/python_ocr/venv'

# def extract_text_from_image(image_path):
#     print("-------------extract_text_from_image-----------------")
#     image = Image.open(image_path)
#     print(image, "-----------------------image------------------")
#     text = pytesseract.image_to_string(image)
#     print(text, "---------------------text--------------------")
#     return text

# file1_path = 'media/file1.jpeg'
# file2_path = 'media/file2.jpeg'

# file1_text = extract_text_from_image(file1_path)
# file2_text = extract_text_from_image(file2_path)



# def compare_text(text1, text2):
#     print("------------------compare_text------------------")
#     text1 = text1.lower()
#     text2 = text2.lower()
#     same_count = sum(1 for word in text1.split() if word in text2.split())
#     total_words = max(len(text1.split()), len(text2.split()))
#     percentage_same = (same_count / total_words) * 100
#     percentage_different = 100 - percentage_same
#     return percentage_same, percentage_different

# percentage_same, percentage_different = compare_text(file1_text, file2_text)


# print(f"Percentage of same content: {percentage_same}%")
# print(f"Percentage of different content: {percentage_different}%")
