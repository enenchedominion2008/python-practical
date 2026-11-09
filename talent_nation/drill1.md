# Py-Section 1 Mission Project — The Digital Translator

## Tier 1 – The Literal Assistant

### Precise Instructions for “Make me breakfast”

1. Go to the kitchen.
2. Open the refrigerator.
3. Take out 2 fresh eggs from the egg carton.
4. Take out 1 slice of bread from the bread package.
5. Close the refrigerator.
6. Place a frying pan on the stove.
7. Turn the stove burner to medium heat.
8. Add 1 teaspoon of cooking oil to the frying pan.
9. Crack the 2 eggs into the frying pan.
10. Cook the eggs for 3 minutes, then flip them and cook for another 2 minutes.
11. While the eggs are cooking, put the slice of bread into the toaster and toast it until golden brown.
12. When the eggs are fully cooked (the whites are solid and the yolks are still slightly soft), turn off the stove.
13. Place the cooked eggs and the toast on a clean plate.
14. Put the plate on the table.
15. The task is finished when the plate with eggs and toast is on the table.

### Assumptions I had to make
- The person wants fried eggs and toast (not cereal, oatmeal, or something else).
- There are eggs and bread available in the refrigerator.
- A frying pan, stove, toaster, and plate are available.
- The person wants the food cooked and served on a plate at the table.
- “Breakfast” means a simple egg-and-toast meal.

---

## Tier 2 – ATM Algorithm

### Algorithm: Withdraw money from an ATM

1. Insert the bank card into the card reader.
2. Wait for the machine to read the card.
3. Enter the correct 4-digit PIN using the keypad.
4. Select the “Withdraw Cash” option on the screen.
5. Choose the account type (Savings or Current).
6. Enter the amount of money to withdraw.
7. Confirm that the amount is correct.
8. Wait for the machine to check the account balance and available cash.
9. Collect the cash from the cash dispenser.
10. Collect the printed receipt (if requested) and remove the bank card.

### Handling failures
- If the card cannot be read: Display “Card Error – Please try again or use another card” and eject the card.
- If the PIN is incorrect: Allow 2 more attempts. After 3 wrong attempts, retain the card and display “Card retained – Contact your bank”.
- If the requested amount is greater than the available balance: Display “Insufficient funds” and return to the amount selection screen.
- If the ATM does not have enough cash: Display “Unable to dispense this amount – Please try a smaller amount” and return to the amount selection screen.
- If the transaction cannot be completed: Cancel the transaction, eject the card, and display “Transaction failed – Please try again later”.

---

## Tier 3 – Simple Calculator

### Addition
- **Input:** Two numbers (number_1 and number_2)
- **Processing:** Add number_1 + number_2
- **Output:** The sum of the two numbers

### Subtraction
- **Input:** Two numbers (number_1 and number_2)
- **Processing:** Subtract number_2 from number_1 (number_1 − number_2)
- **Output:** The difference of the two numbers

### Multiplication
- **Input:** Two numbers (number_1 and number_2)
- **Processing:** Multiply number_1 × number_2
- **Output:** The product of the two numbers

### Division
- **Input:** Two numbers (number_1 and number_2)
- **Processing:** Divide number_1 by number_2 (number_1 ÷ number_2)
- **Output:** The quotient of the two numbers

### Division by zero (number_2 = 0)
What a well-designed program should do:  
It should detect that the second number is zero and display an error message such as “Error: Cannot divide by zero” instead of trying to perform the division. The program should not crash.

---

## Tier 4 – Data Translator

| Information     | Kind of information | Why it needs a specific representation |
|-----------------|---------------------|----------------------------------------|
| Victor          | Text / String       | Names are made of letters and must be stored as text so the computer can display and compare them correctly. |
| 30              | Integer / Whole number | Age is a whole number. Storing it as an integer allows calculations (e.g., age next year). |
| 150000.50       | Float / Decimal number | Money often has decimal places (kobo/cents). A float (or better, decimal type) is needed to keep the exact amount. |
| Yes             | Boolean (True/False)| This is a yes/no answer. Storing it as True/False makes decision-making in the program clear and efficient. |

### What could go wrong if the account balance is stored incorrectly?
If the account balance is stored as text instead of a number, the program cannot perform mathematical operations (addition, subtraction).  
If it is stored as an integer instead of a decimal, the kobo/cents part will be lost (150000.50 becomes 150000).  
This can lead to wrong balances, failed transactions, or money disappearing from the account.

---

## Tier 5 – Online Store System

### Full system explanation

1. **Customer Input**  
   The customer selects products, enters quantity, shipping address, and payment details on the website or app.

2. **Application / Program**  
   The online store software receives the customer’s order and begins processing it according to its programmed rules.

3. **Instructions**  
   The program follows a set of coded instructions: check stock, calculate total price, verify payment, create order record, and prepare shipping.

4. **Data Processing**  
   The system calculates the total cost (price × quantity + shipping), checks if the items are available, and processes the payment with the bank.

5. **Stored Data**  
   Customer details, order details, product stock levels, and payment status are saved in the database.

6. **Result / Output**  
   The customer receives an order confirmation, the warehouse receives a packing list, and the stock quantity is reduced.

### Simplified chain (in my own words)

Customer  
↓  
Enters order details  
↓  
Program receives and processes the order  
↓  
System checks stock and payment  
↓  
Data is stored and stock is updated  
↓  
Result (confirmation + shipping starts)

### Reflection questions
- What is the computer doing?  
  Following the program’s instructions step by step to process the order.
- What is the program doing?  
  Turning the customer’s request into a sequence of actions the computer can perform.
- What data is involved?  
  Product information, prices, stock levels, customer details, and payment information.
- What instructions are being executed?  
  Check stock → Calculate total → Process payment → Save order → Update stock → Send confirmation.
- What is the output?  
  Order confirmation to the customer and packing instructions to the warehouse.
- What information might need to be stored?  
  Customer details, order history, current stock levels, and transaction records.

---

## Final Reflection

**Statement:**  
“A computer does not understand the real world directly. It works with representations of information and follows instructions for processing those representations.”

**My explanation:**  
A computer has no real understanding of eggs, money, or online shopping. It only works with numbers, text, and true/false values that we give it. We must translate real-world things into data the computer can store and process, and we must write clear step-by-step instructions (algorithms) so the computer knows exactly what to do with that data.

**How this applies to the examples:**
- **Breakfast:** The computer does not know what “breakfast” means. We had to break it into exact steps and specific items.
- **ATM:** The machine does not understand money. It only follows programmed rules about cards, PINs, and numbers.
- **Calculator:** The computer does not understand addition or division. It only performs mathematical operations on numbers we provide.
- **Customer data:** Names, ages, and balances must be stored in the correct format (text, integer, decimal) or the system will make mistakes.
- **Online store:** The computer does not understand shopping. It only follows instructions that process product codes, quantities, and payment data.

---