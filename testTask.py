## the main test 
from imageModel import ImageModel
from matplotlib import pyplot as plt
from modesEnum import Modes

from task3Test import Task3Test

# Assign vaild paths to the following 2 variables
image1Path : str = "test.jpg"
image2Path : str = "test2.jpg"

# this format --> 'variable : variableType' is called annotation
# as you have noticed, python is not a static typed language, so many errors can happen by passing a different type than the expected one to a function
# type annotations can help you not to do this terrible mistake

test = Task3Test(image2Path, image2Path, ImageModel)
test.testMagAndPhaseMode(0.7, 0.3)
test.testRealAndImagMode(0.7, 0.3)