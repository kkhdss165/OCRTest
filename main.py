from pororo import Pororo

# print (Pororo.available_tasks())

IMAGE_PATH = "./images/test_image.jpg"
ocr = Pororo(task="ocr", lang="ko")
print(ocr(IMAGE_PATH))