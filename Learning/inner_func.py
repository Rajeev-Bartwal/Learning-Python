def outer():
    print("in outer")

    def inner(x):
        print("in inner",x)
    return inner


somthing = outer()
somthing(5)

