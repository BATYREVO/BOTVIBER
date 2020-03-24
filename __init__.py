from datetime import timedelta

a = None
if a is None:
    a = timedelta(minutes=1)
a = a + timedelta(minutes=1)

print(a)