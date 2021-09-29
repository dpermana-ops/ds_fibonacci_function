# def find_fibonacci(x: int) -> bool:
#     """
#     Menemukan bilangan bulat x di dalam suatu deret fibonacci.
#     Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
#     Jika tidak ada, maka kembalikan False
#     """
    # write your code here
def find_fibonacci(N):
    #initialize the list with starting elements: 0, 1
    fibonacciSeries = [0,1]
<<<<<<< HEAD
=======

    if N>2:
        for i in range(2, N+1):
            #next elment in series = sum of its previous two numbers
            nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
            #append the element to the series
            fibonacciSeries.append(nextElement)


    # Check Fibonacci Number (fibonacciSeries)
    if N in fibonacciSeries:
        return True
    else:
        return False
>>>>>>> multithreading

    if N>2:
        for i in range(2, N+1):
            #next elment in series = sum of its previous two numbers
            nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
            #append the element to the series
            fibonacciSeries.append(nextElement)


    # Check Fibonacci Number (fibonacciSeries)
    if N in fibonacciSeries:
        return True
    else:
        return False

# Masukkan angka untuk dicek Fibonacci member atau bukan
# N = int(input("Masukkan angka untuk dicek sebagai member deret Fibonacci: "))

# # Print hasil cek Fibonacci
# print(find_fibonacci(N))

if __name__ == "__main__":
    """Jalankan beberapa test-case di bawah sini
    """
    print(find_fibonacci(1))
    print(find_fibonacci(10))
    print(find_fibonacci(11))