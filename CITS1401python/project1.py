### UWA CITS1401 Project 1, written by Erica Kong, student ID: 24071068
### This project is aim to analyse user demographics to better understand social media usage.

# get the average of a list of numbers, return the average value
def get_avg(lst):
    sum = 0
    n = len(lst)
    for i in lst:
        sum = sum+i   # sum of list of numbers
    try:
        avg = sum/n   # average of list of numbers
    except ZeroDivisionError:  # catch ZeroDivisionError
        print("A zero division error when use get_avg()!")
        avg = 0
    return avg

# get the standard deviation of a list of numbers, return the standard deviation value
def get_stddev(lst):
    try:
        avg = get_avg(lst)  # get average of list of numbers by calling get_avg()
        n = len(lst)
        sum = 0
        for i in lst:
            sum = sum + (i-avg)**2
        stddev = (sum/(n-1))**(1/2)  
    except ZeroDivisionError:  # catch ZeroDivisionError
        print("A zero division error when use get_stddev()!")
        stddev = 0 
    return stddev

# convert a list into a list of lists, return a list of lists
def list_to_listOfLists(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
    return res

# main function, return four variables
def main(csvfile, age_group, country): 
    with open(csvfile, "r") as Fopen:  #open file
        data = Fopen.read()   # read file to contain string of the file content
        data = data.split('\n')  # convert to list of the each lines
        if len(data) > 1:  # check if the input file has data in it
            data = data[1:] # exclude the label
            data = [value for value in data if value != '']  # remove blank row
            data_list = [i.split(',') for i in data] # convert to list of lists of the each lines
        else: # if the file doesn't have data, return empty list and 0 value
            print("The input file doesn't have data!")
            OP1,OP2,OP3,OP4 = [],[],[],0 
            return OP1, OP2, OP3, OP4

    # 1. return the list of student details(ID and income) for a specific country who are in
    #    debt (or have debt status True) and spending more than 7 hours on any social media.
    OP1 = []
    # loop through each row to find target student
    for i in data_list:                
        time = int(i[3]) # convert string into integer
        # find students that spend more than 7 hours on any social media and come from the input country 
        if time > 7 and i[10]=='TRUE' and i[6].lower() == country.lower():
            # create a list that contains two elements of the matching student: student ID and income
            sub_data=[]   # sub_data: List[lists]
            income = round(float(i[9]),1)
            sub_data.extend((i[0],income)) 
            OP1.append(sub_data)  # append each matching list
    if len(OP1) > 0: # check if there are matching data
        OP1.sort(key=lambda x: x[0]) # sort ascendingly by student id    
    else:
        print("No matching data for OP1!")         
 
    
    
    # 2.return a list of unique countries for users whose age falls within the lower and upper bound of input age_group                     
    OP2 = []
    for i in data_list:
        age = int(i[1])
        if age >= age_group[0] and age <= age_group[1]:  # find users in the input age group
            if i[6].lower() not in OP2:    # unique countries
                OP2.append(i[6].lower())    # append country
    if len(OP2)>0: # check if there are matching data
        OP2.sort() # sort in alphabetically ascending order
    else:
        print("No matching data for OP2!")

    # 3.return the age statistics for a specific age group.
    OP3 = []
    time_spent = [] # list of time spent of the age group
    income_list = []  # list of income of the age group
    demographics = []  # list of demographics of the age group
    age_list = []  # list of age of the age group
    # get data of the input age_group
    for i in data_list:
        age = int(i[1])
        if age >= age_group[0] and age <= age_group[1]:
            time_spent.append(float(i[3]))
            income_list.append(float(i[9]))
            age_list.append(i)
            if i[7] not in demographics:
                demographics.append(i[7])
    if len(time_spent) > 0: # check if there are matching data
        OP3.append(round(get_avg(time_spent),4)) # get the first desired value in OP3
        OP3.append(round(get_stddev(income_list),4))  # get the second desired value in OP3
        # give a list that have the average time spent on social media and the demograph respectively
        avg_time = []
        demographics = list_to_listOfLists(demographics)  #convert the demographics list into a list of lists to append the average time of demographics to each demographics
        for i in demographics:
            # give a list of time that students spent on social media in one region
            each_time = []
            for j in age_list:
                if i[0] == j[7]: 
                    each_time.append(float(j[3]))                   
            avg_time.append(get_avg(each_time))
            i.append(get_avg(each_time))
        # sort the value ascendingly
        demographics= sorted(demographics, key = lambda x:(x[1], x[0]))
        OP3.append(demographics[0][0].lower())
    else:
        print("No matching data for OP3!")

    # 4. return the platform that has the highest number of users and calculate the correlation
    # between the age and the income for that user base.
    social_media = [] # get the list of social media (unique)
    for i in data_list: 
        if i[4] not in social_media:   
            social_media.append(i[4]) 
    social_media = list_to_listOfLists(social_media)
    # get the number of users of each social media platform and append to the social_media list
    for i in social_media:
        n = 0
        for j in data_list:
            if j[4] == i[0]:
                n += 1
        i.append(n)
    social_media = sorted(social_media, key = lambda x:(-x[1], x[0]))  # sort social media platform by the number of users descendingly and social media platform name ascendingly
    tg_platform = social_media[0][0] # find the target platform 
    # calculate the numeric value for correlation between age and income
    age_list4 = []  
    income_list4 = []
    for i in data_list:
        if i[4] == tg_platform:
            age_list4.append(float(i[1])) # get list of the users' age
            income_list4.append(float(i[9])) # get list of the users' income
    age_avg4 = get_avg(age_list4) # list of age that belong to the users of the target platform
    income_avg4 = get_avg(income_list4) # list of income that belong to the users of the target platform
    sum1, sum2,sum3 = 0,0,0   # three sums in the correlation formula
    for i in range(len(age_list4)):
        sum1 = sum1+(age_list4[i]-age_avg4)*(income_list4[i]-income_avg4)
        sum2 = sum2+(age_list4[i]-age_avg4)**2
        sum3 = sum3+(income_list4[i]-income_avg4)**2
    try:
        coef = sum1/(sum2*sum3)**(1/2)  # Correlation coefficient
        OP4 = round(coef,4)
    except ZeroDivisionError:  # catch ZeroDivisionError
        print("A zero division error when try to get OP4!")
        OP4 = 0
     

    return OP1, OP2, OP3, OP4