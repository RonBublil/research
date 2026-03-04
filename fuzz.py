import random
import string

TARGET = 0x394  # 916

# You can adjust the character set
CHARSET = string.ascii_letters + string.digits

def random_string(max_len=32):
    length = random.randint(1, max_len)
    return ''.join(random.choice(CHARSET) for _ in range(length))

def byte_sum(s: str) -> int:
    return sum(ord(c) for c in s)

while True:
    s = random_string()
    total = byte_sum(s)

    if total == TARGET:
        print(f"Found string: {s}")
        print(f"Sum: {total} (0x{total:x})")
        break
