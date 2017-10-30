
# coding: utf-8

# In[1]:

import numpy as np
import numpy.linalg as LA


# In[ ]:

VzRange = np.linspace(0,2,50);
fig = plt.figure( figsize = (6,4));
ax = fig.add_subplot(1,1,1);
for Vz in VzRange:
    NSN_dict['Vz'] = Vz;
    H = hamRing(NSN_dict);
    energies, wfs = LA.eigh(H);
    ax.scatter(Vz*np.ones(len(energies)), energies);
ax.set_xlim([0,2]);
ax.set_ylim([-1.5, 1.5]);
fig.show();


# In[ ]:



