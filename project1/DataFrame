import random
import pandas as pd
import time

# Ορισμός seed σε 2565.
random.seed(2565)

# Λίστα για αποθήκευση των τυχαίων αριθμών πιστωτικών καρτών.
numbers = []

# Δημιουργία 20000 τυχαίων αριθμών πιστωτικών καρτών.
for _ in range(20000):
    # Δημιουργία τυχαίων 16 ψήφιων αριθμών.
    random_number = random.randint(0000000000000000, 9999999999999999)
   # Προσθήκη των τυχαίων αριθμών στην λίστα numbers.
    numbers.append(random_number)
    
# Λίστα για αποθήκευση των χρεώσεων μιας τυχαίας κάρτας.
charges = []

# Δημιουργία 1000000 τυχαίων χρεώσεων.
for _ in range(1_000_000):
    # Επιλογή ένός τυχαίου αριθμού κάρτας από τη λίστα numbers.
    random_number = random.choice(numbers)
    # Επιλογή ενός τυχαίου ποσού χρέωσης από 10 έως 1000 ευρώ.
    random_amount = random.randint(10, 1000)
    # Δημιουργία ενός tuple που περιλαμβάνει το ζευγάρι (αριθμός κάρτας, ποσό) και προσθήκη του στην λίστα charges.Σε κάθε επανάληψη προστίθεται και ένα νέο ζευγάρι στην λίστα.
    charges.append((random_number, random_amount))
    
# Δημιουργία ενός DataFrame με 2 στήλες από τη λίστα charges.
charges_df = pd.DataFrame(charges, columns=['Αριθμός Κάρτας', 'Ποσό Χρέωσης'])

# Αρχή χρονομέτρησης.
start = time.time()

# Υπολογισμός των απαιτούμενων ερωτημάτων.
min_total_payment_card = charges_df.groupby('Αριθμός Κάρτας')['Ποσό Χρέωσης'].sum().idxmin()
max_total_payment_card = charges_df.groupby('Αριθμός Κάρτας')['Ποσό Χρέωσης'].sum().idxmax()
min_transaction_count_card = charges_df['Αριθμός Κάρτας'].value_counts().idxmin()
max_transaction_count_card = charges_df['Αριθμός Κάρτας'].value_counts().idxmax()

# Υπολογισμός των ποσών πληρωμής και του πλήθους συναλλαγών αντίστοιχα.
min_total_payment = charges_df.groupby('Αριθμός Κάρτας')['Ποσό Χρέωσης'].sum().min()
max_total_payment = charges_df.groupby('Αριθμός Κάρτας')['Ποσό Χρέωσης'].sum().max()
min_transaction_count = charges_df['Αριθμός Κάρτας'].value_counts().min()
max_transaction_count = charges_df['Αριθμός Κάρτας'].value_counts().max()

# Τέλος χρονομέτρησης.
elapsed_time = time.time() - start

# Εμφάνιση των αποτελεσμάτων μαζί με τα ποσά πληρωμών και το πλήθος συναλλαγών.
print(f"Η κάρτα με το μικρότερο συνολικό ποσό πληρωμών είναι η {min_total_payment_card} με ποσό {min_total_payment} ευρώ.")
print(f"Η κάρτα με το μεγαλύτερο συνολικό ποσό πληρωμών είναι η {max_total_payment_card} με ποσό {max_total_payment} ευρώ.")
print(f"Η κάρτα με το μικρότερο πλήθος συναλλαγών είναι η {min_transaction_count_card} με {min_transaction_count} χρεώσεις.")
print(f"Η κάρτα με το μεγαλύτερο πλήθος συναλλαγών είναι η {max_transaction_count_card} με {max_transaction_count} χρεώσεις.")

# Εμφάνιση συνολικού χρόνου λειτουργιών.
print(f"Ο συνολικός χρόνος εκτέλεσης είναι {elapsed_time:.2f} δευτερόλεπτα.")
