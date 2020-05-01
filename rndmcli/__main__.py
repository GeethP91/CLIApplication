import sys
import random
#from .classmodule import MyClass
#from .funcmodule import my_function
def main():
    print('Random List')
    rndm_list= list(range(0,10))
    random.shuffle(rndm_list)
    print(rndm_list)
if __name__ == '__main__':
    main()


