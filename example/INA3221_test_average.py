import os
import sys

SOURCE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"src")
sys.path.append(SOURCE_PATH)

from INA3221_linux import INA3221
import time


ina = INA3221(address=0x40, bus=2)

if __name__ == "__main__":

    if not ina.begin():
        print("Could not connect. Fix and Reboot.")
        sys.exit(1)
    else:
        print(f"Address: \t{hex(ina.get_address())}")
        ina.reset()

    print(f"Configuration:\t{hex(ina.get_configuration())}")  # should be 0x7127

    # Set shunt resistor and enable channel 0
    ina.set_shunt_resistor(0, 0.100)
    ina.enable_channel(0)
    time.sleep(0.1)  # flush IO

    print("Testing Averaging Settings...")
    for avg in range(8):

        ina.set_average(avg)
        print(f"AVG:\t{ina.get_average()}")
        time.sleep(0.1)

        start = time.time()
        bus_voltage = ina.get_bus_voltage(0)
        stop = time.time()
        elapsed_us = int((stop - start) * 1_000_000)

        print(f"BUS V:\t{bus_voltage:.3f} V\t{elapsed_us} µs")
        time.sleep(0.1)
