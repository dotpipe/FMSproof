import math

def is_real_integrand(radius, tolerance=1e-6):
    # Calculate the length of a semicircle with the given radius
    semicircle_length = math.pi * (radius * 0.56418958354775628694807945156085) ** 2
    print(semicircle_length)
    # Use the n function to calculate the length of the integrand
    integrand_length, no = n(radius, int(semicircle_length))
    print(integrand_length)
    print(no)
    # Compare the two lengths within the given tolerance
    return abs(semicircle_length - integrand_length)

def n(nonce, semicircle, length=2):
    familiar = 0
    segment_length = 2
    n = 0
    nonce = nonce
    midpoint = 1
    while familiar < semicircle:
        midpoint = nonce / segment_length
        
        x0, y0 = 0, math.sin(nonce)
        x1, y1 = 1, math.cos(nonce)
        
        dx = x1 - x0
        dy = y1 - y0
        
        segment_length = (dx**2 + dy**2) / 2 
        
        familiar += segment_length
        print(familiar)
        n += 1
        nonce -= 1
    
    return familiar, n # Test the function
radius = 10
result = is_real_integrand(radius)
print(f"Is the function the real integrand for a semicircle with radius {radius}? {result}")
