import matplotlib.pyplot as plt
import numpy as np

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
print(data[r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la01.txt']),



def calculate_makespan_spt(num_jobs, num_machines, job_times, job_sequences):
    # Αρχικοποίηση των προγραμμάτων των μηχανημάτων
    # Δημιουργία λίστας για την καταγραφή του τρέχοντος χρόνου για κάθε μηχάνημα
    machine_schedule = [0] * num_machines

    # Αρχικοποίηση των χρόνων ολοκλήρωσης εργασιών
    # Δημιουργία λίστας για την καταγραφή του χρόνου ολοκλήρωσης για κάθε εργασία
    job_completion = [0] * num_jobs

    # Κατάταξη των εργασιών με βάση τον συνολικό ελάχιστο χρόνο επεξεργασίας
    # Αυτό είναι το βασικό βήμα του αλγορίθμου SPT, όπου προτεραιοποιούνται οι εργασίες με τον συντομότερο συνολικό χρόνο
    sorted_jobs = sorted(range(num_jobs), key=lambda x: sum(job_times[x]))

    # Διαδικασία προγραμματισμού για κάθε εργασία
    for job in sorted_jobs:
        # Διαδοχική επεξεργασία κάθε βήματος (μηχανήματος) της εργασίας
        for step in range(num_machines):
            # Εύρεση του αντίστοιχου μηχανήματος για το τρέχον βήμα
            machine = job_sequences[job][step] - 1
            # Χρόνος επεξεργασίας για το βήμα στο συγκεκριμένο μηχάνημα
            time = job_times[job][step]
            # Ενημέρωση του προγράμματος του μηχανήματος
            # Λαμβάνεται υπόψη ο τρέχων χρόνος του μηχανήματος και η ολοκλήρωση της προηγούμενης εργασίας
            machine_schedule[machine] = max(machine_schedule[machine], job_completion[job]) + time
            # Ενημέρωση του χρόνου ολοκλήρωσης της εργασίας
            job_completion[job] = machine_schedule[machine]

    # Επιστροφή του makespan
    # Το μέγιστο στοιχείο του προγράμματος των μηχανημάτων αντιπροσωπεύει τον συνολικό χρόνο ολοκλήρωσης όλων των εργασιών
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
        
        
        

def plot_gantt_chart_with_jobs(num_machines, num_jobs, start_times, end_times, makespan):
    # Δημιουργία σχήματος και αξόνων για την απεικόνιση του διαγράμματος Gantt.
    fig, ax = plt.subplots(figsize=(12, 6))
    # Καθορισμός χρωμάτων για τις διάφορες εργασίες.
    colors = plt.cm.tab20.colors
    # Επανάληψη για κάθε εργασία και κάθε μηχάνημα.
    for job in range(num_jobs):
        for machine in range(num_machines):
            # Ανάθεση των χρόνων έναρξης και λήξης της εργασίας στο συγκεκριμένο μηχάνημα.
            start = start_times[job][machine]
            end = end_times[job][machine]
            # Δημιουργία μπάρας στο διάγραμμα αν ο χρόνος έναρξης είναι μικρότερος από τον χρόνο λήξης.
            if start < end:
                ax.barh(machine, end - start, left=start, color=colors[job % len(colors)], edgecolor='black')
    # Ορισμός των ετικετών για τους άξονες y.
    ax.set_yticks(range(num_machines))
    ax.set_yticklabels([f'M{m+1}' for m in range(num_machines)])
    # Αντιστροφή του άξονα y για να εμφανίζεται το μηχάνημα 1 στην κορυφή.
    ax.invert_yaxis()
    # Ορισμός ετικετών για τους άξονες x και y και τίτλος του διαγράμματος.
    ax.set_xlabel('Time')
    ax.set_ylabel('Machine')
    ax.set_title(f'SPT Gantt Chart (Makespan: {int(makespan)})')
    # Δημιουργία προσαρμοσμένης λεζάντας για τις εργασίες.
    custom_lines = [plt.Line2D([0], [0], color=colors[job % len(colors)], lw=4) for job in range(num_jobs)]
    # Προσθήκη λεζάντας στο διάγραμμα με αναφορά στις εργασίες και τα αντίστοιχα χρώματα τους.
    ax.legend(custom_lines, [f'Job {j+1}' for j in range(num_jobs)], loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=num_jobs)
    # Ρύθμιση της διάταξης του διαγράμματος για καλύτερη εμφάνιση.
    plt.tight_layout()
    # Εμφάνιση του διαγράμματος στην οθόνη.
    plt.show()

def read_jssp_data(file_path):
    # Άνοιγμα αρχείου με τη διαδρομή file_path για ανάγνωση.
    with open(file_path, 'r', encoding='utf-8') as file:
        # Διάβασμα του αριθμού των εργασιών από την πρώτη γραμμή του αρχείου.
        num_jobs = int(file.readline().split('#')[0].strip())
        # Διάβασμα του αριθμού των μηχανημάτων από τη δεύτερη γραμμή του αρχείου.
        num_machines = int(file.readline().split('#')[0].strip())
        # Παράλειψη της γραμμής με τον βέλτιστο χρόνο (makespan).
        file.readline()
        # Διάβασμα των χρόνων επεξεργασίας για κάθε εργασία.
        processing_times = [list(map(int, file.readline().split('#')[0].strip().split())) for _ in range(num_jobs)]
        # Διάβασμα της σειράς επίσκεψης των μηχανημάτων για κάθε εργασία.
        machine_orders = [list(map(int, file.readline().split('#')[0].strip().split())) for _ in range(num_jobs)]
    # Επιστροφή του αριθμού των εργασιών, του αριθμού των μηχανημάτων, των χρόνων επεξεργασίας και των σειρών επίσκεψης των μηχανημάτων.
    return num_jobs, num_machines, processing_times, machine_orders



# Ορίζει τη διαδρομή του αρχείου για ανάγνωση των δεδομένων JSSP.
file_path =  r'D:\1-Dit Uoi\5ο\ΑΛΓΟΡΙΘΜΟΙ ΚΑΙ ΠΟΛΥΠΛΟΚΟΤΗΤΑ\project2\la01.txt'
# Διαβάζει τα δεδομένα JSSP από το αρχείο και αποθηκεύει τον αριθμό των εργασιών, των μηχανημάτων, τους χρόνους επεξεργασίας και τη σειρά επίσκεψης μηχανημάτων.
parsed_num_jobs, parsed_num_machines, parsed_processing_times, parsed_machine_orders = read_jssp_data(file_path)
# Υπολογίζει το makespan (συνολικό χρόνο ολοκλήρωσης) χρησιμοποιώντας τον αλγόριθμο SPT (Shortest Processing Time).
makespan_spt_user = calculate_makespan_spt(parsed_num_jobs, parsed_num_machines, parsed_processing_times, parsed_machine_orders)
# Αρχικοποιεί δύο πίνακες για τους χρόνους έναρξης και λήξης κάθε εργασίας σε κάθε μηχάνημα.
start_times = np.zeros((parsed_num_jobs, parsed_num_machines))
end_times = np.zeros((parsed_num_jobs, parsed_num_machines))
# Αρχικοποιεί έναν πίνακα για τη διαθεσιμότητα κάθε μηχανήματος.
machine_availability = [0] * parsed_num_machines
# Αρχικοποιεί έναν πίνακα για τον χρόνο ολοκλήρωσης κάθε εργασίας.
job_completion_times = [0] * parsed_num_jobs
# Ταξινομεί τις εργασίες βάσει του συνολικού ελάχιστου χρόνου επεξεργασίας.
sorted_jobs = sorted(range(parsed_num_jobs), key=lambda x: sum(parsed_processing_times[x]))
# Για κάθε εργασία στην ταξινομημένη λίστα:
for job in sorted_jobs:
    # Για κάθε βήμα (μηχάνημα) της εργασίας:
    for step in range(parsed_num_machines):
        # Εύρεση του αντίστοιχου μηχανήματος για το συγκεκριμένο βήμα.
        machine = parsed_machine_orders[job][step] - 1
        # Χρόνος επεξεργασίας για το βήμα στο συγκεκριμένο μηχάνημα.
        proc_time = parsed_processing_times[job][step]
        # Υπολογισμός του χρόνου έναρξης της εργασίας στο μηχάνημα.
        start_time = max(machine_availability[machine], job_completion_times[job])
        # Υπολογισμός του χρόνου λήξης της εργασίας στο μηχάνημα.
        end_time = start_time + proc_time
        # Κατγραφή των χρόνων έναρξης και λήξης στους αντίστοιχους πίνακες.
        start_times[job][machine] = start_time
        end_times[job][machine] = end_time
        # Ενημέρωση της διαθεσιμότητας του μηχανήματος και του χρόνου ολοκλήρωσης της εργασίας.
        machine_availability[machine] = end_time
        job_completion_times[job] = end_time
