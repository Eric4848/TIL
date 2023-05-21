# Django

## object filter에서의 부등호

> filter에서 >, <등의 부등호 사용이 불가능하다 따라서 `__`(2개)를 붙여 부등호를 대신한다

- lt == <
- gt == >
- lte == <=
- gte == >=

```python
[db명].filter([column명]__lt = [조건])
```

> filter에서 양방향 부등호를 사용하기 위해 range를 사용한다

```python
[db명].filter([column명]__range = [작은조건, 큰조건])
```

## models(table) join
