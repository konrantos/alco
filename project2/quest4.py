# Define the plotting function for the Gantt chart.
def plot_gantt(machine_schedule, job_sequences, num_machines, processing_times):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Define colors for each job
    colors = plt.cm.tab10.colors  # Get 10 different colors from matplotlib's colormap

    # Loop through each machine schedule and plot the jobs
    for job_id, (schedule, sequence) in enumerate(zip(machine_schedule, job_sequences)):
        for i, end_time in enumerate(schedule):
            # Find the start time for the job at the machine
            if i == 0:
                start_time = 0
            else:
                # Start time is the end time of the previous operation
                start_time = schedule[i - 1]
            # Calculate the duration of the job on the machine
            duration = processing_times[job_id][i]
            # Plot the job as a bar
            ax.broken_barh([(start_time, duration)], (num_machines - sequence[i], 0.8), facecolors=colors[job_id % len(colors)], edgecolor='black', label=f'Job {job_id+1}' if i == 0 else "")

    # Set the y-ticks to correspond to machines
    ax.set_yticks([num_machines - 0.5 - i for i in range(num_machines)])
    ax.set_yticklabels([f'Machine {i+1}' for i in range(num_machines)])
    
    # Set labels and title
    ax.set_xlabel('Time')
    ax.set_title('Job Shop Scheduling - Gantt Chart')

    # Add a legend with unique labels (jobs)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    # Grid and layout settings
    ax.grid(True)
    plt.tight_layout()

    # Show the plot
    plt.show()

# The data for processing times and machine sequences should be defined above this line.
# Call the plotting function to generate the Gantt chart with the machine schedule calculated earlier.
# plot_gantt(machine_schedule, machine_sequences, num_machines, processing_times)
