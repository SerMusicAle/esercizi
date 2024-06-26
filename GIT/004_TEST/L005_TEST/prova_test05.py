def prime_factors(n: int) -> list[int]:
    factors = []
    divisor = 2

    # Continua a trovare fattori finché n non diventa 1
    while n > 1:
        # Verifica se il divisore è un fattore primo di n
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

# Esempio di utilizzo:
number = 84
print(f"I fattori primi di {number} sono:", prime_factors(number))
