# controller.py

def calculate_daily(total_money, calculated_label):
    daily_money = total_money / 31
    calculated_label.config(text=f"Max amount of money that can be spent every day without going broke: {daily_money:.2f}")
