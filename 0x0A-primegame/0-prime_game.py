#!/usr/bin/python3
"""determine who the winner of each game is."""


def isWinner(x, nums):
    """determine who the winner of each game is."""
    

    max_n = 10000
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(max_n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                is_prime[multiple] = False
    primes = [num for num, prime in enumerate(is_prime) if prime]

    # Step 2: Function to determine the winner for a given n
    def determine_winner(n):
        if n < 2:
            return "Ben"  # If n is 1, Maria cannot make a move
        
        # Create a list to track the state of numbers
        numbers = [True] * (n + 1)  # True means the number is still in the game
        turn = 0  # 0 for Maria, 1 for Ben
        
        for prime in primes:
            if prime > n:
                break
            if numbers[prime]:  # If the prime is still in the game
                # Remove the prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    numbers[multiple] = False
                turn = 1 - turn  # Switch turns
        
        return "Ben" if turn == 0 else "Maria"

    # Step 3: Count wins
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = determine_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
