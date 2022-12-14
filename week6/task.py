import numpy as np
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from PIL import Image

# 3.6.1 MNIST 이미지 확인해보기
def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# load_mnist 함수를 사용하여 훈련데이터와 학습 데이터를 가져옴
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,
    normalize=False)

img = x_train[0]  # 100번째 훈련 데이터 이미지
label = t_train[0]  # 100번째 훈련 데이터 라벨
print(label)  # 100번째 훈련 데이터 라벨 출력
print(img.shape)  # (784,), 28x28 이미지를 flatten 했기 때문
img = img.reshape(28, 28)  # 원래 이미지 모양으로 변형
print(img.shape)  # (28, 28)

img_show(img)  # 100번째 훈련 데이터 이미지 출력