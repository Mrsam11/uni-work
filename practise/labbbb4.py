a = open("Sameer", "w")
a.write("Hello My Name is Sameer")
a.close()
a = open("Sameer", "a")
a.write("I am A student")
a.close()
a = open("Sameer", "r")
print(a.read())
a.close()
a = open("Sameer", "w")
a.flush()
a.close()