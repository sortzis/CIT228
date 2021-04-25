import matplotlib.pyplot as plt

cubed = []
inputVal = [1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num)
ax1 = plt.subplot(1,2,1)
ax1.plot(inputVal,cubed, marker="o",c="red",lw="2.0",ls="--")
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()

squared = []
inputVal = [1,2,3,4,5]
for num in inputVal:
    squared.append(num*num)
ax2 = plt.subplot(1,2,2)
plt.style.use("seaborn-dark-palette")
ax2.plot(inputVal,squared, marker="*",c="orange",lw="2.0",ls="--")
plt.title("Squared Numbers")
plt.ylabel("Values Squared")
plt.xlabel("Input Values")
plt.grid()

plt.suptitle("Fun with Numbers",c="green",fontsize="18",fontfamily="Comic Sans MS")
plt.subplots_adjust(top=.8,wspace=1)
plt.show()