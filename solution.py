#logic: 
# to find (x, y, z) 
# 1. look at every number other than the first as a potential y
# 2. count the number of potential x's each y has
# 3. for every z each y has, add the number of potential x's  

def solution(l):

    #counter for the number of lucky tripples
    counter = 0

    #counter of number of number that can be divided by that number behind it to give (x, n1, n2)
    pair_counter = [0]*len(l)

    #loop through list
    for index_one, test_number in enumerate(l):

        #the last number cannot be the second number of a lucky tripple
        if (index_one == len(l)-1): continue

        #loop through list ending at the first potential y
        for number_to_be_tested in l[:index_one]:
            
            #the first number cannot be the second number of a lucky tripple
            if (index_one == 0): continue

            #if the first test number is divisible by the number being tested
            if test_number % number_to_be_tested == 0:
                
                #count number of potential x's for each y
                pair_counter[index_one] += 1

    #loop through the list again
    for index_one, test_number in enumerate(l):

        #first and last numbers cann't be potetnial y
        if (index_one == 0 or index_one == len(l)-1): continue

        #loop through list after each potential y
        for number_to_be_tested in l[index_one+1:]:
            
            #check for potential z 
            if number_to_be_tested % test_number == 0:

                #if potential z, add on all of that numbers potential x's
                counter += pair_counter[index_one]

    #return number of full tripples
    return counter


#test generator
def generate_test(x):
    test_case = list()
    counter = 1
    while x+1 != counter:
        test_case.append(counter*1000)
        counter = counter + 1
    print("Test case = ", test_case)
    return test_case


print("solution 2 = ", solution([1, 1, 1]))