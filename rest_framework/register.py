from models.models import *
import inspect
import sys


class ClassDecorator(object):
    def __init__(self, models_list=None):
        self.ml = models_list or 'models_list'
    def __call__(self, cls):
        class Wrapped(cls):
            if not self.ml in globals():
                globals()[self.ml] = []
            globals()[self.ml].append(cls.__name__)
        return Wrapped
    ''' 
	@ClassDecorator()
	class BB(BaseModel):                   
	    def b(self):
	        return 1
    '''

register_models = [i for i, j in globals().copy().items() if inspect.isclass(j) and j.__mro__[1].__name__ == 'BaseModel']
objects = {model: getattr(sys.modules[__name__], model) for model in register_models} # objects = {'Song': Song}


if __name__ == '__main__':
    print(objects)