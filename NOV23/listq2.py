products = ["Laptop", "Mobile", "Keyboard"]


print(f"At first teh lits {products}")

products.append("Mouse")

products.extend(["Monitor", "Headphones"])

print(f"after extens 2products {products}")

products.insert(1,"Tablet")

print(f"after inset at index 1 {products}")

products.remove("Keyboard")

print(f"At after remove keyboar {products}")