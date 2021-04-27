UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="

def sandwich(func):
    def sandwich_wrapper(*args, **kwargs):
        print(UPPER_SLICE)
        func(*args, **kwargs)
        print(LOWER_SLICE)
    return sandwich_wrapper

@sandwich
def add_integrants(integrants):
    print(' / '.join(integrants))
    
add_integrants(['bacon', 'tomato'])