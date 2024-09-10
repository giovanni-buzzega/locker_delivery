#!/usr/bin/python3
import sys
class node():
	def __init__(self,n, xcoord, ycoord, start_tw, end_tw, other):
		self.id = n
		self.xcoord = xcoord
		self.ycoord = ycoord
		self.start_tw = start_tw
		self.end_tw = end_tw
		self.other = other
	def __str__(self):
		return str((self.id, self.xcoord, self.ycoord))

def euclid_distance(node1, node2):
	return round(((node1.xcoord-node2.xcoord)**2 + (node1.ycoord-node2.ycoord)**2)**.5, 2)
###############################################################
#print(sys.argv)
if (len(sys.argv) < 2) :
	print("Insert file name")
else :
	input_file = sys.argv[1]
	nodes = []
	r_b = 20
	capacity = 5
	with open(input_file, mode='r') as f:
		firstline = next(f)
		for line in f:
			if line.isspace(): #start new set of results
				continue
				
			linelist = line.split()
			if (not linelist[0].isdigit()):
				#print(linelist)
				continue
			newnode = node(int(linelist[0])-1,float(linelist[1]),float(linelist[2]), float(linelist[4]), float(linelist[5]), [float(item) for item in (linelist[3],linelist[6])])
			nodes.append(newnode)

	#for n in nodes: print(n)

	print(input_file)
	n = max(nodes, key=lambda x: x.end_tw)
	if n.id != 0:
		print("UNEXPECTED ERROR\n\n\n\n", n)
	print(input_file.split('/'))
	numbers = input_file.split('/')[-1].lstrip('n').split('w')
	num_of_clients = int(numbers[0])
	#print(num_of_clients)
	num_nodes = nodes[-1].id+1
	while (num_nodes > 900):
		nodes.pop()
		num_nodes = nodes[-1].id+1
	print("Num nodes:", num_nodes)
	distance_matrix = []
	for i in range(num_nodes):
		distance_matrix.append([])
		for j in range(num_nodes):
			distance_matrix[i].append(0)
	#print(distance_matrix)
	for i in range(num_nodes):
		for j in range(num_nodes):
			distance_matrix[i][j] = euclid_distance(nodes[i], nodes[j])
#	for i in range(num_nodes):
#		for j in range(num_nodes):
#			for k in range(num_nodes):
#				if (distance_matrix[i][j] > (distance_matrix[i][k] + distance_matrix[k][j])):
#					distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j];



	#print(distance_matrix)
	num_lockers = num_nodes-1-num_of_clients
	output_file = 'n' + str(num_of_clients) + 'l' + str(num_lockers) + 'w' + input_file.split('w')[-1]
	print(output_file)
	with open(output_file, mode='w') as f:
		f.write(str(num_of_clients))
		f.write("\n")
		f.write(str(distance_matrix))
		f.write("\n")
		f.write(str([r_b for i in range(num_lockers)]))
		f.write("\n")
		f.write(str(capacity))
		f.write("\n")
		f.write(str([[n.start_tw, n.end_tw] for n in nodes]))
		f.write("\n")
		f.write(str([[n.xcoord, n.ycoord] for n in nodes]))
		f.write("\n")
		f.write(str([n.other for n in nodes]))
		f.write("\n")
		f.write("^demand; service time^\n")
		for n in nodes:
			if (n.other[0] > 0 or n.other[1] > 0):
				print("!!!!",n.other)
		f.write(firstline)




