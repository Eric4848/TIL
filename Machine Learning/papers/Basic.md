# Deep Learning Basic

## Convolution
> 학습시킬 이미지 데이터의 사이즈를 줄여 학습에 필요한 자원을 줄이고 receptive field를 크게 만들어 정확도를 올려준다.
- receptive field : 출력 레이어에 미치는 입력 뉴런들의 크기, 클수록 정확도가 높아진다.
- kernel size : Convolution할 크기, 클수록 receptive field가 커지고 정확도가 높아지지만, 물체의 경계를 잘 구분하지 못하게 된다.
    - high level feature : convolution layer를 많이 거쳐 정확도는 높지만 경계구분 취약
    - low level feature : convolution layer를 적게 거쳐 경계구분은 잘하지만 정확도 취약

## sementic vs instance segmentation

- sementic : 객체를 탐지하고 박스를 쳐준다
- instance : 객체를 탐지하고 경계선을 그어준다

## R-CNN
>Regions with Convolutional Neural Networks features

- CNN 모델을 object detection에서 활용함

## ResNet
> layer가 깊어질수록 성능이 향상되다가 다시 낮아지는 현상 발생, 이를 해결하기 위해 개발
- layer가 깊어지며 gradiant vanishing 현상이 발생하고, 이를 해결하기위해 output에 input값을 더해주어 해결하는 방식
- gradiant가 유지되어 정확도가 유지, 더 깊게 layer를 쌓을 수 있게되었다
- 연산량도 더 줄어든다

## ResNext
>Cardinality를 증가시켜 성능을 향상시킨다
- Crdinality : 채널수를 분할하는 그룹의 수
- Width : 채널 수

## momentum
> local minimum이나 saddle point에서 학습이 중단되는것을 막기 위해 이전 기울기에 크기를 고려하여 추가로 이동시키는 것
- 적절한 값 사용이 중요
- 보통 0.9를 사용

## learning rate(lr)
> 경사하강법에서의 계수
- 적절한 값 사용이 중요
- 보통 0.01을 사용