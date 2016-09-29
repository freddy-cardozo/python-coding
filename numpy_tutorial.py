import numpy as np
from pdb import set_trace as st

def arrayCreation():
    if sub_choice==1:
        print "Syntax: arange([start,] stop[, step,], dtype=None) \n"
        print "--- EXAMPLES ----\n\n"
        print ('{} => {}'.format('np.arange(3)', np.arange(3)))
        print ('{} => {}'.format('np.arange(3.0)', np.arange(3.0)))
        print ('{} => {}'.format('np.arange(3,7)', np.arange(3,7)))
        print ('{} => {}'.format('np.arange(3,7,2)', np.arange(3,7,2)))
        print ('{} => {}'.format('np.arange(3,7,2)', np.arange(0.5, 10.4, 0.8, int)))
    if sub_choice==2:
        print "Syntax: numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0) \n"
        print "--- EXAMPLES ----\n\n"
        print ('{} => {}'.format('np.array([1, 2, 3])', np.array([1, 2, 3])))
        print ('{} => {}'.format('np.array([1, 2, 3.0]))', np.array([1, 2, 3.0])))
        print ('{} => {}'.format('np.array([[1, 2], [3, 4]])))', np.array([[1, 2], [3, 4]])))
        print ('{} => {}'.format('np.array([1, 2, 3], ndmin=2))))', np.array([[1, 2], [3, 4]])))
        print ('{} => {}'.format('np.array([1, 2, 3, 4, 5, 6, 7, 8 , 9], ndmin=9))))', np.array([[1, 2], [3, 4]])))
        print ('{} => {}'.format("np.array(np.mat('1 2; 3 4')))", np.array([[1, 2], [3, 4]])))
        print ('{} => {}'.format("np.array(np.mat('1 2; 3 4'), subok=True)", np.array(np.mat('1 2; 3 4'), subok=True)))
    if sub_choice==3:
        print "Syntax: numpy.copy(a, order='K')\n"
        print "--- EXAMPLES ----\n\n"
        print ('{} => {}'.format('np.copy([1, 2, 3])', np.copy([1, 2, 3])))
    if sub_choice==4:
        print "Syntax: numpy.empty(shape, dtype=float, order='C')\n"
        print " Return a new array of given shape and type, without initializing entries."
        print "--- EXAMPLES ----\n\n"
        print ('{} => {}'.format('np.empty([2, 2])', np.empty([2, 2])))
        print ('{} => {}'.format('np.empty((2, 2))', np.empty((2, 2))))
        print ('{} => {}'.format('np.empty((3, 3))', np.empty((3, 3))))
    if sub_choice==4:
        print "Syntax: numpy.empty_like(a, dtype=None, order='K', subok=True)\n"
        print " Return a new array with the same shape and type as a given array."
        print "--- EXAMPLES ----\n\n"
        a = [1, 2, 3, 4]
        print ('{} => {}'.format('a = [1, 2, 3, 4] np.empty_like(a)', np.empty_like(a)))
    if sub_choice==5:
        print "Syntax: numpy.eye(N, M=None, k=0, dtype=<type 'float'>)[source]\n"
        print "Return a 2-D array with ones on the diagonal and zeros elsewhere."
        print "--- EXAMPLES ----\n\n"
        print ('{} => {}'.format('np.eye(2, dtype=int)', np.eye(2, dtype=int)))
        print ('{} => {}'.format('np.eye(3, k = 1)', np.eye(3, k=1)))
    if sub_choice==6:
        print "Syntax: numpy.identity(n, dtype=None)\n"
        print "Return the identity array. \nThe identity array is a square array with ones on the main diagonal.\n"
        print ('{} => {}'.format('np.identity(3)', np.identity(3)))
    if sub_choice==7:
        print "Syntax: numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)\n"
        print "Return evenly spaced numbers over a specified interval.Returns num evenly spaced samples, calculated over the interval [start, stop].\n"
        print ('{} => {}'.format('np.linspace(2.0, 3.0, num=5)', np.linspace(2.0, 3.0, num=5)))
        print ('{} => {}'.format('np.linspace(2.0, 3.0, num=5, endpoint=False)', np.linspace(2.0, 3.0, num=5, retstep=True)))
    if sub_choice==8:
        print "Syntax: numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)[source]\n"
        print "Return numbers spaced evenly on a log scale. In linear space, the sequence starts at base ** start (base to the power of start) and ends with base ** stop (see endpoint below).\n"
        print ('{} => {}'.format('np.logspace(2.0, 3.0, num=4)', np.logspace(2.0, 3.0, num=4)))
        print ('{} => {}'.format('np.logspace(2.0, 3.0, num=4, endpoint=False)', np.logspace(2.0, 3.0, num=4, endpoint=False)))
        print ('{} => {}'.format('np.logspace(2.0, 3.0, num=4, base=2.0)', np.logspace(2.0, 3.0, num=4, base=2.0)))
    if sub_choice==9:
        print "Syntax: numpy.zeros(shape, dtype=float, order='C')\n"
        print "Return a new array of given shape and type, filled with zeros..\n"
        print ('{} => {}'.format('np.zeros(5)', eval('np.zeros(5)')))
        print ('{} => {}'.format('np.zeros((5,), dtype=np.int)', np.zeros((5,), dtype=np.int)))
        print ('{} => {}'.format('np.zeros((2, 1))', np.zeros((2, 1))))
        s=(2, 2)
        print ('{} => {}'.format('s = (2,2) np.zeros(s)', np.zeros(s)))

main_menu = {
        1: "Array creation"
      }

sub_menu = {
    1:['arange', 'array', 'copy', 'empty', 'empty_like', 'eye', 'identity', 'linspace', 'logspace', 'mgrid', 'ogrid', 'ones', 'ones_like', 'fromfunction', 'fromfile']
    }

main_choice = int(raw_input('''Enter your main choice : 
 {}\n'''.format('\n'.join(['{}:{} '.format(k,v) for k, v in  main_menu.items()]))))
 
sub_choice = int(raw_input('''Enter your sub choice \n : {}\n '''.format('\n'.join(['{}:{} '.format(k,v) for k, v in  enumerate(sub_menu[main_choice])]))))

if (main_choice == 1):
    arrayCreation()

