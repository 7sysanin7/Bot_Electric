# utils/electric_calculator.py

def calculate_electricity_consumption(power_watts: float, time_hours: float) -> float:
    """
    Calculate electricity consumption in kWh.
    
    :param power_watts: Power consumption in watts
    :param time_hours: Usage time in hours
    :return: Electricity consumption in kWh
    """
    return (power_watts * time_hours) / 1000

def calculate_cost(consumption_kwh: float, cost_per_kwh: float) -> float:
    """
    Calculate the cost of electricity consumption.
    
    :param consumption_kwh: Electricity consumption in kWh
    :param cost_per_kwh: Cost per kWh
    :return: Total cost
    """
    return consumption_kwh * cost_per_kwh
