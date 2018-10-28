#finds a bounded list of primes
import math
import time
import matplotlib.pyplot as plt
import numpy as np

def isPrime(i):
	if i % 2 == 0:	#if divisble by 2, would work for any even divisor
		return False
	for d in range (3, math.floor(math.sqrt(i))+1, 2):	#odd divisors to test against i, +1 to amke inclusive
		if i % d == 0:
			return False	#divisor found, stop testing i not prime
	return True


def sieve(n):	#stores primes less than n in a list
	primes = []
	if n >= 2:	#2 is the only even prime
		primes.append(2)
	for i in range(3, n, 2):	#odd i is potential prime
		if isPrime(i):
			primes.append(i)
	return primes

def timed(func, min, max):	#executes func() using input min to max, with increments ofdelta
	times = []
	for m in range(min, max + 1):	#so upper limit is included
		times.append(10**m)
		start = time.time()	#keep track of when function started
		func(10**m)
		times.append(time.time() - start);	#time elapsed since function call
	return times

def plotSieve(trials, min_n, max_n):	#plots multiple trials of the efficiency of a sieve function for finding primes
	for i in range (0, trials):
		data = timed(sieve, min_n, max_n)
		x = data[0::2]	#even elements (n)
		y = data[1::2]	#odd elements (t)
		plt.plot(x, y)
		print("trial",i,"complete")
	
	plt.title("Sieve Effieciency")
	plt.xlabel("Numbers searched for primes (n)")
	plt.ylabel("Calculation time (s)")
	plt.show()

def pi(n):	#stores number of primes found up to each value of n >= 0
	pi = [0, 0, 1]	#n=0,1,2
	count = 1
	currPow = 0	#start in 10^0 range (0, 1, 2,...,9)
	for i in range (3, n+1):	#check odds only after 2 is cleared
		pow = int(math.log10(i))	#checks current power of 10 calculation is running
		if (pow > currPow):
			print("order", pow, "completed")
			currPow = pow
		if isPrime(i):
			count+=1
		pi.append(count)
	return pi

def a(x): #aprrox
    	return x / np.log(x)

def plotCounter(n):	#prime number counter, up to n
	x = range(0, 10**n + 1)
	y = pi(10**n)	#must be calculated for all natural numbers, no shortcuts
	
	plt.plot(x, y, label="pi(n)")
	plt.plot(x, a(x), label="n/logn")
	plt.xlabel("n")
	plt.ylabel("primes <= n")
	
	plt.title("Prime counting function")
	plt.legend()
	plt.show()

def plotRatio(n, res):	#ratio of actual primes to approximated number
	y = pi(10**n)	#must be calculated for all natural numbers, no shortcuts
	x_log = []	#integer values of n
	r = []	#ratio of pi(n) to a(n)
	
	#to cut down on calculation time, there will be res subdivsions between each power of 10
	#desired spacing for res = 100: 1, 2, 3,..., 100, 110, 120,..., 1000, 1100, 1200...
	
	#first entry = 0
	x_log.append(0)
	r.append(y[0]/a(0))
	
	for power in range (0, n, res):	#res must be a factor of n, or skipping will occur -> index out of range
		for prefix in range (1, 10**res):	#1-99
			s = prefix * 10**power	#subdivision marker
			x_log.append(s)
			r.append(y[s]/a(s))
	
	#last entry = 10^n	
	x_log.append(10**n)
	r.append(y[10**n]/a(10**n))	
	#print(x_log)
		
	plt.plot(x_log, r, label="pi(n)/(n/logn)")
	plt.axhline(y=1.0, color="g", linestyle="-")
	plt.ylim([0.8,1.3])
	plt.xscale("log")
	plt.xlabel("n")
	plt.ylabel("ratio of actual to approximation")

	plt.title("Asymptotic prime distribution")
	plt.legend()
	plt.show()

def main():
	t = int(input("Enter the type of graph (1, 2, or 3): "))
	if t == 1:
		tr = int(input("Enter trials: "))
		min = int(input("Enter n_min: "))
		max = int(input("Enter n_max: "))
		plotSieve(tr, min, max)
	elif t == 2:
		n = int(input("Enter n: 10^"))
		plotCounter(n)
	elif t == 3:
		n = int(input("Enter n: 10^"))
		r = int(input("Enter the resolution power (a factor of n's power): "))
		plotRatio(n, r)

if __name__ == "__main__":
    main()