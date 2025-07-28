# Mobile Pet Spa Services
services = {
    1: ("Dog Grooming", 49.99),
    2: ("Cat Grooming", 39.99),
    3: ("Pet Bathing", 29.99),
    4: ("Pet Nail Clipping", 19.99),
    5: ("Pet Sitting", 24.99),
    6: ("Pet Walking", 14.99),
    7: ("Pet Training", 59.99),
    8: ("Pet Boarding", 89.99),
    9: ("Pet Transportation", 39.99),
    10: ("Pet Photography", 99.99)
}

def display_services():
    print("\nAvailable Services:")
    for key, (name, price) in services.items():
        print(f"{key}. {name} - ${price:.2f}")

def get_order():
    order = []
    while True:
        try:
            choice = input("\nEnter service number to add to your order (or type 'done' to finish): ")
            if choice.lower() == 'done':
                break
            choice = int(choice)
            if choice in services:
                order.append(choice)
                print(f"Added: {services[choice][0]}")
            else:
                print("Invalid selection. Please choose a number from the list.")
        except ValueError:
            print("Please enter a valid number or 'done'.")
    return order

def summarize_order(order):
    if not order:
        print("\nNo services selected.")
        return

    print("\nOrder Summary:")
    total = 0
    for item in order:
        name, price = services[item]
        print(f"- {name}: ${price:.2f}")
        total += price
    print(f"\nTotal: ${total:.2f}")

def main():
    print("Welcome to the Mobile Pet Spa!")
    display_services()
    order = get_order()
    summarize_order(order)

if __name__ == "__main__":
    main()

# --- Classes ---
class Customer:
    def __init__(self, name):
        self.name = name
        self.order = []

    def add_service(self, service_id):
        if service_id in services:
            self.order.append(service_id)
            print(f"Added: {services[service_id][0]}")
        else:
            print("Service ID not valid.")

    def get_total(self):
        return sum(services[s_id][1] for s_id in self.order)

class PremiumCustomer(Customer):
    def apply_discount(self):
        return self.get_total() * 0.9  # 10% discount

class OrderSummary:
    def __init__(self, customer):
        self.customer = customer

    def display(self):
        print(f"\nOrder Summary for {self.customer.name}:")
        if not self.customer.order:
            print("No services selected.")
            return
        total = 0
        for sid in self.customer.order:
            name, price = services[sid]
            print(f"- {name}: ${price:.2f}")
            total += price
        print(f"Total: ${total:.2f}")

# --- Functions ---
def display_services():
    print("\n--- Available Services ---")
    for sid, (name, price) in services.items():
        print(f"{sid}. {name} - ${price:.2f}")

def get_customer():
    name = input("Enter your name: ")
    customer_type = input("Are you a premium customer? (yes/no): ").strip().lower()
    if customer_type == 'yes':
        return PremiumCustomer(name)
    else:
        return Customer(name)

def get_order(customer):
    while True:
        try:
            choice = input("\nEnter service number to add (or 'done' to finish): ").strip()
            if choice.lower() == 'done':
                break
            choice = int(choice)
            customer.add_service(choice)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

# --- Main Program ---
def main():
    print("🐶 Welcome to the Mobile Pet Spa 🐱")
    display_services()
    
    customer = get_customer()
    get_order(customer)

    summary = OrderSummary(customer)
    summary.display()

    if isinstance(customer, PremiumCustomer):
        discounted = customer.apply_discount()
        print(f"\nPremium Discount Applied! New Total: ${discounted:.2f}")

if __name__ == "__main__":
    main()
