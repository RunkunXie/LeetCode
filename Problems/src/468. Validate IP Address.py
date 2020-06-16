class Solution:
    """my sol, 1st attempt"""
    def validIPAddress(self, IP: str) -> str:

        if '.' in IP:
            ip = IP.split('.')
            if len(ip) != 4:
                return "Neither"
            for s in ip:
                if not s.isdigit() or (s.startswith('0') and len(s) > 1) or len(s) > 4 or not 0 <= int(s) <= 255:
                    return "Neither"
            return "IPv4"

        elif ':' in IP:
            ip = IP.split(':')
            if len(ip) != 8:
                return "Neither"
            for s in ip:
                if not s.isalnum() or len(s) > 4:
                    return "Neither"
                for c in s:
                    if c.isalpha() and c.lower() not in "abcdef":
                        return "Neither"
            return "IPv6"

        return "Neither"