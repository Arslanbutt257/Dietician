import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from .apps import DeiticianConfig


data = DeiticianConfig.data
Breakfastdata = data['Breakfast']
BreakfastdataNumpy = Breakfastdata.to_numpy()

Lunchdata = data['Lunch']
LunchdataNumpy = Lunchdata.to_numpy()

Dinnerdata = data['Dinner']
DinnerdataNumpy = Dinnerdata.to_numpy()
Food_itemsdata = data['Food_items']



def suggestions(inputs):
    breakfastfoodseparated = []
    Lunchfoodseparated = []
    Dinnerfoodseparated = []

    breakfastfoodseparatedID = []
    LunchfoodseparatedID = []
    DinnerfoodseparatedID = []

    for i in range(len(Breakfastdata)):
        if BreakfastdataNumpy[i] == 1:
            breakfastfoodseparated.append(Food_itemsdata[i])
            breakfastfoodseparatedID.append(i)
        if LunchdataNumpy[i] == 1:
            Lunchfoodseparated.append(Food_itemsdata[i])
            LunchfoodseparatedID.append(i)
        if DinnerdataNumpy[i] == 1:
            Dinnerfoodseparated.append(Food_itemsdata[i])
            DinnerfoodseparatedID.append(i)

    # retrieving Lunch data rows by loc method |
    LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T
    # print(LunchfoodseparatedIDdata)
    val = list(np.arange(5, 15))
    Valapnd = [0] + val
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.iloc[Valapnd]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T
    # print(LunchfoodseparatedIDdata)

    # retrieving Breafast data rows by loc method 
    breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    Valapnd = [0] + val
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.iloc[Valapnd]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T

    # retrieving Dinner Data rows by loc method 
    DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    Valapnd = [0] + val
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.iloc[Valapnd]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T

    # calculating BMI
    age = int(inputs[0])
    veg = int(inputs[1])
    weight = float(inputs[2])
    height = float(inputs[3])
    bmi = weight / ((height / 100) ** 2)
    agewiseinp = 0

    for lp in range(0, 80, 20):
        test_list = np.arange(lp, lp + 20)
        for i in test_list:
            if (i == age):
                tr = round(lp / 20)
                agecl = round(lp / 20)

                # conditions
    k = ''
    result = {}
    if (bmi < 16):
        result['bmi'] = bmi
        result['bmi_msg'] = "Acoording to your BMI, you are Severely Underweight"
        clbmi = 4
        k = 'wg'
    elif (bmi >= 16 and bmi < 18.5):
        result['bmi'] = bmi
        result['bmi_msg'] = "Acoording to your BMI, you are Underweight"
        clbmi = 3
        k = 'wg'
    elif (bmi >= 18.5 and bmi < 25):
        result['bmi'] = bmi
        result['bmi_msg'] = "Acoording to your BMI, you are Healthy"
        clbmi = 2
        k = 'h'
    elif (bmi >= 25 and bmi < 30):
        result['bmi'] = bmi
        result['bmi_msg'] = "Acoording to your BMI, you are Overweight"
        clbmi = 1
        k = 'wl'
    elif (bmi >= 30):
        result['bmi'] = bmi
        result['bmi_msg'] = "Acoording to your BMI, you are Severely Overweight"
        clbmi = 0
        k = 'wl'

    # converting into numpy array
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.to_numpy()
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.to_numpy()
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.to_numpy()
    ti = (clbmi + agecl) / 2

    ## K-Means Based  Dinner Food
    Datacalorie = DinnerfoodseparatedIDdata[1:, 1:len(DinnerfoodseparatedIDdata)]

    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

    XValu = np.arange(0, len(kmeans.labels_))

    # retrieving the labels for dinner food
    dnrlbl = kmeans.labels_

    ## K-Means Based  lunch Food
    Datacalorie = LunchfoodseparatedIDdata[1:, 1:len(LunchfoodseparatedIDdata)]

    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

    XValu = np.arange(0, len(kmeans.labels_))

    # retrieving the labels for lunch food
    lnchlbl = kmeans.labels_

    ## K-Means Based  lunch Food
    Datacalorie = breakfastfoodseparatedIDdata[1:, 1:len(breakfastfoodseparatedIDdata)]

    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

    XValu = np.arange(0, len(kmeans.labels_))

    # retrieving the labels for breakfast food
    brklbl = kmeans.labels_

    inp = []
    ## Reading of the Dataet
    datafin = DeiticianConfig.datafin

    ## train set
    dataTog = datafin.T
    bmicls = [0, 1, 2, 3, 4]
    agecls = [0, 1, 2, 3, 4]
    weightlosscat = dataTog.iloc[[1, 2, 7, 8]]
    weightlosscat = weightlosscat.T
    weightgaincat = dataTog.iloc[[0, 1, 2, 3, 4, 7, 9, 10]]
    weightgaincat = weightgaincat.T
    healthycat = dataTog.iloc[[1, 2, 3, 4, 6, 7, 9]]
    healthycat = healthycat.T
    weightlosscatDdata = weightlosscat.to_numpy()
    weightgaincatDdata = weightgaincat.to_numpy()
    healthycatDdata = healthycat.to_numpy()
    weightlosscat = weightlosscatDdata[1:, 0:len(weightlosscatDdata)]
    weightgaincat = weightgaincatDdata[1:, 0:len(weightgaincatDdata)]
    healthycat = healthycatDdata[1:, 0:len(healthycatDdata)]

    weightlossfin = np.zeros((len(weightlosscat) * 5, 6), dtype=np.float32)
    weightgainfin = np.zeros((len(weightgaincat) * 5, 10), dtype=np.float32)
    healthycatfin = np.zeros((len(healthycat) * 5, 9), dtype=np.float32)
    t = 0
    r = 0
    s = 0
    yt = []
    yr = []
    ys = []
    for zz in range(5):
        for jj in range(len(weightlosscat)):
            valloc = list(weightlosscat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightlossfin[t] = np.array(valloc)
            yt.append(brklbl[jj])
            t += 1
        for jj in range(len(weightgaincat)):
            valloc = list(weightgaincat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightgainfin[r] = np.array(valloc)
            yr.append(lnchlbl[jj])
            r += 1
        for jj in range(len(healthycat)):
            valloc = list(healthycat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            healthycatfin[s] = np.array(valloc)
            ys.append(dnrlbl[jj])
            s += 1

    if k == 'wl':
        X_test = np.zeros((len(weightlosscat), 6), dtype=np.float32)


        # randomforest
        for jj in range(len(weightlosscat)):
            valloc = list(weightlosscat[jj])
            valloc.append(agecl)
            valloc.append(clbmi)
            X_test[jj] = np.array(valloc) * ti

        X_train = weightlossfin  # Features
        y_train = yt  # Labels
    elif k == 'wg':
        X_test = np.zeros((len(weightgaincat), 10), dtype=np.float32)

        # In[287]:
        for jj in range(len(weightgaincat)):
            valloc = list(weightgaincat[jj])
            valloc.append(agecl)
            valloc.append(clbmi)
            X_test[jj] = np.array(valloc) * ti

        X_train = weightgainfin  # Features
        y_train = yr  # Labels
    else:
        X_test = np.zeros((len(healthycat) * 5, 9), dtype=np.float32)

        for jj in range(len(healthycat)):
            valloc = list(healthycat[jj])
            valloc.append(agecl)
            valloc.append(clbmi)
            X_test[jj] = np.array(valloc) * ti

        X_train = healthycatfin  # Features
        y_train = ys  # Labels

    # Create a Gaussian Classifier
    clf = RandomForestClassifier(n_estimators=100)

    # Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train, y_train)

    # print (X_test[1])
    X_test2 = X_test
    y_pred = clf.predict(X_test)
    suggested_foods = []
    try:
        for ii in range(len(y_pred)):
            if y_pred[ii] == 2:  # weightloss
                findata = Food_itemsdata[ii]
                suggested_foods.append(findata)
    except:
        pass
    if len(suggested_foods) < 1:
        suggested_foods.extend(Food_itemsdata[:10])
    result['Suggestions'] = suggested_foods
    return result
