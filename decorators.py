def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        if not func(input_text):
            raise ValueError("Input must be positive value")
        print('함수 끝!')
    return decorated


def check_integer(func):
    def decorated(width, height):
        if width >=0 and height >= 0:
            return func(width,height)
        else:
            raise ValueError("Input must be positive value")
    return decorated

def login_required(func):
    def decorated():
        func()
    return decorated

@check_integer
def rect_area(width, height):
    return(width*height)

@check_integer
def tri_area(width, height):
    return(width*height*0.5)

@decorator
def hello_world(input_text):
    print(input_text)

@decorator
def triangle(x):
    if x <= 0:
        return 0
    print("한변의 길이가 {}인 정삼각형의 넓이 :".format(x), round((3**0.5)*(x**2)/4,2))
    return 1
@decorator
def square(x):
    if x <= 0:
        return 0
    print("한변의 길이가 {}인 정사각형의 넓이 :".format(x), x**2)
    return 1

hello_world('Hello World!')

triangle(-1)

square(2)

rect_area(10,2)

tri_area(-4,3)


def check_integer(func):
    def decorated(user, width, height):
        if width >=0 and height >= 0:
            return func(user, width,height)
        else:
            raise ValueError("Input must be positive value")
    return decorated

class User:
    def __init__(self, auth):
        self.is_authenticated = auth

user = User(auth=False)

r_area = rect_area(user, 10,10)