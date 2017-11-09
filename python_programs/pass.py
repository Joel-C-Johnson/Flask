import uuid
import re
verification_code = str(uuid.uuid4()).replace("-", "")
a = re.sub(r'[a-zA-Z]', r'', verification_code)
b = re.sub(r'[2,4,6,8]', r'', a)
m = list(set(b))
print m
