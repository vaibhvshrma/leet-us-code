class Solution:
    def countPrimes(self, n: int) -> int:
        primes = self.get_primes(n)
        return len(primes)

    @staticmethod
    def get_primes(N):
        # sieve of eratosthenes
        composite = [False] * N
        prime = []
        for i in range(2, N):
            if not composite[i]:       # Found prime number
                prime.append(i)

            for j in range(len(prime)):
                if i * prime[j] >= N:
                    break
                composite[i*prime[j]] = True
                if i % prime[j] == 0:
                    break
        return prime
