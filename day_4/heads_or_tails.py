import random


coin = {0: "Heads", 1: "Tails"}

def main():
    print("Flip a coin: ")
    
    result = coinflip()
    print(result)
    
    
def coinflip():
    result = random.choice(list(coin.values()))
    return result

if __name__ == "__main__":
    main()