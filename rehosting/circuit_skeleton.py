#!/usr/bin/which python3
from keystone import *
from capstone import *
from unicorn import *
from unicorn.arm_const import *

"""
Hint: always document the mappings properly!

In this case, the size is always in KiloByte and we calculate the bytes in the mapping function 
"""
Memory_mappings =  [
        {
            "name": "internal_flash",
            "address": 0x0,
            "size": 128,
        },
        {
            "name": "internal_RWW_section",
            "address": 0x00400000,
            "size": 4,
        },
        {
            "name": "internal_SRAM",
            "address": 0x20000000,
            "size": 32,
        },
        {
            "name": "peripheral_bridge_A",
            "address": 0x40000000,
            "size": 64,
        },
        {
            "name": "peripheral_bridge_A",
            "address": 0x41000000,
            "size": 64,
        },
        {
            "name": "peripheral_bridge_C",
            "address": 0x42000000,
            "size": 64,
        },
        {
            "name": "IOBUS",
            "address": 0x60000000,
            "size": 1,
        },
    ]



def main():
    uc = Uc(UC_ARCH_ARM, UC_MODE_ARM)
    ''''We now start the mapping process'''
    for memory in Memory_mappings:
        print(f"adding:{memory['name']}")
        uc.mem_map(memory["address"],int(memory["size"]*1024))


if __name__ == "__main__":
    main()
