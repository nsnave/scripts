import argparse
import random
import re


parser = argparse.ArgumentParser(description='Rolls some dice...')
parser.add_argument("rolls", type=str, help="Rolls the specified dice using 'xdy' format; e.g., to rolls 4 six-sided dice, input '4d6'. \
                                            Multiple sets of rolls may be specified by putting all rolls within double- or single-quotes, seperated by spaces; e.g., \
                                            '4d6 1d20' rolls 4 six-sided dice and 1 twenty-sided die. \
                                            If only rolling of a six-side die is desired, then only an integer input is required; e.g. '3' will roll 3 six-sided dice. \
                                            Optionally, a \"take max\" number may be included in the form 'm,xdy' which only returns the highest 'm' rolls.")
parser.add_argument("-s", "--sum", help="Sums the dice rolls.", action="store_true")
parser.add_argument("-m", "--max", type=int, help="Specifies that each set of rolls should be repeated MAX times and the maximum returned.")
parser.add_argument("--min", type=int, help="Specifies that each set of rolls should be repeated MIN times and the minimum returned.")
parser.add_argument("-r", "--repeat", type=int, help="Specifies that each set of rolls should be repeated REPEAT times.")
parser.add_argument("--dist", help="Returns a distribution of the results as percentages. Must be used with the --repeat argument.", action="store_true")


def get_sample(upper, k):
  return random.choices(range(1, upper + 1), k=k)

def handle_roll(roll):
  if re.match("\d,\dd\d", roll):
    parts = re.split("[,d]", roll)

    maximum = int(parts[0])
    rolls = int(parts[1])
    sides = int(parts[2])

    results = get_sample(sides, rolls)
    results.sort(reverse=True)
    results = results[:maximum]

  elif re.match("\dd\d", roll):
    parts = roll.split('d')
    
    rolls = int(parts[0])
    sides = int(parts[1])

    results = get_sample(sides, rolls)

  elif re.match("\d", roll):
    results = get_sample(6, int(roll))
  else:
    results = None

  return results

def handle_max_min(is_max, bound, roll):
  rolls = [handle_roll(roll) for _ in range(0, bound)]
  sums = [sum(ls) for ls in rolls]
  func = max if is_max else min
  results = rolls[sums.index(func(sums))]

  results.sort(reverse = True if is_max else False)
  results = results[:bound]

  return results


def main():
  args = parser.parse_args()

  if args.dist and not args.repeat:
    print("Error: the --repeat argument must be specified if --dist is used.")
    return

  all_rolls = args.rolls.split()
  number_of_rolls = len(all_rolls)
  for roll in all_rolls:
    if not re.match("(\d,)?(\dd)?\d", roll):
      print("Error: roll \"{}\" is in an invalid format.".format(roll))
      continue

    final_results = [] if not args.dist else dict()

    # Prints the roll label to help clarify what rolls are which
    if number_of_rolls > 1:
      print("{}:".format(roll))
    
    # Rolls this set of dice the desired number of times
    repeat = args.repeat if args.repeat else 1
    for _ in range(0, repeat):

      # Handles the --max and --min arguments
      if args.max and args.min:
        print("Error: max and min arguments cannot be used at the same time.")
      elif args.max:
        results = handle_max_min(True, args.max, roll)
      elif args.min:
        results = handle_max_min(False, args.min, roll)
      else:
        results = handle_roll(roll)

      # Handles the --sum argument
      if args.sum:
        results = [sum(results)]

      if args.dist:
        # Handles the --dist argument
        value = sum(results)
        if value in final_results:
          final_results[value] += 1
        else:
          final_results[value] = 1
      else:
        # Stores the results to print later
        final_results.append(results)

    # Prints the final results
    if not args.dist:
      for results in final_results:
          print(" ".join(str(e) for e in results))
    else:
      keys = list(final_results.keys())
      keys.sort()
      for key in keys:
        print("{}: {}".format(key, round(final_results[key] / repeat, 5)))


    # Print a newline to separate multiple rolls
    if number_of_rolls > 1:
        print()


if __name__ == '__main__':
  main()