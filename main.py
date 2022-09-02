import random
from collections import namedtuple, deque, OrderedDict, Counter, defaultdict
from itertools import chain, groupby, product, permutations
from functools import cache, lru_cache, partial

Person = namedtuple('Person', ['name', 'age'], defaults=[20])
print('---namedtuple---')
print(Person('Test'))
person = Person('Bob', 30)
print(person.name, person.age)
print(person._asdict())
print('---namedtuple---')

print('---deque---')
dq = deque(maxlen=3)
dq.extend([Person('Bob1', 30), Person('Bob2', 30), Person('Bob3', 30), Person('Bob4', 30)])
print(dq)
dq.appendleft(Person('Bob0', 30))
print(dq)
print('---deque---')
print('---Counter---')
dq.appendleft(Person('Bob0', 30))
cnt = Counter(dq)
print(cnt.total())
print(cnt.most_common(3))
print('---Counter---')
print('---OrderedDict---')


def my_cache_decor(size=4):
    values = OrderedDict()

    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if (args, tuple(kwargs.items())) in values:
                print('cached value')
                return values[(args, tuple(kwargs.items()))]

            result = func(*args, **kwargs)
            values[(args, tuple(kwargs.items()))] = result
            if len(values) > size:
                print('del')
                values.popitem(last=False)
            return result

        return inner_wrapper

    return wrapper


@my_cache_decor()
def test(*args, **kwargs):
    return 42


print(test(1, a=1))
print(test(1, a=1))
print(test(a=3))
print(test(a=4))
print(test(a=5))
print(test(a=6))
print('---OrderedDict---')
print('---defaultdict---')


def factory(a, b):
    return lambda: random.randint(a, b)


dd = defaultdict(factory(1, 5))
print(dd['1'])
print(dd['2'])
print(dd['3'])
print(dd['4'])
print('---defaultdict---')
print('---chain---')
print(list(chain('ABC', 'ABC')))
print(list(chain('ABC', ['ABC'])))
print(list(chain.from_iterable(['ABC', 'ABC'])))
print('---chain---')
print('---groupby---')
kfunc = lambda y: y % 2 == 0
num_list = [x for x in range(10)]
num_list = sorted(num_list, key=kfunc, reverse=True)
groups = [list(y) for x, y in groupby(num_list, key=kfunc)]
print(groups)
print('---groupby---')
print('---product---')
y = ['0', '1']
print(list(product(y, repeat=3)))
print('---product---')
print('---permutations---')
yy = ['0', '1']
print(list(permutations('ABCDd', 4)))
print('---permutations---')
print('---partial---')


def test_partial_func(a, b, c, d=0):
    print(a, b, c, d)


test_partial_func(1, 2, 3, 4)
new_func = partial(test_partial_func, 5, c=10, b=40)
new_func(d=14)
print('---partial---')
print('---cache---')


@cache
def test_cache(a):
    res = 0
    for i in range(a):
        res += 1
    return res


print(test_cache(100000000))
print(test_cache(100000000))

print('---cache---')

print('---lru_cache---')


@lru_cache(maxsize=4)
def test_lru_cache(a):
    res = 0
    for i in range(a):
        res += 1
    return res


print(test_lru_cache(100000001))
print(test_lru_cache(100000002))
print(test_lru_cache(100000002))
print(test_lru_cache(100000003))
print(test_lru_cache(100000004))
print(test_lru_cache(100000000))
print(test_lru_cache(100000001))

print('---lru_cache---')

