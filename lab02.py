h_1 = int(input())
m_1 = int(input())
h_2 = int(input())
m_2 = int(input())

hour_1 = h_1 + m_1/60;
hour_2 = 24. + h_2 + m_2/60;

print(hour_2 - hour_1 >= 8)
