# Smart Energy Estimator function by T.A.

def smart_energy_estimator(voltage, current, time_hours, price_per_kwh):
    power_watts = voltage * current
    energy_kwh = (power_watts * time_hours) / 1000
    daily_estimate = energy_kwh * (24 / time_hours)
    monthly_estimate = daily_estimate * 30
    cost_estimate = monthly_estimate * price_per_kwh

    return {
        "instant_power_W": power_watts,
        "energy_kWh": energy_kwh,
        "daily_kWh": daily_estimate,
        "monthly_kWh": monthly_estimate,
        "monthly_cost": cost_estimate
    }

# Get user input
voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))
time_hours = float(input("Enter time duration (hours): "))
price_per_kwh = float(input("Enter energy price per kWh: "))

# Calculate and display results
result = smart_energy_estimator(voltage, current, time_hours, price_per_kwh)
print("\n--- Energy Consumption Report ---")
for key, value in result.items():
    print(f"{key}: {value:.2f}")