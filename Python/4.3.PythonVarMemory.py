##Program (PythonVarMemory.py)
#Program to demo Python Variable Memory allocation & de-allocation

#Same-var diff-values(latest-value)
a=10
print(a)
a=10.5
print(a)
a="Hello"
print(a)

print()
#Diff-vars Same-value
a=10
b=10
print(a,b)
print(id(a),id(b))

print()
#Diff-vars diff-values
a=10
b=20
print(a,b)
print(id(a),id(b))



