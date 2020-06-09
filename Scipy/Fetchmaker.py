import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))
whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
p_value = binom_test(num_whippet_rescues, num_whippets, p=0.08)
print(p_value)

w = fetchmaker.get_weight("whippet")
t = fetchmaker.get_weight("terrier")
p = fetchmaker.get_weight("pitbull")
f_oneway(w, t, p)
print(f_oneway(w, t, p).pvalue)
values = np.concatenate([w, t, p])
labels = ["whippet"] * len(w) + ["terrier"] * len(t) + ["pitbull"] * len(p)
# print labels
print(pairwise_tukeyhsd(values, labels, 0.05))

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

color_table = [
[
  np.count_nonzero(poodle_colors == "black"),
  np.count_nonzero(shihtzu_colors == "black")
],
[
  np.count_nonzero(poodle_colors == "brown"),
  np.count_nonzero(shihtzu_colors == "brown")
],
[
  np.count_nonzero(poodle_colors == "gold"),
  np.count_nonzero(shihtzu_colors == "gold")
],
[
  np.count_nonzero(poodle_colors == "grey"),
  np.count_nonzero(shihtzu_colors == "grey")
],
[
  np.count_nonzero(poodle_colors == "white"),
  np.count_nonzero(shihtzu_colors == "white")
]
]

print color_table
_, color_pval, _, _ = chi2_contingency(color_table)
print color_pval

