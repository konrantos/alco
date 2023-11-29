#Δημιουργία αντικειμένου της κλάσης Linear_Probing_Hash_Table.
hash_table = Linear_Probing_Hash_Table()
Ν=10_000
# Εκτέλεση των ίδιων λειτουργιών όπως και με το λεξικό αλλά με χρήση του πίνακα κατακερματισμού.

for _ in range(20_000):
    random_number = random.randint(0000000000000000, 9999999999999999)
    numbers.append(random_number)

for _ in range(Ν): 
    random_number = random.choice(numbers)
    random_amount = random.randint(10, 1000)
    
    # Έλεγχος αν ο αριθμός της κάρτας υπάρχει στον πίνακα κατακερματισμού.
    if hash_table.get(random_number) is None:
        # Αν ο αριθμός πιστωτικής κάρτας δεν υπάρχει, τότε προσθέτουμε ένα νέο στοιχείο στον πίνακα κατακερματισμού. 
        #Εισάγουμε ως κλειδί τον αριθμό πιστωτικής κάρτας, και η τιμή της είναι μια λίστα που περιέχει το ποσό της χρέωσης και τον αριθμό 1 (πλήθος συνναλαγών της κάρτας).
        hash_table.put(random_number, [random_amount, 1])
    else:
        # Αλλιώς, γίνεται ενημέρωση του στοιχείου του πίνακα κατακερματισμού με τη νέα χρέωση.
        card_info = hash_table.get(random_number)
        # Αυξάνουμε το ποσό χρέωσης της κάρτας με το τυχαίο ποσό.
        card_info[0] += random_amount
         # Αυξάνουμε το πλήθος των συναλλαγών κατά 1.
        card_info[1] += 1

# Υπολογισμός και εκτύπωση των αποτελεσμάτων και του αντίστοιχου χρόνου χρησιμοποιώντας τον πίνακα κατακερματισμού.
start = time.time()

min_total_payment_card_table = min(hash_table.table, key=lambda item: item[1][0] if item is not None else float('inf'))
max_total_payment_card_table = max(hash_table.table, key=lambda item: item[1][0] if item is not None else float('-inf'))
min_transaction_count_card_table = min(hash_table.table, key=lambda item: item[1][1] if item is not None else float('inf'))
max_transaction_count_card_table = max(hash_table.table, key=lambda item: item[1][1] if item is not None else float('-inf'))

elapsed_time_table = time.time() - start

print(f"\nΑποτελέσματα χρησιμοποιώντας τον πίνακα κατακερματισμού για {Ν} επαναλήψεις:")
print(f"Η κάρτα με το μικρότερο συνολικό ποσό πληρωμών είναι η {min_total_payment_card_table[0]} με ποσό {min_total_payment_card_table[1][0]} ευρώ.")
print(f"Η κάρτα με το μεγαλύτερο συνολικό ποσό πληρωμών είναι η {max_total_payment_card_table[0]} με ποσό {max_total_payment_card_table[1][0]} ευρώ.")
print(f"Η κάρτα με το μικρότερο πλήθος συναλλαγών είναι η {min_transaction_count_card_table[0]} με {min_transaction_count_card_table[1][1]} χρεώσεις.")
print(f"Η κάρτα με το μεγαλύτερο πλήθος συναλλαγών είναι η {max_transaction_count_card_table[0]} με {max_transaction_count_card_table[1][1]} χρεώσεις.")

print(f"Ο συνολικός χρόνος εκτέλεσης είναι {elapsed_time_table:.2f} δευτερόλεπτα.")
