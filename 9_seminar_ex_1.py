def computation():
  xs = []
  while True:
    x = yield
    xs.append(x) 
    
    n_items = len(xs)
    var = sum( list(map(lambda x: x*x/n_items, xs)) )
    mean = sum(xs)/n_items 
    print(f'n_items:{n_items}, var:{var}, mean:{mean}')


compute = computation()
next(compute) #инициализация корутины

compute.send(1) #запросы к программе
compute.send(2)
compute.send(-1)
