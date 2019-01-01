Реализуйте метакласс `InstanceSemaphore`, который следил бы за количеством инстансов классов, использующих его.
Количество инстансов указывается в свойстве класса `__max_instance_count__`.

Обратите внимание, что число объектов каждого класса регулируется отдельно.

Пример:
```python
class A(metaclass=InstanceSemaphore):
    __max_instance_count__ = 2

class B(metaclass=InstanceSemaphore):
    __max_instance_count__ = 1

a_one = A('one')
a_two = A('two')
b_one = B('one')
```

до этого момента всё шло гладко, а вот
```python
a_three = A('three')
```
выкинет исключение `TypeError`

Для простоты считайте что все инстансы живут вечно в однопоточном мире.
