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
        # Αν η τρίτη γραμμή δεν είναι ακέραιος, υποθέτουμε ότι δεν παρέχεται βέλτιστο makespan (None) και συνεχίζουμε τους υπολογισμούς από την τρίτη γραμμή.
        optimal_makespan = None
        job_data_start_index = 2

    job_times = [list(map(int, lines[i].split())) for i in range(job_data_start_index, job_data_start_index + num_jobs)]
    job_sequences = [list(map(int, lines[i].split())) for i in range(job_data_start_index + num_jobs, job_data_start_index + 2 * num_jobs)]
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
# print(data[r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la01.txt']),


def calculate_makespan_spt(num_jobs, num_machines, job_times, job_sequences):
    # Δημιουργία λίστας για την καταγραφή του τρέχοντος χρόνου για κάθε μηχάνημα.
    machine_schedule = [0] * num_machines
    # Δημιουργία λίστας για την καταγραφή του χρόνου ολοκλήρωσης για κάθε εργασία.
    job_completion = [0] * num_jobs
    # Κατάταξη των εργασιών με βάση τον συνολικό ελάχιστο χρόνο επεξεργασίας όπως αναφέρει ο SPT.
    sorted_jobs = sorted(range(num_jobs), key=lambda x: sum(job_times[x]))
    for job in sorted_jobs:
        for step in range(num_machines):
            machine = job_sequences[job][step] - 1
            time = job_times[job][step]
            machine_schedule[machine] = max(machine_schedule[machine], job_completion[job]) + time
            job_completion[job] = machine_schedule[machine]
    # Επιστροφή του makespan.
    return max(machine_schedule)


# Συνάρτηση για την επεξεργασία κάθε αρχείου.
def process_file(file_path):
    # Ανάγνωση και επεξεργασία των δεδομένων από το αρχείο.
    num_jobs, num_machines, optimal_makespan, job_times, job_sequences = read_file(file_path)
    # Υπολογισμός του makespan χρησιμοποιώντας τον κανόνα SPT.
    makespan_spt = calculate_makespan_spt(num_jobs, num_machines, job_times, job_sequences)
    # Εκτύπωση των αποτελεσμάτων για κάθε αρχείο.
    print(f'Αρχείο: {file_path}')
    print(f'Υπολογισμένο Makespan (SPT): {makespan_spt}')
    if optimal_makespan is not None:
        print(f'Βέλτιστο Makespan: {optimal_makespan}')
        print(f'Διαφορά: {makespan_spt - optimal_makespan}')


if __name__ == '__main__':
    for file_path in file_paths:
        process_file(file_path)
