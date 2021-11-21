from PIL import Image
import numpy as np

k = 1                         ####коэффициент контрастности (0: 1]

file_names = ['lunar01_raw.jpg', 'lunar02_raw.jpg', 'lunar03_raw.jpg']
result_numbers = [i+1 for i in range(len(file_names))]


for file_name, i in zip(file_names, result_numbers):
    img = Image.open(file_name)
    data = np.array(img)

    mn = data.min()
    mx = data.max()

    data = k*(255/(mx-mn))*(data - mn)
    data = data.astype('uint8')

    res_img = Image.fromarray(data)
    res_img.save('result'+str(i)+'.jpg')


