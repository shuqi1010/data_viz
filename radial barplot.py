import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['axes.labelsize'] = 10



PATH = r'processed_data_p1.csv'
data = pd.read_csv(PATH)
data.head()
limit = len(data) - 1




N = 327
# Fixing random state for reproducibility


# Compute pie slices
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
width = (2*np.pi) / (N+200)

radii_p1 = 10 * data.iloc[:,5]
colors_p1 = plt.cm.viridis(radii_p1 / 200.)

radii_p2 = 10 * data.iloc[:,7]
colors_p2 = plt.cm.viridis(radii_p2 / 200.)

radii_cover = 10 * data.iloc[:,8]
radii_change = 10* data.iloc[:,9]
colors_change = plt.cm.viridis(radii_change / 40.)
#fig = plt.figure(figsize=(10,10))
#step one
#ax_p1 = plt.subplot(111, projection='polar')
#ax_p1.bar(theta, radii_p1, width=width, bottom=0.0, color=colors_p1, alpha=0.5)
#step two
#ax_p2 = plt.subplot(111, projection='polar')
#ax_p2.bar(theta, radii_p2, width=width, bottom=0.0, color=colors_p2, alpha=0.5)
#step three
#ax_cover = plt.subplot(111, projection='polar')
#ax_cover.bar(theta, radii_cover, width=width+0.01, bottom=0.0, color='white', alpha=1)
#step four
ax_change = plt.subplot(111, projection='polar')
ax_change.bar(theta, radii_change, width=width+0.01, bottom=80.0, color= colors_change, alpha=1)

#ax = fig.add_axes([0.1, 0.1, 0.75, 0.75], polar=True)
#arrCnts = np.array(data.iloc[:,1])
#bars = ax_p1.bar(theta, arrCnts, width=0.0, bottom=0.0)
#plt.axis('off')

#rotations = np.rad2deg(theta)
#for x, bar, rotation, label in zip(theta, bars, rotations, data.iloc[:,1]):
#    lab = ax_p1.text(x,120 , label, 
#             ha='left', va='center', rotation=rotation, rotation_mode="anchor", fontsize = 0.5)   


plt.show()





