import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
vein_pack_lifespans = familiar.lifespans(package = 'vein')
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
vein_pack_pval = vein_pack_test.pvalue
print(vein_pack_test.pvalue)
print(format(vein_pack_test.pvalue, '0.10f'))
if vein_pack_pval < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

#Upselling Familiar: Pumping Life Into The Company
artery_pack_lifespans = familiar.lifespans(package = 'artery')
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
artery_pack_pval = package_comparison_results.pvalue
if artery_pack_pval < 0.05:
  print("The Artery Pack Is Proven To Make You Live Longer!")
else:
  print("The Artery Package is also a great product!")

#Benefitting Everyone: A Familiar Problem
iron_contingency_table = familiar.iron_counts_for_package()
print(iron_contingency_table)

_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)

if iron_pvalue < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We Cannot Say The Artery Package Will Help You, I Bet It is Nice!")


