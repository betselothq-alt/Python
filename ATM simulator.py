print(f"Current Balance: ${balance:.2f}")
withdrawal = float(input("Enter withdrawal amount: $"))

if withdrawal > balance:
    print("Insufficient funds.")

elif withdrawal == balance:
    balance = 0
    print("Balance will be 0.")
    print(f"New Balance: ${balance:.2f}")

else:
    balance -= withdrawal
    print("Withdrawal successful.")
    print(f"New Balance: ${balance:.2f}")
