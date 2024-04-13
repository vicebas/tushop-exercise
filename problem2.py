import sys


def read_goodies_file(file_name="sample_input.txt"):
  lines = []
  with open(file_name) as file:
    lines = file.readlines()
  employees = int(lines[0].split(":")[1].strip())
  goodies = []
  for line  in lines[2:]:
    goodie = line.split(":")
    if len(goodie) < 2:
      continue;
    goodies.append((goodie[0], int(goodie[1].strip())))
  return employees, goodies

def get_goodies(employees, goodies):
  goodies.sort(key=lambda x: x[1])
  lowest_diff = goodies[employees][1] - goodies[0][1]
  selected_goodies = goodies[:employees]
  for i in range(len(goodies)-employees+1):
    diff = goodies[i+employees-1][1] - goodies[i][1]
    if diff < lowest_diff:
      lowest_diff = diff
      selected_goodies = goodies[i:i+employees]
  return lowest_diff, selected_goodies

def write_goodies_file(price_diff, goodies, output_file="sample_output.txt"):
  with open(output_file, "w") as file:
    file.write(f"The goodies selected for distribution are:\n")
    file.writelines([f"{goodie[0]}: {goodie[1]}\n" for goodie in goodies])
    file.write(f"\nAnd the difference between the chosen goodie with highest price and the lowest price is {price_diff}\n")
def main(args):
  file_name = args[0] if len(args) > 0 else "sample_input.txt"
  output_file = args[1] if len(args) > 1 else "sample_output.txt"
  print(f"Reading goodies from {file_name}")
  employees, goodies = read_goodies_file(file_name)
  price_diff, goodies = get_goodies(employees, goodies)
  write_goodies_file(price_diff, goodies,output_file)
  print(f"Output written to {output_file}")


if __name__ == "__main__":
  main(args=sys.argv[1:])