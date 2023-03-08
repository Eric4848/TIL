# SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation
> Encoder Decoder 사용, Encoder feature를 전달할 때 max-pooling을 할 때 사용한 index를 전달하여 un-maxpooling진행

## Encoder
> VGG16에서 FC(Fully Connected) layer를 제거하여 convolution layer들만 사용
- FC layer 제거하는 이유
    - FC layer에서 학습이 일어나서 메모리 사용이 많아진다
    - local 정보를 잃어버린다.

## Decoder
> Encoder의 대칭

## upsampling
> 기존 FCN의 skip connection 대비 메모리 효율 증가
