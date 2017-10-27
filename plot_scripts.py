
# coding: utf-8

# In[ ]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']});
rc('text', usetex = True);



# In[ ]:

fontsize = fs;
fig = plt.figure(figsize = (10,4));

fig.add_subplot(1, 2, 1);
plt.scatter(ZRange, Gammas, c='red');
plt.plot(ZRange, 0.45/np.array(ZRange)**2, '--', color = 'red', label = '$\Gamma\ \propto\ 1/Z^2$')
lgd = plt.legend(fontsize = fs)

plt.xscale('log');
plt.xlim([0.1, 45]);
plt.xlabel(r'$Z$', fontsize = fs);
plt.xticks([0.1, 1, 10], fontsize = fs);

plt.yscale('log');
plt.ylim([0.0001, 0.1]);
plt.ylabel(r'$\Gamma/\Delta_0$', fontsize = fs);
plt.yticks([1e-4, 1e-3, 1e-2, 0.1, 1], fontsize = fs);

plt.title('log-log plot', fontsize = fs);
plt.text(0.2, 0.3, '(a)', fontsize = fs)


fig.add_subplot(1, 2, 2);
plt.scatter(ZRange, Gammas, c='red');
plt.plot(Zs, 0.45/Zs**2, '--', color = 'red', label = '$\Gamma\ \propto\ 1/Z^2$')
lgd = plt.legend(fontsize = fs)

plt.xlabel(r'$Z$', fontsize = fs);
plt.xticks([0, 10, 20, 30, 40], fontsize = fs)
plt.xlim([-2, 42]);

plt.ylabel(r'$\Gamma/\Delta_0$', fontsize = fs);
plt.yticks([0, 0.05, 0.1], fontsize = fs);
plt.ylim([-0.01, 0.1])

plt.title('linear plot', fontsize = fs);
plt.text(7, 0.085, '(b)', fontsize = fs);

plt.tight_layout();

#fig.savefig('gammOverZ_ABS.pdf', bbox_extra_artists = (lgd, ), bbox_inches = 'tight');

plt.show();


# In[ ]:




# In[ ]:

fs = 15; 
fig = plt.figure(figsize=(8, 3)); 

gcp = plt.pcolormesh(VzRange, vols, g.transpose(), cmap = cm.coolwarm, vmin = 0, vmax = 3.0);

plt.xticks(range(4), fontsize = fs); 
plt.xlabel(r'$V_Z$ (meV)', fontsize = fs); 
plt.xlim([0, 3]);

plt.yticks([-1, 0, 1], fontsize = fs); 
plt.ylabel(r'$V$ (mV)', fontsize = fs); 
plt.ylim([-1.5, 1.5]);

plt.title(r'$G\ (e^2/h)$',fontsize=fs)
cbar = fig.colorbar(gcp, ticks = range(5)); 
cbar.ax.tick_params(labelsize=fs)
plt.text(2.7, 1.6, '(a)', fontsize = fs);


fig.add_subplot(1, 2, 2);
Nzerobias = (voltageNumber - 1)/2;
plt.plot(VzRange, g[:, Nzerobias]);

plt.xticks(range(4), fontsize = fs); 
plt.xlabel(r'$V_Z$ (meV)', fontsize = fs); 
plt.xlim([0, 3]); 

plt.yticks(range(5), fontsize = fs); 
plt.ylabel(r'$G_S$ ($e^2/h$)', fontsize = fs); 
plt.ylim([0, 4]);

plt.title(r'Conductance at zero bias',fontsize=fs)
plt.text(2.7, 4.2, '(b)', fontsize = fs)

fig.tight_layout()

#fig.savefig('haha.png', dpi = 200);

plt.show()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



