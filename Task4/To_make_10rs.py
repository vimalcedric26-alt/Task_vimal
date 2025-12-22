for one in range(0, 11):# Loop for number of 1rs
    for two in range(0, 6):# Loop for number of 2rs
         for five in range(0, 3):# Loop for number of 5rs
            for ten in range(0, 2): # Loop for number of 10rs
                total = (one * 1) + (two * 2) + (five * 5) + (ten * 10) # total amount
                if total == 10:
                    print(f"₹1:{one}, ₹2:{two}, ₹5:{five}, ₹10:{ten}")