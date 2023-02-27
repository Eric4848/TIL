# FCN(Fully Convolutional Networks for Semantic Segmentation)

## Convolutionalization
> 모든 layer를 convolutional layer로 구성
- 위치정보를 기억

## Upsampling(Deconvolution)
> pooling 시 줄어드는 이미지 사이즈를 원래 사이즈로 만들기 위해 적절한 값을 적용한다
- pooling 시 receptive field가 넓어져 더 많은 주변 요소를 사용할 수 있다.
- 하지만 정답과 비교를 위해 원래 사이즈로 맞춰야 해서 upsampling 사용

### bilinear interpolation
> linear interpolation을 가로,세로 두번 적용한다
- bilinear interpolation만 사용 시 경계 구분이 힘들고 대체로 smooth한 결과만 나온다

## Skip connection architecture
> 전 단계의 pooling 결과를 upscale한 값과 같이 사용하여 detail정보를 보완하는 방식
