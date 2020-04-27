# LIBRARIES
import os.path
import re
import sys
from scipy.sparse import coo_matrix


# OTHER FUNCTIONS
# parser
# matrix build
def no_file():
    print 'Dataset not found'


def fetch_data():




	# Chicago restaurant data   
	file_path = 'entree_data/entree/data/chicago.txt'
	if not os.path.exists(file_path):
		return no_file()

	restaurant_names = {}

	# Restaurant dictionary
	with open(file_path) as data_file:
		for n, line in enumerate(data_file):

        	#Readable data (for humans)
			readable_data = line.split()
			ID = int(readable_data[0][-3:])
			name = ''
			for part in readable_data:
				if not part.isdigit():
					name += part+' '

			restaurant_names[ID] = name





	# User-Restaurant data
	file_paths = []

	file_paths.append('entree_data/entree/session/session.1996-Q3')
	file_paths.append('entree_data/entree/session/session.1996-Q4')

	file_paths.append('entree_data/entree/session/session.1997-Q1')
	file_paths.append('entree_data/entree/session/session.1997-Q2')
	file_paths.append('entree_data/entree/session/session.1997-Q3')
	file_paths.append('entree_data/entree/session/session.1997-Q4')

	file_paths.append('entree_data/entree/session/session.1998-Q1')
	file_paths.append('entree_data/entree/session/session.1998-Q2')
	file_paths.append('entree_data/entree/session/session.1998-Q3')
	file_paths.append('entree_data/entree/session/session.1998-Q4')

	file_paths.append('entree_data/entree/session/session.1999-Q1')
	file_paths.append('entree_data/entree/session/session.1999-Q2')

	# Data to create our coo_matrix
	data, row, col = [], [], []

    # Restaurants and users
	restaurants, users = {}, {}

	for file_path in file_paths:
		if not os.path.exists(file_path):
			return no_file()

	    # Read file and fill variables
		with open(file_path) as data_file:
			for n, line in enumerate(data_file):

	            # Readable data (for humans)
				readable_data = line.split('\t')
				date =     		readable_data[0]
				user_IP =     	readable_data[1]
				#entry = 		readable_data[2]
				restaurant =    readable_data[2:]
				#end =     		readable_data[-1]

				# Convert user_ID into user number
				if user_IP not in users:
					users[user_IP] = len(users)

				# Remove restaurant letter and '0' entry point
				rs = []
				for item in restaurant:
					if item not in ['0']:
						item = item[:-1]
						rs.append(int(item))
				restaurant = rs
				
				# Remove -1 and restaurants not in name dictionary
				for item in restaurant:
					if item not in restaurant_names:
						restaurant.remove(item)

			    # Compile restaurants(name,id) dictionary
				for item in restaurant:
					if item not in restaurants: 
						restaurants[item] = {
							'name' : restaurant_names[item],
							'id' : len(restaurants)
							}

				# compile coo_matrix
				for item in restaurant:
					#print users[user_IP], restaurants[item]['id']
					#print user_IP, restaurants[item]['name']
					data.append(1) # restaurant has been visited and liked
					row.append(users[user_IP]) # user number id
					col.append(restaurants[item]['id']) # restaurant id
	              		
	#print len(users)
	#print restaurant_names
	#print data, row, col
	#print len(data), len(row), len(col)
	





    # Our matrix: ((visited, (user, restaurant)))
	coo = coo_matrix((data,(row,col)))

    # We return the matrix, the restaurant dict and the users
	dictionary = {
		'matrix' : coo,
		'restaurants' : restaurants,
		'users' : len(users)
	}

	return dictionary
