import matplotlib.pyplot as plt
import numpy as np

#For Q1
def dist(n,d):
    pts = np.random.uniform(0,1,(n,d))

    dist = []

    for i in range(n-1):
        for k in range(i+1,n):
            dist.append(np.sqrt(np.sum([(pts[i,l]-pts[k,l])**2 for l in range(d)])))

    return dist

# For Q2A
def ecount(n,d):
    pts = np.random.uniform(0,1,(n,d))

    count = 0

    for i in range(n):
        isEdge = False
        for l in range(d): 
            if(pts[i,l] <= 0.01 or pts[i,l] >= 0.99):
                isEdge = True
                # Above lines add point to elist only if values 
                # in current dimension meet edge case requirements 
        if(isEdge == True):
            count+=1

    return count

# For Q2B
def dist3(n,d):

    pts = np.random.uniform(0,1,(n,d))

    dist = []

    for i in range(n):
        dist.append(np.sqrt(np.sum([(0.5 - pts[i,l])**2 for l in range(d)])))
        #checks point distance from center of hyper cube, or .5

    return dist

#For Q1
def getRatio(n,d):
    dlist = dist(n,d)
    R = np.amax(dlist)
    r = np.amin(dlist)
    ratio = r/R
    return ratio

# For Q2A
def getRatio2(n,d):
    Es = ecount(n,d)
    ratio = r=Es/n
    return ratio

# For Q2B
def getRatio3(n,d):
    dlist = dist3(n,d)
    toRet = []
    count1 = 0
    count2 = 0

    for i in dlist:
        count1 += 1
        if(i <= 0.5):
            count2 += 2
            toRet.append(i)
    
    return count2/count1

#For Q1
def runTrials(n,d,t):
    qofX = []
    count = 0
    for i in range(1, d+1):
        avgs = []
        for trials in range(t):
            avgs.append(getRatio(n,i))
        qofX.append(np.mean(avgs))
        count+=1
        print("New val added: %d" %(count))

    return qofX

# For Q2A
def runTrials2(n,d,t):
    qofX = []
    count = 0
    for i in range(1, d+1):
        avgs = []
        for trials in range(t):
            avgs.append(getRatio2(n,i))
        qofX.append(np.mean(avgs))
        count+=1
        print("New val added: %d" %(count))

    return qofX

# For Q2B
def runTrials3(n,d,t):
    qofX = []
    count = 0
    for i in range(1, d+1):
        avgs = []
        for trials in range(t):
            avgs.append(getRatio3(n,i))
        qofX.append(np.mean(avgs))
        count+=1
        print("New val added: %d" %(count))

    return qofX
    

def getQ1A(d):
    print("starting")
    q1b = runTrials(10, 500, 5)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(d,q1b, c = 'r', label = "N = 10")
    ax1.set_xlabel("d")
    ax1.set_ylabel("q(d)")
    plt.legend(loc='upper left')
    plt.savefig("q1a.pdf")

def getQ1B(d):
    print("starting")
    q1b = runTrials(10, 500, 5)
    print("One done")
    q1b1 = runTrials(20, 500, 5)
    print("Two done")
    q1b2 = runTrials(30, 500, 5)
    print("Three done")
    q1b3 = runTrials(40, 500, 5)
    print("Four done")
    q1b4 = runTrials(50, 500, 5)
    print("Five done")

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.scatter(d,q1b, c = 'r', label = "N = 10")
    ax1.scatter(d,q1b1, c = 'y', label = "N = 20")
    ax1.scatter(d,q1b2, c = 'm', label = "N = 30")
    ax1.scatter(d,q1b3, c = 'g', label = "N = 40")
    ax1.scatter(d,q1b4, c = 'b', label = "N = 50")

    ax1.set_xlabel("d")
    ax1.set_ylabel("q(d)")

    plt.legend(loc='upper left')

    plt.savefig("q1b.pdf")

def getQ2A(d):
    q2a = runTrials2(100, 500, 10)

    fig2 = plt.figure()
    ax1 = fig2.add_subplot(111)
    ax1.scatter(d,q2a, c = 'r', label = "Edge Point Ratios")
    ax1.set_xlabel("d")
    ax1.set_ylabel("Ratio of Edge points")
    plt.legend(loc='upper left')
    plt.savefig("q2a.pdf")

def getQ2B(d):
    q2b = runTrials3(100, 500, 10)

    fig3 = plt.figure()
    ax1 = fig3.add_subplot(111)
    ax1.scatter(d,q2b, c = 'r', label = "Hypersphere Ratios")
    ax1.set_xlabel("d")
    ax1.set_ylabel("Ratio of Points inside Hypersphere")
    plt.legend(loc='upper left')
    plt.savefig("q2b.pdf")

if __name__ == "__main__":

    d = [i for i in range(500)]

    end = False
    while (end != True):
        op = input("Enter:\n\t 1 for Q1A\n\t 2 for Q1B\n\t 3 for Q2A\n\t 4 for Q2B\n\t A for all\n\t or E to exit:\n\t ")
        if (op == '1'):
            print("Q1A...\n")
            getQ1A(d)
        elif (op == '2'):
            print("Q1B...\n")
            getQ1B(d)
        elif (op == '3'):
            print("Q2A...\n")
            getQ2A(d)
        elif (op == '4'):
            print("Q2B...\n")
            getQ2B(d)
        elif (op == 'a' or op == 'A'):
            print("All...\n")
            getQ1A(d)
            getQ1B(d)
            getQ2A(d)
            getQ2B(d)
        elif (op == 'e' or op == 'E'):
            print("Ending...\n")
            end = True

    

    
    

    
