from numpy import *
from scipy.signal import *
from pylab import * 
import matplotlib.pyplot as plt

w = logspace(-2,2,100) # creating array of evenly spaced samples of log(w)

#part b -> k =1
b = [1] # numerator coefficients 
a = [1,1,1] #demoninator coefficients 
H1 = freqs(b,a,w)
print(a)
print(H1)

#part c-> k = .09 and k =4
d = [.09] #numerator coefficients when k = 0.09
c = [1,.424,.09] #denominator coefficients when k = .09

f = [4] #denominator coefficients when k = 4
e = [1,2.82,4] #demoninator coefficients when k = 4

H2 = freqs(d,c,w) #frequency of k = .09
H3 = freqs(f,e,w) #frequency of k = 4

#part d
basex = 10
basey = 10
plt.subplot(2,1,1)
plt.xlabel('log w') #labels log w axis
plt.ylabel('20log H(jw)') # labels power axis
loglog(w, abs(H1[1])**20,'ro',basex,basey,w,abs(H2[1])**20,'b^',basex,basey,w,abs(H3[1])**20,'g--',basex,basey) 
#creates layered Bode plot for H1 (red),H2 (blue), and H3(green)

print('done')

#part e 
t = linspace(0,30)
h1t = step2((b,a),T=t)  #h1(t)response for H1(jw)
h2t = step2((d,c),T=t)  #h2(t) response for H2(jw)
h3t = step2((f,e),T=t)  #h3(t) response for H3(jw)
plt.figure(2) #creates seperate figure
plt.subplot(2,1,1)
plt.xlabel('time (s)') #label time axis
plt.ylabel('h(t)') #label h(t) axis
plt.plot(t, h1t[1], 'r--', t, h2t[1], 'b--', t, h3t[1], 'g--')
plt.show()