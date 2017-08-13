# processing


sp.gold.gold(n)[source]

Generate a set of 2^n +1 Gold Codes

sp.gold.gen_gold(seq1, seq2)[source]

Function to produce a gold sequence based on two input preferred pair Maximal Length Sequences


.gauss.gaussian2(size, sigma)[source]

Returns a normalized circularly symmetric 2D gauss kernel array

f(x,y) = A.e^{-(x^2/2*sigma^2 + y^2/2*sigma^2)} where

A = 1/(2*pi*sigma^2)

as define by Wolfram Mathworld http://mathworld.wolfram.com/GaussianFunction.html

sp.gauss.fspecial_gauss(size, sigma)[source]

Function to mimic the ‘fspecial’ gaussian MATLAB function


sp.filter.cconv(x, y)[source]

Calculate the circular convolution of 1-D input numpy arrays using DFT

sp.filter.ccorr(x, y)[source]

Calculate the circular correlation of 1-D input numpy arrays using DFT
