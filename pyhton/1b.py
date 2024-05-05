
import matplotlib.pyplot as plt
left = [1,2,3,4,5]
height = [600,4000,2000,1500,700]
tick_label=['clothing','Food','Rent','Petrol','Misc']
plt.bar (left,height,tick_label = tick_label,width = 0.8 ,color = ['green','red'])
plt.xlabel('Item')
plt.ylabel('Expenditure')
plt. show()