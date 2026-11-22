
print("==============================")
print("      SMART BUDGET ADVISOR")
print("==============================")

budget = float(input("Enter your budget (₹1,000 - ₹10,000): ₹"))

print(f"\nYour budget: ₹{budget}")

if budget < 1000 or budget > 10000:
    print("Invalid budget! Please enter between ₹1,000 and ₹10,000.")

elif budget <= 3000:
    print("\nBudget Category: LOW")
    print("Advice: Prioritize essential expenses and avoid unnecessary spending.")

elif budget <= 6000:
    print("\nBudget Category: MODERATE")
    print("Advice: Maintain a balance between spending and saving.")

else:
    print("\nBudget Category: HIGH")
    print("Advice: Save a portion of your budget and plan your expenses wisely.")

print("\nThank you for using Smart Budget Advisor!")
