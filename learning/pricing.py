print("pricing loaded")

def apply_discount(price: float, percent: float) -> float:
    return price - price * percent / 100

if __name__ == "__main__":
    print(apply_discount(100.0, 10))