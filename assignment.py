'''
Date  : 27 Aug 2020
Task  : Python Assigment 1
'''
class __CityTraverasl:

	def __init__(self):

		self.__cities = ['Arad','Craiova','Drobeta','Eforie','Faragas','Giurgiu','Hirsova','Iasi','Lugoj','Mehadia','Neamt','Oradea','Pitesti','Rimnicu Vilcea','Sibiu','Timisoara','Urziceni','Vaslui','Zerind']
		self.__distances = [366,160,242,161,176,77,151,226,244,241,234,380,100,193,253,329,80,199,374]

		self.__main()

	def __find_city(self,__arg):

			__arg = str(__arg)


			if __arg.isnumeric():

				__arg = int(__arg)

				__is_found = False

				__citi_dis = "";

				for i in range(len(self.__distances)):

					if __arg == self.__distances[i]:

						__citi_dis = "City: " + self.__cities[i] + ", Heuristic Distance: " + str(self.__distances[i])

						__is_found = True

						break;

				if __is_found:

					print(__citi_dis)

				else:

					print("No matching heuristic distance for value : "  + str(__arg))				

			else:

				__arg = __arg.capitalize()

				__is_found = False

				__citi_dis = ""

				for i in range(len(self.__cities)):

					if self.__cities[i] == __arg:

						__citi_dis = "City: " + self.__cities[i] + ", Heuristic Distance: " + str(self.__distances[i])

						__is_found = True

						break;

				if __is_found: 

					print(__citi_dis)

				else:

					print("No matching city for: " + __arg)

	def __shortest_distance(self):

		__lowest_distance = self.__distances[0];

		for i in self.__distances:

			if i < __lowest_distance:

				__lowest_distance = i


		print("Shortest distance is : " +  str(__lowest_distance))

	def __main(self):

		print("***********************MAIN MENU************************")
		print("1. Find City And Its Distance")
		print("2. Check The Shortest Path")
		print("3. QUIT")

		__selection = input("Answer : ")

		if int(__selection) == 1:

			self.__find_city(input("Enter city or heuristic distance to search city and its distance: "))

		elif int(__selection) == 2:

			self.__shortest_distance()

		elif int(__selection) == 3:

			import sys

			sys.exit()

		else:

			print("Print Invalid Input")













				

OBJ = __CityTraverasl()
