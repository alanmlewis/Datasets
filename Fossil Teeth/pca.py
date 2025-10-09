import numpy as np

data = np.loadtxt('allteeth.csv',skiprows=1,delimiter=',')
data = data[-88:,1:]

covar = np.cov(data.T)

eigval, eigvec = np.linalg.eigh(covar)

tot_var = sum(eigval)
print(eigval/tot_var)

data_pca = np.matmul(data,eigvec[:,-2:])

unit_vecs = np.matmul(np.eye(9)*0.5,eigvec[:,-2:])

unit_vecs[:,1] -= 2.0

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"] = (6,4.5)
plt.rcParams["figure.dpi"] = 200

plt.scatter(data_pca[:,1],data_pca[:,0],marker = 'X',s=100)
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.tight_layout()
plt.savefig('PCA.png')

#plt.annotate("LENGTH", xy=(-2, 0), xytext=(unit_vecs[0,1]-2,unit_vecs[0,0]), arrowprops=dict(arrowstyle="->"))
plt.plot(-2,0)
plt.plot([-2,unit_vecs[0,1]],[0,unit_vecs[0,0]],label='LENGTH',linewidth=3)
plt.legend()
plt.tight_layout()
plt.savefig('PCA_length.png')

plt.plot([-2,unit_vecs[1,1]],[0,unit_vecs[1,0]],label='WIDTH',linewidth=3)
plt.legend()
plt.tight_layout()
plt.savefig('PCA_length_width.png')

plt.plot([-2,unit_vecs[2,1]],[0,unit_vecs[2,0]],label='TRILENGTH',linewidth=3)
plt.legend()
plt.tight_layout()
plt.savefig('PCA_trilength.png')
