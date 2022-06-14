import my_module

my_module.func_in_module()
#Bite code -> __pycache__ - Faster load next time

import my_module as mm
mm.func_in_module()

from my_module import func_in_module
func_in_module()

from my_module import *
func_in_module()
