teste = "blablDaalab"

print({c.lower() for c in teste})




start = 0
end = 2025

from math import sqrt
print({num : sqrt(num) for num in range(start, end+1) if int(sqrt(num)) ** 2 == num})