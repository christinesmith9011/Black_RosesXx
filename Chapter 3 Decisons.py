speed_limit=float(input("What is the speed limit(mph):"))
average_speed_limit=float(input("What is the average speed limit(mph):"))
distance=float(input("How many miles did you travel(miles):"))
time_saved= (distance/speed_limit-distance/ average_speed_limit) *60
print(f"I saved{(time_saved):.0f}minutes")
                                
