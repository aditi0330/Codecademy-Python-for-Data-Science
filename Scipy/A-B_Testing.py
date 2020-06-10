#A/B Testing: Understanding the Baseline
# Find the size of both of these lists
number_of_site_visitors = 2000.0
number_of_converted_visitors = 1300.0

# Calculate the conversion rate in terms of the above two variables here
conversion_rate = number_of_converted_visitors/number_of_site_visitors

#A/B Testing: Determining Lift
#We’re running an A/B Test in order to know if Option B is better than Option A 
#but if Option B were only a tiny percent better, would we really care? In order to detect precise differences, 
#we need a very large sample size.
# In order to choose a sample size, we need to know the smallest difference that we actually care to measure.
# This “smallest difference” is called lift.
# 100 * (Final - Initial) / Initial
lift_eight_percent_to_twelve_percent = 100 * (12 - 8) / 8.
print lift_eight_percent_to_twelve_percent

# Initial + Initial * Percent Increase
ten_percent_up_fifty_percent = (10) + (10 * 0.50)
print ten_percent_up_fifty_percent

#A/B Testing: Don't Interfere With Your Tests

