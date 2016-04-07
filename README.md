# strainrate-analysis
This is the Documentation of the Python Creep Macro.

########

Lukas Gartmair
Lukas_Gartmair@gmx.de
v.1.0
########

Usage:

The program is written for a certain data scheme (only this scheme) that looks as the following:

Zeit [s]	Weg [mm]	Kraft [N]	Epsilon 0	Epsilon w	Sigma 0	Sigma w	Epsilon w Punkt	Temperatur [°C]	
0.24	2.9546998e-4	4.080	0	-3.8922959e-5	0	-0.198	-1.8551e-05	1099.97	
0.74	3.6588452e-4	10.200	0	-4.8198611e-5	0	-0.495	-1.1669e-05	1100.00	

- It has to contain at least the columns TIME / LONGITUDINATION / FORCE exactly in this order!
	Addiotional columns are ignored.
- The longitudination is decreasing 
- So does the force
This fact becomes corrected in the program.

Options:

Enter all options with a dot! Example: height = 22.45 mm
	A comma will raise an error.

- Number of windows: This parameter says in how many subsets the data is divided for
	calculating the strainrate etc.
	Both a window size too small and too big result in higher fitting errors.

- Number of points to be stored (nopts): This parameter says how many points per window
	chosen by the number of windows parameter are stored.
	This parameter has to be chosen sensitive in order to depict the original
	shape of the curve as well as possible.
	The only restriction for this parameter is of course that one can't store more 
	points than the window size is great.

Output:

Datapoint Nr.	Strain / %	Strainrate / %/s	Filtered Strain / %	Filtered Strainrate / %/s

What the program does:

1st 

- Read in the specimen data and file paths
- Correct height/area with respect to the thermal expansion coeff
- Get the start of the desired stresslevel
- Check for equally small values in the beginning and cut them 
- Get the slope of long - force plot and correct longitudination

2nd

- Calculate strain true and stress true
- Get the transition from elast to plast and get the elast slope
- Calculate strain plast and strainrate plast

3rd 

- Filter the data like getting iteratively windows, calc the linear sub slope and
	take the desired number of points that are closest to this fit
- Get the errors for the slope and the y-intersection for each window

4th

- Plot the results
- Write a summary file

The function for the window_selcetion works this way:

1st define a window_interval for the slopes 

3rd the slopes refering to the window size from stepp 1 are calculated
	and depending on their value decided whether a new window start has to take place or not

------------------------------
2nd define a window interval for the strain dependent selection

4th a new strain based window is placed every nth percentage of total strain 

--------------------------------------------------

5th the windows are generated with the intervals determined above

-----------------------------

6th the window indices are reduced - every window must have at least 3 points to generate the fit in the next step

------------------------------

7th. fit every window and get the closest point to its fit
