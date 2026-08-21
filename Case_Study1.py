def get_user_inputs():
    order_amount = eval(input("Enter the order amount: "))
    delivery_distance = eval(input("Enter the delivery distance in kilometers: "))
    customer_type = input("Enter the customer type (Regular/Premium): ")
    customer_rating = eval(input("Enter the customer rating (1-5): "))
    restaurant_rating = eval(input("Enter the restaurant rating (1-5): "))
    preparation_time = eval(input("Enter the preparation time in minutes: "))
    payment_method = input("Enter the payment method (Cash/Card): ")
    weather_condition = input("Enter the weather condition (Sunny/Rainy/Snowy): ")
    demand_level = input("Enter the demand level (Low/Medium/High): ")
    peak_hour = input("Is it peak hour? (Yes/No): ")
    previous_cancellations = eval(input("Enter the number of previous cancellations by the customer: "))
    return order_amount, delivery_distance, customer_type, customer_rating, restaurant_rating, preparation_time, payment_method, weather_condition, demand_level, peak_hour, previous_cancellations


def order_risk(previous_cancellations, customer_rating, demand_level, peak_hour):
    cancellations_chance = 0
    if peak_hour.lower() == 'yes':
        cancellations_chance += 1
    if previous_cancellations > 3:
        cancellations_chance += 3
    elif previous_cancellations > 0:
        cancellations_chance += 1
    if customer_rating < 3.0:
        cancellations_chance += 2
    elif customer_rating < 4.0:
        cancellations_chance += 1
    if demand_level.lower() == 'low':
        cancellations_chance += 0
    elif demand_level.lower() == 'medium':
        cancellations_chance += 1
    else:
        cancellations_chance += 2
    if cancellations_chance >= 5:
        return 'High'
    elif cancellations_chance >= 3:
        return 'Medium'
    else:
        return 'Low'


def Discount(order_amount, customer_type, payment_method, customer_rating):
    discount = 0
    if customer_type.lower() == 'premium':
        discount += 0.1 * order_amount
    elif customer_type.lower() == 'regular':
        discount += 0.05 * order_amount

    if payment_method.lower() == 'card':
        discount += 0.02 * order_amount
    elif payment_method.lower() == 'cash':
        discount += 0.01 * order_amount

    if customer_rating >= 4.8:
        discount += 0.03 * order_amount
    elif customer_rating <= 2.5:
        discount -= 0.02 * order_amount
    return discount


def delivery_charge(delivery_distance, weather_condition, demand_level, peak_hour):
    charge = 0
    if delivery_distance <= 5:
        charge += 30
    elif delivery_distance <= 10:
        charge += 50
    else:
        charge += 75
    if weather_condition.lower() == 'rainy':
        charge += 10
    elif weather_condition.lower() == 'snowy':
        charge += 15
    if demand_level.lower() == 'high':
        charge += 15
    elif demand_level.lower() == 'medium':
        charge += 10
    if peak_hour.lower() == 'yes':
        charge += 5
    return charge


def restaurant_status(weather_condition, restaurant_rating, preparation_time):
    status = 'Open'
    if restaurant_rating < 3.0:
        status = 'Temporary Closed'

    if preparation_time > 60:
        status = 'slow service'

    if weather_condition.lower() == 'snowy':
        status = 'Temporary Closed'

    return status


def priority_delivery(order_amount, customer_type, customer_rating, payment_method):
    priority = False

    if order_amount >= 1000:
        priority = True
    elif customer_type.lower() == 'premium' and customer_rating >= 4.5:
        priority = True
    elif payment_method.lower() == 'card' and customer_rating >= 4.8:
        priority = True

    return priority


