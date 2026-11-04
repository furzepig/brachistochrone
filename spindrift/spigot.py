def stream_pi_digits():
    """
    An unbounded streaming spigot algorithm for the decimal digits of Pi.
    Yields digits sequentially using O(1) memory per iteration.
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            # Reduce and scale state matrices for the next digit
            q, r, t, k, n, l = (
                10 * q, 
                10 * (r - n * t), 
                t, 
                k, 
                (10 * (3 * q + r)) // t - 10 * n, 
                l
            )
        else:
            # Factoring step to process next fractional term
            q, r, t, k, n, l = (
                q * k, 
                (2 * q + r) * l, 
                t * l, 
                k + 1, 
                (q * (7 * k + 2) + r * l) // (t * l), 
                l + 2
            )

# Example Usage: Stream and print the first 50 digits
pi_stream = stream_pi_digits()
digits = [str(next(pi_stream)) for _ in range(50)]
print(f"{digits[0]}.{''.join(digits[1:])}")
