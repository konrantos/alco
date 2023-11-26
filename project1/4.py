#Δημιουργία αντικειμένου της κλάσης Linear_Probing_Hash_Table.
hash_table = Linear_Probing_Hash_Table()

# Εκτέλεση των ίδιων λειτουργιών όπως και με το λεξικό αλλά με χρήση του πίνακα κατακερματισμού.
for _ in range(1_000_000):
    random_number = random.choice(numbers)
    random_amount = random.randint(10, 1000)
    
    # Έλεγχος αν ο αριθμός της κάρτας υπάρχει στον πίνακα κατακερματισμού.
    if hash_table.get(random_number) is None:
        # Αν ο αριθμός πιστωτικής κάρτας δεν υπάρχει, τότε προσθέτουμε ένα νέο στοιχείο στον πίνακα κατακερματισμού. 
        #Εισάγουμε ως κλειδί τον αριθμό πιστωτικής κάρτας, και η τιμή της είναι μια λίστα που περιέχει το ποσό της χρέωσης και τον αριθμό 1 (πλήθος συνναλαγών της κάρτας).
        hash_table.put(random_number, [random_amount, 1])
    else:
        # Αλλιώς, γίνεται Ενημέρωση του στοιχείου του πίνακα κατακερματισμού με τη νέα χρέωση.
        card_info = hash_table.get(random_number)
        # Αυξάνουμε το ποσό χρέωσης της κάρτας με το τυχαίο ποσό.
        card_info[0] += random_amount
         # Αυξάνουμε το πλήθος των συναλλαγών κατά 1.
        card_info[1] += 1
        # Ενημέρωση του πίνακα κατακερματισμού με τα νέα στοιχεία της κάρτας, βάζοντας την ενημερωμένη λίστα στη θέση της προηγούμενης.
        hash_table.put(random_number, card_info)

# Υπολογισμός και εκτύπωση των αποτελεσμάτων και του αντίστοιχου χρόνου χρησιμοποιώντας τον πίνακα κατακερματισμού.
start = time.time()

min_total_payment_card_table = min(hash_table.table, key=lambda item: item[1][0])
max_total_payment_card_table = max(hash_table.table, key=lambda item: item[1][0])
min_transaction_count_card_table = min(hash_table.table, key=lambda item: item[1][1])
max_transaction_count_card_table = max(hash_table.table, key=lambda item: item[1][1])

elapsed_time = time.time() - start

print("\nΑποτελέσματα χρησιμοποιώντας τον Πίνακα Κατακερματισμού:")
print(f"Κάρτα με το μικρότερο συνολικό ποσό πληρωμών: {min_total_payment_card_table[0]} με ποσό {min_total_payment_card_table[1][0]} ευρώ.")
print(f"Κάρτα με το μεγαλύτερο συνολικό ποσό πληρωμών: {max_total_payment_card_table[0]} με ποσό {max_total_payment_card_table[1][0]} ευρώ.")
print(f"Κάρτα με το μικρότερο πλήθος συναλλαγών: {min_transaction_count_card_table[0]} με {min_transaction_count_card_table[1][1]} χρεώσεις.")
print(f"Κάρτα με το μεγαλύτερο πλήθος συναλλαγών: {max_transaction_count_card_table[0]} με {max_transaction_count_card_table[1][1]} χρεώσεις.")

print(f"Ο συνολικός χρόνος εκτέλεσης είναι {elapsed_time:.2f} δευτερόλεπτα.")
