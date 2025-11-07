def approximate_pi(n_terms):
 list_of_alternating_signs = []
 for i in range(n_terms):
  if i % 2 == 0 :
    list_of_alternating_signs.append(1)
  else :
    list_of_alternating_signs.append(-1)
 leibniz_series = []
 for i in range(n_terms) :
  sign = list_of_alternating_signs[i]
  num = (1/(2*i + 1)) * sign
  leibniz_series.append(num)
 total = sum( leibniz_series )
 pie = total*4
 return pie


 
