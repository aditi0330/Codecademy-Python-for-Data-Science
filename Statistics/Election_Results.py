
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = survey_responses.count('Ceballos')
print(total_ceballos)
survey_length = float(len(survey_responses))
percentage_ceballos = 100 * total_ceballos/survey_length
print(percentage_ceballos)
possible_surveys = np.random.binomial(survey_length, 0.54, size=10000) / survey_length
plt.hist(possible_surveys, range =(0, 1), bins=20)
plt.show()

possible_surveys_length = float(len(possible_surveys))
incorrect_predictions = len(possible_surveys[possible_surveys < .5])
ceballos_loss_surveys = incorrect_predictions/possible_surveys_length
print(ceballos_loss_surveys)

large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, .54, size = 10000)/large_survey_length
incorrect_predictions = len(large_survey[large_survey < .5])
ceballos_loss_new = incorrect_predictions/large_survey_length
print(ceballos_loss_new)

