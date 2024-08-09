# Input number of each genotype
k, m, n = map(int, input().split())

# Total number of individuals
total = k + m + n

# Probability of getting an 'AA' allele
prob_AA = (k / total) * ((k - 1) / (total - 1))  # Probability from k * k
prob_AA += (k / total) * (m / (total - 1))  # Probability from k * m
prob_AA += (k / total) * (n / (total - 1))  # Probability from k * n

prob_AA += (m / total) * ((k / (total - 1)))  # Probability from m * k
prob_AA += (m / total) * ((m - 1) / (total - 1)) * (3 / 4)  # Probability from m * m
prob_AA += (m / total) * (n / (total - 1)) * (1 / 2)  # Probability from m * n

prob_AA += (n / total) * (k / (total - 1))  # Probability from n * k
prob_AA += (n / total) * (m / (total - 1)) * (1 / 2)  # Probability from n * m

# Output the final probability of having at least one 'AA' allele
print(f"{prob_AA:.5f}")
