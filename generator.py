
#### **generator.py**
```python
import matplotlib.pyplot as plt
import random

data = [random.randint(1, 100) for _ in range(100)]
plt.hist(data, bins=10, edgecolor='black')
plt.title("Random Number Distribution")
plt.show()
