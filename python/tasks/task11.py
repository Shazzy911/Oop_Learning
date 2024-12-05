### Problem 6: **Abstraction Using Abstract Base Class** (Intermediate)

**Description:**  
Use the `abc` module to create an abstract base class `Employee` with an abstract method `calculate_pay()`. Create two subclasses, `SalariedEmployee` and `HourlyEmployee`, that implement `calculate_pay()` based on fixed salary and hourly rate respectively.

**Guidance:**  
This problem demonstrates abstraction by requiring each subclass to implement its own way of calculating pay.

**Goal:**  
```python
# Expected Output Example:
# Salary of salaried employee: $3000
# Salary of hourly employee: $200 (for 20 hours at $10/hour)
```

---