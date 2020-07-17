import colorsys
import pandas as pd

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 6,
                   'B' : ['A', 'B', 'C'] * 8,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                   'D' : np.random.randn(24),
                   'E' : np.random.randn(24)})









"""
num = 5
listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
"""
