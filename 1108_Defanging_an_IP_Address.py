class Solution(object):
    def defangIPaddr(self, address):
        defanged_address = ""
        for char in address:
            if char == ".":
                defanged_address += "[.]"
            else:
                defanged_address += char
        return defanged_address