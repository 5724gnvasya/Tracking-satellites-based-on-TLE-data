<h1 align="center">Tracking satellites based on TLE data</h1>
<!-- <h2 align="center"> -->

<h2>Description</h2>

This software is designed to monitor the trajectories of satellites located in the [site's database](https://celestrak.org/).

Tracking satellites is an essential task in various fields, and a program for tracking satellites can be beneficial to several groups of people. Here are some reasons why:

<h3>Who needs a satellite tracking program:</h3>

* <b>Space agencies and satellite operators:</b>
  To monitor the health and position of their satellites, ensuring they remain in orbit and perform their intended functions.
* <b>Astronomers and researchers:</b>
   To study the behavior of satellites, asteroids, and other celestial objects, gaining insights into the universe and its phenomena.
* <b>Amateur satellite enthusiasts:</b>
  To observe and track satellites, learning about their orbits, purposes, and characteristics.
* <b>Environmental monitoring and disaster response teams:</b>
  To track satellites used for Earth observation, such as those monitoring weather patterns, climate change, or natural disasters.
  
<h3>Benefits of a satellite tracking program:</h3>

* <b>Enhanced scientific research:</b>
   Accurate tracking data enables researchers to study satellite behavior, orbit dynamics, and the effects of space weather on satellite operations.
* <b>Increased situational awareness:</b>
   Tracking satellites helps identify potential collisions, enabling evasive maneuvers to prevent damage or loss of satellites.
* <b>Education and outreach:</b>
  Satellite tracking programs can engage the public in space exploration, inspiring interest in STEM fields and promoting a better understanding of space and its applications.
* <b>Commercial applications:</b>
  Accurate tracking data can be used in various commercial applications, such as satellite-based navigation, remote sensing, and Earth observation.

<h2>Technologies Used</h2>

<a href="https://flask.palletsprojects.com/">
  <img src="https://img.shields.io/badge/Framework-Flask-%23000.svg" alt="Flask">
</a>
<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/Language-Python-%233776AB.svg" alt="Python">
</a>
<a href="https://www.w3.org/html/">
  <img src="https://img.shields.io/badge/Language-HTML%2FCSS-%23E34F26.svg" alt="HTML/CSS">
</a>
<a href="https://csv.org/">
  <img src="https://img.shields.io/badge/Data%20Storage-CSV-%23FFD700.svg" alt="CSV">
</a>
<a href="https://matplotlib.org/">
  <img src="https://img.shields.io/badge/Library-Matplotlib-%23FFC107.svg" alt="Matplotlib">
</a>
<a href="https://numpy.org/">
  <img src="https://img.shields.io/badge/Library-Numpy-%23007ACC.svg" alt="Numpy">
</a>
<a href="https://pandas.pydata.org/">
  <img src="https://img.shields.io/badge/Library-Pandas-%23150458.svg" alt="Pandas">
</a>
<a href="https://pypi.org/project/spacetrack/">
  <img src="https://img.shields.io/badge/Library-Spacetrack-%232F4F4F.svg" alt="Spacetrack">
</a>


**Getting Started**
---------------

<p align="center">
 <img src="https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data/assets/110739884/2856fa3b-290b-4728-872f-00237c521e60" width="400">
  </p>
</div>

### Prerequisites

* Python 3.x installed on your system
* Git installed on your system

### Installation

Note, that the final version is on the final_version branch.
1. Clone the repository: `git clone https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data.git`
2. Install dependencies in your virtual environment: `pip install -r requirements.txt`

### Running the Project

To start tracking satellites, run `python main.py` command in the command line of the cloned project.
A few seconds after you will see:
```
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
Just do it!

**Here is what you will see**
-------------
<h3>After pressing "Select Satellites" button you will be taken to the page, where you will be able to select the satellites that you will be tracking </h3>

![image](https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data/assets/110739884/7f9ec2a0-d06e-4fc4-9349-5fe4e6caf524)


Thanks to the user-friendly design, you can easily select the satellites you are interested in from the list, which is updated every 20 seconds according to the site database. you can also speed up the time to search for a satellite, because if you start entering its name in the field, the list will automatically leave only the names corresponding to your input


![image](https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data/assets/110739884/5c15f0f1-d700-4f6f-8f69-a253fa8979eb)

<h4>The selected satellites will be highlighted with active checkboxes.</h4>

<h3>After pressing the button "View Trajectories" the trajectories of all the satellites you have selected will be presented</h3>

![image](https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data/assets/110739884/645b6a68-4ed5-4f04-a0cf-e559bdda0b99)
<h3>If you want to see another satellites, just return to a previous page and select new satellites:</h3>

![image](https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data/assets/110739884/b68a2f40-a9b2-4948-8b02-6d803dc4211c)



<h4>This simple application is also comfortable in use with your smartphone! </h4>
<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data/assets/110739884/4de8bd0e-7dbf-4aa1-9f02-c15b6f1cc9fe" width="400">
  <img src="https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data/assets/110739884/6fc4ee0d-851d-4c21-b15c-f75fd218d9d6" width="400">
</div>



⚠️ 
Note that not all satellites from the database can be illustrated due to the fact that it is impossible to build their orbit, since they are too far from earth. A message about this is displayed in user's console.
Here is an example how this message will be shown:

![image](https://github.com/5724gnvasya/Tracking-satellites-based-on-TLE-data/assets/110739884/0cae51a1-af6a-4430-84c6-a334810f009d)



**Author**
---------

[Alla Chernova](https://github.com/5724gnvasya)

