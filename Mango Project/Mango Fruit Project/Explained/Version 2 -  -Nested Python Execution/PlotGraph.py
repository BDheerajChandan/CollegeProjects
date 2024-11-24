import matplotlib.pyplot as plt
import ArrayNumLimit
l=ArrayNumLimit.n()
print(l)

plt.title("Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.bar([i for i in range(len(l))],l,color="red")
plt.plot(l,'x',color="Black")
plt.plot(l)
def plotG():
    return plt.show()