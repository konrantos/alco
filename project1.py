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
    
# Ενδεικτική εμφάνιση των 5 πρώτων χρεώσεων.
for i in range(5):
    # Δημιουργία μεταβλητής first_charges που αποθηκε΄θει τις πρώτες i τυχαίες χρεώσεις της λίστας charges.
    first_charges = charges[i]
    # Σπάσιμο του tuple σε δύο μεταβλητές, τις random_number και random_amount. 
    random_number, random_amount = first_charges
    # Εκτύπωση των χρεώσων.
    print(f"Χρέωση {i+1}: Αριθμός: {random_number}, Ποσό: {random_amount} ευρώ.")

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
print(f"Κάρτα με το μικρότερο συνολικό ποσό πληρωμών: {min_total_payment_card}, Ποσό: {min_total_payment} ευρώ.")
print(f"Κάρτα με το μεγαλύτερο συνολικό ποσό πληρωμών: {max_total_payment_card}, Ποσό: {max_total_payment} ευρώ.")
print(f"Κάρτα με το μικρότερο πλήθος συναλλαγών: {min_transaction_count_card}, Πλήθος: {min_transaction_count} χρεώσεις.")
print(f"Κάρτα με το μεγαλύτερο πλήθος συναλλαγών: {max_transaction_count_card}, Πλήθος: {max_transaction_count} χρεώσεις.")

# Εμφάνιση συνολικού χρόνου λειτουργιών.
print(f"Χρόνος εκτέλεσης: {elapsed_time:.2f} δευτερόλεπτα.")
