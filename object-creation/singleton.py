"""
In python you shouldn't use a singleton at all because python has modules
which offer most of the same functionalities and none of the problems we
mention at the end.
"""

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    def __init__(self):
        print("Creating Logger")

    def log(self, msg):
        print(msg)


class CustomLogger(Logger):
    def __init__(self):
        print("Creating Custom logger")
        super().__init__()

# they both refer to the same object with the same id 0x000;lkfas
logger = CustomLogger()
logger2 = CustomLogger()
print(logger)
print(logger2)
logger.log("Hello")
logger2.log("Helloooo")

"""
 Singletons are considered an anti-pattern for several reasons, the first is that
 singleton break object-oriented design principles because if you inherit from it
 this allows you to create multiple instances of that singleton by creating multiple
 subclasses, which shouldn't be allowed.
 Another issue is that you don't have control over creation, when you create an instance
 you don't know if it's an existing instance or a newly created one, and that leads to testing
 code is really hard, because you can't easily create a new fresh instance for each test.
 And finally singletons don't work well in multi-threaded applications due to raise condition
 where multiple threads access the not yet instantiated singleton at the same time you end up
 creating multiple instance.
"""