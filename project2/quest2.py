def read_file(file_path):
    # Άνοιγμα του αρχείου με τη διαδρομή file_path για ανάγνωση.
    with open(file_path, 'r') as file:
         # Διάβασμα όλων των γραμμών του αρχείου.
        lines = file.readlines()
    # Μετατροπή της πρώτης γραμμής σε ακέραιο για τον αριθμό των εργασιών.
    num_jobs = int(lines[0].strip())
    # Μετατροπή της δεύτερης γραμμής σε ακέραιο για τον αριθμό των μηχανημάτων.
    num_machines = int(lines[1].strip())

    # Προσπάθεια εμφάνισης του βέλτιστου makespan μέσω της τρίτης γραμμής και συνέχεια των υπολογισμομών από την τέταρτη γραμμή.
    try:
        optimal_makespan = int(lines[2].strip())
        job_data_start_index = 3
    except ValueError:
        # Αν η τρίτη γραμμή δεν είναι ακέραιος, υποθέτουμε ότι δεν παρέχεται βέλτιστο makespan(None) και συνεχίζουμε τους υπολογισμούς από την τρίτη γραμμή.
        optimal_makespan = None
        job_data_start_index = 2

    # Υπολογισμός του χρόνου που πρέπει να περάσει από την κάθε μηχανή η κάθε μία από τις εργασίες.
    job_times = []
    # For loop από την γραμμή του job_data_start_index και φτάνοντας μέχρι την γραμμή num_jobs(αριθμός εργασιών) + job_data_start_index.
    for i, line in enumerate(lines[job_data_start_index:num_jobs + job_data_start_index]):
        # Κάθε γραμμή διαχωρίζεται σε ακέραιους αριθμούς και αποθηκεύεται στη λίστα job_times.
        annotated_line = f"Εργασία {i + 1} " + str(list(map(int, line.split())))
        job_times.append(annotated_line)

    # Υπολογισμός της σειράς επίσκεψης των μηχανών για κάθε μία από τις εργασίες, με αντίστοιχη διαδικασία.
    job_sequences = []
    for i, line in enumerate(lines[num_jobs + job_data_start_index:]):
        annotated_line = f"Εργασία {i + 1} " + str(list(map(int, line.split())))
        job_sequences.append(annotated_line)
        
    # Επιστροφή ενός tuple.   
    return num_jobs, num_machines, optimal_makespan, job_times, job_sequences


# Ορισμός λίστας με τις διαδρομές των αρχείων.
file_paths = [
    r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la01.txt',
    r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la02.txt',
    r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la03.txt',
    r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la04.txt',
    r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la05.txt',
    r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\mt06.txt',
    r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\mt10.txt',
    r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\mt20.txt'
]

# Αρχικοποίηση λεξικού για αποθήκευση δεδομένων από κάθε αρχείο.
data = {}
# Επανάληψη για κάθε διαδρομή αρχείου στη λίστα file_paths.
for file_path in file_paths:
    # Ανάγνωση και αποθήκευση δεδομένων από το αρχείο.
    num_jobs, num_machines, optimal_makespan, job_times, job_sequences = read_file(file_path)
    # Αποθήκευση των δεδομένων στο λεξικό data με κλειδί τη διαδρομή του αρχείου.
    data[file_path] = {
        'Πλήθος εργασιών': num_jobs,
        'Πλήθος μηχανών': num_machines,
        'Βέλτιστο makespan': optimal_makespan,
        'Χρόνος σε κάθε μηχανή' : job_times,
        'Σειρά επίσκεψης μηχανών': job_sequences
    }

# Εκτύπωση των δεδομένων από ένα συγκεκριμένο αρχείο για παράδειγμα.
print(data[r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la01.txt'])
