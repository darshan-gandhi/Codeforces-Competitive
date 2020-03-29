import numpy as np

f = open('train.csv')
x = []
beta = [0,0,0,0,0,0,0]
beta_new = [0,0,0,0,0,0,0]
li = []
yi = []
params = []
alpha = 0.001

cnt = 0

for line in f:
    a = line.split(',')
    if(cnt == 0):
        params = a
    else:
        x.append([1.0,float(a[1]),float(a[2]),float(a[3]),float(a[4]),float(a[5]),float(a[6])])
    li.append(a)
    yi.append(float(a[7]))
    cnt+=1

#print(params)
#print(li)
#print(x)
#print((np.array(beta)[np.newaxis]).T)

def h_beta():
    return np.array(x).dot(np.array(beta)[np.newaxis].T)

y = h_beta()
#print(y)

def cost():
    s = 0.0
    m = len(x)
    for i in range(m):
        s+=(float(y[i])-yi[i])*(float(y[i])-yi[i])
        return s/(2*m)

def update():
    n = len(beta)
    for j in range(n):
        s = 0.0
        m = len(x)
        for i in range(m):
            s += (float(y[i])-yi[i])*x[i][j]
            beta_new[j] = beta[j] - (alpha*s)/m

for i in range(15):
    y = h_beta()

    cost_value = cost()
    # print(cost_value)
    update()
    #print(beta_new)
    #print(beta)
    for j in range(len(beta)):
        beta[j] = beta_new[j]

print("Beta values")
print(beta)
print("\n\nError after training")
print(cost_value)

for line in f:
    a = line.split(',')
    if(cnt == 0):
        params = a
    else:
        x.append([1.0,float(a[1]),float(a[2]),float(a[3]),float(a[4]),float(a[5]),float(a[6])])
        li.append(a)
        yi.append(float(a[7]))
        cnt+=1

print("\n\nTesting\n\n")
x = []
li = []
yi = []
cnt = 0
f = open('test.csv')
for line in f:
    a = line.split(',')
    if(cnt == 0):
        params = a
    else:
        x.append([1.0,float(a[1]),float(a[2]),float(a[3]),float(a[4]),float(a[5]),float(a[6])])
        li.append(a)
        yi.append(float(a[7]))
        cnt+=1
y = h_beta()
print("\nPointer Predicted")
print(y)
print("\nPointer Actual")
print(yi)
print("\nError")
cost_value = cost()
print(cost_value)

