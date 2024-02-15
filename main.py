remaining_value = int(input(("Enter a value: ")))

while remaining_value > 0:
        try:
            subtrahend = int(input("Enter subtrahend: "))
    
            new_remain_value = remaining_value - subtrahend
           
            print(f"{remaining_value} - {subtrahend} = {new_remain_value}")
            print()
            
            remaining_value = new_remain_value
        
        except ValueError:
                print("Invalid input")
                print()
    




