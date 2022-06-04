#!/usr/bin/which python3
from keystone import *
from capstone import *
from unicorn import *
from unicorn.arm_const import *
ADDRESS = 0x1000
CODE ='''
    mov r1,0x4;
    mov r2,1
    mov r4,0x4;
    mov r1, r2;
    '''
def main():
#First we define some assembly
    #Now we tell what kind of assembler we want to use from keystone!
    ks = Ks(KS_ARCH_ARM,KS_MODE_ARM)
    encoding, count = ks.asm(CODE,as_bytes=True)
    #now we start build ourselves a unicorn engine!
    uc = Uc(UC_ARCH_ARM,UC_MODE_ARM)
    uc.mem_map(ADDRESS,2*1024*1024)
    uc.mem_write(ADDRESS, encoding)
    uc.emu_start(ADDRESS,ADDRESS+len(encoding),count=2000)
    print(f"<<<<PC = {hex(uc.reg_read(UC_ARM_REG_PC))}")
    print(f"<<<<R1 = {hex(uc.reg_read(UC_ARM_REG_R1))}")

if __name__ == "__main__":
    main()
