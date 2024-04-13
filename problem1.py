

class Job:
  def __init__(self, start_time, end_time, profit):
    self.start_time = start_time
    self.end_time = end_time
    self.profit = profit

  def __repr__(self):
    return f"Job(start_time={self.start_time}, end_time={self.end_time}, profit={self.profit})"

def parse_jobs_input():
  n = int(input("Enter the number of Jobs\n"))
  if n < 1 or n > 100:
    print("Invalid number of jobs")
    return []
  jobs = []
  for _ in range(n):
    start_time = input("Enter job start time: ")
    end_time = input("Enter job end time: ")
    profit = int(input("Enter job profit: "))
    if(int(start_time) < 0 or int(start_time) > 2359 or int(end_time) < 0 or int(end_time) > 2359):
      print("Invalid start or end time")
      return []
    if int(start_time) >= int(end_time):
      print("Start time should be less than end time")
      return []
    jobs.append(Job(int(start_time), int(end_time), profit))
  return jobs

def findLastNonConflict(jobs, n):
  for key in reversed(range(n)):
    if jobs[key].end_time <= jobs[n].start_time:
      return key
  return -1

def jobs_left(jobs):
  if not jobs:
    return 0
  jobs.sort(key=lambda x: x.end_time)
  max_profit = [[0,0] for _ in jobs]
  max_profit[0] = [jobs[0].profit,1]
  total_profit = jobs[0].profit
  for i in range(1, len(jobs)):
    total_profit += jobs[i].profit
    key = findLastNonConflict(jobs, i)
    profit = [jobs[i].profit,1]
    if key != -1:
      profit = [max_profit[key][0]+jobs[i].profit,max_profit[key][1]+1]

    profit = [profit, max_profit[i - 1]]
    profit.sort(key=lambda x: x[0])
    max_profit[i] = profit[-1]
  total_profit = total_profit - max_profit[-1][0]
  jobs_left = len(jobs) - max_profit[-1][1]
  return [jobs_left, total_profit]

# Main program
def main():
  jobs = parse_jobs_input()

  result = jobs_left(jobs)
  print("The number of tasks and earnings available for others")
  print("Task Remaining:", result[0])
  print("Earnings Remaining:", result[1])

if __name__ == "__main__":
  main()