import numpy as np

### author: heltonbiker Jul'5 12 http://stackoverflow.com/questions/11352047/finding-moving-average-from-data-points-in-python ### 

def movingaverage(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)

    return np.convolve(interval, window, 'same')

# Best way to apply a moving/sliding average (or any other sliding window function) to a signal is by using numpy.convolve().
##
# def movingaverage(interval, window_size):
##    window = numpy.ones(int(window_size))/float(window_size)
# return numpy.convolve(interval, window, 'same')
##
# Here, interval is your x array, and window_size is the number of samples to consider. The window will be centered on each sample, so it takes samples before and after the current sample in order to calculate the average. Your code would become:
##
# plot(x,y)
# xlim(0,1000)
##
##x_av = movingaverage(interval, r)
##plot(x_av, y)
##
##xlabel("Months since Jan 1749.")
##ylabel("No. of Sun spots")
# show()
##
# Hope this helps!
