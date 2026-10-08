import heapq
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


class JobScheduler:
    def __init__(self):
        self.job_queue = []   # Min-heap of (priority, counter, job_name)
        self.counter = 0      # Tie-breaker so equal priorities stay FIFO

    def add_job(self, job_name: str, priority: int) -> None:
        heapq.heappush(self.job_queue, (priority, self.counter, job_name))
        self.counter += 1
        print(f"Job '{job_name}' with priority {priority} added!")

    def execute_job(self) -> None:
        if not self.job_queue:
            print("No jobs in the queue!")
            return
        priority, _, job_name = heapq.heappop(self.job_queue)
        print(f"Executing job: {job_name} (Priority: {priority})")

    def show_jobs(self) -> None:
        if not self.job_queue:
            print("No jobs in the queue!")
            return
        print("\nCurrent Job Queue:")
        # sorted() makes a new list, so the heap itself is untouched
        for priority, _, job_name in sorted(self.job_queue):
            print(f"- {job_name} (Priority: {priority})")


def get_priority() -> int:
    while True:
        try:
            return int(input("Enter job priority (lower number = higher priority): ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main() -> None:
    scheduler = JobScheduler()

    while True:
        print()
        print("1. Add Job")
        print("2. Execute Job")
        print("3. Show Jobs")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            job_name = input("Enter job name: ").strip()
            if not job_name:
                print("Job name cannot be empty.")
                continue
            priority = get_priority()
            scheduler.add_job(job_name, priority)

        elif choice == "2":
            scheduler.execute_job()

        elif choice == "3":
            scheduler.show_jobs()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
