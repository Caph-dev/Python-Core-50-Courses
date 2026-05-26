from is_prime import isPrime

ans = []
for num in range(2, 101):
    if isPrime(num):
        ans.append(num)
print(ans)        