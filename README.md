# Project 3 for Udacity FSND - Log Analysis

## About
This is the third project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

## How to run
### Requirements:
* Python 2
* Vagrant
* VirtualBox

### Setup
1. Install Vagrant and VirtualBox
2. Clone the following repo:
https://github.com/udacity/fullstack-nanodegree-vm

### Running

Launch Vagrant VM by running vagrant up, you can then log in with vagrant ssh

To load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.

The database includes three tables:
* Authors table
* Articles table
* Log table

Copy the fsnd-p3.py file to the same folder you cloned (it should be next to the 'catalog', 'forum' and 'tournament' folders and the 'Vagrantfile'). Once copied, run `python fsnd-p3.py` from the command line to see the results.
