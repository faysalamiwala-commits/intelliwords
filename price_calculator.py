# IntelliWords - KDP Price Calculator v1.0
# Made by Faysal Amiwala - Karachi, Pakistan

def calculate_price(pages, price=9.99):
    print("="*40)
    print(f"💰 PRICE CALCULATOR")
    print(f"📖 Pages: {pages}")
    print(f"💵 Book Price: ${price}")
    royalty = price * 0.60
    print(f"💸 Your Royalty: ${royalty:.2f} per book")
    print(f"📚 If 100 books sell: ${royalty*100:.2f}")
    print(f"📚 If 500 books sell: ${royalty*500:.2f}")
    print(f"🎯 Target $2000/month = {int(2000/royalty)} books")
    print("="*40)
    print("Made by IntelliWords - From Idea to Next Reader")

# Example
calculate_price(100, 9.99)
calculate_price(200, 14.99)
