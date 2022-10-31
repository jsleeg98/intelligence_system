# 신경망 학습
* 신경망의 적절한 weight, bias 값을 찾는 것
* 학습을 위해서는 데이터가 굉장히 많아야 한다.

## 데이터 분류
* 학습 데이터(Training Data)
* 시험 데이터(Test Data)

## 손실 함수(Loss function)
* 평균제곱오차(MSE : Mean Squared Error) 👉 회귀 문제, 분류 문제
* 교차 엔트로피 오차(CEE : Cross Entropy Error) 👉 분류 문제
* 학습은 결국 손실 함수의 값을 최소화하는 것

## 미니배치 학습(Mini Batch)
* 작은 덩어리 단위 학습
* 예를 들면 60000장의 훈련 데이터 중에서 100장을 **무작위**로 뽑아 그 100장만을 사용하여 학습하는 것

## 경사 하강법(Gradient Descent)
* 손실함수의 최소값을 찾으로 가는 방법



