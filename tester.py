while True:
    try: 
        username = input("Enter username: ").strip()
        if not username:
            raise ValueError("Please enter username")
        break
    except ValueError as e:
        print(e)
        
print("hello")
        
        