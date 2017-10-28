
# coding: utf-8


get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']});
rc('text', usetex = True);


import numpy as np
from numpy import pi



# # Plot using OOP


x = np.arange(0, 5.1, 0.1);
y1 = x;
y2 = x**2;
y3 = np.sin(x);



def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)



fig = plt.figure( figsize = (8,4), tight_layout = True );

word_fs = 20;
legend_fs = 14;
number_fs = 15;

ax1 = fig.add_subplot(1,2,1); #create axes object
ax1.plot(x, y1, linewidth=3, label='linear function' );
ax1.scatter(x, y3, c='r', edgecolors='face', label='sine function');

ax1.set_xscale('log');
ax1.set_xlim(left=0.5, right=5);
ax1.set_xticks([ pi, 3*pi/2]);
ax1.set_xlabel('time', {'fontsize': word_fs});
ax1.xaxis.set_major_formatter(plt.FuncFormatter(format_func));

ax1.set_ylim(bottom=-1.2, top=5);
ax1.set_yticks([0,2,4]);
ax1.set_ylabel('distance', {'fontsize': word_fs});

ax1.tick_params(labelsize=number_fs); #set the fontsize of ticks
ax1.legend( bbox_to_anchor=(0.66, 1), fontsize=legend_fs, shadow=True);
ax1.set_title('Simple functions', {'fontsize': word_fs} );


ax2 = fig.add_subplot(1,2,2);
ax2.plot(x,y2);
ax2.set_xticks(range(0,6) );
ax2.tick_params(labelsize=number_fs);
ax2.set_xlabel('time', {'fontsize': word_fs});
ax2.set_ylabel('distance', {'fontsize': word_fs});
ax2.set_title('$y=x^2$', {'fontsize': word_fs} );

fig.savefig('hello.pdf', dpi=300);

fig.show();




