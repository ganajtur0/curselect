# this is to test if the __del__ method is working or not

import curselect

menu = curselect.CurSelect("we won't end up activating this menu".split(' '))
print(menu) # just print the object so __init__ gets called on it
print("Hello World!")
