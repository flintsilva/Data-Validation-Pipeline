# Data Validation and Defensive Security Pipeline
### [PT-BR] Pipeline de Sanitização e Validação Defensiva de Dados

---

## 🇺🇸 English Version

This project simulates a critical data processing and sanitization layer for customer registration inputs (specifically Brazilian CPF numbers) within a Back-end ecosystem. It was developed to demonstrate core concepts of Data Engineering, robust string manipulation, and Application Security (AppSec) using pure Python.

### 🚀 Features

The script processes raw string inputs, simulating data received from an external API or form, and executes a multi-stage validation pipeline:
1. **Defensive Security:** Preventive detection and blocking of logical injection attacks (SQL Injection) by auditing raw strings for malicious query patterns.
2. **Data Sanitization:** Cleaning structural noise (spaces, dots, hyphens) using Regular Expressions (`re.sub`), ensuring a standardized payload.
3. **Integrity Auditing:** Identification and blocking of false-positives that usually bypass algorithmic checks (such as structurally invalid repetitive sequences like `111.111.111-11`).
4. **Algorithmic Validation:** Implementation of the official Brazilian Revenue (Receita Federal) Modulo 11 algorithm via loop structures (`for`) to mathematically verify both check digits.
5. **Architectural Isolation:** Uses Python's native `if __name__ == "__main__":` block to isolate unit tests, ensuring the validation functions can be safely imported by other corporate systems without triggering test logs.

### 🛠️ Technologies
* **Python 3.x** (Using native `re` module for Regex and mathematical operators)
