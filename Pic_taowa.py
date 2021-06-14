from PIL import Image

def fill_img_with_img(imgParent, imgChild):
	imgSize = (imgParent.width * imgChild.width, imgParent.height * imgChild.height)
	imgRet = Image.new("L",imgSize, "white")

	for w in range(imgParent.width):
		for h in range(imgParent.height):
			if imgParent.getpixel((w, h)) < 240:
				imgRet.paste(imgChild, (w*imgChild.width, h*imgChild.height))

	return imgRet

if __name__ == '__main__':
	#读取图片
	imgParent = Image.open("imgParent.jpg")
	imgParent = imgParent.convert("L")

	imgChild = Image.open("imgChild.jpg")
	imgChild = imgChild.convert("L")

	#字套娃
	imgRet = fill_img_with_img(imgParent, imgParent)
	imgRet = fill_img_with_img(imgRet, imgChild)

	#生成图片
	imgRet.save("imgRet.jpg")
