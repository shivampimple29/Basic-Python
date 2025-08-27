def CTF(temp):
    return ((9/5)*temp-32)

temp=int(input('Enter the temp:'))
ans=CTF(temp)
print(f'''Temperature in celsius is :{temp}
Temperature in fahrenheit is :{ans}''')
