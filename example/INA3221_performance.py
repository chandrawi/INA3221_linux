import os
import sys

SOURCE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"src")
sys.path.append(SOURCE_PATH)

from INA3221_linux import INA3221
import time


ina = INA3221(address=0x40, bus=2)

# Optional: Custom method for I2C clock speed setting (platform-dependent)
def set_i2c_clock_speed(speed_hz):
    # This is platform-specific; usually done via OS/hardware config, not runtime.
    # Left here for compatibility with Arduino-style sketches.
    print(f"(Simulated) Set I2C speed to {speed_hz} Hz")

def performance(speed):
    set_i2c_clock_speed(speed)
    print(f"Speed:\t{speed}")
    time.sleep(0.1)  # flush IO

    start = time.time()
    bus_voltage = ina.get_bus_voltage(1)
    stop = time.time()
    print(f"BUS V:\t{bus_voltage:.3f}\t{int((stop - start) * 1_000_000)} µs")

    time.sleep(0.1)

    start = time.time()
    shunt_voltage = ina.get_shunt_voltage(1)
    stop = time.time()
    print(f"SHUNT V:\t{shunt_voltage:.3f}\t{int((stop - start) * 1_000_000)} µs")

    time.sleep(0.1)

    start = time.time()
    current = ina.get_current(1)
    stop = time.time()
    print(f"A:\t{current:.3f}\t{int((stop - start) * 1_000_000)} µs")

    time.sleep(0.1)

    start = time.time()
    power = ina.get_power(1)
    stop = time.time()
    print(f"W:\t{power:.3f}\t{int((stop - start) * 1_000_000)} µs")


if __name__ == "__main__":

    if not ina.begin():
        print("Could not connect. Fix and Reboot.")
        sys.exit(1)
    else:
        print(f"Address: \t{hex(ina.get_address())}")

    print(f"Die ID: \t{hex(ina.get_die_id())}")
    print(f"Manufacture ID: \t{hex(ina.get_manufacturer_id())}")
    print(f"Configuration: \t{hex(ina.get_configuration())}")

    # Set shunt resistors
    ina.set_shunt_resistor(0, 0.100)
    ina.set_shunt_resistor(1, 0.102)
    ina.set_shunt_resistor(2, 0.099)

    # Run performance tests
    for speed in [100_000, 200_000, 300_000, 400_000]:
        performance(speed)
