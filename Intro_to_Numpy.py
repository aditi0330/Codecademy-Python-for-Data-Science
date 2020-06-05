import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])

test_2 = np.genfromtxt('test_2.csv', delimiter=',')
#NumPy arrays are more efficient than lists. 
#One reason is that they allow you to do element-wise operations. 

# With a list
l = [1, 2, 3, 4, 5]
l_plus_3 = []
for i in range(len(l)):
    l_plus_3.append(l[i] + 3)
    
# With an array
a = np.array(l)
a_plus_3 = a + 3

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = test_3 + 2
total_grade = test_1 +test_2 + test_3_fixed
final_grade = total_grade/3
print(final_grade)

# heads = 1 tails = 0
coin_toss = np.array([1, 0, 0, 1, 0])

coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])

#	Tanya	Manual	Adwoa	Jeremy	Cody
jeremy_test_2 = test_2[3]
manual_adwoa_test_1 = test_1[1:3]

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])
tanya_test_3 = student_scores[2,0]
cody_test_scores = student_scores[:,4]

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
cold = porridge[porridge < 60]
hot = porridge[porridge > 80]
just_right = porridge[(porridge > 60) & (porridge < 80)]
print(hot)
print(cold)
print(just_right)

#[[ 43.6  45.1  58.8  53. ]
 #[ 47.   44.5  58.3  52.6]
 #[ 46.7  44.2  57.9  52.2]
 #[ 46.5  44.1  57.6  51.9]
 #[ 46.2  43.9  57.2  51.5]]
temperatures = np.genfromtxt('temperature_data.csv', delimiter = ',')
print(temperatures)
temperatures_fixed = temperatures + 3
monday_temperatures = temperatures_fixed[0,:]
thursday_friday_morning = temperatures_fixed[3:,1]
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
temperatures = np.genfromtxt('temperature_data.csv', delimiter = ',')
print(temperatures)
temperatures_fixed = temperatures + 3
monday_temperatures = temperatures_fixed[0,:]
thursday_friday_morning = temperatures_fixed[3:,1]
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]