from cpu_job.job import Job
from scheduler.scheduler import Scheduler
import random
import time

def main():
    scheduler = Scheduler()
    i = 0

    while True:

        scheduler.update_scheduled_job()
        scheduler.assign_job()

        if bool(random.getrandbits(1)):
            new_job = generate_job(i)
            i += 1
            priority = random.randrange(-20, 19)
            scheduler.add(new_job, priority)
        else:
            print("No new job this slice")

        scheduler.update_job_priorities()

        time.sleep(3)


def generate_job(i):
    name = "PROCESS" + str(i)
    length = random.randrange(5, 25)  # va da 1 a 100. Per comodità mettiamo una lunghezza tra 5 e 25
    return Job(name, length)

main()
