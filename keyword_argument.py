def details(**kwargs):
    print(kwargs)
    print(kwargs.items())
    print(type(kwargs))
details(name="nishan", age=22, city="POkhara")
details(name="GU", estd=2019)