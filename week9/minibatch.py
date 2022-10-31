import sys
import os
import numpy as np
from dataset.mnist import load_mnist
import matplotlib.pyplot as plt
sys.path.append(os.pardir)


(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

minibatch = np.random.choice(60000, 10)
print(minibatch)

minibatch_data = x_train[minibatch]
print(minibatch_data.shape)

# minibatch 학습 데이터 시각화
fig, ax = plt.subplots(1, 10)
for i in range(10):
    tmp = x_train[minibatch[i]]
    tmp_img = tmp.reshape(28, 28)
    ax[i].imshow(tmp_img)
    ax[i].axis('off')
    ax[i].set_title(str(minibatch[i]))

plt.tight_layout()
plt.show()
