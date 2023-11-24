import random
import time

# Ορισμός seed σε 2565.
random.seed(2565)

# Λίστα για αποθήκευση των τυχαίων αριθμών πιστωτικών καρτών.
numbers = []

# Λεξικό για αποθήκευση των χρεώσεων για κάθε κάρτα.
# Στήν θέση [0] θα αποθηκευτεί το ποσό χρεώσεων και στην θέση [1] το πλήθος των χρεώσεων.
card_charges = {}

# Δημιουργία 20000 τυχαίων αριθμών πιστωτικών καρτών.
for _ in range(20000):
    # Δημιουργία τυχαίων 16 ψήφιων αριθμών.
    random_number = random.randint(0000000000000000, 9999999999999999)
    # Προσθήκη των τυχαίων αριθμών στην λίστα numbers.
    numbers.append(random_number)

# Δημιουργία 1.000.000 τυχαίων χρεώσεων.
for _ in range(1_000_000):
    # Επιλογή τυχαίου αριθμού κάρτας από τη λίστα numbers.
    random_number = random.choice(numbers)
    # Επιλογή τυχαίου ποσού χρέωσης από 10 έως 1000 ευρώ.
    random_amount = random.randint(10, 1000)
    
    # Αν ο αριθμός κάρτας δεν υπάρχει στο λεξικό, προσθέτεται και αρχικοποιείται μαζί με το αντοίστιχο ποσό χρέωσης.
    if random_number not in card_charges:
        card_charges[random_number] = [random_amount, 1]
    else:
        # Ενώ, αν προυοπάρχει ο αριθμός κάρτας στό λεξικό προσθέτεται το ποσό χρέωσης στο ήδη υπάρχον ποσό και αυξάνεται κατά 1 το πλήθος των συναλλαγών.
        card_charges[random_number][0] += random_amount
        card_charges[random_number][1] += 1

# Αρχή χρονομέτρησης.
start = time.time()

# Υπολογισμός των απαιτούμενων ερωτημάτων, με χρήση των αντίστοιχων συναρτήσεων και σαν κρτιτίριο την αντίστοιχη θέση του λεξικού. 
min_total_payment_card = min(card_charges, key=lambda card: card_charges[card][0])
max_total_payment_card = max(card_charges, key=lambda card: card_charges[card][0])
min_transaction_count_card = min(card_charges, key=lambda card: card_charges[card][1])
max_transaction_count_card = max(card_charges, key=lambda card: card_charges[card][1])

# Τέλος χρονομέτρησης.
elapsed_time = time.time() - start

# Εμφάνιση των αποτελεσμάτων μαζί με τα ποσά πληρωμών και το πλήθος συναλλαγών.
print(f"Η κάρτα με το μικρότερο συνολικό ποσό πληρωμών είναι η {min_total_payment_card} με ποσό {card_charges[min_total_payment_card][0]} ευρώ.")
print(f"Η κάρτα με το μεγαλύτερο συνολικό ποσό πληρωμών είναι η {max_total_payment_card} με ποσό {card_charges[max_total_payment_card][0]} ευρώ.")
print(f"Η κάρτα με το μικρότερο πλήθος συναλλαγών είναι η {min_transaction_count_card} με {card_charges[min_transaction_count_card][1]} χρεώσεις.")
print(f"Η κάρτα με το μεγαλύτερο πλήθος συναλλαγών είναι η {max_transaction_count_card} με {card_charges[max_transaction_count_card][1]} χρεώσεις.")

# Εμφάνιση συνολικού χρόνου λειτουργιών.
print(f"Ο συνολικός χρόνος εκτέλεσης είναι {elapsed_time:.2f} δευτερόλεπτα.")
