
estimated_stones_used = int(input("Estimated number of stones used: "))
average_weight_of_stone = float(input("Average weight of each stone (in kilograms): "))
years_taken_to_build = int(input("Number of years taken to build the pyramid: "))


total_weight = estimated_stones_used * average_weight_of_stone


weight_built_per_year = total_weight / years_taken_to_build


weight_built_per_hour = weight_built_per_year / (365 * 24)


weight_built_per_minute = weight_built_per_hour / 60


print("Estimated weight of the pyramid: {:.2f} kilograms".format(total_weight))
print("Weight built each year: {:.2f} kilograms".format(weight_built_per_year))
print("Weight built each hour: {:.2f} kilograms".format(weight_built_per_hour))
print("Weight built each minute: {:.2f} kilograms".format(weight_built_per_minute))
