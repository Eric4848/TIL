# ParseNet: Looking Wider to See better
> global information 고려해야한다 -> global average pooling을 이용하여 global information을 담고있는 feature를 기존 feature와 합쳐 사용

## proposed method
### 1. Global Pooling
> network의 convolution layer를 거쳐 나온 feature map을 이용, 영상 전체 정보를 담기 위한 모듈
- 1X1 feature map을 만든다

### 2. L2 Norm
> feature map과 1.의 global feature에 대해 L2 normalize를 진행
- feature크기를 0~1사이로 맞춘다

### 3. UnPool
> Normalize한 global feature를 feature map과 동일한 크기로 바꾸는 과정
- 1X1 global feature vector를 spacial size에 맞게 복사하여 구성

### 4. Concat
> feature map과 global feature map을 채널 축 기반으로 concat하여 하나로 합치고 1X1 convolution으로 채널을 줄인다.
- pytorch의 경우 torch.nn.AvgPool2d 사용

## Conclusion
> FCN에 global information feature를 추가함으로서 성능을 향상시켰다.