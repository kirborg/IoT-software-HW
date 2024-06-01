import threading
import time
import random

def gardener(gardener_id, flowers):
	while(True):
		time.sleep(random.uniform(1, 2)) # delay before watering next flower
		with threading.Lock():
			for idx, flower in enumerate(flowers):
				if flower == 'dry':
					flowers[idx] = 'wet'
					print(f"flower {idx} watered by gardener {gardener_id}")
					break

def update_flower_status(flowers):
	while(True):
		time.sleep(random.uniform(0.5, 2)) # delay before next flower goes dry 
		with threading.Lock():
			index = random.randint(0, len(flowers) - 1)
			flowers[index] = 'dry'
			print(f"flower {index} dry \n")

def print_flowers(flowers):
	while(True):
		time.sleep(2)
		for i, flower in enumerate(flowers):
			print(f"flower {i} is {flower} ", end=" ")
		print("\n")

def main():
	flowers_cnt = 10
	gardeners_cnt = 3
	flowers = ['wet']*flowers_cnt
	# wet - политый
	# dry - увядающий
	
	threads = []
	flower_thread = threading.Thread(target = update_flower_status, args = (flowers,))
	flower_thread.start()
	threads.append(flower_thread)
	
	print_thread = threading.Thread(target = print_flowers, args = (flowers,))
	print_thread.start()
	threads.append(print_thread)

	for i in range(gardeners_cnt):
		t = threading.Thread(target = gardener, args = (i, flowers))
		t.start()
		threads.append(t)

	for t in threads:
		t.join()
	

if __name__ =="__main__":
	main()