word_fs = 20;
number_fs = 15;

fig = plt.figure( figsize = (5.5,4) );
ax = fig.add_subplot(1,1,1); #create axes object
ax.plot(x,y);

ax.set_xlim(left=0, right=20);
ax.set_xlabel('x', {'fontsize': word_fs});
ax.set_ylim(bottom=0, top=1);
ax.set_ylabel('y', {'fontsize': word_fs});