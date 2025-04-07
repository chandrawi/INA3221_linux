import os
import sys

SOURCE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"src")
sys.path.append(SOURCE_PATH)

from INA3221_linux import INA3221


ina = INA3221(address=0x40, bus=2)

if __name__ == "__main__":

    if not ina.begin():
        print("could not connect. Fix and Reboot")
        sys.exit(1)
    else:
        print(f"Address: \t{hex(ina.get_address())}")
        ina.reset()

    print(f"Die ID: \t{hex(ina.get_die_id())}")
    print(f"Manufacture ID: \t{hex(ina.get_manufacturer_id())}")
    print(f"Configuration: \t{hex(ina.get_configuration())}")

    print("SHUNT0\tSHUNT1\tSHUNT2 (Ohm)")
    for ch in range(3):
        print(f"{ina.get_shunt_r(ch)}\t", end="")
    print()

    ina.set_shunt_resistor(0, 0.100)
    ina.set_shunt_resistor(1, 0.102)
    ina.set_shunt_resistor(2, 0.099)

    for ch in range(3):
        print(f"{ina.get_shunt_r(ch)}\t", end="")
    print()

    print("CHAN\tCRITIC\tWARNING\t (uV)")
    for ch in range(3):
        print(f"{ch}\t{ina.get_critical_alert(ch)}\t{ina.get_warning_alert(ch)}")

    ina.set_critical_alert(0, 50000)
    ina.set_critical_alert(1, 100000)
    ina.set_critical_alert(2, 150000)
    ina.set_warning_alert(0, 25000)
    ina.set_warning_alert(1, 75000)
    ina.set_warning_alert(2, 125000)

    print("CHAN\tCRITIC\tWARNING\t (uV)")
    for ch in range(3):
        print(f"{ch}\t{ina.get_critical_alert(ch)}\t{ina.get_warning_alert(ch)}")

    print("Shunt Voltage (uV)")
    print(f"  SVSUM:\t{ina.get_shunt_voltage_sum()}")
    print(f"SVLIMIT:\t{ina.get_shunt_voltage_sum_limit()}")

    ina.set_shunt_voltage_sum_limit(32198)
    print(f"SVLIMIT:\t{ina.get_shunt_voltage_sum_limit()}")

    print("Mask/ Enable")
    print(f"M/E:\t{hex(ina.get_mask_enable())}")

    print("Power Limit")
    print(f"UPPER:\t{ina.get_power_upper_limit()}")
    print(f"LOWER:\t{ina.get_power_lower_limit()}")

    ina.set_power_upper_limit(5000)
    ina.set_power_lower_limit(4000)

    print(f"UPPER:\t{ina.get_power_upper_limit()}")
    print(f"LOWER:\t{ina.get_power_lower_limit()}")

    print("getEnableChannel")
    for ch in range(3):
        print(f"{ina.get_enable_channel(ch)}\t", end="")
    print()

    print("Disable Channel")
    for ch in range(3):
        ina.disable_channel(ch)
        print(f"{ina.get_enable_channel(ch)}\t", end="")
    print()

    print("Enable Channel")
    for ch in range(3):
        ina.enable_channel(ch)
        print(f"{ina.get_enable_channel(ch)}\t", end="")
    print()

    print("Average")
    for avg in range(8):
        ina.set_average(avg)
        print(f"{ina.get_average()}\t", end="")
    print()
    ina.set_average(0)

    print("BusVoltageConversionTime")
    for bvct in range(8):
        ina.set_bus_voltage_conversion_time(bvct)
        print(f"{ina.get_bus_voltage_conversion_time()}\t", end="")
    print()
    ina.set_bus_voltage_conversion_time(0)

    print("ShuntVoltageConversionTime")
    for svct in range(8):
        ina.set_shunt_voltage_conversion_time(svct)
        print(f"{ina.get_shunt_voltage_conversion_time()}\t", end="")
    print()
    ina.set_shunt_voltage_conversion_time(0)
