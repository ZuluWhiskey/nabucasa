# Define the empty list to be added to later on
days = []

# Define a function to calculate the average of a list
def Average(lst): 
	return sum(lst) / len(lst)

# Open the water softener log
with open('/home/zander/homeassistant/water_softener.log') as file:
  # Read the lines in the file, ensuring to skip the first two lines as they aren't needed
  output = file.readlines()[2:]
  # Remove '/n' from each item in the list
  output = [item.rstrip() for item in output]
  # Start a For Loop for every item in the output list
  for items in output:
    # Split the items at each blank space (needed as the file has timestamp then the number)
    items_split = items.split(' ')
	# Add the second item from what we've just split to the 'days' list we defined at the start
    days.append(items_split[1])
  # As the original file had the numbers (integers) stored as text (strings) we need to convert them to integers to be able to carry out calculations
  days = list(map(int, days))
  # Calculate the average number of days utilising the function we defined earlier
  average_days = Average(days)
  average_days = round(average_days)
  # Close the file that we opened at the start
  file.close()

file = open("/home/zander/homeassistant/water_softener_average.txt", "a")
file.write('\n' + str(average_days))
file.close()
