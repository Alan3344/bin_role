#!/usr/bin/env python
# -*- ecoding: utf-8 -*-


# Super administrator
# SUPER_ADMIN = 0xFFFF
SUPER_ADMIN = 0xFF


class ROLE:
    Home = 0x1
    SysMgr = 0x2
    MemberList = 0x3
    Report = 0x4


class RangeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Role:
    def __init__(self, role=0x0, admin=SUPER_ADMIN) -> None:
        self.role = role
        self.admin = admin
        self.roleList = []
        if SUPER_ADMIN > 16**4:
            raise RangeError('Out of range')
        self.isOutOfRange(self.role)

    def isOutOfRange(self, roleValue: int):
        if roleValue > self.admin or roleValue < 0:
            raise RangeError(f'{self.role} Out of range [0x0000, {hex(self.admin)}]')

    def __add__(self, roleValue: int):
        self.isOutOfRange(roleValue)
        return Role(self.role | roleValue)

    def __iadd__(self, roleValue: int):
        self.isOutOfRange(roleValue)
        self.role = self.role | roleValue
        return self

    def __sub__(self, roleValue: int):
        self.isOutOfRange(roleValue)
        return Role(self.role & (~roleValue))

    def __isub__(self, roleValue: int):
        self.isOutOfRange(roleValue)
        self.role = self.role & (~roleValue)
        return self

    def __contains__(self, roleValue: int):
        if self.role & roleValue == 0:
            return False
        return self.role & roleValue == roleValue

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if SUPER_ADMIN < 16:
            return f'{self.role:04b}'
        if SUPER_ADMIN < 16**2:
            return f'{self.role:08b}'
        if SUPER_ADMIN < 16**3:
            return f'{self.role:016b}'
        if SUPER_ADMIN < 16**4:
            return f'{self.role:032b}'


if __name__ == '__main__':
    role = Role(ROLE.Home)
    print(role)
    print(ROLE.Report in role)
    role += ROLE.MemberList
    print(ROLE.MemberList in role)
    role -= ROLE.MemberList
    print(ROLE.MemberList in role)
