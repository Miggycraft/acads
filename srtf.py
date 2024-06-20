class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


def srtf_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)
    current_process = None

    while completed != n:
        min_remaining_time = float('inf')
        for process in processes:
            if process.arrival_time <= time and process.remaining_time > 0:
                if process.remaining_time < min_remaining_time:
                    min_remaining_time = process.remaining_time
                    current_process = process

        if current_process:
            time += 1
            current_process.remaining_time -= 1

            if current_process.remaining_time == 0:
                completed += 1
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            current_process = None
        else:
            time += 1

    return processes

processes = [
    Process(1, 0, 2),
    Process(2, 2, 5),
    Process(3, 4, 2),
    Process(4, 6, 4),
    Process(5, 8, 3),
]

# Perform SRTF scheduling
scheduled_processes = srtf_scheduling(processes)

total_turnaround = 0
total_waiting = 0
print("PID | Arrival | Burst | Completion | Turnaround | Waiting")
for process in scheduled_processes:
    total_turnaround += process.turnaround_time
    total_waiting += process.waiting_time
    print(f"%-3d   %-3d       %-3d     %-3d          %-3d          %-3d"
          % (process.pid,process.arrival_time,process.burst_time,
             process.completion_time,process.turnaround_time, process.waiting_time))

print("Average Turn Around Time:", total_turnaround / len(processes))
print("Average Waiting Time:", total_waiting / len(processes))
