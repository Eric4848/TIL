# pytorch
## pytorch의 구성요소
- torch: 메인 네임스페이스, 텐서 등 수학함수 포함
- torch.autograd: 자동미분 라이브러리
- torch.nn: 신경만 구축을 위한 데이터 구조, 레이으 등의 라이브러리
- torch.multiprocessing: 병렬처리 라이브러리
- torch.optim: SGD를 중심으로 한 파라미터 최적화 알고리즘 제공
- torch.utils: 유틸리티 기능
- torch.onnx: 다른 프레임워크간 모델 공유

## Tensor

- 데이터 표현의 기본 구조
- 텐서는 데이터를 담는 컨테이너, 수치형 데이터 저장
- Numpy의 ndarray와 유사
- GPU를 사용한 연산 가속 가능

```python
import torch

torch.__version__
```

```python
x = torch.empty(4,2)
print(x)
```