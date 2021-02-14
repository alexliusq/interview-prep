def outer_scope_error():
    def inner():
        # print(x)
        try:
            x = x + 1
        except Exception as inst:
            print(inst)
            print('x is local, so x + 1 not defined')

    x = 123
    inner()

outer_scope_error()