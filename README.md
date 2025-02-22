# Smart Energy Consumption Estimator

"""
This function calculates energy consumption based on voltage, current, and time duration.
It also estimates daily and monthly energy usage and cost.

## Function Definition

def smart_energy_estimator(voltage, current, time_seconds, price_per_kwh=0.15):
    """
    Estimates energy consumption and cost based on electrical parameters.

    Parameters:
    voltage (float): Measured voltage in volts (V).
    current (float): Measured current in amperes (A).
    time_seconds (int): Duration in seconds for which power is consumed.
    price_per_kwh (float, optional): Cost of 1 kWh of energy (default is 0.15).

    Returns:
    dict: Contains power (W), energy (kWh), daily/monthly usage, and cost.
    """
    power_watts = voltage * current  # Calculate instantaneous power (Watts)
    energy_kwh = (power_watts * time_seconds) / 3600000  # Convert to kWh

    daily_estimate = energy_kwh * (86400 / time_seconds)  # Estimate daily kWh
    monthly_estimate = daily_estimate * 30  # Estimate monthly kWh
    cost_estimate = monthly_estimate * price_per_kwh  # Monthly cost estimate

    return {
        "instant_power_W": power_watts,
        "energy_kWh": energy_kwh,
        "daily_kWh": daily_estimate,
        "monthly_kWh": monthly_estimate,
        "monthly_cost": cost_estimate
    }

## Example Usage

result = smart_energy_estimator(230, 2, 3600, 0.15)
print(result)

### Expected Output:

{
    "instant_power_W": 460,
    "energy_kWh": 0.46,
    "daily_kWh": 11.04,
    "monthly_kWh": 331.2,
    "monthly_cost": 49.68
}

## Features
✅ Simple and efficient calculation
✅ Supports cost estimation
✅ Useful for home automation and energy monitoring
✅ Can be extended for IoT integration

## Future Improvements
- Add real-time data logging
- Support multiple readings for better accuracy
- Integrate with ESP32 and MQTT for remote monitoring

---
*This project is open for contributions. Feel free to suggest improvements!*
"""

