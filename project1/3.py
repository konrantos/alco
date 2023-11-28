# Kλάση για την υλοποίηση ενός πίνακα κατακερματισμού με γραμμική διερεύνηση.
class Linear_Probing_Hash_Table:
    
    
    
    # Συνάρτηση αρχικοποίησης του πίνακα κατακερματισμού.
    def __init__(self, size=101):
        # Το default size του πίνακα κατακερματισμού είναι 101.
        self.size = size 
        # Δημιουργία μιας λίστας με size στοιχεία, όλα αρχικοποιημένα στην τιμή None.
        # Η τιμή None αναπαριστά την έλλειψη ή την απουσία μίας τιμής.
        self.table = [None] * size
        # Αρχικό load fαctor = 0%.
        self.load_factor = 0
        
        
        
    # Συνάρτηση κατακερματισμού με χρήση της Jenkins hash function.
    def hash_function(self, key):
        hash_value = 0
        key_str = str(key)
        for char in key_str:
            hash_value += ord(char)
            hash_value += (hash_value << 10)
            hash_value ^= (hash_value >> 6)
        hash_value += (hash_value << 3)
        hash_value ^= (hash_value >> 11)
        hash_value += (hash_value << 15)
        return hash_value % self.size
        
        
        
    # Συνάρτηση εισγωγής ενός ζευγαριού (key, value) στον πίνακα κατακερματισμού.
    def put(self, key, value):
        # Υπολογισμός του δείκτη (index) όπου θα αποθηκευτεί ένα κλειδί (key) στον πίνακα κατακερματισμού.
        index = self.hash_function(key)
        # Γραμμική διερεύνηση για εύρεση κενής θέσης.
        # Η while επαναλαμβάνεται μέχρι να βρεθεί μια κενή θέση στον πίνακα.
        # Κάθε φορά που εκτελείται η while, ο δείκτης (index) αυξάνεται κατά 1 και υπολογίζεται ο νέος δείκτης με χρήση του υπολοίπου της διαίρεσης με το μέγεθος του πίνακα ((index + 1) % self.size).
        while self.table[index] is not None:
            index = (index + 1) % self.size
        # Εισαγωγή ενός στοιχείου στον πίνακα.
        self.table[index] = (key, value)
        # Ενημέρωση του συντελεστή φόρτωσης.
        self.load_factor += 1 / self.size
        # Έλεγχος για αναγκαίο rehash του πίνακα κατακερματισμού, αν το load factor >= 70%.
        if self.load_factor >= 0.7:
            self.rehash()
        

    
    
    
    # Συνάρτηση αναζήτησης ενός κλειδού απο τον πίνακα κατακερματισμού.
    def get(self, key):
        index = self.hash_function(key)
        # Η while εκτελείται όσο η θέση του πίνακα (self.table[index]) έχει κάποιο στοιχείο σε αυτή την θέση.
        while self.table[index] is not None:
            # Σε κάθε επανάληψη, ελέγχουμε αν το κλειδί του τρέχοντος στοιχείου είναι ίσο με το κλειδί που ψάχχνουμε.  
            if self.table[index][0] == key:
                #Αν βρεθεί, επιστέφεται η σχετική τιμή.    
                return self.table[index][1]
            # Αν το στοιχείο δεν είναι αυτό που αναζητούμε, μετακινούμαστε στο επόμενο. 
            # Η επιλογή του επόμενου στοιχείου γίνεται με χρήση γραμμική διερεύνησης.
            index = (index + 1) % self.size
        # Επιστροφή 'None' αν δε βρεθεί το κλειδί.
        return None
            
            
            
    # Συνάρτηση ελέγχου για το αν ένας αριθμός είναι πρώτος.
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
        
      
      
    # Συνάρτηση για την εύρεση επόμενου πρώτου αριθμού μεγαλύτερου ή ίσου με το n.
    def next_prime(self, n):
        n += 1
        while not self.is_prime(n):
            n += 1
        return n
          
       
       
    # Συνάρτηση αύξησης του μεγέθους του πίνακα κατακερματισμού στον επόμενο τουλάχιστον διπλάσιο πρώτο αριθμό.
    def rehash(self):
        # Αύξηση του μεγέθους του πίνακα κατακερματισμού.
        new_size = self.next_prime(self.size * 2)
        # Ο νέος πίνακας κατακερματισμού αρχικοποιείται με κενές θέσεις.
        new_table = [None] * new_size
        # Αρχικοποίηση μετρητής πραγματικών στοιχείων.
        count = 0 
        # Επανατοποθέτηση υπαρχόντων στοιχείων στο νέο μέγεθος πίνακα για κάθε ζεύγος item που δεν έχει τιμή 'Νονε'.
        for item in self.table:
            if item is not None:
                # Unpacking του tuple item σε δύο μεταβλητές, key και value.
                key, value = item 
                # Υπολογισμός νέου δείκτη (index) για το νέο μέγεθος.
                index = self.hash_function(key)
                # Εύρεση νέας κενής θέσης με γραμμική διερεύνηση.
                while new_table[index] is not None:
                    index = (index + 1) % new_size
                # Το στοιχείο τοποθετείται στην εντοπισμένη κενή θέση του νέου πίνακα, βάζοντας το tuple (key, value).
                new_table[index] = (key, value)
                # Αυξάνεται ο μετρητής για κάθε πραγματικό στοιχείο.
                count += 1
        # Ενημέρωση του μεγέθους, του πίνακα κατακερματισμού και του load factor.
        self.size = new_size
        self.table = new_table
        self.load_factor = count / new_size
