# AuraFin: Smart Budget Tracker & Expenses Analyzer

AuraFin is a command-line Python application designed to help users manage their incomes, expenses, and savings goals efficiently. It features user authentication, income and expense tracking, summaries, intelligent financial insights, and category-wise analysis, all while allowing customization of currency symbols and savings targets.

## Features

### User Authentication
- Secure login system with:
  - Username validation (must contain at least one letter).
  - Password validation (must contain at least one digit).

### Customization
- Users can:
  - Choose their preferred currency symbol (e.g., $, Rs, INR).
  - Set personal savings goals.

### Income Management
- Add new income entries with optional notes.
- List all income records with notes.
- Edit existing income entries.
- Delete income entries.

### Expense Management
- Add new expenses with category and optional notes.
- List all expenses grouped by category.
- Edit individual expenses (amount, category, and note).
- Delete expense entries.

### Summary & Analysis
- Overview of:
  - Total income
  - Total expenses
  - Current balance
- Intelligent financial tips based on balance.
- Goal-based feedback (e.g., saving above goal, spending too much).
- Optional category-wise analysis:
  - User-defined limits per category.
  - Insights on overspending or staying within budget.

### Input Flexibility
- Accepts formatted numbers (e.g., `10,000` or `10000`).
- Case-insensitive category handling to avoid duplicates.
- Skippable optional fields (like notes).

### User Interface
- Clear and interactive command-line interface.
- Menu-driven navigation for ease of use.
- Friendly error handling and prompts for valid inputs.

## Program Flow

1. **Login**: User logs in with valid credentials.
2. **Preferences**: User sets currency and savings goal.
3. **Menu**: User navigates through various options:
   - Add income/expense
   - View or edit entries
   - Analyze summary and spending habits
   - Export final report on exit

## Technologies Used

- **Language**: Python 3
- **Data Storage**: In-memory lists (no external file or database dependency)
- **Validation**: Custom logic for username/password and numeric fields

## How to Run

1. Make sure you have Python 3 installed.
2. Run the script in your terminal or preferred IDE:
   ```bash
   python aurafin.py
