from jupyturtle import make_turtle, forward, left, right, penup, pendown
import math

# تشغيل السلحفاة
make_turtle()

# حل تمرين rhombus (المعين)
def rhombus(side, angle):
    for i in range(2):
        forward(side)
        left(angle)
        forward(side)
        left(180 - angle)

# جرب الرسم
rhombus(50, 60)

# خلي النافذة مفتوحة 5 ثواني عشان تشوف الرسم
import time
time.sleep(5)