def order_decision(order_amount, delivery_distance, customer_rating, restaurant_rating, preparation_time, weather_condition, demand_level, peak_hour, previous_cancellations):

    cancellation_risk = order_risk(
        previous_cancellations,
        customer_rating,
        demand_level,
        peak_hour
    )
    restaurant = restaurant_status(
        weather_condition,
        restaurant_rating,
        preparation_time
    )

    if order_amount < 100:
        return "Rejected"

    elif delivery_distance > 20:
        return "Rejected"

    elif restaurant_rating < 2.5:
        return "Rejected"

    elif restaurant == "Temporary Closed":
        return "Rejected"

    elif weather_condition.lower() == "snowy" and delivery_distance > 15:
        return "Rejected"

    elif cancellation_risk == "High":
        return "Manual Review"

    elif customer_rating < 3.0 and previous_cancellations >= 3:
        return "Manual Review"

    elif preparation_time > 60:
        return "Manual Review"

    elif (demand_level.lower() == "high"
          and peak_hour.lower() == "yes"
          and delivery_distance > 10):
        return "Manual Review"

    else:
        return "Accepted"


def generate_report(order_amount, delivery_distance, customer_type, customer_rating, restaurant_rating, preparation_time, payment_method, weather_condition, demand_level, peak_hour, previous_cancellations):
    cancellation_risk = order_risk(
        previous_cancellations,
        customer_rating,
        demand_level,
        peak_hour
    )
    restaurant = restaurant_status(
        weather_condition,
        restaurant_rating,
        preparation_time
    )
    discount = Discount(order_amount, customer_type, payment_method, customer_rating)
    delivery_fee = delivery_charge(delivery_distance, weather_condition, demand_level, peak_hour)
    decision = order_decision(
        order_amount,
        delivery_distance,
        customer_rating,
        restaurant_rating,
        preparation_time,
        weather_condition,
        demand_level,
        peak_hour,
        previous_cancellations
    )
    priority = priority_delivery(order_amount, customer_type, customer_rating, payment_method)

    order_status = decision
    charge = delivery_fee
    manual_review = (decision == "Manual Review")
    final_category = decision
    final_payable = order_amount - discount + delivery_fee

    report = {
        "Order Amount": order_amount,
        "Delivery Distance": delivery_distance,
        "Customer Type": customer_type,
        "Customer Rating": customer_rating,
        "Restaurant Rating": restaurant_rating,
        "Preparation Time": preparation_time,
        "Payment Method": payment_method,
        "Weather Condition": weather_condition,
        "Demand Level": demand_level,
        "Peak Hour Status": peak_hour,
        "Previous Cancellations": previous_cancellations,
        "Cancellation Risk": cancellation_risk,
        "Restaurant Status": restaurant,
        "Discount Applied": discount,
        "Delivery Fee": delivery_fee,
        "Final Decision": decision
    }

    print("=" * 55)
    print("             FOOD DELIVERY ORDER REPORT")
    print("=" * 55)

    print("Order Amount           :", f"₹{order_amount:.2f}")
    print("Delivery Distance      :", f"{delivery_distance} km")
    print("Customer Type          :", customer_type)
    print("Customer Rating        :", customer_rating)
    print("Restaurant Rating      :", restaurant_rating)
    print("Preparation Time       :", f"{preparation_time} minutes")
    print("Payment Method         :", payment_method)
    print("Weather Condition      :", weather_condition)
    print("Demand Level           :", demand_level)
    print("Peak Hour              :", peak_hour)
    print("Previous Cancellations :", previous_cancellations)

    print("-" * 55)

    print("Order Status           :", order_status)
    print("Delivery Charge        :", f"₹{charge:.2f}")
    print("Discount               :", f"₹{discount:.2f}")
    print("Priority Delivery      :", "Yes" if priority else "No")
    print("Cancellation Risk      :", cancellation_risk)
    print("Restaurant Status      :", restaurant)
    print("Manual Review          :", manual_review)
    print("Final Order Category   :", final_category)
    print("Final Payable Amount   :", f"₹{final_payable:.2f}")

    print("=" * 55)

    return report


if __name__ == "__main__":
    inputs = get_user_inputs()
    report = generate_report(*inputs)